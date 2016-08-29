import math
import bpy
from .python.arnold import *
from . import utils

#################
# Lights
################
class Lights:
    '''This class handles the export of all lights'''
    def __init__(self):
        self.lightDict = {}

    def writeLights(self):
        for li in bpy.data.lamps:
            if li.users !=0:
                blight = BaseLight(li)
                if li.arnold.lamp_atype == '0':
                    blight.alight = AiNode("point_light")
                elif li.arnold.lamp_atype == '1':
                    blight.alight = AiNode("spot_light")
                elif li.arnold.lamp_atype == '2':
                    blight.alight = AiNode("distant_light")
                elif li.arnold.lamp_atype == '3':
                    blight.alight = AiNode("quad_light")
                elif li.arnold.lamp_atype == '4':
                    blight.alight = AiNode("photometric_light")

                AiNodeSetStr(blight.alight,"name",blight.lightdata.name)
                # set position
                # fist apply the matrix
                matrices = AiArrayAllocate(1, 1, AI_TYPE_MATRIX);
                lmatrix = blight.light.matrix_world.copy()
                matrix = utils.getYUpMatrix(lmatrix)
                AiArraySetMtx(matrices,  0 , matrix)
                AiNodeSetArray(blight.alight, "matrix", matrices)
                # write all common attributes
                blight.write()
class BaseLight():
    def __init__(self, light):
        self.lightdata = light
        self.light = bpy.context.scene.objects[light.name]
        self.alight = None

    def write(self):
        ld = self.lightdata.arnold
        # intensity and color
        AiNodeSetStr(self.alight,"name",ld.name)
        AiNodeSetFlt(self.alight,"intensity",ld.lamp_intensity*100)
        AiNodeSetFlt(self.alight,"exposure",ld.lamp_exposure)
        AiNodeSetRGB(self.alight,"color",ld.lamp_color.r,ld.lamp_color.g,ld.lamp_color.b)

##        AiNodeSetBool(self.alight,b"mis",bl.mis)
##        # bounces
##        AiNodeSetInt(self.alight,b"max_bounces",bl.max_bounces)
##        AiNodeSetFlt(self.alight,b"indirect",bl.indirect)
##
##        # shadows
##        if not self.lightdata.BtoA.shadow_enable:
##            AiNodeSetBool(self.alight,b"cast_shadows",0)
##        else:
##            scol = self.lightdata.shadow_color
##            AiNodeSetRGB(self.alight,b"shadow_color",scol.r,scol.g,scol.b)
##            AiNodeSetFlt(self.alight,b"shadow_density",self.lightdata.BtoA.shadow_density)
##            AiNodeSetFlt(self.alight,b"radius",self.lightdata.shadow_soft_size)
##            AiNodeSetInt(self.alight,b"samples",self.lightdata.shadow_ray_samples)
##
##            AiNodeSetBool(self.alight,b"affect_diffuse",self.lightdata.use_diffuse)
##            AiNodeSetBool(self.alight,b"affect_specular",self.lightdata.use_specular)
