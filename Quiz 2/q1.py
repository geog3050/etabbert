mystr = input("Enter a string: ")
findLetter = input("Enter a letter to find out if it is in the string: ")

containStatus = ""
i = 0

if len(findLetter) == 1:
    while i < len(mystr) and containStatus != "Yes":
        if mystr[i] == findLetter:
            containStatus = "Yes"
        else:
            containStatus = "No"
        i += 1
else:
    print("Please enter only one letter")

print(containStatus)
