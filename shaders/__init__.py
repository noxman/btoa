#
# arnold For Blender
#

from .aiStandard import *

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)