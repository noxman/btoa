#
# arnold For Blender
#
import bpy
from .python.arnold import *
from . import shaders

class Materials:
    def __init__(self, scene,textures=None):
        self.scene = scene
        self.textures = None
##        if textures:
##            self.textures = textures.texturesDict
        self.materialDict = {}

    def writeMaterials(self):
        for mat in bpy.data.materials:
            self.writeMaterial(mat)

    def writeMaterial(self,mat):
        outmat = None
        currentMaterial = mat.arnold.loadedMaterials[mat.arnold.shaderType]
        outmat = currentMaterial.write(mat,self.textures)

        AiNodeSetStr(outmat,"name",mat.name)
        self.materialDict[mat.as_pointer()] = outmat
        return outmat