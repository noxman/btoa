#
# arnold For Blender
#
import bpy
from .python.arnold import *
##from . import shaders

class Materials:
    def __init__(self, scene):
        self.scene = scene
##        if textures:
##            self.textures = textures.texturesDict
##        self.materialDict = {}

    def writeMaterials(self):
        for mat in bpy.data.materials:
            outmat = self.writeMaterial(mat)
        return outmat
    def writeMaterial(self, mat):
##        outmat = None
##        currentMaterial = mat.arnold.loadedMaterials[mat.arnold.shaderType]
        self.mat = mat
        st = self.mat.arnold
        outmat = AiNode("standard")

        AiNodeSetStr(outmat,"name",self.mat.name)
        AiNodeSetRGB(outmat,"Kd_color",st.diffuse_color.r,
                                          st.diffuse_color.g,
                                          st.diffuse_color.b)
        return outmat