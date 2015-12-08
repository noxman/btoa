#
# arnold For Blender
#

def register():
    from btoa.ui import tools
    from btoa.ui import properties_render

    tools.register()
    properties_render.register()


def unregister():
    from btoa.ui import tools
    from btoa.ui import properties_render
    
    tools.unregister()
    properties_render.unregister()
