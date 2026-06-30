# print("hello world")

# variables and naming conventions

# pascal naming coventions
# Student_Final_Result = 80
# StudentFinalResult = 80

# Camel naming coventions
# student_Final_Result = 80
# studentFinalResult = 80

# Snake naming coventions
# student_final_result = 80
# studentfinalresult = 80

# correct naming convention
# student = 4
# score2 = 70

# incorrect naming convention
# 3score = 60
# students score = 40

# DAta Type(int, float, str, bool)
# a = 12
# b = "Apple"
# c = True
# d = 20.0

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# TYpe conversion or casting
# 1 = float(a)
# print(float(a))
# print(1)
# p = str(c)
# print(type(p))


# s = 4
# w = 5
# print(float(s + w))
# k = float(s)
# x = float(w)
# print(k + x)

# comments and code documentation
# Type of commets in python

# 1 single line commets
# print("banana")

# 2 Multi-line or triple line of comments
# def addition(a,b):
#     """This function is use to add two number and output the result"""
#     result = a+b
#     return result

# print(addition(12, 5))
# print(addition.__doc__)

# Arithemetics operators
# val1 = 10
# val2 = 3
# print("Add ", val1 + val2)
# print("Sub ", val1 - val2)
# print("Mult ", val1 * val2)
# print("Div ", val1 / val2)
# print("Floor_div ", val1 // val2)
# print("Mod ", val1 % val2)
# print("Exp ", val1 ** val2)


# Assignment operators(=,+=,-=)
# score = 60
# score += 10
# print(score)

# score -= 10
# print(score)

# 3. Comparison operator(==, >,<,>=,<=, !=)
val1 = 30
val2 = 20
# print(val1==val2)
# val3 = val1==val2
# print (val3)

# print(val1>val2)
# print(val1<val2)

# print(val1>=val2)
# print(val1<=val2)

# print(val2 != val1)

# 4. Logical operators(and, or, not)

val4 = 40
val5 = 25
# result = val4>=val5 and val1
# result = val4>=val5 or val1<=val2
# print(result)

# name = "john"
# if not "N" in name:
#     print("Not available") 

# else:
#     print("Available")

# 5. Membership operators(in,not in)
list_fruit = ['Apple', 'Banan', 'Orange', 'Pineapple']

# if "orange" in list_fruit:
#     print("present")

# else:
#     print("Absent")

# if "Cocoa" not in list_fruit:

#  else:
#     print("present")

# 6. Identify operator(is)
val4 = 40
val4 = 50

# print(val4.bit_length)
# print(val5.bit_length)
# print(val4 is val5)

# num1 = [1, 2, 3, 4]
# num2 = [1, 2, 3, 4]

# print (num1 is num2)

# print(num1.index)
# print(num2.index)

"""
Module 3: Strings and string manipulation
        Creating and accessing strings
        string indexing and slicing
        common string methods
        string formating(f-strings)
        string concatination
"""
# Creating and accessing strings
# message = "this is a python class"
# print(type(message))

# string indexing 
# print(message[0])
# print(message[10])
# print(message[-1])
# print(message[-15])
# print(len(message))

# slicing
# print(message[:])
# print(message[:4])
# print(message[15:])
# print(message[7:18])
# print(message[::2])
# print(message[::-1])

# common string methods
# print(message.capitalize())
# print(message.center(100))
# print(message.upper())
# print(message.count("s"))
# print(message.count(" "))
# print(message.endswith("s"))
# print(message.startswith("t"))
# print(message.__contains__(" "))
# print(message.__add__(" hello"))


# Assignment
# 10 string method
# simple calculator
# full_name = input("enter your full name:").capitalize
# print(full_name)


# string Formating
# student = "Samuel"
# score = "80"
# print(F"My name is {student} and my score is {score}")

# Formatting using percentage (%)
# result = "My name is %s and score is %s"%(student, score)
# print(result)

# formatting using .format()
# result = "My name is {} and score is {}".format(student, score)
# print(result)

# String concatination
# concatination using comma
# print("My name is", student, "and my score is",score)

# concatination plus
# print("My name is"+" "+student+" "+"and my score is"+" "+str(score))