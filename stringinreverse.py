# take an string input from a user than reverse it using loops

string = input("Enter a string:")
reversedstring = ""

for i in range(len(string)-1, -1, -1 ):
    reversedstring += string[i]

print("reversed string:", reversedstring)

countofo = 0
for i in range(len(string)):
    if  string[i] == "o":
        countofo += 1

print("the count of o in the given phrase is:", countofo)

findt = 0
countoft = "No"
for i in range(len(string)):
    if string[i] == "o":
        countoft = "Yes"

print(countoft, "the letter o is excisting in the given string")

