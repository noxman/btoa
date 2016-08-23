#
# arnold For Blender
#
import bpy

class ARNOLD_system_rendersettings(bpy.types.Panel):
    bl_label = "Render settings"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    #bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'2'}
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
        row.prop(scn, 'Render_bucket_scanning')
        row = layout.row()
        row.prop(scn, 'Render_buket_size')
        row = layout.row()
        row.prop(scn, 'Render_display_bucket')
        row = layout.row()
        row.prop(scn, 'Render_autodetect_threads')
        col = layout.column()
        col.enabled = False
        row = col.row()
        row.prop(scn, 'Render_threads')
        if scn.Render_autodetect_threads == False:
            col.enabled = True
        row = layout.row()
        row.prop(scn, 'Render_expand_procedurals')
        row = layout.row()
        row.prop(scn, 'Render_export_scale')
        row = layout.row()
        row.prop(scn, 'Ipr_progressive_refinement')
        row = layout.row()
        row.prop(scn, 'Ipr_initial_sampling')

class ARNOLD_system_ipr(bpy.types.Panel):
    bl_label = "IPR"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'2'}
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
        row.prop(scn, 'Ipr_progressive_refinement')
        row = layout.row()
        row.prop(scn, 'Ipr_initial_sampling')

class ARNOLD_system_searchpaths(bpy.types.Panel):
    bl_label = "Search paths"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'2'}
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
        row.prop(scn, 'Search_procedural_path')
        row = layout.row()
        row.prop(scn, 'Search_shader_path')
        row = layout.row()
        row.prop(scn, 'Search_texture_path')

class ARNOLD_system_licensing(bpy.types.Panel):
    bl_label = "Licensing"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'2'}
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
        row.prop(scn, 'Licensing_abort')
        row = layout.row()
        row.prop(scn, 'Licensing_skip')

##def register():
##    bpy.utils.register_module(__name__)
##
##def unregister():
##    bpy.utils.unregister_module(__name__)