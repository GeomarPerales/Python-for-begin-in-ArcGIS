'''----------------------------------------------------------------------------
 Tool Name:     Massive MXD Conversion.tbx
 Source Name:   allMXDtoJPG.py
 Version:       ArcGIS 10.5
 Author:        Geomar Perales Apaico.
 E-mail:        perales.geomar@gmail.com
 Required Arguments:  An input folder with all file MXDs
                        An input resolution value in DPI

 Description:   convert all MXD files of an Folder to JPG files.
----------------------------------------------------------------------------'''

import arcpy,os

def allMXDtoJPG(ruta_MXD,calidad):
    
    arcpy.env.workspace = ruta_MXD
    ruta = arcpy.env.workspace
    
    mxd_list = arcpy.ListFiles("*.mxd")
    print(mxd_list)
    
    for mxd in mxd_list:
        current_mxd = arcpy.mapping.MapDocument(os.path.join(ruta, mxd))
        jpg = mxd[:-4] + ".jpg"
        print(jpg)
        arcpy.mapping.ExportToJPEG(current_mxd, jpg,
                                  resolution = calidad,
                                  data_frame = "PAGE_LAYOUT")

        return mxd_list, jpg, resolution


if __name__ == '__main__':
    ruta_MXD = arcpy.GetParameter(0)
    calidad = arcpy.GetParameter(1)

    try:
        allMXDtoJPG(ruta_MXD,calidad)
    except:
        print('')
