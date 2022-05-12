

def import_data(filename):
    
    majorityValuePerZone = []
    minorityValuePerZone = []
    percentileValue95 = []

    firstLine = True
    
    file = open(filename, 'r')
    for row in file:
        if firstLine == True:
            firstLine = False
            continue
        placeholder = ""
        location = 0
        for element in row:
            if element.isalpha() == True or element.isdigit() == True or element == ".":
                placeholder += element
            else:
                if location == 12:
                    majorityValuePerZone.append(int(placeholder))
                elif location == 13:
                    minorityValuePerZone.append(int(placeholder))
                elif location == 15:
                    percentileValue95.append(int(placeholder))
                else:
                    pass
                placeholder = ""
                location += 1

    majorityValueList = []
    minorityValueList = []
    percentileValueList = []

    totalCount = 0
    majorityCropCount = 0
    percentileCropCount = 0
    
    for i in majorityValuePerZone:
        if i not in majorityValueList:
            majorityValueList.append(i)
        
    for i in minorityValuePerZone:
        if i not in minorityValueList:
            minorityValueList.append(i)

    for i in percentileValue95:
        if i not in percentileValueList:
            percentileValueList.append(i)

    for i in majorityValuePerZone:
        totalCount += 1
        if i == 82:
            majorityCropCount += 1

    for i in percentileValue95:
        if i == 82:
            percentileCropCount += 1

    majorityPercent = majorityCropCount / totalCount * 100
    percentilePercent = percentileCropCount / totalCount * 100

            
    print("Total Count: " + str(totalCount))
    print("Zones where majority is cropland: " + str(majorityCropCount))
    print("Zones where cropland takes up 95% or more of the zone: " + str(percentileCropCount))
    print("Percent of zones with majority cropland: {:.2f}".format(majorityPercent))
    print("Percent of zones with over 95% cropland: {:.2f}".format(percentilePercent))
