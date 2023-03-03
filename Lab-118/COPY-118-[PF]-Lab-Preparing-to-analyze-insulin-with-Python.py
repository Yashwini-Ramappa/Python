#Python code that can delete the "ORIGIN", "1", "61", "//", and the spaces from the given input:

import re

input_file = "preproinsulin-seq.txt"
output_file = "preproinsulin-seq-clean.txt"

with open(input_file, "r") as f:
    text = f.read()

print(text)

count_letters = 0
for i in text:
    count_letters += 1

print (count_letters, "\n")

# Remove all characters, except small letters; 
text = re.sub(r'[^a-z]', '', text)

print(text, "\n")

count_letters = 0
for i in text:
    count_letters += 1

print (count_letters)

with open(output_file, "w") as f:
    f.write(text)

#OUTPUT in preproinsulin-seq-clean.txt file will change to (malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicsslyqlenycn)
#Note that this assumes the input is a single string with newlines represented by "\n". If the input is in a different format, the code may need to be modified accordingly.

#Explanation: This is a Python code that manipulates a string called input_str that contains a DNA sequence with some additional characters.
#The first line defines the input_str variable and initializes it with the DNA sequence and some additional characters. The additional characters include a line with the number "1" and the string "malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed", a line with the number "61" and the string "lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn", and the "//" string at the end.
#The second line removes the "ORIGIN" string from the input_str using the replace method. If the "ORIGIN" string is not present in the input string, this line has no effect.
#The third line removes the numbers "1" and "61" from the input_str by calling the replace method twice, first to remove "1" and then to remove "61". This line removes the position numbers from the DNA sequence.
#The fourth line removes the "//" string from the input_str.
#The fifth line removes all the spaces from the input_str by calling the replace method with a space character as the first argument and an empty string as the second argument.
#The last line prints the final input_str string with all the modifications made.
#Overall, this code removes unwanted characters from the DNA sequence represented by input_str, such as the position numbers and additional symbols, and returns a string with only the DNA sequence itself.


#--------------------------------------------alternate command-----------------------------------
# import required module
#import os
# assign directory
#path_of_the_directory = '/Users/fischee/Working/java example/python/restart-first-repo'
 
# iterate over files in
# that directory
#for filename in os.listdir(path_of_the_directory):
    #file = os.path.join(path_of_the_directory,filename)
    #if os.path.isfile(file):
        #with open(file) as f:
            #lines = f.readlines()
            #data = ''.join(lines)
            #print('')
            #print('File Name =',f.name)
            #print('lines =',len(lines))
            #print('Words = ',len(data.split()))
            #data = ''.join(data.split())
            #print('characters = ',len(data))
            #print('')
                #read the content of file
        #data = f.read()

        #get the length of the data
        #number_of_characters = len(data)

        #print('Number of characters in text file :', number_of_characters)
        #print(f)