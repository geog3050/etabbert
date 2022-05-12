#Ethan Tabbert
#February 8, 2022
#Geospatial Programming

def statusOfLeaves(climate, temps):
    outputStatus = ""
    
    #Setting these to lowercase so that they can be compared regardless of input case
    
    if climate.lower() == "tropical":

        for i in temps:
            if i <= float(30):
                outputStatus += 'F \n'
            else:
                outputStatus += 'U \n'
    elif climate.lower() == "continental":

        for i in temps:
            if i <= float(25):
                outputStatus += 'F \n'
            else:
                outputStatus += 'U \n'
    else:

        for i in temps:
            if i <= float(18):
                outputStatus += 'F \n'
            else:
                outputStatus += 'U \n'

    #Printing because return does not allow usage of \n newline
    print(outputStatus)
