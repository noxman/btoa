import bpy
from .python.arnold import *
from . import utils

from bl_ui import properties_data_mesh
for member in dir(properties_data_mesh):
    subclass = getattr(properties_data_mesh, member)
    try:
        subclass.COMPAT_ENGINES.add('arnold_renderer')
    except:
        pass
del properties_data_mesh

class Polymesh:
    def __init__(self,scene,shader_node):
        self.scene = scene
        self.shader_node = shader_node

    def writePolymesh(self):
        for pm in self.scene.objects:
            if pm.hide_render == False and pm.type == "MESH":
                # create the node
                self.amesh = AiNode("polymesh")
                AiNodeSetStr(self.amesh,"name",pm.name)

                # create shorthand variables
                faces = pm.data.polygons
                vertices = pm.data.vertices
                numFaces = len(faces)
                numVerts = len(vertices)

                # Number of sides per polygon
                nsides = AiArrayAllocate(numFaces, 1, AI_TYPE_UINT)
                for i in range(numFaces):
                    face = faces[i]
                    AiArraySetUInt(nsides, i, len(face.vertices))
                AiNodeSetArray(self.amesh,"nsides",nsides)

                # IDs of each vertex
                numindex = 0
                for i in faces:
                    numindex += len(i.vertices)
                vidxs = AiArrayAllocate(numindex, 1, AI_TYPE_UINT)

                count = 0
                for i in range(numFaces):
                    face = faces[i]
                    for j in face.vertices:
                        AiArraySetUInt(vidxs, count, j.numerator)
                        count +=1
                AiNodeSetArray(self.amesh,"vidxs",vidxs)

                vlist = AiArrayAllocate(numVerts,1,AI_TYPE_POINT)
                for i in range(numVerts):
                    vertex = vertices[i].co
                    AiArraySetPnt(vlist,i,AtPoint(vertex.x,vertex.y,vertex.z))
                AiNodeSetArray(self.amesh,"vlist",vlist)

                # uvs
                if len(pm.data.uv_textures) > 0:
                    uvset = pm.data.uv_textures[0]
                    numuv = len(uvset.data[0].uv)
                    uvidxs = AiArrayAllocate(numuv,1,AI_TYPE_UINT)
                    uvlist = AiArrayAllocate(numuv,1,AI_TYPE_POINT2)
                    for i in range(numuv):
                        AiArraySetUInt(uvidxs,i,i)
                        AiArraySetPnt2(uvlist,i,AtPoint2(uvset.data[0].uv[i][0],uvset.data[0].uv[i][1]))
                    AiNodeSetArray(self.amesh,"uvidxs",uvidxs)
                    AiNodeSetArray(self.amesh,"uvlist",uvlist)

                # write the matrix
                matrices = AiArrayAllocate(1, 1, AI_TYPE_MATRIX);
                mmatrix = pm.matrix_world.copy()
##                mmatrix = pm.matrix_world.copy().identity()
##                #tmatrix = mmatrix.transposed()
                matrix = utils.getYUpMatrix(mmatrix)
                AiArraySetMtx(matrices,0,matrix)
                AiNodeSetArray(self.amesh,'matrix',matrices)

                # write shader
                AiNodeSetPtr(self.amesh,"shader",self.shader_node)
