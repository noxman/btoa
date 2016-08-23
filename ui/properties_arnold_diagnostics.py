#
# arnold For Blender
#
import bpy

class ARNOLD_diagnostics_log(bpy.types.Panel):
    bl_label = "Log"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    #bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'4'}
    COMPAT_ENGINES = {'arnold_renderer'}
    @classmethod
    def poll(cls, context):
        arnold_menu = context.scene.arnold.ArnoldEnum
        rd = context.scene.render
        return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES) and (arnold_menu in cls.tabNum)
    def draw(self, context):
        layout = self.layout
        scn = context.scene.arnold
        row = layout.row()
        row.prop(scn, 'Log_verbosity_level')
        row = layout.row()
        row.prop(scn, 'Log_console')
        row = layout.row()
        row.prop(scn, 'Log_file')
        col = layout.column()
        col.enabled = False
        row = col.row()
        if scn.Log_file == True:
            col.enabled = True
        row.prop(scn, 'Log_file_path')
        row = layout.row()
        row.prop(scn, 'Log_max_warnings')

class ARNOLD_diagnostics_error(bpy.types.Panel):
    bl_label = "Error handing"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'4'}
    COMPAT_ENGINES = {'arnold_renderer'}
    @classmethod
    def poll(cls, context):
        arnold_menu = context.scene.arnold.ArnoldEnum
        rd = context.scene.render
        return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES) and (arnold_menu in cls.tabNum)
    def draw(self, context):
        layout = self.layout
        scn = context.scene.arnold
        row = layout.row()
        row.prop(scn, 'Error_abort')
        row = layout.row()
        row.prop(scn, 'Error_texture_error')
        row = layout.row()
        row.prop(scn, 'Error_nan_error')
##def register():
##    bpy.utils.register_module(__name__)
##
##def unregister():
##    bpy.utils.unregister_module(__name__)