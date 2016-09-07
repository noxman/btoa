import bpy
from .python.arnold import *
from . import utils

class Curves:
    def __init__(self,scene,shader_node):
        self.scene = scene
        self.shader_node = shader_node

    def writeCurves(self):
        for pm in self.scene.objects:
            if pm.hide_render == False and pm.type == "CURVE":
                if len(pm.modifiers) == 0:
                    numCurves = len(pm.data.splines)
                    if numCurves:
                        # create the node
                        curves = AiNode("curves")
                        AiNodeSetStr(curves,"name",pm.name)

                        # calculate number of points
                        ptCounter = 0
                        cvCounter = 0
                        for curveIdx in range(numCurves):
                            spline = pm.data.splines[curveIdx]
                            if spline.type == 'BEZIER':
                                cvCounter += 1
                                numPoints = len(spline.bezier_points)
                                ptCounter += numPoints *3 -2
                        # set number of points
                        num_points = AiArrayAllocate(cvCounter,1,AI_TYPE_UINT)
                        points = AiArrayAllocate(ptCounter,1,AI_TYPE_POINT)
                        # use one radius for all curves !!!
                        radius = AiArrayAllocate(1,1,AI_TYPE_FLOAT)
                        AiArraySetFlt(radius, 0, 0.005)
                        ptCounter = 0
                        for curveIdx in range(numCurves):
                            spline = pm.data.splines[curveIdx]
                            if spline.type == 'BEZIER':
                                numPoints = len(spline.bezier_points)
                                AiArraySetUInt(num_points, curveIdx,
                                                      numPoints * 3 - 2)
                                for ptIdx in range(numPoints):
                                    pt = spline.bezier_points[ptIdx]
                                    if ptIdx == 0:
                                        AiArraySetPnt(points,
                                                             ptCounter,
                                                             AtPoint(pt.co[0], pt.co[1], pt.co[2]))
                                        ptCounter += 1
                                        AiArraySetPnt(points,
                                                             ptCounter,
                                                             AtPoint(pt.handle_right[0], pt.handle_right[1], pt.handle_right[2]))
                                        ptCounter += 1
                                    elif ptIdx == numPoints - 1:
                                        AiArraySetPnt(points,
                                                             ptCounter,
                                                             AtPoint(pt.handle_left[0], pt.handle_left[1], pt.handle_left[2]))
                                        ptCounter += 1
                                        AiArraySetPnt(points,
                                                             ptCounter,
                                                             AtPoint(pt.co[0], pt.co[1], pt.co[2]))
                                        ptCounter += 1
                                    else:
                                        AiArraySetPnt(points,
                                                             ptCounter,
                                                             AtPoint(pt.handle_left[0], pt.handle_left[1], pt.handle_left[2]))
                                        ptCounter += 1
                                        AiArraySetPnt(points,
                                                             ptCounter,
                                                             AtPoint(pt.co[0], pt.co[1], pt.co[2]))
                                        ptCounter += 1
                                        AiArraySetPnt(points,
                                                             ptCounter,
                                                             AtPoint(pt.handle_right[0], pt.handle_right[1], pt.handle_right[2]))
                                        ptCounter += 1

                        AiNodeSetArray(curves,"num_points",num_points)
                        AiNodeSetArray(curves,"points",points)
                        AiNodeSetArray(curves,"radius",radius)
                        matrices = AiArrayAllocate(1, 1, AI_TYPE_MATRIX);
                        mmatrix = pm.matrix_world.copy()
                        matrix = utils.getYUpMatrix(mmatrix)
                        AiArraySetMtx(matrices,0,matrix)
                        AiNodeSetArray(curves,'matrix',matrices)
##                # uvs
##                if len(pm_data.uv_textures) > 0:
##                    uvset = pm_data.uv_textures[0]
##                    numuv = len(uvset.data[0].uv)
##                    uvidxs = AiArrayAllocate(numuv,1,AI_TYPE_UINT)
##                    uvlist = AiArrayAllocate(numuv,1,AI_TYPE_POINT2)
##                    for i in range(numuv):
##                        AiArraySetUInt(uvidxs,i,i)
##                        AiArraySetPnt2(uvlist,i,AtPoint2(uvset.data[0].uv[i][0],uvset.data[0].uv[i][1]))
##                    AiNodeSetArray(self.amesh,"uvidxs",uvidxs)
##                    AiNodeSetArray(self.amesh,"uvlist",uvlist)
##
                        # write shader
                        AiNodeSetPtr(curves,"shader",self.shader_node)

##                if len(pm.modifiers) > 0: