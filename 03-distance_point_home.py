#python file to calc home to gps point distance

#loop through home address point zip loop through all gps points

#split homes into single feature classes 

arcpy.env.workspace = r'V:\Dropbox\GIS\Data\temp_split'
output_location = r'V:\Dropbox\GIS\Data\temp_distance'

fake_home = r'V:\Dropbox\GIS\Data\temp_fake_home\p1.shp'

#for homept, gpspt in 


fc_List = arcpy.ListFeatureClasses()


for fcList in fc_List:
	print str(fcList[:7])

	arcpy.PointDistance_analysis(fake_home,fcList,output_location+'/'+fcList[:7]+".dbf","#")