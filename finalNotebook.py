import os
import arcpy

arcpy.env.overwriteOutput = True

arcpy.management.CreateFileGDB("E:/Final Project/finalProject", "FinalProject")

arcpy.env.workspace = "FinalProject.gdb"

arcpy.conversion.FeatureClassToGeodatabase("E:/Final Project/tl_2021_us_state/tl_2021_us_state.shp", "FinalProject.gdb")

arcpy.conversion.FeatureClassToGeodatabase("E:/Final Project/watershed/WBD_HU_08_IA.shp", "FinalProject.gdb")

arcpy.conversion.FeatureClassToGeodatabase("E:/Final Project/watershed/WBD_HU_10_IA.shp", "FinalProject.gdb")

arcpy.conversion.FeatureClassToGeodatabase("E:/Final Project/watershed/WBD_HU_12_IA.shp", "FinalProject.gdb")

arcpy.analysis.Clip("E:/Final Project/watershed/WBD_HU_08_IA.shp", "E:/Final Project/finalProject/FinalProject.gdb/iowa_shape", "iowaWatershed_clipped")

arcpy.analysis.Clip("E:/Final Project/watershed/WBD_HU_10_IA.shp", "E:/Final Project/finalProject/FinalProject.gdb/iowa_shape", "iowaWatershed_clipped_huc10")

arcpy.analysis.Clip("E:/Final Project/watershed/WBD_HU_12_IA.shp", "E:/Final Project/finalProject/FinalProject.gdb/iowa_shape", "iowaWatershed_clipped_huc12")

arcpy.conversion.RasterToGeodatabase("E:/Final Project/land_cover/landCover2019.tiff", "FinalProject.gdb")

arcpy.ValidateTableName("landCover2019")

arcpy.management.Clip("landCover2019", "#", "landCover2019Clipped", "iowa_shape", "#", "ClippingGeometry", "#")

arcpy.conversion.TableToGeodatabase("E:/Final Project/land_cover/landCoverLegend.csv", "finalProject.gdb")

arcpy.conversion.FeatureClassToGeodatabase("E:/Final Project/2020_Impaired_Streams_of_Iowa/2020_Impaired_Streams_of_Iowa.shp", "finalProject.gdb")

arcpy.analysis.SummarizeWithin("iowaWatershed_clipped_huc12", "2020_Impaired_Streams_of_Iowa", "huc12_impaired_streams", "ONLY_INTERSECTING")

arcpy.sa.ZonalStatisticsAsTable("huc12_impaired_streams", "HUC_12", "landCover2019Clipped", "landCoverImpairedStreamsStats", "#", "#", "#", "95", "#")

arcpy.conversion.TableToTable("landCoverImpairedStreamsStats", "E:/Final Project", "outputData.csv")


