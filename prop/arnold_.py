#
# arnold For Blender
#

import bpy
from bpy.types import (PropertyGroup,
                        )
from bpy.props import (StringProperty,
                        BoolProperty,
                        IntProperty,
                        FloatProperty,
                        FloatVectorProperty,
                        EnumProperty,
                        PointerProperty,
                        FloatVectorProperty,
                        BoolVectorProperty
                        )
from .classes import (PanelGroups,
                        FilterTypes,
                        FilterDomain,
                        MotionblurPositon,
                        RenderBucketscanning,
                        RenderDisplaybucket,
                        LogVerbositylevel,
                        AovsDriverType
                        )
from ..ui.properties_arnold_aovs import Aovs_new_driver

class ArnoldSceneSetting(PropertyGroup):
    #===========================================================================
    # #Render Tab --------------------------------------------------------------
    #===========================================================================
    ArnoldEnum = EnumProperty(items=PanelGroups)

    #===========================================================================
    # #Main --------------------------------------------------------------------
    #===========================================================================
    # Sampling -----------------------------------------------------------------
    CameraInt = IntProperty(
        name = "Camera(AA)",
        min = 1, max = 10,
        description = "Enter an integer",default = 3)
    DiffuseInt = IntProperty(
        name = "Diffuse",
        min = 0, max = 10,
        description = "Enter an integer",default = 2)
    GlossyInt = IntProperty(
        name = "Glossy",
        min = 0, max = 10,
        description = "Enter an integer",default = 2)
    RefractionInt = IntProperty(
        name = "Refraction",
        min = 0, max = 10,
        description = "Enter an integer",default = 2)
    SSSInt = IntProperty(
        name = "SSS",
        min = 0, max = 10,
        description = "Enter an integer",default = 2)
    Volume_indirectInt = IntProperty(
        name = "Volumeindirect",
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
        name = "Max value",
        min = 0.001, max = 100.000,
        precision = 3,
        step = 1,
        description = "Enter an float",default = 10)
    Filter_Types = EnumProperty(items = FilterTypes, default = "10", name = "Default filter.type")
    Filter_width = FloatProperty(
        name = "Default filter.width",
        precision = 2,
        step = 1,
        description = "Enter an float",default = 2)
    Filter_Domain = EnumProperty(items = FilterDomain)
    Filter_minimum = FloatProperty(
        name = "Default filter.minimum",
        precision = 2,
        step = 1,
        description = "Enter an float",default = 0)
    Filter_maximum = FloatProperty(
        name = "Default filter.maximum",
        precision = 2,
        step = 1,
        description = "Enter an float",default = 1)
    Filter_scalar_mode = BoolProperty(
        name = "Default filter.scalar_mode",
        description = "True or False?")
    # Ray depth ----------------------------------------------------------------
    Ray_depth_total = IntProperty(
        name = "Total",
        min = 0, max = 16,
        description = "Enter an integer",default = 10)
    Ray_depth_diffuse = IntProperty(
        name = "Diffuse",
        min = 0, max = 16,
        description = "Enter an integer",default = 1)
    Ray_depth_glossy = IntProperty(
        name = "Glossy",
        min = 0, max = 16,
        description = "Enter an integer",default = 1)
    Ray_depth_reflection = IntProperty(
        name = "Reflection",
        min = 0, max = 16,
        description = "Enter an integer",default = 2)
    Ray_depth_refraction = IntProperty(
        name = "Refraction",
        min = 0, max = 16,
        description = "Enter an integer",default = 2)
    Ray_depth_volume = IntProperty(
        name = "Volume",
        min = 0, max = 16,
        description = "Enter an integer",default = 0)
    Ray_depth_trans_depth = IntProperty(
        name = "Transparency depth",
        min = 0, max = 16,
        description = "Enter an integer",default = 10)
    Ray_depth_trans_threshold = FloatProperty(
        name = "Transparency threshold",
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
    Motion_blur_position = EnumProperty(items = MotionblurPositon, default = "1", name = "Positon")
    Motion_blur_length = FloatProperty(
        name = "Length",
        min = 0, max = 1,
        precision = 2,
        step = 1,
        description = "Enter an float",default = 0.5)
    Motion_blur_start = FloatProperty(
        name = "Start",
        min = 0, max = 1,
        precision = 2,
        step = 1,
        description = "Enter an float",default = -0.25)
    Motion_blur_end = FloatProperty(
        name = "End",
        min = 0, max = 1,
        precision = 2,
        step = 1,
        description = "Enter an float",default = 0.25)
    # Lights -------------------------------------------------------------------
    Main_lights = FloatProperty(
        name = "Low light threshold",
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
    Render_bucket_scanning = EnumProperty(items = RenderBucketscanning, default = "6", name = "Bucket scanning")
    Render_buket_size = IntProperty(
        name = "Bucket size",
        min = 16, max = 256,
        description = "Enter an integer", default = 16)
    Render_display_bucket = EnumProperty(items = RenderDisplaybucket, default = "1", name = "Display bucket corners")
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
        default = ""
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
    #===========================================================================
    # AOVs
    #===========================================================================
    # Aovs ---------------------------------------------------------------------
    Avos_is_setup =  BoolProperty(
        name = "Set button",
        description = "True or False?",
        default = False)
    Avos_driver_list = StringProperty(
        name="Options",
        description="arnold kick options",
        default = "0,<display driver>(driver_blender_display),default driver,\
                    0,0,0,0,0,0,0,\
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0;"
        )
    Aovs_driver = EnumProperty(items = Aovs_new_driver.get_list, name = "Driver", update = Aovs_new_driver.update_driver)
    Aovs_driver_type = EnumProperty(items = AovsDriverType, default = "2", name = "Type")
    Aovs_driver_type_name = StringProperty(name="Name",
        description="New add driver name",
        default = "")
    Aovs_shaders_builtin = BoolProperty(
        name = "<built-in>",
        description = "True or False?",
        default = False,
        update = Aovs_new_driver.update_item)
    Aovs_shaders_hair = BoolProperty(
        name = "hair",
        description = "True or False?",
        default = False,
        update = Aovs_new_driver.update_item)
    Aovs_shaders_lambert = BoolProperty(
        name = "lambert",
        description = "True or False?",
        default = False,
        update = Aovs_new_driver.update_item)
    Aovs_shaders_mix = BoolProperty(
        name = "mix",
        description = "True or False?",
        default = False,
        update = Aovs_new_driver.update_item)
    Aovs_shaders_shadowmatte = BoolProperty(
        name = "shadow_matte",
        description = "True or False?",
        default = False,
        update = Aovs_new_driver.update_item)
    Aovs_shaders_skin = BoolProperty(
        name = "skin",
        description = "True or False?",
        default = False,
        update = Aovs_new_driver.update_item)
    Aovs_shaders_standard = BoolProperty(
        name = "standard",
        description = "True or False?",
        default = False,
        update = Aovs_new_driver.update_item)
    Aovs_shaders_item = BoolVectorProperty(
        name = "Item",
        size = 32,
        description = "True or False?",
        update = Aovs_new_driver.update_item)

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)
