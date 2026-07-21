# Function is a block of code, which can be defined once and call multiple times

def greet(name):
    print("Hello " + name)

greet("Sushit")

# Parameter are the var inside function parenthiesis while defining
# Argument is the real value we give while calling that function
# Function can be built-in or custom, built-in function like print(), len() and so on
# Return keyword is used for reuturning the final output from function to caller

def sum(num1, num2):
    return num1 + num2

print(sum(2,4))

def sq_num(num):
    return num*num

result1 = sq_num(2)
print(result1)

# lambda is used for one line function execution
result2 = lambda num:num*num
print(result2(3))