#
# arnold For Blender
#
import bpy
from .python.arnold import *

class Standard():
    def write(mat,textures):
        tslots = {}
        tslots['kd_color'] = None