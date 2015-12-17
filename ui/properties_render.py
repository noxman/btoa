#
# arnold For Blender
#
import bpy
from btoa.ui import classes

class ArnoldPanel(bpy.types.Panel):
    COMPAT_ENGINES = {'arnold_renderer'}
    @classmethod
    def poll(cls, context):
        rd = context.scene.render
        return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES)
    
class ArnoldRenderPanel(ArnoldPanel):
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    
class ARNOLD_RP_render(ArnoldRenderPanel):
    bl_label = ""
    bl_options = {'HIDE_HEADER'}
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("arnold.button", text="Render",icon="RENDER_STILL")
        
class ARNOLD_tab_render(ArnoldRenderPanel):
    bl_label = ""
    bl_options = {'HIDE_HEADER'}
    def draw(self, context):      
        layout = self.layout
        scn = context.scene.arnold
        layout.prop(scn,'ArnoldEnum',expand=True)
        #arnold_menu = context.scene.ArnoldEnum       

class ARNOLD_main_sampling(ArnoldRenderPanel):
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
       
class ARNOLD_main_Ray_depth(ArnoldRenderPanel):
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
        
class ARNOLD_main_Environment(ArnoldRenderPanel):
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
        
class ARNOLD_main_Motion_blur(ArnoldRenderPanel):
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
        
class ARNOLD_main_lights(ArnoldRenderPanel):
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
        
class ARNOLD_main_textures(ArnoldRenderPanel):
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
        
class ARNOLD_system_rendersettings(ArnoldRenderPanel):
    bl_label = "Render settings"
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
        row = layout.row()
        row.prop(scn, 'Render_bucket_scanning', text = "Bucket scanning") 
        row = layout.row()
        row.prop(scn, 'Render_buket_size') 
        row = layout.row()
        row.prop(scn, 'Render_display_bucket', text = "Display bucket corners") 
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
        
class ARNOLD_system_ipr(ArnoldRenderPanel):
    bl_label = "IPR"
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
        row.prop(scn, 'Ipr_progressive_refinement') 
        row = layout.row()
        row.prop(scn, 'Ipr_initial_sampling')
        
class ARNOLD_system_searchpaths(ArnoldRenderPanel):
    bl_label = "Search paths"
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
        row.prop(scn, 'Search_procedural_path') 
        row = layout.row()
        row.prop(scn, 'Search_shader_path') 
        row = layout.row()
        row.prop(scn, 'Search_texture_path') 
        
class ARNOLD_system_licensing(ArnoldRenderPanel):
    bl_label = "Licensing"
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
        row.prop(scn, 'Licensing_abort') 
        row = layout.row()
        row.prop(scn, 'Licensing_skip')   

class ARNOLD_avos_setup(ArnoldRenderPanel):
    bl_label = "AOVs"
    #bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'2'}
    COMPAT_ENGINES = {'arnold_renderer'}
    is_setup = False
    @classmethod
    def poll(cls, context):
        arnold_menu = context.scene.arnold.ArnoldEnum
        rd = context.scene.render
        return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES) and (arnold_menu in cls.tabNum)
    def draw(self, context):      
        layout = self.layout 
        scn = context.scene.arnold
        row = layout.row()
        row.operator('aovs.setup', text = "Setup AOVs") 
        if self.is_setup == True:
            col = layout.column()
            row = col.row()
            row.prop(scn, 'Aovs_shaders_builtin')
            row.prop(scn, 'Aovs_shaders_hair')
            row = col.row()
            row.prop(scn, 'Aovs_shaders_lambert')
            row.prop(scn, 'Aovs_shaders_mix')
            row = col.row()
            row.prop(scn, 'Aovs_shaders_shadowmatte')
            row.prop(scn, 'Aovs_shaders_skin')
            row = col.row()
            row.prop(scn, 'Aovs_shaders_standard')
            shaders = ['Aovs_shaders_builtin','Aovs_shaders_hair',
                       'Aovs_shaders_lambert','Aovs_shaders_mix',
                       'Aovs_shaders_shadowmatte','Aovs_shaders_skin',
                       'Aovs_shaders_standard']   
            built_in = ["ID","N","P","Pref","Z",
                        "cputime","motionvector",
                        "opacity","raycount","texturetime",
                        "volume","volume_direct",
                        "volume_indirect","volum_opacity"]
            hair = ["direct_diffuse","direct_specular",
                    "direct_transmission","indirect_diffuse",
                    ]
            lambert = ["direct_diffuse","indirect_diffuse"
                    ]
            mix = ["direct_diffuse","direct_specular",
                   "emission","indirect_diffuse",
                   "indirect_specular","reflection",
                   "refraction","refraction_opactiy",
                   "sss","volume","volum_opacity"
                   ]
            shadow_matte = ["indirect_diffuse","indirect_specular",
                   "shadow","shadow_matte",
                   ]
            skin = ["direct_sss","indirect_sss",
                   "cheen","specular",
                   ]
            standard = ["direct_diffuse","direct_specular",
                        "direct_sss","emission",
                        "indirect_diffuse","indirect_specular",
                        "reflection","refraction",
                        "refraction_opactiy","sss"
                        ]
            shaders_select = False
            for shader in shaders:
                if '%s."%s' %(scn, shader) == True:
                    shaders_select = True
                    print(shaders_select)
            if shaders_select == True:
                row = col.row()
                box = row.box()
            if scn.Aovs_shaders_builtin == True:
                for builtin_item in built_in:      
                    box.prop(scn, 'Aovs_shaders_standard', text = builtin_item)      
            if scn.Aovs_shaders_hair == True:
                for hair_item in hair:
                    box.prop(scn, 'Aovs_shaders_standard', text = hair_item) 
            if scn.Aovs_shaders_lambert == True:
                for lambert_item in lambert:
                    box.prop(scn, 'Aovs_shaders_standard', text = lambert_item)  
            if scn.Aovs_shaders_mix == True:
                for mix_item in mix:
                    box.prop(scn, 'Aovs_shaders_standard', text = mix_item) 
            if scn.Aovs_shaders_shadowmatte == True:
                for shadow_matte_item in shadow_matte:
                    box.prop(scn, 'Aovs_shaders_standard', text = shadow_matte_item)  
            if scn.Aovs_shaders_skin == True:
                for skin_item in skin:
                    box.prop(scn, 'Aovs_shaders_standard', text = skin_item) 
            if scn.Aovs_shaders_standard == True:
                for standard_item in standard:
                    box.prop(scn, 'Aovs_shaders_standard', text = standard_item)                        

class ARNOLD_diagnostics_log(ArnoldRenderPanel):
    bl_label = "Log"
    #bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'3'}
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
                                    
class ARNOLD_diagnostics_error(ArnoldRenderPanel):
    bl_label = "Error handing"
    bl_options = {'DEFAULT_CLOSED'}
    tabNum = {'3'}
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

class ARNOLD_override_user(ArnoldRenderPanel):
    bl_label = "User options"
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
        row.prop(scn, 'User_options_overrider') 
        
class ARNOLD_override_feature(ArnoldRenderPanel):
    bl_label = "Feature overrides"
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
                            
class ARNOLD_override_subdivision(ArnoldRenderPanel):
    bl_label = "Subdivision"
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
        row.prop(scn, 'Subdivision_max_subdivisions') 
                      
class Arnold_panel_Button(bpy.types.Operator):
    bl_idname = "arnold.button"
    bl_label = "Button"
    
class Aovs_setup(bpy.types.Operator): 
    bl_idname = "aovs.setup" 
    bl_label = "AvosSetupButton" 
    def execute(self, context):
        ARNOLD_avos_setup.is_setup = not ARNOLD_avos_setup.is_setup
        return {'FINISHED'}
                  
def register():
    bpy.utils.register_module(__name__)
    
def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
