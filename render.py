#
# arnold For Blender
#
import bpy
import os
import sys
from btoa.python.arnold import *

class Arnold_Render_Button(bpy.types.Operator):
    bl_idname = "arnold.render"
    bl_label = "Button"
    def execute(self, context):
# this should be a directory full of .ass files
        assdir = 'D:\\cornell.ass'
# begin, load first frame, and render it.
        AiBegin()
# use sorted() to get them in sequence
        AiMsgSetConsoleFlags(AI_LOG_ALL);
# first time, load ALL nodes
        AiASSLoad (assdir)
# and render your first frame.
        AiRender()
        print('done')
        return {'FINISHED'} 
        AiEnd()
def register():
    bpy.utils.register_module(__name__)
    
def unregister():
    bpy.utils.unregister_module(__name__)