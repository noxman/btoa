#
# arnold For Blender
#
import bpy

from bl_ui import properties_material
properties_material.MATERIAL_PT_preview.COMPAT_ENGINES.add('arnold_renderer')
del properties_material

class ARNOLD_renderer_sampling(bpy.types.Panel):
    bl_label = "Sampling"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    #bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'1'}
    COMPAT_ENGINES = {'arnold_renderer'}
    @classmethod
    def poll(cls, context):
        arnold_menu = context.scene.arnold.ArnoldEnum
        rd = context.scene.render
        return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES) and (arnold_menu in cls.tabNum)
    def draw(self, context):
        layout = self.layout
        scn = context.scene.arnold
        row=layout.row()
        row.label(("Camera(AA) Samples:%d") %(scn.CameraInt**2))
        row =layout.row()
        row.label(("Diffuse Samples:%d(max:%d)") %(((scn.DiffuseInt*scn.CameraInt)**2),((scn.DiffuseInt*scn.CameraInt)**2)))
        row =layout.row()
        row.label(("Glossy Samples:%d(max:%d)") %(((scn.GlossyInt*scn.CameraInt)**2),((scn.GlossyInt*scn.CameraInt)**2)))
        row =layout.row()
        row.label(("Refraction Samples:%d(max:%d)") %(((scn.RefractionInt*scn.CameraInt)**2),((scn.RefractionInt*scn.CameraInt)**2)+(scn.CameraInt**2)))
        row =layout.row()
        row.label(("Total (no light):%d(max:%d)") %((scn.CameraInt**2)*(1+scn.DiffuseInt**2+scn.GlossyInt**2+scn.RefractionInt**2),\
                                                    ((scn.CameraInt**2)*(1+scn.DiffuseInt**2+scn.GlossyInt**2+scn.RefractionInt**2)+scn.CameraInt**2)))

        row = layout.row()
        row.prop(scn, 'CameraInt')
        row = layout.row()
        row.prop(scn, 'DiffuseInt')
        row = layout.row()
        row.prop(scn, 'GlossyInt')
        row = layout.row()
        row.prop(scn, 'RefractionInt')
        row = layout.row()
        row.prop(scn, 'SSSInt')
        row = layout.row()
        row.prop(scn, 'Volume_indirectInt')
        row = layout.row()
        row.separator()
        row = layout.row()
        row.prop(scn, 'Lock_sampling')
        row = layout.row()
        row.prop(scn, 'Use_autobump_in_sss')
        row = layout.row()
        row.prop(scn, 'Clamp_sample')
        if scn.Clamp_sample ==True:
            row = layout.row()
            row.prop(scn, 'Affect_aovs')
            row.prop(scn, 'Clamp_max')
        row = layout.row()
        row.prop(scn,'Filter_Types')
        row = layout.row()
        t_sub_filter = ['9','11','15']
        sub_filter = ['0','5','6','8','10','13','14']
        for choice in sub_filter:
            if scn.Filter_Types == choice:
                row = layout.row()
                #box = row.box()
                row.prop(scn, 'Filter_width')
        if scn.Filter_Types == '9':
            row = layout.row()
            row.prop(scn, 'Filter_Domain')
        elif scn.Filter_Types == '11':
            row = layout.row()
            row.prop(scn, 'Filter_minimum')
            row.prop(scn, 'Filter_minimum')
        elif scn.Filter_Types == '15':
            row = layout.row()
            row.prop(scn, 'Filter_width')
            row = layout.row()
            row.prop(scn, 'Motion_blur_position')

class ARNOLD_renderer_Ray_depth(bpy.types.Panel):
    bl_label = "Ray depth"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'1'}
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
        row.prop(scn, 'Ray_depth_total')
        row = layout.row()
        row.prop(scn, 'Ray_depth_diffuse')
        row = layout.row()
        row.prop(scn, 'Ray_depth_glossy')
        row = layout.row()
        row.prop(scn, 'Ray_depth_reflection')
        row = layout.row()
        row.prop(scn, 'Ray_depth_refraction')
        row = layout.row()
        row.prop(scn, 'Ray_depth_volume')
        row = layout.row()
        row.prop(scn, 'Ray_depth_trans_depth')
        row = layout.row()
        row.prop(scn, 'Ray_depth_trans_threshold')

class ARNOLD_renderer_Environment(bpy.types.Panel):
    bl_label = "Environment"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'1'}
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
        row.prop(scn, 'Ray_depth_total')

class ARNOLD_renderer_Motion_blur(bpy.types.Panel):
    bl_label = "Motion blur"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'1'}
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
        row.prop(scn, 'Motion_blur_enable')
        col = layout.column()
        col.enabled = False
        if scn.Motion_blur_enable == True:
            col.enabled = True
        row = col.row()
        row.prop(scn, 'Motion_blur_deformation')
        row.prop(scn, 'Motion_blur_camera')
        row = col.row()
        row.prop(scn, 'Motion_blur_keys')
        row = col.row()
        row.label('Shutter angle 180.00')
        row = col.row()
        row.prop(scn, 'Motion_blur_position')
        row = col.row()
        sub_col = row.column()
        sub_row = sub_col.row()
        sub_row.enabled = False
        if scn.Motion_blur_position == '3':
            sub_row.enabled = True
        sub_row.prop(scn, 'Motion_blur_start')
        sub_row.prop(scn, 'Motion_blur_end')
        sub_row_l = sub_col.row()
        sub_row_l.enabled = False
        if scn.Motion_blur_position != '3':
            sub_row_l.enabled = True
            sub_row.enabled = False
        sub_row_l.prop(scn, 'Motion_blur_length')

class ARNOLD_renderer_lights(bpy.types.Panel):
    bl_label = "Lights"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'1'}
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
        row.prop(scn, 'Main_lights')

class ARNOLD_renderer_textures(bpy.types.Panel):
    bl_label = "Textures"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'1'}
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
        row.prop(scn, 'Texture_accept_unmipped')
        row = layout.row()
        row.prop(scn, 'Texture_auto_mipmap')
        row = layout.row()
        row.prop(scn, 'Texture_accept_untiled')
        row = layout.row()
        row.prop(scn, 'Texture_auto_tile')
        row = layout.row()
        row.prop(scn, 'Texture_tile_size')
        row = layout.row()
        row.prop(scn, 'Texture_use_existing')
        row = layout.row()
        row.prop(scn, 'Texture_max_cache')
        row = layout.row()
        row.prop(scn, 'Texture_max_open')
        row = layout.row()
        row.prop(scn, 'Texture_diffuse_blur')
        row = layout.row()
        row.prop(scn, 'Texture_glossy_blur')
##def register():
##    bpy.utils.register_module(__name__)
##
##def unregister():
##    bpy.utils.unregister_module(__name__)