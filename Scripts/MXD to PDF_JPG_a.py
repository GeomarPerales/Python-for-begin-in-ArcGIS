#demo 8
import arcpy,os

#ruta general - parametro 1

#impresion de archivos mxd en ruta

arcpy.env.workspace = arcpy.GetParameter(0)
ruta = arcpy.env.workspace
mxd_list = arcpy.ListFiles("*.mxd")

calidad = arcpy.GetParameter(1)

#ciclo iterativo para pedefear todos los mxd
for mxd in mxd_list:

    current_mxd = arcpy.mapping.MapDocument(os.path.join(ruta, mxd))
    pdf = mxd[:-4] + ".pdf"
    jpg = mxd[:-4] + ".jpg"
    arcpy.mapping.ExportToPDF(current_mxd, pdf, resolution = calidad)
    arcpy.mapping.ExportToJPEG(current_mxd, jpg, resolution = calidad)

