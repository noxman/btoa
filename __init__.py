bl_info = {
    "name": "Blender to Arnold 0.1",
    "author": "Noxman - xxc1982@gmail.com",
    "version": (0, 0, 1),
    "blender": (2, 7, 6),
    "location": "Render > Engine > Arnold",
    "description": "Arnold integration for blender",
    "warning": "Still early alpha",
    "wiki_url": "https://github.com/noxman/btoa",
    "tracker_url": "https://github.com/noxman/btoa/issues",
    "category": "Render"}
    
import bpy
from btoa import ui
from btoa import engine

def register():
    engine.register()
    ui.register()

def unregister():
    engine.unregister()
    ui.unregister()
