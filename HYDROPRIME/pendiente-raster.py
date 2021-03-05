import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = "D:\\Geomar\\2-CODE\\2.1-PYTHON\\Hydroprime"
RAS_list = arcpy.ListFiles("*.tif")
RAS_list
outSlope = Slope( RAS_list[0], "DEGREE")




