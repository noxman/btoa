#
# arnold For Blender
#
import bpy
from btoa.ui import classes
from btoa.ui.classes import PanelGroups,FilterTypes,FilterDomain,MotionblurPositon
from bpy.props import *
from bpy.types import PropertyGroup
def initSceneProperties(scn):
 
    bpy.types.Scene.MyString = StringProperty(
        name = "String")
    scn['MyString'] = "Lorem ipsum dolor sit amet"
    return
class SceneSettingItem(bpy.types.PropertyGroup):
    ###------Render Tab------
    bpy.types.Scene.ArnoldEnum = bpy.props.EnumProperty(items=PanelGroups)
    ###------Sampling-------
    bpy.types.Scene.CameraInt = IntProperty(
        name = "", 
        min = 1, max = 10,
        description = "Enter an integer",default = 3)
    bpy.types.Scene.DiffuseInt = IntProperty(
        name = "", 
        min = 0, max = 10,
        description = "Enter an integer",default = 2)
    bpy.types.Scene.GlossyInt = IntProperty(
        name = "", 
        min = 0, max = 10,
        description = "Enter an integer",default = 2)
    bpy.types.Scene.RefractionInt = IntProperty(
        name = "", 
        min = 0, max = 10,
        description = "Enter an integer",default = 2)
    bpy.types.Scene.SSSInt = IntProperty(
        name = "", 
        min = 0, max = 10,
        description = "Enter an integer",default = 2)
    bpy.types.Scene.Volume_indirectInt = IntProperty(
        name = "", 
        min = 0, max = 10,
        description = "Enter an integer",default = 2)
    bpy.types.Scene.Lock_sampling = BoolProperty(
        name = "Lock sampling pattern", 
        description = "True or False?")
    bpy.types.Scene.Use_autobump_in_sss = BoolProperty(
        name = "Use autobump in SSS", 
        description = "True or False?")
    bpy.types.Scene.Clamp_sample = BoolProperty(
        name = "Clamp sample values", 
        description = "True or False?") 
    bpy.types.Scene.Affect_aovs = BoolProperty(
        name = "Affect AOVs", 
        description = "True or False?") 
    bpy.types.Scene.Clamp_max = FloatProperty(
        name = "", 
        min = 0.001, max = 100.000,
        precision = 3,
        step = 1,
        description = "Enter an float",default = 10)
    bpy.types.Scene.Filter_Types = bpy.props.EnumProperty(items=FilterTypes,default = "10")
    bpy.types.Scene.Filter_width = FloatProperty(
        name = "",
        precision = 2,
        step = 1,
        description = "Enter an float",default = 2) 
    bpy.types.Scene.Filter_Domain = bpy.props.EnumProperty(items=FilterDomain)
    bpy.types.Scene.Filter_minimum = FloatProperty(
        name = "",
        precision = 2,
        step = 1,
        description = "Enter an float",default = 0) 
    bpy.types.Scene.Filter_maximum = FloatProperty(
        name = "",
        precision = 2,
        step = 1,
        description = "Enter an float",default = 1) 
    bpy.types.Scene.Filter_scalar_mode = BoolProperty(
        name = "Default filter.scalar_mode", 
        description = "True or False?") 
    ###------Ray depth
    bpy.types.Scene.Ray_depth_total = IntProperty(
        name = "", 
        min = 0, max = 16,
        description = "Enter an integer",default = 10)
    bpy.types.Scene.Ray_depth_diffuse = IntProperty(
        name = "", 
        min = 0, max = 16,
        description = "Enter an integer",default = 1) 
    bpy.types.Scene.Ray_depth_glossy = IntProperty(
        name = "", 
        min = 0, max = 16,
        description = "Enter an integer",default = 1)           
    bpy.types.Scene.Ray_depth_reflection = IntProperty(
        name = "", 
        min = 0, max = 16,
        description = "Enter an integer",default = 2)     
    bpy.types.Scene.Ray_depth_refraction = IntProperty(
        name = "", 
        min = 0, max = 16,
        description = "Enter an integer",default = 2)  
    bpy.types.Scene.Ray_depth_volume = IntProperty(
        name = "", 
        min = 0, max = 16,
        description = "Enter an integer",default = 0)   
    bpy.types.Scene.Ray_depth_trans_depth = IntProperty(
        name = "", 
        min = 0, max = 16,
        description = "Enter an integer",default = 10)
    bpy.types.Scene.Ray_depth_trans_threshold = FloatProperty(
        name = "",
        min = 0, max = 1,
        precision = 2,
        step = 1,
        description = "Enter an float",default = 0.99) 
    ###------Environment------ 
    
    ###------Motion blur------
    bpy.types.Scene.Motion_blur_enable = BoolProperty(
        name = "Enable", 
        description = "True or False?") 
    bpy.types.Scene.Motion_blur_deformation = BoolProperty(
        name = "Deformation", 
        description = "True or False?") 
    bpy.types.Scene.Motion_blur_camera = BoolProperty(
        name = "Camera", 
        description = "True or False?") 
    bpy.types.Scene.Motion_blur_keys = IntProperty(
        name = "Keys", 
        min = 2, max = 30,
        description = "Enter an integer",default = 2) 
    bpy.types.Scene.Motion_blur_position = bpy.props.EnumProperty(items=MotionblurPositon, default = "1")                                           
    bpy.types.Scene.Motion_blur_length = FloatProperty(
        name = "",
        min = 0, max = 1,
        precision = 2,
        step = 1,
        description = "Enter an float",default = 0.5)
    bpy.types.Scene.Motion_blur_start = FloatProperty(
        name = "",
        min = 0, max = 1,
        precision = 2,
        step = 1,
        description = "Enter an float",default = -0.25) 
    bpy.types.Scene.Motion_blur_end = FloatProperty(
        name = "",
        min = 0, max = 1,
        precision = 2,
        step = 1,
        description = "Enter an float",default = 0.25) 
    ###------Lights------
    bpy.types.Scene.Main_lights = FloatProperty(
        name = "",
        min = 0, max = 0.1,
        precision = 3,
        step = 1,
        description = "Enter an float",default = 0.001) 
    ###------Textures------
    bpy.types.Scene.Texture_accept_unmipped = BoolProperty(
        name = "Accept unmipped", 
        description = "True or False?",
        default = True) 
    bpy.types.Scene.Texture_auto_mipmap = BoolProperty(
        name = "Auto-mipmap", 
        description = "True or False?",
        default = True) 
    bpy.types.Scene.Texture_accept_untiled = BoolProperty(
        name = "Accept untiled", 
        description = "True or False?",
        default = True) 
    bpy.types.Scene.Texture_auto_tile = BoolProperty(
        name = "Auto-tile", 
        description = "True or False?",
        default = True) 
    bpy.types.Scene.Texture_tile_size = IntProperty(
        name = "Tile size", 
        min = 16, max = 64,
        description = "Enter an integer", default = 64)       
    bpy.types.Scene.Texture_use_existing = BoolProperty(
        name = "Use existiong.tx textures", 
        description = "True or False?",)
    bpy.types.Scene.Texture_max_cache = FloatProperty(
        name = "Max cache size(MB)",
        precision = 2,
        step = 1,
        description = "Enter an float", default = 1024) 
    bpy.types.Scene.Texture_max_open = IntProperty(
        name = "Max open files", 
        description = "Enter an integer", default = 0)
    bpy.types.Scene.Texture_diffuse_blur = FloatProperty(
        name = "Diffuse blur",
        precision = 3,
        step = 1,
        description = "Enter an float", default = 0.031)
    bpy.types.Scene.Texture_glossy_blur = FloatProperty(
        name = "Glossy blur",
        precision = 2,
        step = 1,
        description = "Enter an float", default = 0) 
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
        layout.prop(context.scene,'ArnoldEnum',expand=True)
        #arnold_menu = context.scene.ArnoldEnum       

class ARNOLD_main_sampling(classes.ArnoldRenderPanel):
    bl_label = "Sampling"
    #bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'0'}
    COMPAT_ENGINES = {'arnold_renderer'}
    @classmethod
    def poll(cls, context):
        arnold_menu = context.scene.ArnoldEnum
        rd = context.scene.render
        return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES) and (arnold_menu in cls.tabNum)
    def draw(self, context):      
        layout = self.layout
        scn = context.scene
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
        arnold_menu = context.scene.ArnoldEnum
        rd = context.scene.render
        return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES) and (arnold_menu in cls.tabNum)
    def draw(self, context):      
        layout = self.layout 
        scn = context.scene
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
        arnold_menu = context.scene.ArnoldEnum
        rd = context.scene.render
        return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES) and (arnold_menu in cls.tabNum)
    def draw(self, context):      
        layout = self.layout 
        scn = context.scene
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
        arnold_menu = context.scene.ArnoldEnum
        rd = context.scene.render
        return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES) and (arnold_menu in cls.tabNum)
    def draw(self, context):      
        layout = self.layout 
        scn = context.scene
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
        arnold_menu = context.scene.ArnoldEnum
        rd = context.scene.render
        return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES) and (arnold_menu in cls.tabNum)
    def draw(self, context):      
        layout = self.layout 
        scn = context.scene
        row = layout.row()
        row.prop(scn, 'Main_lights', text = "Low light threshold")
class ARNOLD_main_textures(classes.ArnoldRenderPanel):
    bl_label = "Textures"
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'0'}
    COMPAT_ENGINES = {'arnold_renderer'}
    @classmethod
    def poll(cls, context):
        arnold_menu = context.scene.ArnoldEnum
        rd = context.scene.render
        return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES) and (arnold_menu in cls.tabNum)
    def draw(self, context):      
        layout = self.layout 
        scn = context.scene
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
    bpy.utils.register_class(SceneSettingItem)

    
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
    bpy.utils.unregister_class(SceneSettingItem)

if __name__ == "__main__":
    register()
