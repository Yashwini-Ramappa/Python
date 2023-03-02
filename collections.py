myFruitList = ["apple", "banana", "cherry"] #we are creating a list here 
print(myFruitList) #myfruitlist is a variable
print(type(myFruitList)) # it is a string data type but will be count as list

#Accessing a list by position
#In programming languages, the list position starts at zero (0). The brackets tell Python which position in the list you want. 
print(myFruitList[0]) #To access the apple string
print(myFruitList[1]) #To access the banana string
print(myFruitList[2]) #To access the cherry string

#Changing the values in a list
#The values of a list can be changed. In this activity, you will change cherry to orange.
#In Python, list position starts at zero (0), so you must use the numeral 2 to access the third position.
myFruitList[2] = "orange"
print(myFruitList)

#Exercise 2: Introducing the tuple data type
#Defining a tuple
#The tuple is like a list, but it can't be changed. A data type that can't be changed after it's created is said to be immutable. 
#To define a tuple, you use parentheses instead of brackets ([]).
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#Accessing a tuple by position
#Like a list, the items of a tuple can also be accessed by position:
print(myFinalAnswerTuple[0]) #To access the apple string
print(myFinalAnswerTuple[1]) #To access the banana string
print(myFinalAnswerTuple[2]) #To access the pineapple string

#Exercise 3: Introducing the dictionary data type
#Defining a dictionary
#A dictionary is a list with named positions (keys). Imagine that your list shows people’s favorite fruit.
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary) #Use the print() function to write the dictionary to the shell
print(type(myFavoriteFruitDictionary)) #Use the type() function to write the data type to the shell

#Accessing a dictionary by name
#In this activity, you will use the name of the individuals to get their favorite fruit, instead of numbers.
print(myFavoriteFruitDictionary["Akua"]) #To access Akua's favorite fruit
print(myFavoriteFruitDictionary["Saanvi"]) #To access Saanvi's favorite fruit
print(myFavoriteFruitDictionary["Paulo"]) #To access Paulo's favorite fruit