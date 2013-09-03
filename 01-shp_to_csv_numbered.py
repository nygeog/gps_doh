import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True

arcpy.ImportToolbox('C:\Program Files (x86)\DataEast\XTools Pro\Toolbox\XTOOLS PRO.tbx')

arcpy.env.workspace = r'V:\...\GIS\Data\temp_split'
output_location = r'V:\...\GIS\Data\temp_split_csv'

fc_List = arcpy.ListFeatureClasses()
fnum    = 0

print '______ started at this time: ' + time.strftime('%c') 

for fcList in fc_List:
	print fcList
	#fields = arcpy.ListFeatureClasses(fcList, "HD01_VD*") #"HD0*_VD*" if you wanted both estimates and margin of error

	arcpy.XToolsPro_Table2Text(fcList,"longitude;latitude;thirdaxis",output_location+"/p"+str(fnum)+".csv")

	fnum = fnum + 1



print 'Script ended at this time: ' + time.strftime('%c') 
raw_input("Congrats! Processing has been completed effectively. Press any key to exit") 