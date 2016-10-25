#
# arnold For Blender
#
import math
import bpy
from .python.arnold import *

class World:
    def __init__(self, scene, options=None):
        self.scene = scene
        self.options = options
    def writeWorld(self):
        if self.scene.world:
            world = self.scene.world.arnold
            worldname = self.scene.world.name
            if world.arnold_sky == True:
                if world.sky_type == '0':
                    arnoldworld = AiNode("sky")
                    if self.options:
                        AiNodeSetPtr(self.options,"background",arnoldworld)
                    AiNodeSetStr(arnoldworld,"name",worldname)
                    AiNodeSetRGB(arnoldworld,"color",world.sky_color.r,world.sky_color.g,world.sky_color.b)
                    if world.sky_format == '0':
                        AiNodeSetStr(arnoldworld,"format",'0')
                    elif world.sky_format == '1':
                        AiNodeSetStr(arnoldworld,"format",'1')
                    else:
                        AiNodeSetStr(arnoldworld,"format",'2')
                    AiNodeSetFlt(arnoldworld,"intensity",world.sky_intensity)
                    # if world.casts_shadows == True:
                    #     AiNodeSetBool(arnoldworld,"casts_shadows",True)
                    # else:    
                    #     AiNodeSetBool(arnoldworld,"casts_shadows",False)
                    # if world.primary_visibility == True:
                    #     AiNodeSetBool(arnoldworld,"primary_visibility",True)
                    # else:    
                    #     AiNodeSetBool(arnoldworld,"primary_visibility",False)
                    # if world.visible_reflections == True:
                    #     AiNodeSetBool(arnoldworld,"visible_reflections",True)
                    # else:    
                    #     AiNodeSetBool(arnoldworld,"visible_reflections",False)
                    # if world.visible_refractions == True:
                    #     AiNodeSetBool(arnoldworld,"visible_refractions",True)
                    # else:    
                    #     AiNodeSetBool(arnoldworld,"visible_refractions",False)
                    # if world.visible_diffuse == True:
                    #     AiNodeSetBool(arnoldworld,"visible_diffuse",True)
                    # else:    
                    #     AiNodeSetBool(arnoldworld,"visible_diffuse",False)
                    # if world.visible_glossy == True:
                    #     AiNodeSetBool(arnoldworld,"visible_glossy",True)
                    # else:    
                    #     AiNodeSetBool(arnoldworld,"visible_glossy",False)
                    AiNodeSetFlt(arnoldworld,"X_angle",world.sky_rotate[0])
                    AiNodeSetFlt(arnoldworld,"Y_angle",world.sky_rotate[1])
                    AiNodeSetFlt(arnoldworld,"Z_angle",world.sky_rotate[2])
                    AiNodeSetVec(arnoldworld,"X",world.sky_scale[0],0,0)
                    AiNodeSetVec(arnoldworld,"Y",0,world.sky_scale[1],0)
                    AiNodeSetVec(arnoldworld,"Z",0,0,world.sky_scale[2])
                    AiNodeSetBool(arnoldworld,"opaque_alpha",True)
                else:
                    arnoldworld = AiNode("physical_sky")
                    if self.options:
                        AiNodeSetPtr(self.options,"background",arnoldworld)
                    AiNodeSetStr(arnoldworld,"name",worldname)
                    AiNodeSetFlt(arnoldworld,"turbidity",world.physical_sky_turbidity)
                    AiNodeSetRGB(arnoldworld,"ground_albedo",world.physical_sky_ground_albedo.r,
                    world.physical_sky_ground_albedo.g,world.physical_sky_ground_albedo.b)
                    # AiNodeSetBool(arnoldworld,"use_degrees",True)
                    AiNodeSetFlt(arnoldworld,"elevation",math.degrees(world.physical_sky_elevation))
                    AiNodeSetFlt(arnoldworld,"azimuth",math.degrees(world.physical_sky_azimuth))
                    AiNodeSetFlt(arnoldworld,"intensity",world.physical_sky_intensity)
                    AiNodeSetRGB(arnoldworld,"sky_tint",world.physical_sky_tint.r,
                    world.physical_sky_tint.g,world.physical_sky_tint.b)
                    AiNodeSetRGB(arnoldworld,"sun_tint",world.physical_sky_sun_tint.r,
                    world.physical_sky_sun_tint.g,world.physical_sky_sun_tint.b)
                    AiNodeSetFlt(arnoldworld,"sun_size",world.physical_sky_sun_size)
                    if world.physical_sky_sun:
                        AiNodeSetBool(arnoldworld,"enable_sun",True)
                    else:
                        AiNodeSetBool(arnoldworld,"enable_sun",False)
                if world.skydome_enable:   
                    arnoldskydome = AiNode("skydome_light")
                    AiNodeSetStr(arnoldskydome,"name",worldname+"_skydome_light")
                    if world.skydome_follow_sky_color:
                        AiNodeSetRGB(arnoldskydome,"color",world.sky_color.r,world.sky_color.g,world.sky_color.b)
                    else:
                        AiNodeSetRGB(arnoldskydome,"color",world.skydome_color.r,world.skydome_color.g,world.skydome_color.b)
                    if world.skydome_follow_sky_intensity:
                        AiNodeSetFlt(arnoldskydome,"intensity",world.sky_intensity)
                    else:
                        AiNodeSetFlt(arnoldskydome,"intensity",world.skydome_intensity) 
                    AiNodeSetFlt(arnoldskydome,"exposure",world.skydome_exposure)
                    AiNodeSetInt(arnoldskydome,"resolution",world.skydome_resolution)
                    if world.skydome_format == '0':
                        AiNodeSetStr(arnoldskydome,"format",'0')
                    elif world.skydome_format == '1':
                        AiNodeSetStr(arnoldskydome,"format",'1')
                    else:
                        AiNodeSetStr(arnoldskydome,"format",'2')
                    AiNodeSetInt(arnoldskydome,"samples",world.skydome_samples)
                    if world.skydome_normalize:
                        AiNodeSetBool(arnoldskydome,"normalize",True)
                    else:
                        AiNodeSetBool(arnoldskydome,"normalize",False)
                    if world.skydome_case_shadows:
                        AiNodeSetBool(arnoldskydome,"cast_shadows",True)
                    else:
                        AiNodeSetBool(arnoldskydome,"cast_shadows",False)
                    AiNodeSetFlt(arnoldskydome,"shadow_density",world.skydome_shadow_density)
                    AiNodeSetRGB(arnoldskydome,"shadow_color",world.skydome_shadow_color.r,world.skydome_shadow_color.g,world.skydome_shadow_color.b)
                    if world.skydome_affect_volumetrics:
                        AiNodeSetBool(arnoldskydome,"affect_volumetrics",True)
                    else:
                        AiNodeSetBool(arnoldskydome,"affect_volumetrics",False)
                    if world.skydome_cast_volumetric_shadows:
                        AiNodeSetBool(arnoldskydome,"cast_volumetric_shadows",True)
                    else:
                        AiNodeSetBool(arnoldskydome,"cast_volumetric_shadows",False)   
                    AiNodeSetInt(arnoldskydome,"volume_samples",world.skydome_volume_samples)
                    AiNodeSetFlt(arnoldskydome,"diffuse",world.skydome_diffuse)
                    AiNodeSetFlt(arnoldskydome,"specular",world.skydome_specular)
                    AiNodeSetFlt(arnoldskydome,"sss",world.skydome_sss)
                    AiNodeSetFlt(arnoldskydome,"indirect",world.skydome_indirect)
                    AiNodeSetFlt(arnoldskydome,"volume",world.skydome_volume)
                    AiNodeSetInt(arnoldskydome,"max_bounces",world.skydome_max_bounces)
            else:
                return       
