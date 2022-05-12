import arcpy

import os

arcpy.env.workspace = "C:/Users/ethan/Desktop/quiz/airports"

arcpy.env.overwriteOutput = True

airports = "airports.shp"

parse = arcpy.da.SearchCursor(airports, ["FEATURE"])

for element in parse:
    containStatus = False
    unit = "Meters"
    bufferValue = 0
    if "Seaplane Base" in element:
        containStatus = True
        bufferValue = 7500
    elif "Airport" in element:
        containStatus = True
        bufferValue = 15000
    
    if containStatus == True:
        arcpy.Buffer_analysis(airports, "C:/Users/ethan/Desktop/quiz/airports/buffer_airports", str(bufferValue) + " " + unit, "#", "#", "All")


