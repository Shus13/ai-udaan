# Question section 1
# 1
print("Welcome to DPLMS Student Registration System")

# 2
courses_list = ["Python with AI/ML", "JavaScript", "Flutter", "MERN Stack"]

# 3
for course in courses_list:
    print(course)

# 4
name = input("Enter your name : ")
email = input("Enter your email : ")
age = input("Enter your age : ")
course = input("Enter the selected course : ")

# 5
student_information = {
    "Name" : name,
    "Email" : email,
    "Age" : age,
    "Course" : course
}

# 6 & 7
if student_information["Course"] in courses_list:
    registration_status = ("Registered")
    print("Registration Successful!")
else:
    registration_status = ("Not Registered")
    print("Course not available")

# 8
print("Student Details : ")
print("Student Name : ", student_information["Name"])
print("Student Email : ", student_information["Email"])
print("Student Age : ", student_information["Age"])
print("Student Course : ", student_information["Course"])
print("Student Status : ", registration_status)


# Question section 2
# 1. 
# While loop is a type of control flow statement(loop) which is use to repeat the execution of code unless the specified condition gets false. 

# Yesko syntax 

#  while  condition(jun chai true hun jel code execute vairakhxa):
#       code here

# Example:

i = 1
while i <= 3:
    print("Count : ", i)
    i += 1
print("While loop is finished")

# Difference between for loop and while loop are :

# -> For loop is mostly used when we know the exact number of repetation/iteration and while loop is used when we are unaware of iteration to be performed

# -> In for loop, initialization, condition and updation terms are written together in one statement and In while loops, we first initialize and then loop(in loop part we write update code)

# -> For loop is more suitable for counter-based controlled loops and while loop is suitable for condition-based controlled loops

# -> While loop is more flexible

# Real life example of while loops are
# -> OTP Entry : We can enter multiple wrong OTP pin unless we provide the correct code and then loops stop

# -> Downloading a movie : Download bar keeps increasing the download percent unless it reaches 100% and completion time also is unknown so while loop is suitable

#  -> Water Tank Censor : Water keeps filling in water tank unless it become full and when it's reaches the threshold point, motor stops running or siren keeps ringing.


# Question section 3
# Function in python is a reusable block of code that performs a specific task. Rather then writing same code multiple times, we can define it once and we can call it whenever we need.

# Functions are useful for reducing the duplicate code by resuing it which simplify the code while debugging and improves the code organization. Also saves time and effort while developing in large scale.

# Difference between built-in and user-defined functions are
# -> built-in functiona are pre-defined function by python while user defined functions are function created by the coder from scratch
# -> we don't need to define the built-in function before using while we must define user-defined function usinf def keyword
# -> built-in function core behaviour can't be change by the user while user-defined functions are fully customizable

# def keyword: def keyword is use to define/create a function in python which is a short term for define. This is used at the beginning of a line to create a user-defined function. example: def sum_func():

# Parameter: Parameters are the variable inside the function parenthesis() when that function is defining. They simply receive the values when function is called. example: def sum_func(num1, num2): here num1, num2 are the parameter

# Arguments: Arguments are the real values we passed into the function when it is called. example: sum_func(2,4), here 2 and 4 are the arguments we pass.

# return values: The final output/result that the function sends back to the caller. We use "return" keyword to sends output once it's execution is completed

# Five built-in Python functions are:
# 1. print(): It simply output the variable, string pr any data directly on the screen. example: print("Hello World"), is display Hello World on screen

# 2. input(): It is use to takes input from the user. example: name = input("Enter your name"), here on screen it shows Enter your name and then we need to enter to further proceed it.

# 3. type(): This is used to return the data type of a variable. example: print(type(13)), it will give output int

# 4. pow(): It is a buit-in function which is use to calculate the exponent simple power calculation. It's syntax is pow(x,y), x raised to the power of y, example: pow(2,3), This will give result 2 to power 3; which will be 8

# 5. map(): This function is used to apply specified function to every item inside an iterable ojects(like list, set, tuple) and return a map object. It's syntax is map(function, iterable onject). example: 

numbers= [1,2,3,4]
result = map(lambda x:x+2, numbers) #lambda is a nameless function in python and we don't need to use def to define it.
print(list(result))
