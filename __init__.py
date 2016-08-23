from email.policy import default
bl_info = {
    "name": "Blender to Arnold 0.1",
    "author": "Noxman - xxc1982@gmail.com",
    "version": (0, 0, 1),
    "blender": (2, 7, 7),
    "location": "Render > Engine > Arnold",
    "description": "Arnold integration for blender",
    "warning": "Still early alpha",
    "wiki_url": "https://github.com/noxman/btoa",
    "tracker_url": "https://github.com/noxman/btoa/issues",
    "category": "Render"}


import bpy
from . import render
from . import prop
from . import ui
from bpy.props import (
                        PointerProperty,
                        )

def register():
    bpy.utils.register_module(__name__)
    bpy.types.Scene.arnold = PointerProperty(type = prop.arnold_scene.ArnoldSceneSetting)

def unregister():
    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.arnold

if __name__ == "__main__":
    register()