import bpy
from .python.arnold import *
from bpy.types import Panel
from rna_prop_ui import PropertyPanel

from bpy.types import Curve, SurfaceCurve, TextCurve

class CurveButtonsPanelCurve(CurveButtonsPanel):
    @classmethod
    def poll(cls, context):
        return (type(context.curve) is Curve)

class Arnold_curve(CurveButtonsPanel, Panel):
    bl_label = "Arnold Curve"
    bl_options = {'DEFAULT_CLOSED'}
    COMPAT_ENGINES = {'arnold_renderer'}

    def draw(self, context):
    	layout = self.layout
        scn = context.curve.arnold
        row = layout.row()
        row.prop(scn, 'curve_render')
    # settings = self.paint_settings(context)

    # brush = settings.brush

    # layout.template_curve_mapping(brush, "curve", brush=True)