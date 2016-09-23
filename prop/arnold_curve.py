import bpy
from bpy.props import (StringProperty,
                        BoolProperty,
                        IntProperty,
                        FloatProperty,
                        FloatVectorProperty,
                        EnumProperty,
                        PointerProperty,
                        FloatVectorProperty,
                        BoolVectorProperty
                        )
from .classes import *

class ArnoldCurveSetting(bpy.types.PropertyGroup):
    name="ArnoldCurveSettings"

    curve_render = BoolProperty(
        name = "Render",
        description = "True or False?")
