#
# arnold For Blender
#
import bpy

class ARNOLD_override_user(bpy.types.Panel):
    bl_label = "User options"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    #bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'5'}
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
        row.prop(scn, 'User_options_overrider')

class ARNOLD_override_feature(bpy.types.Panel):
    bl_label = "Feature overrides"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'5'}
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
        row.prop(scn, 'Feature_override_textures')
        row = layout.row()
        row.prop(scn, 'Feature_override_shaders')
        row = layout.row()
        row.prop(scn, 'Feature_override_atmosphere')
        row = layout.row()
        row.prop(scn, 'Feature_override_lights')
        row = layout.row()
        row.prop(scn, 'Feature_override_shadows')
        row = layout.row()
        row.prop(scn, 'Feature_override_subdivision')
        row = layout.row()
        row.prop(scn, 'Feature_override_displacement')
        row = layout.row()
        row.prop(scn, 'Feature_override_bump')
        row = layout.row()
        row.prop(scn, 'Feature_override_normal')
        row = layout.row()
        row.prop(scn, 'Feature_override_motion')
        row = layout.row()
        row.prop(scn, 'Feature_override_depth')
        row = layout.row()
        row.prop(scn, 'Feature_override_subsurface')

class ARNOLD_override_subdivision(bpy.types.Panel):
    bl_label = "Subdivision"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'5'}
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
        row.prop(scn, 'Subdivision_max_subdivisions')

##def register():
##    bpy.utils.register_module(__name__)
##
##def unregister():
##    bpy.utils.unregister_module(__name__)