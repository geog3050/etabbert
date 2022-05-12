inputString = input("Please enter a list of integers: ")

inputList = []

#This first loop is necessary for the conversion of the input string to a list.
#Using a for loop over the input string includes punctuation.
#This is the best way I could think of to isolate the integers without using .strip()

placeHolder = ''

for i in inputString:
    if i != "," and i != "[" and i != "]":
        placeHolder += i
    elif placeHolder != '':
        inputList.append(int(placeHolder))
        placeHolder = ''
        
duplicateStatus = ""

newList = []

for i in inputList:
    if inputList.count(i) != 1:
        duplicateStatus = "The list provided contains duplicate values."
    elif duplicateStatus != "The list provided contains duplicate values.":
        duplicateStatus = "The list provided does not contain duplicate values."

    if i not in newList:
        newList.append(i)

print(duplicateStatus)

if duplicateStatus == "The list provided contains duplicate values.":
    print("Your new list without duplicates is: %s" %newList)
