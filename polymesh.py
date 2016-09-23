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

    def object_on_visible_layer(self, obj):
        obj_visible = False
        for layer_visible in [object_layers and scene_layers for object_layers, scene_layers in zip(obj.layers, self.scene.layers)]:
            obj_visible |= layer_visible
        return obj_visible

    def writePolymesh(self):
        for pm in self.scene.objects:
            subsurf = False
            if pm.hide_render == False and pm.type == "MESH" and self.object_on_visible_layer(pm):
                if len(pm.modifiers) > 0:
                    for mod in pm.modifiers:
                        if mod.type == "SUBSURF" and mod.show_render:
                            subsurf = mod
                            try:
                                subsurf.show_render = False
                            except:
                                pass
                    pm_data = pm.to_mesh(self.scene,True,'RENDER',True)
                else:
                    pm_data = pm.data
                self.exportPolymesh(pm,pm_data,subsurf)
            elif pm.hide_render == False and (pm.type == "SURFACE" or pm.type == "FONT"):
                pm_data = pm.to_mesh(self.scene,True,'RENDER',True)
                self.exportPolymesh(pm,pm_data)
    def exportPolymesh(self,obj,data,subsurf = False):
        self.obj = obj
        self.data = data
        self.subsurf = subsurf
        # create the node
        self.amesh = AiNode("polymesh")
        AiNodeSetStr(self.amesh,"name",self.obj.name)

        # create shorthand variables
        faces = self.data.polygons
        smooth_count = 0
        for face in faces:
            if face.use_smooth == True:
                smooth_count += 1
        if smooth_count == len(faces):
            AiNodeSetBool(self.amesh,"smoothing",True)
        vertices = self.data.vertices
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

##        # uvs
##        if len(self.data.uv_textures) > 0:
##            uvset = self.data.uv_textures[0]
##            numuv = len(uvset.data[0].uv)
##            uvidxs = AiArrayAllocate(numuv,1,AI_TYPE_UINT)
##            uvlist = AiArrayAllocate(numuv,1,AI_TYPE_POINT2)
##            for i in range(numuv):
##                AiArraySetUInt(uvidxs,i,i)
##                AiArraySetPnt2(uvlist,i,AtPoint2(uvset.data[0].uv[i][0],uvset.data[0].uv[i][1]))
##            AiNodeSetArray(self.amesh,"uvidxs",uvidxs)
##            AiNodeSetArray(self.amesh,"uvlist",uvlist)

        # write the matrix
        matrices = AiArrayAllocate(1, 1, AI_TYPE_MATRIX);
        mmatrix = obj.matrix_world.copy()
        matrix = utils.getYUpMatrix(mmatrix)
        AiArraySetMtx(matrices,0,matrix)
        AiNodeSetArray(self.amesh,'matrix',matrices)

        # write shader
        AiNodeSetPtr(self.amesh,"shader",self.shader_node)

        # Sub surface
        if self.subsurf != False:
            AiNodeSetInt(self.amesh,"subdiv_type",1)
            AiNodeSetInt(self.amesh,"subdiv_iterations",subsurf.render_levels)
            self.subsurf.show_render = True