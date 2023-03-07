#Variables: Variables are used to store data in Python. A variable is created by assigning a value to a name. For example:
x = 10
#In this example, the variable x is assigned the value of 10.


#Data Types: Python supports various data types such as integers, floats, strings, lists, tuples, dictionaries, and more.


#Operators: Operators are used to perform operations on data. Python supports various operators such as arithmetic, comparison, logical, bitwise, and more.


#Control Flow: Control flow statements are used to control the order of execution of code. Python supports various control flow statements such as if-else, for loops, while loops, and more.


#Functions: Functions are used to perform a specific task. In Python, a function is defined using the def keyword. 
# For example: 
def my_function():
    print("Hello, World!")
#my_function(): print("Hello, World!") 
#This function will print "Hello, World!" when called.


#Input/Output: Input/output functions are used to read input from the user and write output to the console or file. Python supports various input/output functions such as input(), print(), open(), read(), and more

#Modules: Python has a vast number of built-in modules that provide additional functionality. To use a module, you need to import it using the import statement.
#For example:
import math
#This statement imports the math module, which provides mathematical functions.


#Commands------------------------------------------------------------------------------------------------------------------------

#1) Print a message:
print("Hello, world!")

#2) Assign a value to a variable:
x = 5

#3) Perform arithmetic operations:
y = x + 3
z = x * y

#4) Get user input:
name = input("What is your name? ")

#5) Control flow with if-else statements:
if x > 0:
    print("x is positive")
else:
    print("x is zero or negative")

#6) Create a function:
def add_numbers(a, b):
    return a + b

#7) Create a list:
my_list = [1, 2, 3, 4, 5]

#8) Access an element in a list:
print(my_list[0])  # prints 1

#9) Loop through a list:
for item in my_list:
    print(item)

#10) Create a dictionary:
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

#11) Access a value in a dictionary:
print(my_dict["name"])  # prints "Alice"

#12) Loop through a dictionary:
for key, value in my_dict.items():
    print(key, value)

#13) Check the length of a string:
my_string = "Hello, world!"
print(len(my_string))  # prints 13

#14) Check if a string contains a substring:
if "world" in my_string:
    print("found world")

#15) Replace a substring in a string:
new_string = my_string.replace("world", "Python")
print(new_string)  # prints "Hello, Python!"

#16) Convert a string to uppercase or lowercase:
print(my_string.upper())
print(my_string.lower())

#17) Split a string into a list:
words = my_string.split(",")
print(words)  # prints ["Hello", " world!"]

#18) Join a list of strings into a single string:
new_string = "-".join(words)
print(new_string)  # prints "Hello- world!"

#19) Check the type of a variable:
print(type(x))  # prints <class 'int'>
print(type(my_list))  # prints <class 'list'>

#20) Check if a variable is of a certain type:
if isinstance(x, int):
    print("x is an integer")

#21) Convert a string to a number:
my_number = int("5")

print("Hello, World!")  #print a message to the console

input("Enter your name: ") #- prompt the user to enter their name

len("hello") #- get the length of a string

type(42) # get the data type of a value

str(42) # convert a value to a string

int("42") #- convert a string to an integer

float(3) #- convert an integer to a float

bool(0) #- convert an integer to a boolean

list(range(5)) #- create a list of numbers from 0 to 4

range(5) #- create a range of numbers from 0 to 4

tuple((1, 2, 3)) #- create a tuple with values 1, 2, and 3

set([1, 2, 3]) #- create a set with values 1, 2, and 3

dict(name="John", age=30) #- create a dictionary with keys "name" and "age" and values "John" and 30

sum([1, 2, 3]) #- get the sum of a list of numbers

max([1, 2, 3]) #- get the maximum value in a list of numbers

min([1, 2, 3]) #- get the minimum value in a list of numbers

sorted([3, 2, 1]) #- sort a list of numbers in ascending order

reversed([3, 2, 1]) #- reverse a list of numbers

zip([1, 2, 3], [4, 5, 6]) #- combine two lists into a list of tuples

enumerate(["apple", "banana", "cherry"]) #- iterate over a list with an index

all([True, False, True]) #- check if all values in a list are True

any([True, False, True]) #- check if any value in a list is True

filter(lambda x: x % 2 == 0, [1, 2, 3, 4]) #- filter a list based on a condition

map(lambda x: x * 2, [1, 2, 3, 4]) #- apply a function to each value in a list

reduce(lambda x, y: x + y, [1, 2, 3, 4]) #- reduce a list to a single value using a function

abs(-5) #- get the absolute value of a number

pow(2, 3) #- raise a number to a power

round(3.14159, 2) #- round a number to a certain number of decimal places

chr(65) #- convert an integer to its corresponding ASCII character

ord("A") #- convert a character to its corresponding ASCII integer

hex(255) #- convert an integer to its corresponding hexadecimal value

bin(8) #- convert an integer to its corresponding binary value

oct(8) #- convert an integer to its corresponding octal value

isinstance(5, int) #- check if a value is an instance of a certain class

issubclass(bool, int) #- check if a class is a subclass of another class

dir(list) #- get a list of all methods and attributes of a class

help(list) #- get help information about a class or function

assert 2 + 2 == 4 #- assert that a condition is true, otherwise raise an error

`try:
some code 
except:
# handle exception
finally:
# code that runs regardless of whether there was an exception or not` - handle exceptions in code and execute code regardless of whether there was an exception or not

with open("file.txt", "r") as f: content = f.read() #- open a file and read its contents, automatically closing the file when finished

with open("file.txt", "w") as f: f.write("Hello, World!") #- open a file and write to it, automatically closing the file when finished

os.getcwd() #- get the current working directory

os.listdir() #- get a list of all files and directories in a directory

os.mkdir("new_dir") #- create a new directory

os.rmdir("new_dir") #- remove a directory

os.remove("file.txt") #- remove a file

os.path.exists("file.txt") #- check if a file or directory exists

os.path.basename("/path/to/file.txt") #- get the filename from a path

os.path.dirname("/path/to/file.txt") #- get the directory from a path

os.path.splitext("file.txt") #- split a filename and its extension into a tuple

time.sleep(1) #- pause execution for a specified number of seconds

datetime.datetime.now() #- get the current date and time

datetime.datetime(2022, 3, 7) #- create a datetime object with a specific date and time

datetime.datetime.strptime("2022-03-07", "%Y-%m-%d") #- convert a string to a datetime object using a specified format

datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #- format a datetime object as a string using a specified format

random.randint(1, 10) #- generate a random integer between 1 and 10

random.choice(["apple", "banana", "cherry"]) #- choose a random item from a list

random.shuffle(["apple", "banana", "cherry"]) #- shuffle the items in a list randomly

math.sqrt(25) #- get the square root of a number

math.pi #- get the value of pi

math.sin(0) #- get the sine of an angle in radians

math.cos(0) #- get the cosine of an angle in radians

math.tan(0) #- get the tangent of an angle in radians

math.degrees(math.pi) #- convert radians to degrees

math.radians(180) #- convert degrees to radians

requests.get("https://www.google.com/") #- send a GET request to a URL and receive the response

requests.post("https://www.google.com/", data={"key": "value"}) #- send a POST

re.search("pattern", "string") #- search for a pattern in a string using regular expressions

re.findall("pattern", "string") #- find all occurrences of a pattern in a string using regular expressions

re.sub("pattern", "replacement", "string") #- substitute a pattern with a replacement in a string using regular expressions

json.dumps({"key": "value"}) #- convert a Python object to a JSON string

json.loads('{"key": "value"}') #- convert a JSON string to a Python object

pickle.dump({"key": "value"}, open("file.pkl", "wb")) #- serialize a Python object to a file using pickle

pickle.load(open("file.pkl", "rb")) #- deserialize a Python object from a file using pickle

zip(["a", "b", "c"], [1, 2, 3]) #- create a list of tuples by combining corresponding elements from two or more lists

enumerate(["a", "b", "c"]) #- create a list of tuples where the first element is the index and the second element is the corresponding value from a list

sorted([3, 1, 2]) #- sort a list in ascending order

sorted([3, 1, 2], reverse=True) #- sort a list in descending order

max([3, 1, 2]) #- get the maximum value in a list

min([3, 1, 2]) #- get the minimum value in a list

sum([1, 2, 3]) #- get the sum of all elements in a list

len([1, 2, 3]) #- get the number of elements in a list

list("abc") #- create a list from a string, where each character is a separate element in the list

set([1, 2, 2, 3]) #- create a set from a list, where duplicate elements are removed

dict(a=1, b=2) #- create a dictionary with key-value pairs

list(range(1, 11)) #- create a list of numbers from a range

map(lambda x: x * 2, [1, 2, 3]) #- apply a function to each element of a list and return a new list with the results

filter(lambda x: x % 2 == 0, [1, 2, 3, 4]) #- apply a function to each element of a list and return a new list with only the elements that satisfy a condition

reduce(lambda x, y: x + y, [1, 2, 3]) #- apply a function to each element of a list and reduce the list to a single value by iteratively applying the function to pairs of elements

any([False, True, False]) #- check if any element in a list is true

all([True, True, False]) #- check if all elements in a list are true

zip(*[(1, 2, 3), (4, 5, 6)]) #- unzip a list of tuples into separate lists

lambda x, y: x + y #- define a lambda function that takes two arguments and returns their sum

def function_name(argument1, argument2): #- define a function that takes two arguments
    
class ClassName: #- define a class
    
class ClassName(BaseClass): #- define a class that inherits from a base class
    
    
    
if condition: #- execute code if a condition is true
    #For example:
    x = 5
if x > 0:
    print("x is positive")
#This will output: x is positive, since the condition x > 0 is true.


    
if condition: ... else: ... #- execute one block of code if a condition is true, and another block of code if the condition is false
#For example:
x = 5
if x > 0:
    print("x is positive")
else:
    print("x is non-positive")
#This will output: x is positive, since the condition x > 0 is true. If x had been -1, then the output would have been: x is non-positive, since the condition x > 0 is false.


    
for item in iterable: #- iterate over an iterable and execute code for each item
    
while condition: #- execute code repeatedly while a condition is true
