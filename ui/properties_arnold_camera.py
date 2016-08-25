#
# arnold For Blender
#
import bpy

from bl_ui import properties_data_camera
properties_data_camera.DATA_PT_context_camera.COMPAT_ENGINES.add('arnold_renderer')
cc = properties_data_camera

class Arnold_camera_lens(cc.CameraButtonsPanel, bpy.types.Panel):
    bl_label = "Lens"
    COMPAT_ENGINES = {'arnold_renderer'}

    def draw(self, context):
        layout = self.layout

        acam = context.camera.arnold
        layout.prop(acam, "camera_type", expand=True)
        split = layout.split()

        col = split.column()
        col.prop(acam, "camera_angle")
        col = split.column()
        col.prop(acam, "camera_lens")


        split = layout.split()

        col = split.column(align=True)
        col.label(text="Clipping:")
        col.prop(acam, "camera_clip_start", text="Start")
        col.prop(acam, "camera_clip_end", text="End")

        col = split.column(align=True)
        col.label(text="Scale:")
        col.prop(acam, "camera_scale")

        layout.prop(acam, "camera_exposure")

        split = layout.split()

        col = split.column(align=True)
        layout.prop(acam, "camera_rollingshutter")
        layout.prop(acam, "damera_rollingshutterduration")

class Arnold_camera_dof(cc.CameraButtonsPanel, bpy.types.Panel):
    bl_label = "Depth of Field"
    COMPAT_ENGINES = {'arnold_renderer'}

    def draw(self, context):
        layout = self.layout

        acam = context.camera
        split = layout.split()
        split.prop(acam, "dof_distance", text="Distance")

        col = split.column()

##        if cam.dof_object != None:
##            col.enabled = False
##        col.prop(cam, "dof_distance", text="Distance")

##        split = layout.split()
##        split.prop(cam,"BtoA_aperture_size")
##        split.prop(cam,"BtoA_aperture_blades")

##def cdraw(cls, context):
##    rd = context.scene.render
##    if rd.engine == 'arnold_renderer':
##        layout = cls.layout
##        scn = context.scene.arnold
##        arnold_menu = scn.ArnoldEnum
##        context.scene.camera.type = arnold_menu
##        layout.prop(scn,'ArnoldEnum',expand=True)
##properties_data_camera.DATA_PT_lens.prepend(cdraw)
##for member in dir(properties_data_camera):
##    subclass = getattr(properties_data_camera, member)
##    try:
##        if subclass.bl_label != "Lens":
##            subclass.COMPAT_ENGINES.add('arnold_renderer')
##    except:
##        pass

del properties_data_camera

##def register():
##    bpy.utils.register_module(__name__)
##
##
##    bpy.utils.unregister_module(__name__)