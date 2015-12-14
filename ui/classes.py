#
# arnold For Blender
#
import bpy
PanelGroups = [("0","Main","main setting"),
                ("1","System","system setting"),
                ("2","AOVs","aovs setting"),
                ("3","Diagnostics","diagnostics setting"),
                ("4","Override","override setting")]
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

