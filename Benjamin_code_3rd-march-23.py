# Enter first number: 2134
# Enter second number: 2134
# Enter the operation: +,-
# result: first number + second number

print("Enter first number: ", end="")
x_input = input()
x = int(x_input)


print("Enter second number: ", end="")
y_input = input()
y = int(y_input)


print("Enter operation: ", end="")
operation = input()

print("The operation is: ", operation)

# = ---> assign the right side to the left side
# == ---> check for equality
if operation == "+":
    result = x + y # All i write here, is totally ignored by python
elif operation == "-":
    result = x - y
else:
    print("Invalid operation")
    exit(-1)

print("The result: ", result)
