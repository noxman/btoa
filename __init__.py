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
    
if "bpy" in locals():
    import imp
    imp.reload(ui)
    imp.reload(engine)

else:
    import bpy
    from btoa import ui
    from btoa import engine
    from bpy.types import (AddonPreferences,
                           PropertyGroup,
                           Operator,
                           )
    from bpy.props import (StringProperty,
                           BoolProperty,
                           IntProperty,
                           FloatProperty,
                           FloatVectorProperty,
                           EnumProperty,
                           PointerProperty,
                           )
    from btoa.ui.classes import (PanelGroups,
                                 FilterTypes,
                                 FilterDomain,
                                 MotionblurPositon
                                 )
class ArnoldRenderSetting(PropertyGroup):
    ###------Render Tab------
    ArnoldEnum = EnumProperty(items=PanelGroups)
    ###------Sampling-------
    CameraInt = IntProperty(
        name = "", 
        min = 1, max = 10,
        description = "Enter an integer",default = 3)
    DiffuseInt = IntProperty(
        name = "", 
        min = 0, max = 10,
        description = "Enter an integer",default = 2)
    GlossyInt = IntProperty(
        name = "", 
        min = 0, max = 10,
        description = "Enter an integer",default = 2)
    RefractionInt = IntProperty(
        name = "", 
        min = 0, max = 10,
        description = "Enter an integer",default = 2)
    SSSInt = IntProperty(
        name = "", 
        min = 0, max = 10,
        description = "Enter an integer",default = 2)
    Volume_indirectInt = IntProperty(
        name = "", 
        min = 0, max = 10,
        description = "Enter an integer",default = 2)
    Lock_sampling = BoolProperty(
        name = "Lock sampling pattern", 
        description = "True or False?")
    Use_autobump_in_sss = BoolProperty(
        name = "Use autobump in SSS", 
        description = "True or False?")
    Clamp_sample = BoolProperty(
        name = "Clamp sample values", 
        description = "True or False?") 
    Affect_aovs = BoolProperty(
        name = "Affect AOVs", 
        description = "True or False?") 
    Clamp_max = FloatProperty(
        name = "", 
        min = 0.001, max = 100.000,
        precision = 3,
        step = 1,
        description = "Enter an float",default = 10)
    Filter_Types = bpy.props.EnumProperty(items=FilterTypes,default = "10")
    Filter_width = FloatProperty(
        name = "",
        precision = 2,
        step = 1,
        description = "Enter an float",default = 2) 
    Filter_Domain = bpy.props.EnumProperty(items=FilterDomain)
    Filter_minimum = FloatProperty(
        name = "",
        precision = 2,
        step = 1,
        description = "Enter an float",default = 0) 
    Filter_maximum = FloatProperty(
        name = "",
        precision = 2,
        step = 1,
        description = "Enter an float",default = 1) 
    Filter_scalar_mode = BoolProperty(
        name = "Default filter.scalar_mode", 
        description = "True or False?") 
    ###------Ray depth
    Ray_depth_total = IntProperty(
        name = "", 
        min = 0, max = 16,
        description = "Enter an integer",default = 10)
    Ray_depth_diffuse = IntProperty(
        name = "", 
        min = 0, max = 16,
        description = "Enter an integer",default = 1) 
    Ray_depth_glossy = IntProperty(
        name = "", 
        min = 0, max = 16,
        description = "Enter an integer",default = 1)           
    Ray_depth_reflection = IntProperty(
        name = "", 
        min = 0, max = 16,
        description = "Enter an integer",default = 2)     
    Ray_depth_refraction = IntProperty(
        name = "", 
        min = 0, max = 16,
        description = "Enter an integer",default = 2)  
    Ray_depth_volume = IntProperty(
        name = "", 
        min = 0, max = 16,
        description = "Enter an integer",default = 0)   
    Ray_depth_trans_depth = IntProperty(
        name = "", 
        min = 0, max = 16,
        description = "Enter an integer",default = 10)
    Ray_depth_trans_threshold = FloatProperty(
        name = "",
        min = 0, max = 1,
        precision = 2,
        step = 1,
        description = "Enter an float",default = 0.99) 
    ###------Environment------ 
    
    ###------Motion blur------
    Motion_blur_enable = BoolProperty(
        name = "Enable", 
        description = "True or False?") 
    Motion_blur_deformation = BoolProperty(
        name = "Deformation", 
        description = "True or False?") 
    bMotion_blur_camera = BoolProperty(
        name = "Camera", 
        description = "True or False?") 
    Motion_blur_keys = IntProperty(
        name = "Keys", 
        min = 2, max = 30,
        description = "Enter an integer",default = 2) 
    Motion_blur_position = bpy.props.EnumProperty(items=MotionblurPositon, default = "1")                                           
    Motion_blur_length = FloatProperty(
        name = "",
        min = 0, max = 1,
        precision = 2,
        step = 1,
        description = "Enter an float",default = 0.5)
    Motion_blur_start = FloatProperty(
        name = "",
        min = 0, max = 1,
        precision = 2,
        step = 1,
        description = "Enter an float",default = -0.25) 
    Motion_blur_end = FloatProperty(
        name = "",
        min = 0, max = 1,
        precision = 2,
        step = 1,
        description = "Enter an float",default = 0.25) 
    ###------Lights------
    Main_lights = FloatProperty(
        name = "",
        min = 0, max = 0.1,
        precision = 3,
        step = 1,
        description = "Enter an float",default = 0.001) 
    ###------Textures------
    Texture_accept_unmipped = BoolProperty(
        name = "Accept unmipped", 
        description = "True or False?",
        default = True) 
    Texture_auto_mipmap = BoolProperty(
        name = "Auto-mipmap", 
        description = "True or False?",
        default = True) 
    Texture_accept_untiled = BoolProperty(
        name = "Accept untiled", 
        description = "True or False?",
        default = True) 
    Texture_auto_tile = BoolProperty(
        name = "Auto-tile", 
        description = "True or False?",
        default = True) 
    Texture_tile_size = IntProperty(
        name = "Tile size", 
        min = 16, max = 64,
        description = "Enter an integer", default = 64)       
    Texture_use_existing = BoolProperty(
        name = "Use existiong.tx textures", 
        description = "True or False?",)
    Texture_max_cache = FloatProperty(
        name = "Max cache size(MB)",
        precision = 2,
        step = 1,
        description = "Enter an float", default = 1024) 
    Texture_max_open = IntProperty(
        name = "Max open files", 
        description = "Enter an integer", default = 0)
    Texture_diffuse_blur = FloatProperty(
        name = "Diffuse blur",
        precision = 3,
        step = 1,
        description = "Enter an float", default = 0.031)
    Texture_glossy_blur = FloatProperty(
        name = "Glossy blur",
        precision = 2,
        step = 1,
        description = "Enter an float", default = 0) 
def register():
    bpy.utils.register_module(__name__)
    #engine.register()
    ui.register()
    bpy.types.Scene.arnold = PointerProperty(type = ArnoldRenderSetting)

def unregister():
    bpy.utils.unregister_module(__name__)
    #engine.unregister()
    ui.unregister()
    del bpy.types.Scene.arnold
