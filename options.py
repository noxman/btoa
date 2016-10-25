import bpy
from .python.arnold import *

class Options:
    def __init__(self,render):
        self.scene = bpy.context.scene
        self.options = AiUniverseGetOptions()
        self.render = render

    def setOutput(self,filter,driver,outType="RGBA"):
        outStr= "%s %s %s %s"%(outType,outType,filter,driver)
        outputs_array = AiArrayAllocate(1, 1, AI_TYPE_STRING)
        outs = AiArraySetStr(outputs_array, 0, outStr)
        AiNodeSetArray(self.options,"outputs",outputs_array)

    def writeOptions(self):
        AiNodeSetStr(self.options,"name","options")
        AiNodeSetInt(self.options,"xres",self.render.size_x)
        AiNodeSetInt(self.options,"yres",self.render.size_y)
        AiNodeSetInt(self.options, "GI_diffuse_depth", 4)
