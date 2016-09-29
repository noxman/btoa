#
# arnold For Blender
#
import bpy

# from bpy.types import Curve, SurfaceCurve, TextCurve
from bl_ui import properties_data_curve
cc = properties_data_curve

# class CurveButtonsPanelCurve(CurveButtonsPanel):
#     @classmethod
#     def poll(cls, context):
#         return (type(context.curve) is Curve)

class Arnold_curve_render(cc.CurveButtonsPanel, bpy.types.Panel):
    bl_label = "Arnold Curve"
    bl_options = {'DEFAULT_CLOSED'}
    COMPAT_ENGINES = {'arnold_renderer'}

    def draw(self, context):
        layout = self.layout

        curve = context.curve.arnold
        layout.prop(curve,'curve_render')
        if curve.curve_render == True:
            row = layout.row()
            row.prop(curve,'curve_width')
            row.prop(curve,'curve_scale')
            if curve.curve_scale == True:
                layout.template_curve_mapping(curve, "curve_scale")
    # settings = self.paint_settings(context)

    # brush = settings.brush

    # layout.template_curve_mapping(brush, "curve", brush=True)