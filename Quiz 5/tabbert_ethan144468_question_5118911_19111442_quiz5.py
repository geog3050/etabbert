#Ethan Tabbert
#Quiz 5

import importlib
print("This program will test for functionality with the Homework 2 assignment.")
print("It will give you a score out of 220 where each successful function gives you 10 points.")
filename = input("Enter the filename to test (without the extension): ")
pyfile = importlib.__import__(filename)

fileList = ["test1.txt", "test2.txt", "test3.txt", "test4.txt", "test5.txt"]
score = 0

print("Testing hawkID function...")

for i in pyfile.hawkid():
    try:
        print(i)
        print("Success!")
        score += 10
    except:
        print("An exception occurred while locating your hawkID")

print("Testing import_data function...")

for i in fileList:
    try:
        print("Importing " + i)
        pyfile.import_data(i)
        print("Success!")
        score += 10
    except:
        print("An exception occurred in " + i + " on function import_data")

print("Testing attack_multiplier function...")

testElements1 = ["Water", "Electric", "Ground", "Fire", "Grass"]
testElements2 = ["Fire", "Water", "Electric", "Grass", "Water"]

for i in range(0, len(testElements1)):
    try:
        print(testElements1[i] + " attacks " + testElements2[i])
        result = pyfile.attack_multiplier(testElements1[i], testElements2[i])
        if testElements1[i] == "Water" and testElements2[i] == "Fire" and result == 2.5:
            print("x2.5 damage - Success!")
            score += 10
        elif testElements1[i] == "Electric" and testElements2[i] == "Water" and result == 1.3:
            print("x1.3 damage - Success!")
            score += 10
        elif testElements1[i] == "Ground" and testElements2[i] == "Electric" and result == 2.0:
            print("x2.0 damage - Success!")
            score += 10
        elif testElements1[i] == "Fire" and testElements2[i] == "Grass" and result == 3.0:
            print("x3.0 damage - Success!")
            score += 10
        elif testElements1[i] == "Grass" and testElements2[i] == "Water" and result == 1.5:
            print("x1.5 damage - Success!")
            score += 10
        else:
            print("Failure")
    except:
        print("An exception occurred while testing " + testElements1[i] + " against " + testElements2[i])

print("Testing fight function...")

for i in fileList:
    try:
        print("Fighting four participants from file " + i)
        for element in range(0, len(pyfile.import_data("test1.txt"))-1):
            pyfile.fight(pyfile.import_data(i)[element], pyfile.import_data(i)[element + 1], 1)
        print("Success!")
        score += 10
    except:
        print("An exception occurred while testing " + i)

print("Testing tournament function...")

for i in fileList:
    try:
        print("Running a tournament with all participants in file " + i)
        pyfile.tournament(pyfile.import_data(i))
        print("Success!")
        score += 10
    except:
        print("An exception occurred while testing file " + i)
    
print("Final Score: " + str(score) + "/220 points")
print("Final Percent: " + str((score/220)*100) + "%")
