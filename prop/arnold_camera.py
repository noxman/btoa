#
# arnold For Blender
#

import bpy
import math

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


class ArnoldCameraSetting(bpy.types.PropertyGroup):
    name="ArnoldCameraSettings"

    camera_type = EnumProperty(items=CameraType)
    camera_angle = FloatProperty(
                                name = "FOV",
                                precision = 3,
                                step = 1,
                                min = math.radians(1), max = math.radians(165),
                                subtype = "ANGLE",
                                description = "Enter an float",default = math.radians(54.43))
    camera_lens = FloatProperty(
                                name = "Lens",
                                precision = 3,
                                step = 1,
                                min = 1,
                                description = "Enter an float",default = 35.0)
    camera_clip_start = FloatProperty(
                                name = "clip_start",
                                precision = 3,
                                step = 1,
                                min = 0.001,
                                description = "Enter an float",default = 0.1)
    camera_clip_end = FloatProperty(
                                name = "clip_end",
                                precision = 3,
                                step = 1,
                                min = 0.001,
                                description = "Enter an float",default = 10000.0)
    camera_scale = FloatProperty(
                                name = "Scale",
                                precision = 3,
                                step = 1,
                                description = "Enter an float",default = 1.0)
    camera_exposure = FloatProperty(
                                name = "Exposure",
                                precision = 3,
                                step = 1,
                                description = "Enter an float",default = 0.000)
    camera_rollingshutter = EnumProperty(items = RollingShutter, default = "0", name = "Rolling Shutter")
    camera_rollingshutterduration = FloatProperty(
                                name = "Rolling Shutter Duration",
                                precision = 3,
                                min = 0, max = 1,
                                step = 1,
                                description = "Enter an float",default = 0.000)

##def register():
##    bpy.utils.register_module(__name__)
##
##def unregister():
##    bpy.utils.unregister_module(__name__)
