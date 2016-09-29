#
# arnold For Blender
#
import bpy
from bl_ui.properties_material import (MaterialButtonsPanel,
                                       active_node_mat,
                                       check_material)
# properties_material.MATERIAL_PT_context_material.COMPAT_ENGINES.add('arnold_renderer')
# properties_material.MATERIAL_PT_preview.COMPAT_ENGINES.add('arnold_renderer')

class Arnold_MATERIAL_PT_preview(MaterialButtonsPanel):
    bl_label = "Preview"
    COMPAT_ENGINES = {'arnold_renderer'}

    def draw(self, context):
        self.layout.template_preview(context.material)

class Arnold_MaterialTypePanel(MaterialButtonsPanel):
    COMPAT_ENGINES = {'arnold_renderer'}

    @classmethod
    def poll(cls, context):
        arnold_mat = context.material
        engine = context.scene.render.engine
        return check_material(arnold_mat) and  (engine in cls.COMPAT_ENGINES)
        # return check_material(arnold_mat) and (arnold_mat.mat_type in cls.material_type) and (engine in cls.COMPAT_ENGINES)

class Arnold_PT_context_material(MaterialButtonsPanel,bpy.types.Panel):
    bl_label = ""
    bl_options = {'HIDE_HEADER'}
    COMPAT_ENGINES = {'arnold_renderer'}

    @classmethod
    def poll(cls, context):
        # An exception, dont call the parent poll func because
        # this manages materials for all engine types
        engine = context.scene.render.engine
        return (context.material or context.object) and (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
        layout = self.layout

        arnold_mat = context.material
        ob = context.object
        slot = context.material_slot
        space = context.space_data

        if ob:
            row = layout.row()
            if bpy.app.version < (2, 65, 3 ):
                row.template_list(ob, "material_slots", ob, "active_material_index", rows=2)
            else:
                row.template_list("MATERIAL_UL_matslots", "", ob, "material_slots", ob, "active_material_index", rows=2)

            col = row.column(align=True)
            col.operator("object.material_slot_add", icon='ZOOMIN', text="")
            col.operator("object.material_slot_remove", icon='ZOOMOUT', text="")

            # TODO: code own operators to copy arnold material settings...
            col.menu("MATERIAL_MT_specials", icon='DOWNARROW_HLT', text="")

            if ob.mode == 'EDIT':
                row = layout.row(align=True)
                row.operator("object.material_slot_assign", text="Assign")
                row.operator("object.material_slot_select", text="Select")
                row.operator("object.material_slot_deselect", text="Deselect")

        split = layout.split(percentage=0.75)

        if ob:
            split.template_ID(ob, "active_material", new="material.new")
            row = split.row()
            if slot:
                row.prop(slot, "link", text="")
            else:
                row.label()

        elif arnold_mat:
            split.template_ID(space, "pin_id")
            split.separator()

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

class Arnold_material_diffuse(Arnold_MaterialTypePanel,bpy.types.Panel):
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