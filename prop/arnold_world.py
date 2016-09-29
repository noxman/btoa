#
# arnold For Blender
#
import bpy
import math

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       EnumProperty,
                       PointerProperty,
                       IntVectorProperty,
                       FloatVectorProperty,
                       BoolVectorProperty
                       )
from .classes import *


class ArnoldWorldSetting(bpy.types.PropertyGroup):
    name = "ArnoldWorldSettings"

    arnold_sky = BoolProperty(
        name = "Enable Sky",
        description = "True or False?")
    sky_type = EnumProperty(items=SkyType)
    sky_valuetype = EnumProperty(items=SkyValueType)
    sky_color = FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        min=0.0, max=1.0,
        default=[1, 1, 1])
    sky_colorvaluetype = EnumProperty(items=SkyValueType)
    sky_format = EnumProperty(items=SkyFormat)
    sky_intensity = FloatProperty(
        name="Intensity",
        precision=3,
        step=1,
        min=0.0,
        description="Enter an float", default=1)
    sky_intensityvaluetype = EnumProperty(items=SkyValueType)
    casts_shadows = BoolProperty(
        name = "Casts Shadows",
        description = "True or False?")
    primary_visibility = BoolProperty(
        name = "Primary visibility",
        description = "True or False?")
    visible_reflections = BoolProperty(
        name = "Reflections",
        description = "True or False?")
    visible_refractions = BoolProperty(
        name = "Refractions",
        description = "True or False?")
    visible_diffuse = BoolProperty(
        name = "Diffuse",
        description = "True or False?")
    visible_glossy = BoolProperty(
        name = "Glossy",
        description = "True or False?")
    sky_rotate = IntVectorProperty(
        name="Rotate", description = "",
        step=1, 
        default=(0, 0, 0), subtype='XYZ')
    sky_scale = IntVectorProperty(
        name="Scale", description = "",
        step=1, 
        default=(1, 1, 1), subtype='XYZ')

    physical_sky_turbidity = FloatProperty(
        name="Turbidity",
        precision=2,
        step=1,
        min=1, max=10,
        description="Enter an float", default=3)
    physical_sky_ground_albedo = FloatVectorProperty(
        name="Ground Albedo",
        subtype='COLOR',
        min=0.0, max=1.0,
        default=[0.1, 0.1, 0.1])
    physical_sky_elevation = FloatProperty(
        name = "Elevation",
        precision = 3,
        step = 1,
        min = math.radians(0), max = math.radians(180),
        subtype = "ANGLE",
        description = "Enter an float",default = math.radians(45))
    physical_sky_azimuth = FloatProperty(
        name = "Azimuth",
        precision = 3,
        step = 1,
        min = math.radians(0), max = math.radians(360),
        subtype = "ANGLE",
        description = "Enter an float",default = math.radians(90)) 
    physical_sky_intensity = FloatProperty(
        name = "Intensity",
        precision = 2,
        step = 1,
        min = 0, max = 10,
        description = "Enter an float",default = 1)
    physical_sky_tint = FloatVectorProperty(
        name="Sky Tint",
        subtype='COLOR',
        min=0.0, max=1.0,
        default=[1, 1, 1])
    physical_sky_sun_tint = FloatVectorProperty(
        name="Sun Tint",
        subtype='COLOR',
        min=0.0, max=1.0,
        default=[1, 1, 1])
    physical_sky_sun_size = FloatProperty(
        name="Sun Size",
        precision = 2,
        step = 1,
        min = 0,
        description = "Enter an float",default = 0.51)
    physical_sky_sun = BoolProperty(
        name = "Enable Sun",
        description = "True or False?")