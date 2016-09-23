#
# arnold For Blender
#

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

def update_preview(self, context):
    context.material.preview_render_type = context.material.preview_render_type

class ArnoldMaterialSetting(bpy.types.PropertyGroup):
    name="ArnoldMaterialSettings"

    diffuse_color = FloatVectorProperty(update=update_preview, name="color",
                                subtype='COLOR',
                                min=0.0, max=1.0,
                                default=[0.8,0.8,0.8])
    lamp_color = FloatVectorProperty(update=update_preview, name="color",
                                subtype='COLOR',
                                min=0.0, max=1.0,
                                default=[1.0,1.0,1.0])
    diffuse_weight = FloatProperty(
                                update=update_preview, name = "Weight",
                                precision = 3,
                                step = 1,
                                min = 0, max = 1,
                                description = "Enter an float",default = 0.7)
    diffuse_roughness = FloatProperty(
                                update=update_preview, name = "Roughness",
                                precision = 3,
                                step = 1,
                                min = 0, max = 1,
                                description = "Enter an float",default = 0)

##def register():
##    bpy.utils.register_module(__name__)
##
##def unregister():
##    bpy.utils.unregister_module(__name__)
