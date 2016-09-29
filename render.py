#
# arnold For Blender
#
import bpy
import ctypes
import re,os,math
from .python.arnold import *
from .options import *
from .polymesh import *
from .camera import *
from .lights import *
from .material import *
from .curves import *
from .presets.preview import *

class ArnoldRenderEngine(bpy.types.RenderEngine):
    # These three members are used by blender to set up the
    # RenderEngine; define its internal name, visible name and capabilities.
    bl_idname = 'arnold_renderer'
    bl_label = 'Arnold Render'
    bl_use_preview = True
    global BtoARend
    global BtoABuckets
    
    def get_instance_materials(self,ob):
        obmats = []
        # Grab materials attached to object instances ...
        if hasattr(ob, 'material_slots'):
            for ms in ob.material_slots:
                obmats.append(ms.material)
        # ... and to the object's mesh data
        if hasattr(ob.data, 'materials'):
            for m in ob.data.materials:
                obmats.append(m)
        return obmats

    def find_preview_material(self,scene):
        # taken from mitsuba exporter
        objects_materials = {}
        for object in [ob for ob in scene.objects if ob.is_visible(scene) and not ob.hide_render]:
            for mat in self.get_instance_materials(object):
                if mat is not None:
                    if object.name not in objects_materials.keys():
                        objects_materials[object] = []
                    objects_materials[object].append(mat)

        # find objects that are likely to be the preview objects
        preview_objects = [o for o in objects_materials.keys()
                           if o.name.startswith('preview')]
        if len(preview_objects) < 1:
            return

        # find the materials attached to the likely preview object
        likely_materials = objects_materials[preview_objects[0]]
        if len(likely_materials) < 1:
            return

        return likely_materials[0]

    # This is the only method called by blender, in this example
    # we use it to detect preview rendering and call the implementation
    # in another method.
    def render(self, scene):
        global BtoARend
        BtoARend = self
        scale = scene.render.resolution_percentage / 100.0
        self.size_x = int(scene.render.resolution_x * scale)
        self.size_y = int(scene.render.resolution_y * scale)

        if self.is_preview:
            self.render_preview(scene)
        elif scene.name == 'final':
            self.render_scene(scene)
        else:
            self.render_scene(scene)

    # In this example, we fill the preview renders with a flat green color.
    def render_preview(self, scene):
        global BtoARend
        global BtoABuckets
        self.scene = scene
        #return

        AiBegin()
        # Filter
        filter = AiNode("cook_filter")
        AiNodeSetStr(filter,"name","outfilter")

        # Display
        output = AiNode("driver_display")
        AiNodeSetStr(output,"name","outdriver")
        AiNodeSetPtr(output,"callback",self.g_displayCallback)

        options = AiUniverseGetOptions()
        outStr= "%s %s %s %s"%("RGBA","RGBA","outfilter","outdriver")
        outs = AiArray(1, 1, AI_TYPE_STRING, outStr.encode('utf-8'))
        AiNodeSetArray(options,"outputs",outs)
        AiNodeSetInt(options,"GI_diffuse_depth",1)
        AiNodeSetInt(options,"GI_diffuse_samples",3)
        AiNodeSetInt(options,"GI_glossy_depth",1)
        AiNodeSetInt(options,"GI_glossy_samples",1)
        AiNodeSetFlt(options,"shader_gamma",2.2)
        AiNodeSetFlt(options,"light_gamma",2.2)
        AiNodeSetFlt(options,"texture_gamma",2.2)
        AiNodeSetFlt(options,"texture_gamma",2.2)
        AiNodeSetInt(options,"AA_samples",0)
        AiNodeSetInt(options,"bucket_size",64)

        AiNodeSetInt(options,"xres",self.size_x)
        AiNodeSetInt(options,"yres",self.size_y)
        
        # Camera
        cam = AiNode("persp_camera")
        AiNodeSetStr(cam,"name","persp")
        pos = AiArrayAllocate(1,1,AI_TYPE_POINT)
        lookat = AiArrayAllocate(1,1,AI_TYPE_POINT)
        AiArraySetPnt(pos,0,AtPoint(0,-3,0))
        AiNodeSetArray(cam,"position",pos)
        AiArraySetPnt(lookat,0,AtPoint(0,0,0))
        AiNodeSetArray(cam,"look_at",lookat)
        AiNodeSetVec(cam,"up",0,0,1)
        fov = math.degrees(2*math.atan((0.5*self.size_x)/(0.5*self.size_y/math.tan(math.radians(45)/2))))
        AiNodeSetFlt(cam,"fov",fov)

        AiNodeSetPtr(options,"camera",cam)
        # light 1
        li01 = AiNode("point_light")
        AiNodeSetStr(li01,"name","li01")
        pos = AiArrayAllocate(1,1,AI_TYPE_POINT)
        AiArraySetPnt(pos,0,AtPoint(-4,-6,4)) 
        AiNodeSetArray(li01,"position",pos)
        AiNodeSetFlt(li01,"intensity",1*300)
        AiNodeSetRGB(li01,"color",1,1,1)
        AiNodeSetFlt(li01,"exposure",0)
        AiNodeSetFlt(li01,"shadow_density",0.25)
        AiNodeSetFlt(li01,"radius",1)
        # light 2
        li02 = AiNode("point_light")
        AiNodeSetStr(li02,"name","li02")
        pos = AiArrayAllocate(1,1,AI_TYPE_POINT)
        AiArraySetPnt(pos,0,AtPoint(5,-3,2)) 
        AiNodeSetArray(li02,"position",pos)
        AiNodeSetFlt(li02,"intensity",1*100)
        AiNodeSetRGB(li02,"color",0.2,0.2,0.2)
        AiNodeSetFlt(li02,"exposure",0)
        AiNodeSetBool(li02,"cast_shadows",False)

        # materials
        mat = self.find_preview_material(scene)
        materials = Materials(scene)
        shader_node = materials.writeMaterial(mat) 
        if mat.preview_render_type not in ['FLAT','SPHERE_A']:     
            # wall
            wall = AiNode("polymesh")
            AiNodeSetStr(wall,"name","wall")
            nsides = wall_nsides
            AiNodeSetArray(wall,"nsides",AiArrayConvert(len(nsides),1,
                AI_TYPE_UINT,(c_uint*len(nsides))(*nsides)))
            vidxs = wall_vidxs
            AiNodeSetArray(wall,"vidxs",AiArrayConvert(len(vidxs),1,
                AI_TYPE_UINT,(c_uint*len(vidxs))(*vidxs)))
            vlist = wall_vlist
            AiNodeSetArray(wall,"vlist",AiArrayConvert(len(vlist),1,
                AI_TYPE_FLOAT,(c_float*len(vlist))(*vlist)))
            am = AiArrayAllocate(1,1,AI_TYPE_MATRIX)
            AiArraySetMtx(am,0,wall_matrix)
            AiNodeSetArray(wall,"matrix",am)
            AiNodeSetBool(wall,"smoothing",True)
            AiNodeSetByte(wall,"visibility",255)
            AiNodeSetInt(wall,"subdiv_type",1)
            AiNodeSetInt(wall,"subdiv_iterations",2)
            wallMat = AiNode("standard")
            AiNodeSetStr(wallMat,"name","wallMat")
            AiNodeSetRGB(wallMat,"Kd_color",0.6,0.6,0.6) 
            AiNodeSetPtr(wall,"shader",wallMat)

        if mat.preview_render_type == 'FLAT':
            # plane
            pl = AiNode("plane")
            AiNodeSetStr(pl,"name","plane")
            AiNodeSetVec(pl,"normal",0,0,1)
            pl_m = AiArrayAllocate(1,1,AI_TYPE_MATRIX)
            AiArraySetMtx(pl_m,0,pl_matrix)
            AiNodeSetArray(pl,"matrix",pl_m)
            AiNodeSetPtr(pl,"shader",shader_node)

        if mat.preview_render_type == 'SPHERE':
            # sphere
            sp = AiNode("sphere")
            AiNodeSetStr(sp,"name","sphere")
            AiNodeSetPnt(sp,"center",0,0,0)
            AiNodeSetFlt(sp,"radius",1)
            AiNodeSetPtr(sp,"shader",shader_node)

        if mat.preview_render_type == 'CUBE':
            # cube
            cu = AiNode("polymesh")
            AiNodeSetStr(cu,"name","cube")
            nsides = [4,4,4,4,4,4]
            AiNodeSetArray(cu,"nsides",AiArrayConvert(len(nsides),1,
                AI_TYPE_UINT,(c_uint*len(nsides))(*nsides)))
            vidxs = cu_vidxs
            AiNodeSetArray(cu,"vidxs",AiArrayConvert(len(vidxs),1,
                AI_TYPE_UINT,(c_uint*len(vidxs))(*vidxs)))
            vlist = cu_vlist
            AiNodeSetArray(cu,"vlist",AiArrayConvert(len(vlist),1,
                AI_TYPE_FLOAT,(c_float*len(vlist))(*vlist)))
            cu_m = AiArrayAllocate(1,1,AI_TYPE_MATRIX)
            AiArraySetMtx(cu_m,0,cu_matrix)
            AiNodeSetArray(cu,"matrix",cu_m)
            AiNodeSetPtr(cu,"shader",shader_node)

        if mat.preview_render_type == 'MONKEY':
            # monkey
            mo = AiNode("polymesh")
            AiNodeSetStr(mo,"name","monkey")
            nsides = mo_nsides
            AiNodeSetArray(mo,"nsides",AiArrayConvert(len(nsides),1,
                AI_TYPE_UINT,(c_uint*len(nsides))(*nsides)))
            vidxs = mo_vidxs
            AiNodeSetArray(mo,"vidxs",AiArrayConvert(len(vidxs),1,
                AI_TYPE_UINT,(c_uint*len(vidxs))(*vidxs)))
            vlist = mo_vlist
            AiNodeSetArray(mo,"vlist",AiArrayConvert(len(vlist),1,
                AI_TYPE_FLOAT,(c_float*len(vlist))(*vlist)))
            AiNodeSetBool(mo,"smoothing",True)
            AiNodeSetInt(mo,"subdiv_type",1)
            AiNodeSetInt(mo,"subdiv_iterations",2)
            mo_m = AiArrayAllocate(1,1,AI_TYPE_MATRIX)
            AiArraySetMtx(mo_m,0,mo_matrix)
            AiNodeSetArray(mo,"matrix",mo_m)
            AiNodeSetPtr(mo,"shader",shader_node) 

        if mat.preview_render_type == 'HAIR':
            # hair
            ha = AiNode("curves")
            AiNodeSetStr(ha,"name","hair")
            num_points = AiArrayAllocate(8,1,AI_TYPE_UINT)
            points = AiArrayAllocate(56,1,AI_TYPE_POINT)
            ptcount = 0
            for count in range(8):
                AiArraySetInt(num_points,count,7)
                for ptidx in range(7):
                    AiArraySetPnt(points,ptcount,
                        AtPoint(ha_point[ptcount*3],ha_point[ptcount*3+1],ha_point[ptcount*3+2]))
                    ptcount += 1      
    
            AiNodeSetArray(ha,"num_points",num_points)
            AiNodeSetArray(ha,"points",points)
            AiNodeSetFlt(ha,"radius",0.01)
            AiNodeSetInt(ha,"mode",1)
            ha_m = AiArrayAllocate(1,1,AI_TYPE_MATRIX)
            AiArraySetMtx(ha_m,0,ha_matrix)
            AiNodeSetArray(ha,"matrix",ha_m)
            AiNodeSetPtr(ha,"shader",shader_node) 

        if mat.preview_render_type == 'SPHERE_A':
            # sphere_a
            sp_a = AiNode("sphere")
            AiNodeSetStr(sp_a,"name","sphere_a")
            AiNodeSetPnt(sp_a,"center",0,0,0)
            AiNodeSetFlt(sp_a,"radius",1)
            sphere_aMat = AiNode("standard")
            AiNodeSetStr(sphere_aMat,"name","sphere_aMat")
            AiNodeSetRGB(sphere_aMat,"Kd_color",0.6,0.6,0.6) 
            AiNodeSetPtr(sp_a,"shader",sphere_aMat) 

        BtoABuckets = {}
        #res = AiRender(AI_RENDER_MODE_CAMERA)
        self.__DoProgressiveRender()
        # AiRender(AI_RENDER_MODE_CAMERA)
        AiASSWrite("D:\\arnold_work\\file.ass", AI_NODE_ALL, False, False)
        BtoABuckets = {}
        AiEnd()

    # In this example, we fill the full renders with a flat blue color.
    def render_scene(self, scene):
        global BtoABuckets
        global mem_peak
        self.scene = scene

        mem_peak = []
        # begin, load first frame, and render it.
        AiBegin()
        # message callback
        AiMsgSetConsoleFlags(AI_LOG_ALL)
        AiMsgSetCallback(self.messagecallback)
##        temp_dir = bpy.app.tempdir + 'progress.log'
##        AiMsgSetLogFileName("D:/log.log")
##        AiMsgSetLogFileFlags(AI_LOG_ALL)
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
        # Curves
        curves = Curves(scene,shader_node)
        curves.writeCurves()
        # Polymesh
        polymesh = Polymesh(scene,shader_node)
        polymesh.writePolymesh()
        # and render your first frame.
        BtoABuckets = {}
        AiRender(AI_RENDER_MODE_CAMERA)
        # AiASSWrite("D:\\arnold_work\\file.ass", AI_NODE_ALL, False, False)
        BtoABuckets = {}
        AiEnd()

    def ArnoldMessageCallback(logMask, severity, msg, tabs):
        global BtoARend
        global mem_peak
        self = BtoARend

        amsg = msg.value.decode()
        mem_use = float((AiMsgUtilGetUsedMemory()/1024/1024))
        mem_use= round(mem_use, 2)
        mem_peak.append(mem_use)

        self.update_memory_stats(mem_use, max(mem_peak))
        self.update_stats('Mem:'+ str(mem_use),'Peak:' + str(max(mem_peak)))

        amsg_progress = re.search('(.*)% done - (.*) rays/pixel', amsg)
        if amsg_progress:
            progress_percent = int(amsg[:3])/100
            self.update_progress(progress_percent)
    messagecallback = AtMsgCallBack(ArnoldMessageCallback)

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
    def __DoProgressiveRender(self):
        '''Handles the rendering of progressive refinement'''
        options = AiUniverseGetOptions()
        sampleLevel = AiNodeGetInt(options,"AA_samples")
        smin = -2
        smax = 2

        samples = [s for s in range(smin, smax + 1) if s != 0 and (s <= 1 or s == smax)]
        sminval = smin
        samples=[]
        while sminval != 0:
            samples.append(sminval)
            sminval = int(math.ceil(sminval*0.5))
        if smax != 0:
            samples.append(smax)
        res = AI_SUCCESS
        for i in samples:
            AiNodeSetInt(options,"AA_samples", i)
            res = AiRender(AI_RENDER_MODE_CAMERA)

            #self.renderFinished.emit(self.renderInterrupted)

            #if res != AI_SUCCESS or self.restartRequested:
            #    break

        # Make sure the original values are restored in case of render interruption
        AiNodeSetInt(options,"AA_samples", sampleLevel)

        return res
# Register the RenderEngine
def register():
    bpy.utils.register_class(ArnoldRenderEngine)

def unregister():
    bpy.utils.unregister_class(ArnoldRenderEngine)