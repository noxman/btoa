#
# arnold For Blender
#
import bpy

from bl_ui import properties_material
properties_material.MATERIAL_PT_context_material.COMPAT_ENGINES.add('arnold_renderer')
properties_material.MATERIAL_PT_preview.COMPAT_ENGINES.add('arnold_renderer')
pm = properties_material

def active_node_mat(mat):
    # TODO, 2.4x has a pipeline section, for 2.5 we need to communicate
    # which settings from node-materials are used
    if mat is not None:
        mat_node = mat.active_node_material
        if mat_node:
            return mat_node
        else:
            return mat
    return None

class Arnold_material_diffuse(pm.MaterialButtonsPanel,bpy.types.Panel):
    bl_label = "Diffuse"
    COMPAT_ENGINES = {'arnold_renderer'}
    def draw(self, context):
        layout = self.layout

        mat = active_node_mat(context.material).arnold

        split = layout.split()

        col = split.column()
        col.prop(mat, "diffuse_color", text="")
        sub = col.column()
##        sub.active = (not mat.use_shadeless)
        sub.prop(mat, "diffuse_weight", text="Weight")

        col = split.column()
##        col.active = (not mat.use_shadeless)
##        col.prop(mat, "diffuse_shader", text="")
##        col.prop(mat, "use_diffuse_ramp", text="Ramp")

        col = layout.column()
##        col.active = (not mat.use_shadeless)
        col.prop(mat, "diffuse_roughness")
##        col.prop(mat, "")

##def register():
##    bpy.utils.register_module(__name__)
##
##def unregister():
##    bpy.utils.unregister_module(__name__)