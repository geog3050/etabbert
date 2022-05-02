import arcpy
import os

osFolder = os.getcwd()
currentFolder = osFolder.replace(os.sep, '/')

arcpy.env.overwriteOutput = True
testWorkspace = currentFolder + "/hw3.gdb"

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
# Problem 1 (10 Points)
#
# This function reads all the feature classes in a workspace (folder or geodatabase) and
# prints the name of each feature class and the geometry type of that feature class in the following format:
# 'states is a point feature class'

###################################################################### 
def printFeatureClassNames(workspace):
    arcpy.env.workspace = workspace
    
    try:
        featureClasses = arcpy.ListFeatureClasses()

        for i in featureClasses:
            obj = arcpy.Describe(i)
            print(i, "is a", obj.shapeType, "feature class")
    except:
        print("An exception occurred")

###################################################################### 
# Problem 2 (20 Points)
#
# This function reads all the attribute names in a feature class or shape file and
# prints the name of each attribute name and its type (e.g., integer, float, double)
# only if it is a numerical type

###################################################################### 
def printNumericalFieldNames(inputFc, workspace):
    arcpy.env.workspace = workspace
    
    try:
        fields = arcpy.ListFields(inputFc)

        for field in fields:
            if field.type == "Integer" or field.type == "Double" or field.type == "Float":
                print("{0} is type {1}".format(field.name, field.type))
    except:
        print("An exception occurred")

###################################################################### 
# Problem 3 (30 Points)
#
# Given a geodatabase with feature classes, and shape type (point, line or polygon) and an output geodatabase:
# this function creates a new geodatabase and copying only the feature classes with the given shape type into the new geodatabase

###################################################################### 
def exportFeatureClassesByShapeType(input_geodatabase, shapeType, output_geodatabase):
    arcpy.env.workspace = input_geodatabase

    try:
        featureClasses = arcpy.ListFeatureClasses()

        arcpy.CreateFileGDB_management(currentFolder, output_geodatabase)

        for i in featureClasses:
            obj = arcpy.Describe(i)
            if obj.shapeType == "Point" or obj.shapeType == "Line" or obj.shapeType == "Polygon":
                arcpy.CopyFeatures_management(i, (currentFolder + "/" + output_geodatabase))
    except:
        print("An exception occurred")

###################################################################### 
# Problem 4 (40 Points)
#
# Given an input feature class or a shape file and a table in a geodatabase or a folder workspace,
# join the table to the feature class using one-to-one and export to a new feature class.
# Print the results of the joined output to show how many records matched and unmatched in the join operation. 

###################################################################### 
def exportAttributeJoin(inputFc, idFieldInputFc, inputTable, idFieldTable, workspace):
    arcpy.env.workspace = workspace
    
    try:
        joinedTable = arcpy.management.AddJoin(inputFc, idFieldInputFc, inputTable, idFieldTable)
        arcpy.CopyFeatures_management(joinedTable, "joinOutput")
    except:
        print("An exception occurred")

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
