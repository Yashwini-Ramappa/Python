myString = "This is a string."
print(myString)
print(type(myString)) #this is a string data type
print(myString + " is of the data type " + str(type(myString)))

#working with string concatenation 

firstString = "water" #this is a string data type
secondString = "fall" #this is a string data type
thirdString = firstString + secondString
print(thirdString)

#working with input strings
name = input("What is your name? ") #input()= user can give any name or identity here
print(name) 

#formatting output strings
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))