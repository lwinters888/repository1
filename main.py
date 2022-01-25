# best practice is to put all import statements at the top
import math
import random

# this is a one line comment
# a comment is "code" that is ignored by Python
# we use comments to document our code

"""
this is a multi 
line comment
AKA a block comment
"""

print("hello world")

# VARIABLES
x = 5 # read this as "x is assigned 5" or "x stores 5"
# NOT "x equals 5"
# a variable stores a value
# a value hasa a data type
# a data type defines a range of values
# example: the int data type (short for integer) represents whole numbers
print(x)
print(type(x))
# let's say we want to reassign x a different value
x = 5.5
print(x)
print(type(x))
# example: the float data type (short for floating point number) represents
# numbers with fractional parts (AKA decimals)
x = "hello"
# example: the string data type represents a sequence of characters
print(x)
print(type(x))
x = "5"
print(x)
print(type(x))

# OPERATORS
# PEMDAS
# * is multiplication
print(4 * 5)
# / is floating point division (the normal division)
print(5 / 2)
# // is integer division (the whole number result of floating point division)
print(5 // 2)
# ** is exponentiation (power)
print(2 ** 5) # if multiple **, they evaluate right to left
# we can also use the pow() function from the math module
# need to import the math module to use it
# (aside: a .py file AKA a module AKA script)
print(math.pow(2, 5))

# GETTING USER INPUT
# print("Enter your favorite number: ")
# favorite_number = input()
# print("Your favorite number is:", favorite_number)
# print("Your favorite number doubled is:", favorite_number * 2, sep="*")
# print(type(favorite_number))
# print("hello" * 2, end = "~~~~~~~~~~~~~~") # sep and end are called keyword arguments
# print("here")
# # let's say, we really do want to double the favorite number
# # we need to convert favorite_number the string to an int (or float)
# # this is called type conversion and there are build in functions to do this
# favorite_number_int = int(favorite_number)
# print(favorite_number_int, type(favorite_number_int))
# print("Your favorite number doubled is", favorite_number_int * 2)

# FORMATTING 
# a few ways to do this
# 1. C style (old school)
print(math.pi)
# round math.pit to 2 decimal places
print("%.2f" %(math.pi))
# 2. Pythonic way (new school)
print("{:.2f}".format(math.pi))
# 3. use the built in round funtction
# round() actually rounds the number (and you could store it as such)
print(round(math.pi, 2))

# CONDITIONALS (aka if statements)
# if some condition (AKA boolean condition) is true:
#    then execute some code (AKA body)
x = 6
if x == 6: # note: == is the equality operator (= assignment operator)
    print ("x is 6")
    # this is the body
    # the body only executes when the value stored in x is equal to 6
    # i.e. the boolean condition evaluates to true
    # note standard indentation is 1 tab = 4 spaces

# we also have an else keyword
# which executes when the preceding if condition is false
if x==6:
    print("x is 6")
else:
    print("x is not 6")

x = 5
if x < 0:
    print("x is negative")
elif x > 0:
    print("x is positive")
else:
    print("x is 0")

# LOOPS
# use a loop to repeat statemetns
# we have for loops and while loops
# for structure
# for item in sequence:
#   body (statements we want to repeat)
# there are lots of sequences in python!
# lists are sequences!!
my_list = {1, 2, 3, 4, 5}
for item in my_list:
    print(item)

# strings are sequences!!
for character in "gonzaga":
    print(character)
print("here", character)

# we can generate our own sequences
# built in function range() generates a sequence
# range(9) # generates a squence [0,9]
for i in range(9):
    print(i, end=" ")
print()

# range(stop) : [0, stop)
# range(start, stop) : [start, stop)
# range(start, stop, step) : [start, stop) going up by step (increment)

for i in range(4,9):
    print(i, end=" ")
print()

for i in range(4, 9, 2):
    print(i, end=" ")
print()

# task 1: try print the previous output in reverse 8 6 4
for i in range(8, 3, -2):
    print(i, end=" ")
print()

# task 2: try printing the first 20 even numbers all on one  line
# separated by a comma and a space
# 2, 4, ..., 38, 40
for i in range(2, 40, 2):
    print(i, end=", ")
print(i + 2)

# while loop structure
# while some condition is true:
#   body
#   prograss towards your condition being false

k = 2
while k <= 38:
    print(k, end=", ")
    k += 2 # progress
print(k)

# ADVANCED LOOPS
# like if statements we can nest loops
# user the break keyword to get an early exit from a loop
# while True:
#     user_input = input("Enter a word (stop to exit): ")
#     if user_input == "stop":
#         break

# FUNCTIONS 
# a function is a named sequence of statements
# minimize redundant code
# write once, call multiple times
# helps with code organization

# help(print)
# examples of function calls: help(), print(), round(), int(), input(),...
# we can write our own
# functions take inputs
# functions produce outputs
# function structure
# def function_name(parameter list):
#   body

# body does not execute until the function is called

# example 1: no parameters (no arguments in call)
# no return value
def say_hello():
    print("hello")

say_hello() # function call
for _ in range(5):
    say_hello()

# example 2: one parameter and no return value
def say(message): # message is a parameter
    print(message) 

say("hi there") # "hi there" is the argument
say("gonzaga")
say("go zags!")
say(5)

# TASK: define/call a function that accepts the radius of a circle
# and prints out the area of that circle

def circle_area(radius):
    area = math.pi * radius ** 2
    print("area:", area)

circle_area(5.0)

# example 3: one parameter and one return value

def circle_area2(radius):
    area = math.pi * radius ** 2
    return area

result = circle_area2(5.0)
print("result:", result)

# example 4: one parameter and two return values!!

def circle_area_and_circumference(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference # tuple (immutable list)

results = circle_area_and_circumference(5.0)
print("results:", results)
print("results:", results[0], results[1]) # results is a tuple
result1, result2 = circle_area_and_circumference(5.0) # tuple unpacking
print(result1, result2)













