"""
module 7: Function
defining and calling function
parameters and arguments
REturn values
Default arguments
positional and keyward argument
parametized and unparametized fuction
variable scope (local and global)
Advanced function concepts
*args and **kwargs
Lambda functions
Writing doc-strings and documentation

"""
# Function definition
def message(): 
    print("I am a python developer,")
# message()  # function invocation or calling

def student_record(name, score):
    print(f"My name is {name} and my score is {score}")
# student_record("Samuel", 90) # Samuel abd score are the argument

# Return values
def addintion(y, x):
    return y + x
# print(addintion(10, 15))

# Default arguments
def calculator(val1=23, val2=10, val3=3):
    return f"Total value: {val1 + val2 + val3}"
# print(calculator())
# print(calculator(5, 2, 3))

# Positional argument
def student_record(name, score): #name and score are the parameters
    print(f"My name is {name} and my score is {score}")
# student_record(90, "Samuel") # Samuel and 90 are the argument


# Keyword argument
def item_price(name, price, quantity):
    print(f"the total price of {name} is {price * quantity}")
# item_price(quantity=2, price=1000, name="Rice")

def message(name): # function definition
    print(f"My name is {name}, I am a python developer")
# message(name=input("Eneter your name: "))

# Variable scope (Local)
def my_record():
    name = "James"
    gender = input("Enter your gender: ")
    
    return f"My name is {name}, I am a {gender}"
# print(my_record())

# Variable scope (Global)
number = [10, 23, 5, 60]
total = 0
def sum_price():
    global total
    for price in number:
        total+=price
    print(total)
# sum_price()

"""
Calcutator
"""

def addition():
    val1 = int(input("Enter val1: "))
    val2 = int(input("Enter val2: "))
    print(val1 + val2)

def subtraction():
    val1 = int(input("Enter val1: "))
    val2 = int(input("Enter val2: "))
    print(val1 - val2)

def multiplication():
    val1 = int(input("Enter val1: "))
    val2 = int(input("Enter val2: "))
    print(val1 * val2)

def Division():
    val1 = int(input("Enter val1: "))
    val2 = int(input("Enter val2: "))
    print(val1 / val2)

def landing_page():
    while True:
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. exit")
    
        user = input("Enter your choice: ")
        if user == "1":
            addition()
    
        elif user == "2":
            subtraction()
    
        elif user == "3":
            multiplication()
    
        elif user == "4":
            Division()
    
        elif user == "5":
            break
landing_page()