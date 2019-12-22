#demo 6
import arcpy,os

#ruta general
ruta = r"E:/Geomar-TYPSA/134 - Piura - lev. obs. Piura/General/"

#impresion de archivos mxd en ruta
arcpy.env.workspace = ruta
mxd_list = arcpy.ListFiles("*.mxd")
print(mxd_list)

#ancho y altura
width = 640
height = 480

for mxd in mxd_list:

    current_mxd = arcpy.mapping.MapDocument(os.path.join(ruta, mxd))
    pdf = mxd[:-4] + ".pdf"
    arcpy.mapping.ExportToPDF(current_mxd, pdf, resolution = "800", width, height)

del mxd_list


