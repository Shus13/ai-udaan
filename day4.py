# Conditional statement

# condition : scenario/environment/rules
# statement : blocks of code

# If it's cloudy then carry umbrella 
#     Condition         Statement

age = 19
if age > 18:
    print("You are elligible")

marks = 80
if marks >= 90:
    print("You got A")

elif marks >=80 and marks <= 90:
    print("You got B")

elif marks >=60  and marks <=80:
    print("You got C")

elif marks >=40  and marks <= 60:
    print("You got D")

else:
    print("You failed")

# Loops : repeat the block of code multipl times

# for loops : use when we know when to stop

fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

# range(start, stop, steps)
for count in range(10,0,-2):
    print(count)


# While loops : yo loops ley code lai infinite times repeat garna sakxa, jaba samma specified condition true hudaina taba samma code repeat vairakxa

count = 3
while count > 0:
    print("Count : ", count)
    count -= 1
print("Count sakkiyo")