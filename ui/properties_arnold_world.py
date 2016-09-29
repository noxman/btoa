#
# arnold For Blender
#
import bpy

from bl_ui import properties_world
cc = properties_world
# WorldButtonsPanel

# Inherit World Preview Panel
cc.WORLD_PT_preview.COMPAT_ENGINES.add('arnold_renderer')
cc.WORLD_PT_context_world.COMPAT_ENGINES.add('arnold_renderer')


class Arnold_PT_world(cc.WorldButtonsPanel, bpy.types.Panel):
    bl_label = "Background(sky)"
    # bl_options = {'HIDE_HEADER'}
    COMPAT_ENGINES = {'arnold_renderer'}

    def draw(self, context):
        layout = self.layout
        world = context.world.arnold
        layout.prop(world, "arnold_sky")
        if world.arnold_sky:
            layout.prop(world, "sky_type", expand=True)
            split = layout.split()
            col = layout.column()
            col.prop(world, "sky_valuetype", text="Valuetype:")


class Arnold_PT_world_sky(cc.WorldButtonsPanel, bpy.types.Panel):
    bl_label = "Sky"
    COMPAT_ENGINES = {'arnold_renderer'}
    tabNum = {'0'}

    @classmethod
    def poll(cls, context):
        sky_type = context.world.arnold.sky_type
        arnold_sky = context.world.arnold.arnold_sky
        rd = context.scene.render
        return ((rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES) 
        and (sky_type in cls.tabNum) and arnold_sky)

    def draw(self, context):
        layout = self.layout
        world = context.world.arnold

        row = layout.row()
        row.prop(world, "sky_color")
        row = layout.row()
        row.prop(world, "sky_colorvaluetype", text="Valuetype:")
        row = layout.row()
        row.prop(world, "sky_format", text="Format:")
        row = layout.row()
        row.prop(world, "sky_intensity")
        row = layout.row()
        row.prop(world, "sky_intensityvaluetype", text="Valuetype:")
        row = layout.row()
        row.prop(world, "casts_shadows")
        row = layout.row()
        row.prop(world, "primary_visibility")
        row = layout.row()
        row.label(text="Visible:")
        row = layout.row()
        split = row.split()
        split.prop(world, "visible_reflections")
        split.prop(world, "visible_refractions")
        row = layout.row()
        split = row.split()
        split.prop(world, "visible_diffuse")
        split.prop(world, "visible_glossy")
        row = layout.row()
        split = row.split()
        col = split.column()
        col.prop(world, "sky_rotate")
        col = split.column()
        col.prop(world, "sky_scale")

class Arnold_PT_world_Physical_sky(cc.WorldButtonsPanel, bpy.types.Panel):
    bl_label = "Physical Sky"
    COMPAT_ENGINES = {'arnold_renderer'}
    tabNum = {'1'}

    @classmethod
    def poll(cls, context):
        sky_type = context.world.arnold.sky_type
        arnold_sky = context.world.arnold.arnold_sky
        rd = context.scene.render
        return ((rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES) 
        and (sky_type in cls.tabNum) and arnold_sky)

    def draw(self, context):
        layout = self.layout
        world = context.world.arnold

        row = layout.row()
        row.prop(world, "physical_sky_turbidity")
        row = layout.row()
        row.prop(world, "physical_sky_ground_albedo")
        row = layout.row()
        row.prop(world, "physical_sky_elevation")
        row = layout.row()
        row.prop(world, "physical_sky_azimuth")
        row = layout.row()
        row.prop(world, "physical_sky_intensity")
        row = layout.row()
        row.prop(world, "physical_sky_tint")
        row = layout.row()
        row.prop(world, "physical_sky_sun_tint")
        row = layout.row()
        row.prop(world, "physical_sky_sun_size")
        row = layout.row()
        row.prop(world, "physical_sky_sun")