import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True

arcpy.ImportToolbox('C:\Program Files (x86)\DataEast\XTools Pro\Toolbox\XTOOLS PRO.tbx')

arcpy.env.workspace = r'V:\...\GIS\Data\temp_split_csv\only_large_files'
output_location = r'V:\...\GIS\Data\temp_split_csv\only_large_files\renumbered'

tb_List = arcpy.ListTables()
fnum    = 0

print '______ started at this time: ' + time.strftime('%c') 

for tbList in tb_List:
	print tbList

	arcpy.Copy_management(tbList, output_location+"/p"+str(fnum)+".csv")

	fnum = fnum + 1