import os
import arcpy
from arcpy.sa import *

###################################################################### 
# Edit the following function definition, replacing the words
# 'name' with your name and 'hawkid' with your hawkid.
# 
# Note: Your hawkid is the login name you use to access ICON, and not
# your firsname-lastname@uiowa.edu email address.
# 
# def hawkid():
#     return(["Caglar Koylu", "ckoylu"])
###################################################################### 
def hawkid():
    return(["Ethan Tabbert", "etabbert"])

###################################################################### 
# Problem 1: 20 Points
#
# Given a csv file import it into the database passed as in the second parameter
# Each parameter is described below:

# csvFile: The absolute path of the file should be included (e.g., C:/users/ckoylu/test.csv)
# geodatabase: The workspace geodatabase
###################################################################### 
def importCSVIntoGeodatabase(csvFile, geodatabase):
    arcpy.env.workspace = geodatabase
    arcpy.env.overwriteOutput = True

    tableName = ""
    currentLetter = ""
    index = -1
    while currentLetter != "/":
        currentLetter = csvFile[index]
        tableName = currentLetter + tableName
        index -= 1

    outputName = tableName[1:-4] + "_gdbConversion.csv"

    arcpy.TableToTable_conversion(csvFile, geodatabase, outputName)

##################################################################################################### 
# Problem 2: 80 Points Total
#
# Given a csv table with point coordinates, this function should create an interpolated
# raster surface, clip it by a polygon shapefile boundary, and generate an isarithmic map

# You can organize your code using multiple functions. For example,
# you can first do the interpolation, then clip then equal interval classification
# to generate an isarithmic map

# Each parameter is described below:

# inTable: The name of the table that contain point observations for interpolation       
# valueField: The name of the field to be used in interpolation
# xField: The field that contains the longitude values
# yField: The field that contains the latitude values
# inClipFc: The input feature class for clipping the interpolated raster
# workspace: The geodatabase workspace

# Below are suggested steps for your program. More code may be needed for exception handling
#    and checking the accuracy of the input values.

# 1- Do not hardcode any parameters or filenames in your code.
#    Name your parameters and output files based on inputs. For example,
#    interpolated raster can be named after the field value field name 
# 2- You can assume the input table should have the coordinates in latitude and longitude (WGS84)
# 3- Generate an input feature later using inTable
# 4- Convert the projection of the input feature layer
#    to match the coordinate system of the clip feature class. Do not clip the features yet.
# 5- Check and enable the spatial analyst extension for kriging
# 6- Use KrigingModelOrdinary function and interpolate the projected feature class
#    that was created from the point feature layer.
# 7- Clip the interpolated kriging raster, and delete the original kriging result
#    after successful clipping. 
#################################################################################################################### 
def krigingFromPointCSV(inTable, valueField, xField, yField, inClipFc, workspace = "assignment3.gdb"):
    arcpy.env.workspace = workspace
    arcpy.env.overwriteOutput = True
    currentFolder = os.getcwd()

    outFC = inTable[:-4] + "_pointClass"

    arcpy.management.XYTableToPoint(inTable, outFC, xField, yField)

    descYearly = arcpy.Describe(outFC)
    cellSize = 0
    width = descYearly.extent.width
    height = descYearly.extent.height
    if width < height:
        cellSize = width / 1000
    else:
        cellSize = height / 1000

    outputName = currentFolder + "\\" + inTable + "_krigingOut"
    outKriging = Kriging(outFC, valueField, "#", cellSize)
    outKriging.save(outputName)

    descClip = arcpy.Describe(inClipFc)
    rectangle = str(descClip.extent.XMin) + " " + str(descClip.extent.YMin) + " " + str(descClip.extent.XMax) + " " + str(descClip.extent.YMax)

    arcpy.Clip_management(outputName, rectangle, outputName + "_clipped", inClipFc, "#", "ClippingGeometry", "MAINTAIN_EXTENT")

    #I am starting to get lost in regards to the isorithmic map generation
    
######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
