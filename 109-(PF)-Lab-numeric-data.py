print("Python has three numeric types: int, float, and complex")

#this is for integer data-type (numericals only)
myValue=1 #myvalue define variable
print (myValue)
print(type(myValue)) #this command show the data type
print(str(myValue) + " is of the data type " + str(type(myValue))) #this is string

#this is for integer data-type (numericals only)
myValue=3.14 #myvalue define variable
print(myValue)
print(type(myValue)) #this command show the data type
print(str(myValue) + " is of the data type " + str(type(myValue))) #this is string

print(int(myValue)) #this command gives myvalue without decimal value i.e., does not show values after thr '.' i.e. it ishows 3
print(float(myValue)) #this command gives full myvalue i.e. 3.14

myValue=5j #it is a complex data type i.e. alphanumerical
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=True #it is a boolean (1= True and 0=False)
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=False #it is a boolean (1= True and 0=False)
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
