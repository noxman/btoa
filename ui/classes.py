#
# arnold For Blender
#
import bpy
PanelGroups = [("0","Main","main setting"),
                ("1","System","system setting"),
                ("2","Diagnostics","diagnostics setting"),
                ("3","Override","override setting")]
FilterTypes = [("0","blackman_harris_filter","filter type"),
                ("1","box_filter","filter type"),
                ("2","catrom2d_filter","filter type"),
                ("3","catrom_filter","filter type"),
                ("4","closest_filter","filter type"),
                ("5","cone_filter","filter type"),
                ("6","cook_filter","filter type"),
                ("7","cubic_filter","filter type"),
                ("8","disk_filter","filter type"),
                ("9","farthest_filter","filter type"),
                ("10","gaussian_filter","filter type"),
                ("11","heatmap_filter","filter type"),
                ("12","mitnet_filter","filter type"),
                ("13","sinc_filter","filter type"),
                ("14","triangle_filter","filter type"),
                ("15","variance_filter","filter type"),
                ("16","video_filter","filter type")]
FilterDomain = [("0","first_hit","filter domain hit"),
                ("1","all_hit","filter domain hit")]
MotionblurPositon = [("0","start on frame","motion blur position"),
                     ("1","center on frame","motion blur position"),
                     ("2","end on frame","motion blur position"),
                     ("3","custom","motion blur position")]
RenderBucketscanning = [("0","top",""),
                       ("1","bottom",""),
                       ("2","left",""),
                       ("3","right",""),
                       ("4","woven",""),
                       ("5","spiral",""),
                       ("6","hilbert","")
                       ]
RenderDisplaybucket = [("0","enabled",""),
                       ("1","disabled in IPR",""),
                       ("2","disabled","")
                       ]
LogVerbositylevel = [("0","Errors",""),
                    ("1","Warnings",""),
                    ("2","Info",""),
                    ("3","Debug","")
                    ]
AovsShaders = ["ID","N","P","Pref","Z","beauty",
                    "cputime","direct_diffuse","direct_specular",
                    "direct_sss","direct_transmission",
                    "emission","indirect_diffuse",
                    "indirect_specular","indirect_sss",
                    "motionvector","opacity",
                    "raycount","reflection",
                    "refraction","refraction_opactiy",
                    "shadow","shadow_matte",
                    "sheen","specular",
                    "sss","texturetime",
                    "volume","volume_direct",
                    "volume_indirect","volum_opacity"
                    ]
AovsDriverType = [("0","driver_arnold_display",""),
                    ("1","driver_deepexr",""),
                    ("2","driver_display",""),
                    ("3","driver_exr",""),
                    ("4","driver_jpeg",""),
                    ("5","driver_png",""),
                    ("6","driver_tiff","")
                    ]
