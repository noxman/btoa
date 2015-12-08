#
# arnold For Blender
#
import bpy
from btoa.ui import classes
from btoa.ui.classes import PanelGroups,FilterTypes,FilterDomain
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
        row = layout.row()
        box = row.box()
        box.enabled = False
        if scn.Clamp_sample ==True:
            box.enabled = True
        box.prop(scn, 'Affect_aovs')  
        box.prop(scn, 'Clamp_max', text = "Max value")   
        row = layout.row()
        row.prop(scn,'Filter_Types', text = "Default filter.type")
        row = layout.row()
        t_sub_filter = ['9','11','15']
        sub_filter = ['0','5','6','8','10','13','14']
        for choice in sub_filter:
            if scn.Filter_Types == choice:
                box = row.box()
                box.prop(scn, 'Filter_width', text = "Default filter.width") 
        if scn.Filter_Types == '9':
            box = row.box()
            box.prop(scn, 'Filter_Domain')
        elif scn.Filter_Types == '11':
            box = row.box()
            box.prop(scn, 'Filter_minimum', text = "Default filter.minimum")
            box.prop(scn, 'Filter_minimum', text = "Default filter.maximum")
        elif scn.Filter_Types == '15':
            box = row.box()
            box.prop(scn, 'Filter_width', text = "Default filter.width") 
            box.prop(scn, 'Filter_scalar_mode')  
                           
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
        row.prop(scn, 'Ray_depth_total',text = "Total")
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
        row = layout.row()
        box = row.box()
        box.enabled = False
        if scn.Motion_blur_enable == True:
            box.enabled = True 
        box.prop(scn, 'Motion_blur_deformation')  
        box.prop(scn, 'Motion_blur_camera') 
        box.prop(scn, 'Motion_blur_keys') 
                        
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
    bpy.utils.register_class(Arnold_panel_Button)
    bpy.utils.register_class(SceneSettingItem)

    
def unregister():
    bpy.utils.unregister_class(ARNOLD_RP_render) 
    bpy.utils.unregister_class(ARNOLD_tab_render) 
    bpy.utils.unregister_class(ARNOLD_main_sampling) 
    bpy.utils.unregister_class(ARNOLD_main_Ray_depth) 
    bpy.utils.unregister_class(ARNOLD_main_Environment)
    bpy.utils.unregister_class(ARNOLD_main_Motion_blur) 
    bpy.utils.unregister_class(Arnold_panel_Button)
    bpy.utils.unregister_class(SceneSettingItem)

if __name__ == "__main__":
    register()
