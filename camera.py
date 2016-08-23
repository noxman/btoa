import math
import bpy
from .python.arnold import *
from . import utils

#################
# Camera
################
##Cam = bpy.types.Camera
##Cam.BtoA_aperture_size = FloatProperty(name="Aperture",description="Aperture Size",
##                        min = 0,max=100,default=0)
##Cam.BtoA_aperture_blades =  IntProperty(
##        name="Aperture Blades", description="Blades",
##        min=0, max=16, default=0)
##
class Camera():
    def __init__(self,render):
        self.scene  = bpy.context.scene
        self.camera = bpy.data.cameras[self.scene.camera.data.name]
        self.render = render

    def writeCamera(self):

        #create the node
        acam = AiNode("persp_camera")
        self.name = self.camera.name
        self.ArnoldCamera = acam
        AiNodeSetStr(acam,"name",self.name)

        # FOV
        if self.render.size_x > self.render.size_y:
            self.fov = self.camera.angle
        else:
            FovV = 2.0 * ( math.atan( ( self.render.size_y / 2.0 ) / self.camera.angle ) )
            self.fov = ( self.render.size_x / 2.0 ) / math.tan( FovV / 2.0 )
##
        fovAr = AiArrayAllocate(1, 1, AI_TYPE_FLOAT)
        AiArraySetFlt(fovAr, 0, math.degrees(self.fov))
        AiNodeSetArray(acam,"fov",fovAr)

        #AiNodeSetFlt(acam,b"aspec_ratio",self.render.size_x/self.render.size_y)
        # matrix
        matrices = AiArrayAllocate(1, 1, AI_TYPE_MATRIX);
        bmatrix= self.scene.camera.matrix_world.copy()
        #bmatrix = Matrix.Rotation(math.radians(-90),4,'X')  * bmatrix
        matrix = utils.getYUpMatrix(bmatrix)
        AiArraySetMtx(matrices,  0 , matrix)
        AiNodeSetArray(acam, "matrix", matrices)
        # clipping
        AiNodeSetFlt(acam,"near_clip",self.camera.clip_start)
        AiNodeSetFlt(acam,"far_clip",self.camera.clip_end)
        # DOF
##        AiNodeSetFlt(acam,"aperture_size",self.camera.BtoA_aperture_size)
##        fpAr = AiArrayAllocate(1, 1, AI_TYPE_FLOAT)
##        AiArraySetFlt(fpAr, 0, self.camera.dof_distance)
##        AiNodeSetArray(acam,"focus_distance",fpAr)