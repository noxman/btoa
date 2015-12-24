import bpy

class ArnoldTools(bpy.types.Panel):
    """Creates a Panel in the TOOLS window"""
    bl_category = "Arnold"
    bl_label = "BtoA"
    bl_idname = "TOOLS_Arnold"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    COMPAT_ENGINES = {'arnold_renderer'}
    @classmethod
    def poll(cls, context):
        scn = context.scene.arnold
        rd = context.scene.render
        return (rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES)
    def draw(self, context):
        layout = self.layout
        layout.label("Light:",icon="LAMP_DATA")
        row = layout.row()
        split = row.split()
        col = split.column()
        light=['cylinder_light','disk_light','distant_light','mesh_light','photometric_light']
        for lightType in light:
            col.operator("arnold.button", text=lightType)
        split = row.split() 
        col = split.column() 
        light=['point_light','quad_light','skydome_light','spot_light']
        for lightType in light:
            col.operator("arnold.button", text=lightType)
            
        row = layout.row()
        split = row.split()
        col = split.column()      
        col.label("Sky:",icon="WORLD_DATA")
        #row = layout.row()
        col.operator("arnold.button", text="Arnold_Sky")
        
        split = row.split()
        col = split.column() 
        col.label("Procedural:",icon="TEXTURE_SHADED")
        #col = layout.row()
        col.operator("arnold.button", text="Arnold_Procedural")
        
        row = layout.row()
        split = row.split()
        col = split.column() 
        col.label("Volume:",icon="SNAP_VOLUME")
        #row = layout.row()
        col.operator("arnold.button", text="Arnold_Volume")
        
        split = row.split()
        col = split.column() 
        col.label("Driver:",icon="DRIVER")
        #row = layout.row()
        col.operator("arnold.button", text="Arnold_Driver")
        
        row = layout.row()
        split = row.split()
        col = split.column() 
        col.label("AOV:",icon="RENDERLAYERS")
        #row = layout.row()
        col.operator("arnold.button", text="Arnold_AOV")
        
        split = row.split()
        col = split.column() 
        col.label("TP Group:",icon="RENDERLAYERS")
        #row = layout.row()
        col.operator("arnold.button", text="Arnold_TP_Group")
        
        row = layout.row()
        split = row.split()
        col = split.column() 
        col.label("IPR:",icon="CAMERA_DATA")
        #row = layout.row()
        col.operator("arnold.button", text="IPR_Winodw")
        
        split = row.split()
        col = split.column() 
        col.label("ASS:",icon="EXPORT")
        #row = layout.row()
        col.operator("arnold.button", text="ASS_Export")

        row = layout.row()
        split = row.split()
        col = split.column() 
        col.label("TX :",icon="TEXTURE_DATA")
        #row = layout.row()
        col.operator("arnold.button", text="TX_Manager")
        
        #no use,just black
        split = row.split()
        col = split.column()
        
        layout.label("Flush Caches:",icon="CANCEL")
        row = layout.row()
        split = row.split()
        col = split.column()
        flush=['Textures','Skydome lights']
        for flushType in flush:
            col.operator("arnold.button", text=flushType)
        split = row.split()
        col = split.column()   
        flush=['Quad lights','ALL']
        for flushType in flush:
            col.operator("arnold.button", text=flushType)
            
class Arnold_Tools_Button(bpy.types.Operator):
    bl_idname = "arnold.button"
    bl_label = "Button"  
         
def register():
    bpy.utils.register_module(__name__)
    
def unregister():
    bpy.utils.unregister_module(__name__)
   
#if __name__ == "__main__":
#    register()    
 
