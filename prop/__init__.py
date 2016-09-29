#
# arnold For Blender
#

from . import arnold_scene
from . import arnold_camera
from . import arnold_lamp
from . import arnold_material
from . import arnold_curve
from . import arnold_world

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)