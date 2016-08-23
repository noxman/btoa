#
# arnold For Blender
#
import bpy

from bl_ui import properties_render
def adraw(cls, context):
    rd = context.scene.render
    if rd.engine == 'arnold_renderer':
        layout = cls.layout
        scn = context.scene.arnold
        layout.prop(scn,'ArnoldEnum',expand=True)
properties_render.RENDER_PT_render.COMPAT_ENGINES.add('arnold_renderer')
properties_render.RENDER_PT_render.append(adraw)

@classmethod
def comm_poll(cls, context):
    tabNum = {'0'}
    arnold_menu = context.scene.arnold.ArnoldEnum
    rd = context.scene.render
    return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES) and (arnold_menu in tabNum)
properties_render.RENDER_PT_dimensions.COMPAT_ENGINES.add('arnold_renderer')
properties_render.RENDER_PT_dimensions.poll = comm_poll
properties_render.RENDER_PT_output.COMPAT_ENGINES.add('arnold_renderer')
properties_render.RENDER_PT_output.poll = comm_poll
del properties_render

##def register():
##    bpy.utils.register_module(__name__)
##
##def unregister():
##    bpy.utils.unregister_module(__name__)