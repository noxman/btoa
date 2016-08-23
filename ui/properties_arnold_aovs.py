#
# arnold For Blender
#
import bpy

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
                        if items[i+10] == '1':
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

class Aovs_del_driver(bpy.types.Operator):
    bl_idname = "aovs.deldriver"
    bl_label = "AvosDelDriver"
    def execute(self, context):
        scn = context.scene.arnold
        driver_items_back = scn.Avos_driver_list
        driver_items_back = driver_items_back.split(";")
        total = ''
        for i_item in driver_items_back:
            if i_item:
                items = i_item.split(",")
                if items[0] == scn.Aovs_driver:
                    scn.Aovs_driver = str(int(items[0])-1)
                    i_item = ''
                else:
                    i_item = i_item + ';'
                total = total + i_item
        scn.Avos_driver_list = total
        return {'FINISHED'}

class ARNOLD_avos_setup(bpy.types.Panel):
    bl_label = "AOVs"
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
        row = layout.row()
        row.operator('aovs.setup', text = "Setup AOVs")
        scn = context.scene.arnold
        if scn.Avos_is_setup == True:
            row = layout.row(align=True)
            row.alignment = 'EXPAND'
            row.prop(scn, 'Aovs_driver')
            row.operator('aovs.newdriver', text = "", icon = "ZOOMIN")
            if scn.Aovs_driver != '0':
                row.operator('aovs.deldriver', text = "", icon = "ZOOMOUT")
            col = layout.column()
            row = col.row()
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
##def register():
##    bpy.utils.register_module(__name__)
##
##def unregister():
##    bpy.utils.unregister_module(__name__)