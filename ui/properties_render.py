#
# arnold For Blender
#
import bpy
from btoa.ui import classes

class Arnold_panel_Button(bpy.types.Operator):
    bl_idname = "arnold.button"
    bl_label = "Button"
    
class Aovs_setup(bpy.types.Operator): 
    bl_idname = "aovs.setup" 
    bl_label = "AvosSetupButton" 
    def execute(self, context):
        scn = context.scene.arnold
        scn.Avos_is_setup = not scn.Avos_is_setup
        return {'FINISHED'}
     
class Aovs_new_driver(bpy.types.Operator): 
    bl_idname = "aovs.newdriver" 
    bl_label = "AvosNewDriver" 
    def update_item(self, context):
        scn = context.scene.arnold
        driver_items_back = scn.Avos_driver_list
        driver_items_back = driver_items_back.split(";")
        total = ''
        for i_item in driver_items_back:
            if i_item:
                items = i_item.split(",")
                t_items = ''
                if items[0] == scn.Aovs_driver:
                    if items:
                        for i in range(42):
                            if scn.Aovs_shaders_builtin == True:
                                items[3] = '1'
                            else:
                                items[3] = '0'
                            if scn.Aovs_shaders_hair == True:
                                items[4] = '1'
                            else:
                                items[4] = '0'
                            if scn.Aovs_shaders_lambert == True:
                                items[5] = '1'
                            else:
                                items[5] = '0'
                            if scn.Aovs_shaders_mix == True:
                                items[6] = '1'
                            else:
                                items[6] = '0'
                            if scn.Aovs_shaders_shadowmatte == True:
                                items[7] = '1'
                            else:
                                items[7] = '0'
                            if scn.Aovs_shaders_skin == True:
                                items[8] = '1'
                            else:
                                items[8] = '0' 
                            if scn.Aovs_shaders_standard == True:
                                items[9] = '1'
                            else:
                                items[9] = '0'    
                            if i>9 and scn.Aovs_shaders_item[i-10] == True:
                                items[i] = '1'
                            elif i>9 and scn.Aovs_shaders_item[i-10] == False:
                                items[i] = '0'                      
                            t_items = t_items + items[i] +','
                    i_item = t_items
                total = total + i_item + ';'     
        scn.Avos_driver_list = total    
    def update_driver(self, context):
        scn = context.scene.arnold
        driver_items_back = scn.Avos_driver_list
        driver_items_back = driver_items_back.split(";")
        for i_item in driver_items_back:
            if i_item:
                items = i_item.split(",")
                if items[0] == scn.Aovs_driver:
                    if items[3] == '1':
                        scn.Aovs_shaders_builtin = True
                    else:
                        scn.Aovs_shaders_builtin = False  
                    if items[4] == '1':
                        scn.Aovs_shaders_hair = True
                    else:
                        scn.Aovs_shaders_hair = False  
                    if items[5] == '1':
                        scn.Aovs_shaders_lambert = True
                    else:
                        scn.Aovs_shaders_lambert = False  
                    if items[6] == '1':
                        scn.Aovs_shaders_mix = True
                    else:
                        scn.Aovs_shaders_mix = False  
                    if items[7] == '1':
                        scn.Aovs_shaders_shadowmatte = True
                    else:
                        scn.Aovs_shaders_shadowmatte = False 
                    if items[8] == '1':
                        scn.Aovs_shaders_skin = True
                    else:
                        scn.Aovs_shaders_skin = False
                    if items[9] == '1':
                        scn.Aovs_shaders_standard = True
                    else:
                        scn.Aovs_shaders_standard = False
                    for i in range(0,32):
                        if items[i+9] == '1':
                            scn.Aovs_shaders_item[i] = True
                        else:
                            scn.Aovs_shaders_item[i] = False       
    def get_list(self, context):
        scn = context.scene.arnold
        driver_items_back = scn.Avos_driver_list
        driver_items_back = driver_items_back.split(";")
        item = []
        for i_item in driver_items_back:
            if i_item:
                items = i_item.split(",")
                enum_list = (items[0],items[1],items[2])
                item.append(enum_list)
        return item
    def execute(self, context):
        scn = context.scene.arnold
        driver_items = scn.Avos_driver_list
        driver_items = driver_items.split(";")
        item = "%d,%s(%s),driver type,"%((len(driver_items)-1) ,
              scn.Aovs_driver_type_name,classes.AovsDriverType[int(scn.Aovs_driver_type)][1])
        scn.Avos_driver_list = scn.Avos_driver_list + item + '0,0,0,0,0,0,0,\
                               0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0;'
        scn.Aovs_driver = "%d"%(len(driver_items)-1)                           
        scn.Aovs_shaders_builtin = False
        scn.Aovs_shaders_hair = False
        scn.Aovs_shaders_lambert = False
        scn.Aovs_shaders_mix = False
        scn.Aovs_shaders_shadowmatte = False
        scn.Aovs_shaders_skin = False
        scn.Aovs_shaders_standard = False
        for i in range(0,31):
            scn.Aovs_shaders_item[i] = False
        return {'FINISHED'}
    def draw(self, context):
        scn = context.scene.arnold
        layout = self.layout
        row = layout.row()
        row.prop(scn, 'Aovs_driver_type')
        row = layout.row()
        row.prop(scn, 'Aovs_driver_type_name')
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    def Aovs_driver_list(self, context): 
        return Aovs_new_driver.driver_items 

class ARNOLD_RP_render(bpy.types.Panel):
    bl_label = ""
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    bl_options = {'HIDE_HEADER'}
    COMPAT_ENGINES = {'arnold_renderer'}
    @classmethod
    def poll(cls, context):
        scn = context.scene.arnold
        rd = context.scene.render
        return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES)
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("arnold.button", text="Render",icon="RENDER_STILL")
        
class ARNOLD_tab_render(bpy.types.Panel):
    bl_label = ""
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
    bl_options = {'HIDE_HEADER'}
    COMPAT_ENGINES = {'arnold_renderer'}
    @classmethod
    def poll(cls, context):
        scn = context.scene.arnold
        rd = context.scene.render
        return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES)
    def draw(self, context):      
        layout = self.layout
        scn = context.scene.arnold
        layout.prop(scn,'ArnoldEnum',expand=True)
        #arnold_menu = context.scene.ArnoldEnum       

class ARNOLD_main_sampling(bpy.types.Panel):
    bl_label = "Sampling"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
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
       
class ARNOLD_main_Ray_depth(bpy.types.Panel):
    bl_label = "Ray depth"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
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
        
class ARNOLD_main_Environment(bpy.types.Panel):
    bl_label = "Environment"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
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
        row.prop(scn, 'Ray_depth_total')
        
class ARNOLD_main_Motion_blur(bpy.types.Panel):
    bl_label = "Motion blur"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
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
        
class ARNOLD_main_lights(bpy.types.Panel):
    bl_label = "Lights"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
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
        row.prop(scn, 'Main_lights')
        
class ARNOLD_main_textures(bpy.types.Panel):
    bl_label = "Textures"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
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
        
class ARNOLD_system_rendersettings(bpy.types.Panel):
    bl_label = "Render settings"
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
        
class ARNOLD_system_searchpaths(bpy.types.Panel):
    bl_label = "Search paths"
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
               
class ARNOLD_diagnostics_log(bpy.types.Panel):
    bl_label = "Log"
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
                                    
class ARNOLD_diagnostics_error(bpy.types.Panel):
    bl_label = "Error handing"
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
        row.prop(scn, 'Error_abort') 
        row = layout.row()
        row.prop(scn, 'Error_texture_error') 
        row = layout.row()
        row.prop(scn, 'Error_nan_error') 

class ARNOLD_override_user(bpy.types.Panel):
    bl_label = "User options"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
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
        row.prop(scn, 'User_options_overrider') 
        
class ARNOLD_override_feature(bpy.types.Panel):
    bl_label = "Feature overrides"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render'
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
        row.prop(scn, 'Subdivision_max_subdivisions') 
        
class ARNOLD_avos_setup(bpy.types.Panel):
    bl_label = "AOVs"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = 'render_layer'
    #bl_options = {'DEFAULT_CLOSED'}
    COMPAT_ENGINES = {'arnold_renderer'}
    @classmethod
    def poll(cls, context):
        rd = context.scene.render
        return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES) 
    def draw(self, context):      
        layout = self.layout 
        row = layout.row()
        row.operator('aovs.setup', text = "Setup AOVs")  
        scn = context.scene.arnold    
        if scn.Avos_is_setup == True:      
            col = layout.column()
            row = col.row()
            row.prop(scn, 'Aovs_driver')
            row.operator('aovs.newdriver', text = "", icon = "ZOOMIN")
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
                    "direct_transmission","indirect_diffuse"
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
                   "sheen","specular",
                   ]
            standard = ["direct_diffuse","direct_specular",
                        "direct_sss","emission",
                        "indirect_diffuse","indirect_specular",
                        "reflection","refraction",
                        "refraction_opactiy","sss"
                        ]
            is_check = []
            if scn.Aovs_shaders_builtin == True:
                for builtin_item in built_in:
                    is_check.append(classes.AovsShaders.index(builtin_item))
                is_check = list(set(is_check))
                is_check = sorted(is_check)      
            if scn.Aovs_shaders_hair == True:
                for hair_item in hair:
                    is_check.append(classes.AovsShaders.index(hair_item))
                is_check = list(set(is_check))
                is_check = sorted(is_check)
            if scn.Aovs_shaders_lambert == True:
                for lambert_item in lambert:
                    is_check.append(classes.AovsShaders.index(lambert_item))
                is_check = list(set(is_check))
                is_check = sorted(is_check) 
            if scn.Aovs_shaders_mix == True:
                for mix_item in mix:
                    is_check.append(classes.AovsShaders.index(mix_item))
                is_check = list(set(is_check))
                is_check = sorted(is_check)
            if scn.Aovs_shaders_shadowmatte == True:
                for shadow_matte_item in shadow_matte:
                    is_check.append(classes.AovsShaders.index(shadow_matte_item))
                is_check = list(set(is_check))
                is_check = sorted(is_check)
            if scn.Aovs_shaders_skin == True:
                for skin_item in skin:
                    is_check.append(classes.AovsShaders.index(skin_item))
                is_check = list(set(is_check))
                is_check = sorted(is_check)
            if scn.Aovs_shaders_standard == True:
                for standard_item in standard:
                    is_check.append(classes.AovsShaders.index(standard_item))
                is_check = list(set(is_check))
                is_check = sorted(is_check)
            if (scn.Aovs_shaders_builtin == True or scn.Aovs_shaders_hair == True or 
                scn.Aovs_shaders_lambert == True or scn.Aovs_shaders_mix == True or 
                scn.Aovs_shaders_shadowmatte == True or scn.Aovs_shaders_skin == True or 
                scn.Aovs_shaders_standard == True):
                row = col.row()
                box = row.box()        
                for item in is_check:        
                    box.prop(scn, 'Aovs_shaders_item', index = is_check.index(item), text = classes.AovsShaders[item])                                          

def register():
    bpy.utils.register_module(__name__)
    
def unregister():
    bpy.utils.unregister_module(__name__)

#if __name__ == "__main__":
#    register()
