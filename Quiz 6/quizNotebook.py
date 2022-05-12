#Ethan Tabbert
#April 4, 2022
#Quiz 6

import arcpy
import os

def calculatePercentAreaOfPolygonAInPolygonB(input_geodatabase, fcPolygon1, fcPolygon2):
    arcpy.env.workspace = input_geodatabase
    arcpy.env.overwriteOutput = True

    arcpy.SummarizeWithin_analysis(fcPolygon1, fcPolygon2, "percent_AinB", "#", "#", "#", "#", "#", "#", "ADD_PERCENT", "#")

    arcpy.AddField_management("percent_AinB", "parkAreaPercent", "DOUBLE")

    cursor = arcpy.UpdateCursor("percent_AinB")

    for row in cursor:
        areaPercent = row.getValue("sum_Area_SQUAREKILOMETERS")
        area = row.getValue("Shape_Area")
        
        percent = 100 * areaPercent / area
        
        row.setValue("parkAreaPercent", percent)
        
        cursor.updateRow(row)

### I don't know why but I can't get the SummarizeWithin function to work, although it works just fine in ArcGIS notebooks.
### Also, I'm having trouble figuring out how to update the row in block_groups rather than my output file.
### I believe this is because there wasn't a good field to join the output to the block_groups table.

