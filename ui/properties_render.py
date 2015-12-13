#
# arnold For Blender
#
import bpy
from btoa.ui import classes

class ARNOLD_RP_render(classes.ArnoldRenderPanel):
    bl_label = ""
    bl_options = {'HIDE_HEADER'}
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("arnold.button", text="Render",icon="RENDER_STILL")
class ARNOLD_tab_render(classes.ArnoldRenderPanel):
    bl_label = ""
    bl_options = {'HIDE_HEADER'}
    def draw(self, context):      
        layout = self.layout
        scn = context.scene.arnold
        layout.prop(scn,'ArnoldEnum',expand=True)
        #arnold_menu = context.scene.ArnoldEnum       

class ARNOLD_main_sampling(classes.ArnoldRenderPanel):
    bl_label = "Sampling"
    #bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'0'}
    COMPAT_ENGINES = {'arnold_renderer'}
    @classmethod
    def poll(cls, context):
        scn = context.scene.arnold
        rd = context.scene.render
        return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES) and (scn.ArnoldEnum in cls.tabNum)
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
        row.prop(scn, 'CameraInt',text = "Camera(AA)")
        row = layout.row()
        row.prop(scn, 'DiffuseInt',text = "Diffuse")
        row = layout.row()
        row.prop(scn, 'GlossyInt',text = "Glossy")
        row = layout.row()
        row.prop(scn, 'RefractionInt',text = "Refraction")
        row = layout.row()
        row.prop(scn, 'SSSInt',text = "SSS")
        row = layout.row()
        row.prop(scn, 'Volume_indirectInt', text = "Volumeindirect")
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
            row.prop(scn, 'Clamp_max', text = "Max value")   
        row = layout.row()
        row.prop(scn,'Filter_Types', text = "Default filter.type")
        row = layout.row()
        t_sub_filter = ['9','11','15']
        sub_filter = ['0','5','6','8','10','13','14']
        for choice in sub_filter:
            if scn.Filter_Types == choice:
                row = layout.row()
                #box = row.box()
                row.prop(scn, 'Filter_width', text = "Default filter.width") 
        if scn.Filter_Types == '9':
            row = layout.row()
            row.prop(scn, 'Filter_Domain')
        elif scn.Filter_Types == '11':
            row = layout.row()
            row.prop(scn, 'Filter_minimum', text = "Default filter.minimum")
            row.prop(scn, 'Filter_minimum', text = "Default filter.maximum")
        elif scn.Filter_Types == '15':
            row = layout.row()
            row.prop(scn, 'Filter_width', text = "Default filter.width") 
            row = layout.row()
            row.prop(scn, 'Motion_blur_position', text = "Positon")  
       
class ARNOLD_main_Ray_depth(classes.ArnoldRenderPanel):
    bl_label = "Ray depth"
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'0'}
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
        row.prop(scn, 'Ray_depth_total',text = "Total")
        row = layout.row()
        row.prop(scn, 'Ray_depth_diffuse',text = "Diffuse")
        row = layout.row()
        row.prop(scn, 'Ray_depth_glossy',text = "Glossy")
        row = layout.row()
        row.prop(scn, 'Ray_depth_reflection',text = "Reflection")
        row = layout.row()
        row.prop(scn, 'Ray_depth_refraction',text = "Refraction")
        row = layout.row()
        row.prop(scn, 'Ray_depth_volume',text = "Volume")
        row = layout.row()
        row.prop(scn, 'Ray_depth_trans_depth',text = "Transparency depth")
        row = layout.row()
        row.prop(scn, 'Ray_depth_trans_threshold',text = "Transparency threshold")
class ARNOLD_main_Environment(classes.ArnoldRenderPanel):
    bl_label = "Environment"
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'0'}
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
        row.prop(scn, 'background_set', text = "Background")
        row = layout.row()
        row.label('Atmosphere')
        row.prop(scn, 'Ray_depth_total')
class ARNOLD_main_Motion_blur(classes.ArnoldRenderPanel):
    bl_label = "Motion blur"
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'0'}
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
        row.prop(scn, 'Motion_blur_position', text = "Posiotn")
        row = col.row()
        sub_col = row.column()
        sub_row = sub_col.row()
        sub_row.enabled = False
        if scn.Motion_blur_position == '3':
            sub_row.enabled = True
        sub_row.prop(scn, 'Motion_blur_start', text = "Start") 
        sub_row.prop(scn, 'Motion_blur_end', text = "End") 
        sub_row_l = sub_col.row()
        sub_row_l.enabled = False
        if scn.Motion_blur_position != '3':
            sub_row_l.enabled = True 
            sub_row.enabled = False    
        sub_row_l.prop(scn, 'Motion_blur_length', text = "Length")
class ARNOLD_main_lights(classes.ArnoldRenderPanel):
    bl_label = "Lights"
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'0'}
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
        row.prop(scn, 'Main_lights', text = "Low light threshold")
class ARNOLD_main_textures(classes.ArnoldRenderPanel):
    bl_label = "Textures"
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'0'}
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
        
class Arnold_panel_Button(bpy.types.Operator):
    bl_idname = "arnold.button"
    bl_label = "Button"
    
def register():
    bpy.utils.register_class(ARNOLD_RP_render) 
    bpy.utils.register_class(ARNOLD_tab_render)
    bpy.utils.register_class(ARNOLD_main_sampling) 
    bpy.utils.register_class(ARNOLD_main_Ray_depth)
    bpy.utils.register_class(ARNOLD_main_Environment) 
    bpy.utils.register_class(ARNOLD_main_Motion_blur)
    bpy.utils.register_class(ARNOLD_main_lights)  
    bpy.utils.register_class(ARNOLD_main_textures)
    bpy.utils.register_class(Arnold_panel_Button)  
    
def unregister():
    bpy.utils.unregister_class(ARNOLD_RP_render) 
    bpy.utils.unregister_class(ARNOLD_tab_render) 
    bpy.utils.unregister_class(ARNOLD_main_sampling) 
    bpy.utils.unregister_class(ARNOLD_main_Ray_depth) 
    bpy.utils.unregister_class(ARNOLD_main_Environment)
    bpy.utils.unregister_class(ARNOLD_main_Motion_blur) 
    bpy.utils.unregister_class(ARNOLD_main_lights)
    bpy.utils.unregister_class(ARNOLD_main_textures)
    bpy.utils.unregister_class(Arnold_panel_Button)

#if __name__ == "__main__":
 #   register()
