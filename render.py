import bpy
import ctypes
from .python.arnold import *
from .options import *
from .polymesh import *
from .camera import *
from .lights import *
from .material import *

class ArnoldRenderEngine(bpy.types.RenderEngine):
    # These three members are used by blender to set up the
    # RenderEngine; define its internal name, visible name and capabilities.
    bl_idname = 'arnold_renderer'
    bl_label = 'Arnold'
    bl_use_preview = True
    global BtoARend
    global BtoABuckets
    # This is the only method called by blender, in this example
    # we use it to detect preview rendering and call the implementation
    # in another method.
    def render(self, scene):
        global BtoARend
        BtoARend = self
        scale = scene.render.resolution_percentage / 100.0
        self.size_x = int(scene.render.resolution_x * scale)
        self.size_y = int(scene.render.resolution_y * scale)

        if scene.name == 'preview':
            self.render_preview(scene)
        else:
            self.render_scene(scene)

    # In this example, we fill the preview renders with a flat green color.
    def render_preview(self, scene):
        pixel_count = self.size_x * self.size_y

        # The framebuffer is defined as a list of pixels, each pixel
        # itself being a list of R,G,B,A values
        green_rect = [[0.0, 1.0, 0.0, 1.0]] * pixel_count

        # Here we write the pixel values to the RenderResult
        result = self.begin_result(0, 0, self.size_x, self.size_y)
        layer = result.layers[0].passes["Combined"]
        layer.rect = green_rect
        self.end_result(result)

    # In this example, we fill the full renders with a flat blue color.
    def render_scene(self, scene):
        global BtoABuckets
        self.scene = scene

        # begin, load first frame, and render it.
        AiBegin()

        # Filter
        filter = AiNode("gaussian_filter")
        AiNodeSetStr(filter,"name","outfilter")
        # Options
        options = Options(self)
        options.writeOptions()
        options.setOutput("outfilter","outdriver",outType="RGBA")
         # Display
        output = AiNode("driver_display")
        AiNodeSetStr(output,"name","outdriver")
        AiNodeSetPtr(output,"callback",self.g_displayCallback)
        # Camera
        camera = Camera(self)
        camera.writeCamera()
        options.setCamera(camera.ArnoldCamera)
        # Lights
        lights = Lights()
        lights.writeLights()
        # Material
        materials = Materials(scene)
        shader_node = materials.writeMaterials()
        # Polymesh
        polymesh = Polymesh(scene,shader_node)
        polymesh.writePolymesh()

##        AiMsgSetConsoleFlags(AI_LOG_ALL);
        # and render your first frame.
        BtoABuckets = {}
        AiRender(AI_RENDER_MODE_CAMERA)
        AiASSWrite("D:\\arnold_work\\file.ass", AI_NODE_ALL, False, False)
        BtoABuckets = {}
        AiEnd()

    def ArnoldDisplayCallback(x, y, width, height, buffer, data):
        global BtoARend
        global BtoABuckets

        self = BtoARend
        result = self.begin_result(x,
                                   self.size_y - y - height,
                                   width,height)
        layer = result.layers[0].passes["Combined"]

        if buffer:
            bucket = []
            row = []
            pixels = ctypes.cast(buffer, POINTER(AtUInt8))
            # Here we write the pixel values to the RenderResult
            for i in range(0,width*height*4,4):
                r = pixels[i]
                g = pixels[i+1]
                b = pixels[i+2]
                a = pixels[i+3]
                pixelColor = [r/255,g/255,b/255,a/255]
                row.append(pixelColor)

            for i in range(0,len(row),width):
                qq = row[i:i+width]
                qq.reverse()
                bucket.extend(qq)

            bucket.reverse()
            BtoABuckets["%s%s"%(x,y)]=bucket
            layer.rect = bucket
        else:
            size = width * height
            try:
                bucket = BtoABuckets["%s%s"%(x,y)]
            except:
                bucket = [[0,0,0,1]] * size

            edge = [0.5,0.25,0.25,1]
            if self.scene.name !="preview":
                for i in range(0,size,width*2):
                    bucket[i] = edge
                    bucket[i+width - 1] = edge
                for i in [0,size - width]:
                    for j in range(i,i+width,2):
                        bucket[j] = edge

            layer.rect = bucket

        if self.test_break():
            AiRenderInterrupt()

        self.end_result(result)

    g_displayCallback = AtDisplayCallBack(ArnoldDisplayCallback)

# Register the RenderEngine
def register():
    bpy.utils.register_class(ArnoldRenderEngine)

def unregister():
    bpy.utils.unregister_class(ArnoldRenderEngine)

