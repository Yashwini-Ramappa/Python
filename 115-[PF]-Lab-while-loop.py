#Working with Loops
#Lab overview
#A loop is a segment of code that repeats. You will be introduced to two types of loops: the while loop and the for loop.
#In this lab, you will:

#Use a while loop
#Use a for loop

#Exercise 1: Working with a while loop

#A while loop makes a section of code repeat until a certain condition is met. In this exercise, you will create a Python script that asks the user to correctly guess a number.
#Printing the game rules
#From the navigation pane of the IDE, choose the .py file that you created in the previous Creating your Python exercise file section.
#Use the print() function to inform the user about your game:
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
#Save and run the file.
#Confirm that the script runs correctly and that the output displays as you expect it to.

#Importing random and writing a while loop
#You will use the import command to include code that someone else wrote. Up to now, you have been using built-in functions. Recall that a function is a piece of reusable code.
#At the top of the file, include the Python module (which is a type of library) called random.
#Note: By convention, import statements are placed at the top of the script.
import random

#Place the cursor on the next line after the second print() statement. Next, enter a statement that will generate a random number between 1 and 10 by using the randint() function of the random module.
number = random.randint(1,10)

#Track whether the user guessed your number by creating a variable called isGuessRight:
isGuessRight = False

#To handle the game logic, create a while loop:
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

#Note: The while loop will repeat the code inside the loop until the number is guessed correctly, which is represented by the condition isGuessRight != True in the code. Additionally, Python uses indentation to determine logic blocks, or what statements are considered to be part of the while loop. You can indent a line by placing the cursor next to a statement and pressing TAB.

#Writing pseudocode
#Before you run the Python script, write out the logic of the while loop in written (non-code) sentences. This technique is called pseudocoding.
#For example:
#If the user has not guessed the correct answer, enter the loop.
#Ask the user for a guess.
#Is the guess the correct number?
#If the correct guess, tell the user it was the correct guess and exit the loop.
#If the wrong guess, tell the user it was the wrong guess and continue the loop.

#Running the script
#Now run the Python script and see if it works.
#Run the file.
#Confirm that the script runs correctly and that the output displays as you expect it to.

