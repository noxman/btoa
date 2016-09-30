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
        name="Enable Sky",
        description="True or False?")
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
        name="Casts Shadows",
        description="True or False?")
    primary_visibility = BoolProperty(
        name="Primary visibility",
        description="True or False?")
    visible_reflections = BoolProperty(
        name="Reflections",
        description="True or False?")
    visible_refractions = BoolProperty(
        name="Refractions",
        description="True or False?")
    visible_diffuse = BoolProperty(
        name="Diffuse",
        description="True or False?")
    visible_glossy = BoolProperty(
        name="Glossy",
        description="True or False?")
    sky_rotate = IntVectorProperty(
        name="Rotate", description="",
        step=1,
        default=(0, 0, 0), subtype='XYZ')
    sky_scale = IntVectorProperty(
        name="Scale", description="",
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
        name="Elevation",
        precision=3,
        step=1,
        min=math.radians(0), max=math.radians(180),
        subtype="ANGLE",
        description="Enter an float", default=math.radians(45))
    physical_sky_azimuth = FloatProperty(
        name="Azimuth",
        precision=3,
        step=1,
        min=math.radians(0), max=math.radians(360),
        subtype="ANGLE",
        description="Enter an float", default=math.radians(90))
    physical_sky_intensity = FloatProperty(
        name="Intensity",
        precision=2,
        step=1,
        min=0, max=10,
        description="Enter an float", default=1)
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
        precision=2,
        step=1,
        min=0,
        description="Enter an float", default=0.51)
    physical_sky_sun = BoolProperty(
        name="Enable Sun",
        description="True or False?")

    skydome_enable = BoolProperty(
        name="Enable",
        description="True or False?",
        default = True)
    skydome_follow_sky_color = BoolProperty(
        name="Follow Sky Color",
        description="True or False?",
        default = True)
    skydome_color = FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        min=0.0, max=1.0,
        default=[1, 1, 1])
    skydome_follow_sky_intensity = BoolProperty(
        name="Follow Sky Color",
        description="True or False?",
        default = True)
    skydome_intensity = FloatProperty(
        name="Intensity",
        precision=2,
        step=1,
        min=0.0,
        description="Enter an float", default=1)
    skydome_exposure = FloatProperty(
        name="Exposure",
        precision=2,
        step=1,
        description="Enter an float", default=0)
    skydome_resolution = IntProperty(
        name="Resolution",
        step=1,
        description="Enter an float", default=1000)
    skydome_format = EnumProperty(items=SkyFormat)
    skydome_samples = IntProperty(
        name="Samples",
        min=0,
        step=1,
        description="Enter an Int", default=1)
    skydome_normalize = BoolProperty(
        name="Normalize",
        description="True or False?",
        default = True)
    skydome_case_shadows = BoolProperty(
        name="Cast Shadows",
        description="True or False?",
        default = True)
    skydome_case_shadows = BoolProperty(
        name="Cast Shadows",
        description="True or False?",
        default = True)
    skydome_shadow_density = FloatProperty(
        name="Shadow Density",
        precision=2,
        step=1,
        min=0.0, max=1.0,
        description="Enter an float", default=1)
    skydome_shadow_color = FloatVectorProperty(
        name="Shadow Color",
        subtype='COLOR',
        min=0.0, max=1.0,
        default=[0, 0, 0])
    skydome_affect_volumetrics = BoolProperty(
        name="Affect Volumetrics",
        description="True or False?",
        default = True)
    skydome_cast_volumetric_shadows = BoolProperty(
        name="Cast Volumetric Shadows",
        description="True or False?",
        default = True)
    skydome_samples = IntProperty(
        name="Samples",
        min=0,
        step=1,
        description="Enter an Int", default=1)
    skydome_volume_samples = IntProperty(
        name="Volume Samples",
        min=0,
        step=1,
        description="Enter an Int", default=2)
    skydome_diffuse = FloatProperty(
        name="Diffuse",
        precision=2,
        step=1,
        min=0.0, max=1.0,
        description="Enter an float", default=1)
    skydome_specular = FloatProperty(
        name="Specular",
        precision=2,
        step=1,
        min=0.0, max=1.0,
        description="Enter an float", default=1)
    skydome_sss = FloatProperty(
        name="SSS",
        precision=2,
        step=1,
        min=0.0, max=1.0,
        description="Enter an float", default=1)
    skydome_indirect = FloatProperty(
        name="Indirect",
        precision=2,
        step=1,
        min=0.0, max=1.0,
        description="Enter an float", default=1)
    skydome_volume = FloatProperty(
        name="Volume",
        precision=2,
        step=1,
        min=0.0, max=1.0,
        description="Enter an float", default=1)
    skydome_max_bounces = IntProperty(
        name="Max Bounces",
        step=1,
        description="Enter an int", default=999)
