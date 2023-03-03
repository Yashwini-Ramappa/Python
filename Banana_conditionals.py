#Create a new file that is called conditionals.py
#Create a set of conditionals using "if", "elf", and "else" statements in python. 
#They should be created so that the below conditions is met:
#if there are 5 or more bananas print "i have a bunch of bananas". 
#if there are 1-4 bananas print "I have a small bunch of bananas".
#if there are no bananas print "I have no bananas".

#Assign print statements to your conditions using the above rules
#create a variable to hold the number of bananas
#run the code to observe the results.

# Creating a variable to hold the number of bananas

x = input("How many Bananas do you have?:")
Bananas = int(x)
if Bananas >= 5 :
    print("I have a bunch of Bananas")
elif Bananas >= 1 and Bananas <= 5:
    print("I have a small bunch of Bananas")
else:
     print("I have no bunch of Bananas")
num_bananas = 3


#run and check the output, give the answer to the output question and observe the final output.