from email.policy import default
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
                        FloatVectorProperty
                        )
from btoa.ui.classes import (PanelGroups,
                            FilterTypes,
                            FilterDomain,
                            MotionblurPositon,
                            RenderBucketscanning,
                            RenderDisplaybucket,
                            LogVerbositylevel
                            )
class ArnoldRenderSetting(PropertyGroup):
    
    #===========================================================================
    # #Render Tab --------------------------------------------------------------
    #===========================================================================
    ArnoldEnum = EnumProperty(items=PanelGroups)
    
    #===========================================================================
    # #Main --------------------------------------------------------------------
    #===========================================================================
    # Sampling -----------------------------------------------------------------
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
    Filter_Types = bpy.props.EnumProperty(items = FilterTypes,default = "10")
    Filter_width = FloatProperty(
        name = "",
        precision = 2,
        step = 1,
        description = "Enter an float",default = 2) 
    Filter_Domain = bpy.props.EnumProperty(items = FilterDomain)
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
    # Ray depth ----------------------------------------------------------------
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
    # Environment --------------------------------------------------------------
    
    # Motion blur --------------------------------------------------------------
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
    Motion_blur_position = EnumProperty(items = MotionblurPositon, default = "1")                                           
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
    # Lights -------------------------------------------------------------------
    Main_lights = FloatProperty(
        name = "",
        min = 0, max = 0.1,
        precision = 3,
        step = 1,
        description = "Enter an float",default = 0.001) 
    # Textures -----------------------------------------------------------------
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
    
    #===========================================================================
    # #System ------------------------------------------------------------------
    #===========================================================================
    # Render setting -----------------------------------------------------------
    Render_bucket_scanning = EnumProperty(items = RenderBucketscanning, default = "6")
    Render_buket_size = IntProperty(
        name = "Bucket size",
        min = 16, max = 256, 
        description = "Enter an integer", default = 16)
    Render_display_bucket = EnumProperty(items = RenderDisplaybucket, default = "1")
    Render_autodetect_threads = BoolProperty(
        name = "Autodetect threads", 
        description = "True or False?",
        default = True)
    Render_threads =  IntProperty(
        name = "THreads",
        description = "Enter an integer", default = 0)
    Render_expand_procedurals = BoolProperty(
        name = "Expand procedurals", 
        description = "True or False?",
        default = False)
    Render_export_scale = FloatProperty(
        name = "Export scale",
        precision = 2,
        step = 1,
        description = "Enter an float", default = 0.01)
    # IPR ----------------------------------------------------------------------
    Ipr_progressive_refinement =  BoolProperty(
        name = "Progressive refinement", 
        description = "True or False?",
        default = True)
    Ipr_initial_sampling =  IntProperty(
        name = "THreads",
        min = -10, max = 1,
        description = "Enter an integer", default = -3)
    # Search paths -------------------------------------------------------------
    Search_procedural_path = StringProperty(
        name="Procedural",
        description="Folders have to be separated with a semicolon (;) character",
        default = "",
        )
    Search_shader_path = StringProperty(
        name="Shader",
        description="Folders have to be separated with a semicolon (;) character",
        default = "",
        )
    Search_texture_path = StringProperty(
        name="Texture",
        description="Folders have to be separated with a semicolon (;) character",
        default = "",
        )
    # Licensing ----------------------------------------------------------------
    Licensing_abort = BoolProperty(
        name = "Abort on license fail", 
        description = "True or False?",
        default = False)
    Licensing_skip = BoolProperty(
        name = "Skip license check", 
        description = "True or False?",
        default = False)
    #===========================================================================
    # AOVs
    #===========================================================================
    # Aovs ---------------------------------------------------------------------
    Aovs_shaders_builtin = BoolProperty(
        name = "<built-in>", 
        description = "True or False?",
        default = False)
    Aovs_shaders_hair = BoolProperty(
        name = "hair", 
        description = "True or False?",
        default = False)
    Aovs_shaders_lambert = BoolProperty(
        name = "lambert", 
        description = "True or False?",
        default = False)
    Aovs_shaders_mix = BoolProperty(
        name = "mix", 
        description = "True or False?",
        default = False)
    Aovs_shaders_shadowmatte = BoolProperty(
        name = "shadow_matte", 
        description = "True or False?",
        default = False)
    Aovs_shaders_skin = BoolProperty(
        name = "skin", 
        description = "True or False?",
        default = False)
    Aovs_shaders_standard = BoolProperty(
        name = "standard", 
        description = "True or False?",
        default = False)
    #===========================================================================
    # Diagonstics
    #===========================================================================
    # Log ----------------------------------------------------------------------
    Log_verbosity_level = EnumProperty(items = LogVerbositylevel, default = "1")
    Log_console = BoolProperty(
        name = "Console", 
        description = "True or False?",
        default = True)
    Log_file = BoolProperty(
        name = "File", 
        description = "True or False?",
        default = False)
    Log_file_path = StringProperty(
        name="File path",
        description="log file path ",
        subtype = "FILE_PATH",
        default = "arnold.log",
        maxlen=1024
        )
    Log_max_warnings = IntProperty(
        name = "Max warnings",
        min = 0, max = 100,
        description = "Enter an integer", default = 5)
    # Error handing ------------------------------------------------------------
    Error_abort = BoolProperty(
        name = "Abort on error", 
        description = "True or False?",
        default = True)
    Error_texture_error = FloatVectorProperty(
        name="Texture error color", description = "",
        precision=4, step=0.01, min=0.0, soft_max=1.0,
        default=(1, 0, 0), subtype='COLOR')
    Error_nan_error = FloatVectorProperty(
        name="NaN error color", description = "",
        precision=4, step=0.01, min=0.0, soft_max=1.0,
        default=(0, 0, 1), subtype='COLOR')
    #===========================================================================
    # Overrider
    #===========================================================================
    # User options -------------------------------------------------------------
    User_options_overrider = StringProperty(
        name="Options",
        description="arnold kick options ",
        default = "",
        )
    # Feature overrides --------------------------------------------------------
    Feature_override_textures = BoolProperty(
        name = "Ignore textures", 
        description = "True or False?",
        default = False)
    Feature_override_shaders = BoolProperty(
        name = "Ignore shaders", 
        description = "True or False?",
        default = False)
    Feature_override_atmosphere = BoolProperty(
        name = "Ignore atmosphere", 
        description = "True or False?",
        default = False)
    Feature_override_lights = BoolProperty(
        name = "Ignore lights", 
        description = "True or False?",
        default = False)
    Feature_override_shadows = BoolProperty(
        name = "Ignore shadows", 
        description = "True or False?",
        default = False)
    Feature_override_subdivision = BoolProperty(
        name = "Ignore subdivision", 
        description = "True or False?",
        default = False)
    Feature_override_displacement = BoolProperty(
        name = "Ignore displacement", 
        description = "True or False?",
        default = False)
    Feature_override_bump = BoolProperty(
        name = "Ignore bump", 
        description = "True or False?",
        default = False)
    Feature_override_normal = BoolProperty(
        name = "Ignore normal smoothing", 
        description = "True or False?",
        default = False)
    Feature_override_motion = BoolProperty(
        name = "Ignore motion blur", 
        description = "True or False?",
        default = False)
    Feature_override_depth = BoolProperty(
        name = "Ignore depth of field", 
        description = "True or False?",
        default = False)
    Feature_override_subsurface = BoolProperty(
        name = "Ignore sub-surface scattering", 
        description = "True or False?",
        default = False)
    # Shader override
    # Subdivision --------------------------------------------------------------
    Subdivision_max_subdivisions = IntProperty(
        name = "Max subdivisions",
        min = 0, max = 999,
        description = "Enter an integer", default = 999)
    
def register():
    bpy.utils.register_module(__name__)
    bpy.types.Scene.arnold = PointerProperty(type = ArnoldRenderSetting)
    

def unregister():
    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.arnold
    
