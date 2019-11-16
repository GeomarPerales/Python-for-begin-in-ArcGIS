#demo 4
import arcpy

#ruta general
ruta = r"E:/Geomar-TYPSA/134 - Piura - lev. obs. Piura/Plano HI-0002/"

#nombre del mxd
mapa = "02.mxd"

#nombre asignado al mapa

PDF = "demo3.pdf"
r_map = ruta + mapa
mxd = arcpy.mapping.MapDocument(r_map)
salida_PDF = ruta + PDF
arcpy.mapping.ExportToPDF(mxd, salida_PDF,resolution = "500")
