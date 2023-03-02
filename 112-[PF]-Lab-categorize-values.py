#Categorizing Values
#Lab overview
#With Python, you can mix types in a list. In this lab, you will create a list with different types and print the values.

#In this lab, you will:

#1) Use numeric data types
#2) Use string data types
#3) Use the list data type
#4) Use a for loop
#5) Use the print() function

#Exercise 1: Creating a mixed-type list
#You can mix data types in a Python list. In other languages, this capability is not a feature of lists. In this exercise, you will explore this capability.
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"] #Define a list with different types

#Use a for loop statement to traverse the list and print the data type for each item in the list:
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
    #This exercise reinforced the Python programming concepts that were covered in labs 1–6. Although the code has only a few lines, it is powerful. Take some time to review the code and make sure you understand everything that happens in it.
#Congratulations to me! I worked with the list data type and learned about Python support for mixing data types in a list declaration.

