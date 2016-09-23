import bpy
from .python.arnold import *
import wx

class Options:

    def __init__(self, render):
        self.scene = bpy.context.scene
        self.options = AiUniverseGetOptions()
        self.render = render

    def setOutput(self, filter, driver, outType="RGBA"):
        outStr = "%s %s %s %s" % (outType, outType, filter, driver)
        outs = AiArray(1, 1, AI_TYPE_STRING, outStr.encode('utf-8'))
        AiNodeSetArray(self.options, "outputs", outs)

    def writeOptions(self):
        AiNodeSetStr(self.options, "name", "options")
        AiNodeSetInt(self.options, "xres", self.render.size_x)
        AiNodeSetInt(self.options, "yres", self.render.size_y)