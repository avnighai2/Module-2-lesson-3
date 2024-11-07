#take an input from a user, then start from 1 and go till the number inputed user do the sum and print it 

userinput = int(input("Enter the number:"))
totalsum = 0 

for i in range(1, userinput+1):
    totalsum += i 
print("the sum of the given user input ", userinput, "is:", totalsum)