import bpy
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

class ArnoldCurveSetting(bpy.types.PropertyGroup):
    name="ArnoldCurveSettings"

    curve_render = BoolProperty(
	        name = "Arnold Render",
	        description = "True or False?")
    curve_width = FloatProperty(
            name = "Curve width",
            min = 0, 
            precision = 3,
            step = 1,
            description = "Enter an float",default = 1)
    curve_scale = BoolProperty(
        name = "Curve scale",
        description = "True or False?")