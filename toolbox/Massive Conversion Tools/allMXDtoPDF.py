'''----------------------------------------------------------------------------
 Tool Name:     Massive MXD Conversion.tbx
 Source Name:   allMXDtoPDF.py
 Version:       ArcGIS 10.5
 Author:        Geomar Perales Apaico.
 E-mail:        perales.geomar@gmail.com
 Required Arguments:  An input folder with all file MXDs
                        An input resolution value in DPI

 Description:   convert all MXD files of an Folder to PDF files.
----------------------------------------------------------------------------'''

import arcpy,os

def allMXDtoPDF(ruta_MXD,calidad):
    
    arcpy.env.workspace = ruta_MXD
    ruta = arcpy.env.workspace
    
    mxd_list = arcpy.ListFiles("*.mxd")
    print(mxd_list)
    
    for mxd in mxd_list:
        current_mxd = arcpy.mapping.MapDocument(os.path.join(ruta, mxd))
        pdf = mxd[:-4] + ".pdf"
        print(pdf)
        arcpy.mapping.ExportToPDF(current_mxd, pdf,
                                  resolution = calidad,
                                  image_quality = "BEST",
                                  data_frame = "PAGE_LAYOUT")
        return ruta_MXD, calidad

    del mxd

if __name__ == '__main__':
    ruta_MXD = arcpy.GetParameter(0)
    calidad = arcpy.GetParameter(1)

    try:
        allMXDtoPDF(ruta_MXD,calidad)
    except:
        print('')
