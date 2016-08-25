#
# arnold For Blender
#
import bpy

from bl_ui import properties_data_lamp
properties_data_lamp.DATA_PT_preview.COMPAT_ENGINES.add('arnold_renderer')
cc = properties_data_lamp

class Arnold_lamp_lamp(cc.DataButtonsPanel, bpy.types.Panel):
    bl_label = "Lamp"
    COMPAT_ENGINES = {'arnold_renderer'}

    def draw(self, context):
        layout = self.layout

        alamp = context.lamp.arnold

        layout.prop(alamp, "lamp_atype", expand=True)
        split = layout.split()

        col1 = split.column()
        col2 = split.column()
        col1.prop(alamp, "lamp_color", text="Color")
        col1.prop(alamp, "lamp_intensity", text="Intensity")
        col1.prop(alamp, "lamp_exposure", text="Exposure")



##def register():
##    bpy.utils.register_module(__name__)
##
##def unregister():
##    bpy.utils.unregister_module(__name__)