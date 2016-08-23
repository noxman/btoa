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
bpy.types.Lamp.atype = EnumProperty(items=LampType)
bpy.types.Lamp.lamp_exposure = FloatProperty(
                                name = "Exposure",
                                precision = 3,
                                step = 1,
                                description = "Enter an float",default = 0)
##bpy.types.Lamp.Camera_exposure = FloatProperty(
##                                name = "Exposure",
##                                precision = 3,
##                                min = -5, max = 5,
##                                step = 1,
##                                description = "Enter an float",default = 0.000)
##bpy.types.Lamp.Camera_rollingshutter = EnumProperty(items = RollingShutter, default = "0", name = "Rolling Shutter")
##bpy.types.Lamp.Camera_rollingshutterduration = FloatProperty(
##                                name = "Rolling Shutter Duration",
##                                precision = 3,
##                                min = 0, max = 1,
##                                step = 1,
##                                description = "Enter an float",default = 0.000)
##
##def register():
##    bpy.utils.register_module(__name__)
##
##def unregister():
##    bpy.utils.unregister_module(__name__)