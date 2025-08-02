#  1) What are the types of Applications ?

# Desktop Applications : Installed on a personal computer or laptop (e.g., MS Word, Photoshop).
#Web Applications :Run in a web browser and don’t require installation (e.g., Gmail, Facebook).
# Mobile Applications : Designed for smartphones and tablets (e.g., WhatsApp, Instagram).
# Console Applications : Text-based programs that run in a command-line interface (e.g., command prompt tools).
# Embedded Applications : Software designed to run on specialized hardware like ATMs, washing machines, and smart TV.


#  2) what is programing ?

# Programming is the process of designing and writing instructions that a computer can understand and 
# execute to perform a specific task. These instructions are written in programming languages like Python, 
# C, or Java. It involves problem-solving, logic building, and implementing algorithms to create functional software.


#  3) What is Python?

# Python is a high-level, interpreted, and general-purpose programming language known for its simple syntax and readability.
# It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. 
# Python is widely used for web development, data analysis, artificial intelligence, machine learning, automation, and more. 
# large standard library and community support make it one of the most popular programming languages in the world.

#  4) Write a Python program to check if a number is positive, negative or zero.? 


# Take input from the user
num = float(input("Enter a number: "))

# Check the condition
if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")
 

# 5) Write a Python program to get the Factorial number of given numbers. 


# Take input from the user
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")


#  6) Write a Python program to get the Fibonacci series of given range.

# Take number of terms from user
n = int(input("Enter the number of terms: "))

# First two terms
a= 0
b= 1

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("Fibonacci sequence:")
    print(a)
else:
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# 7)  How memory is managed in Python? 

#  Private Heap Space :–
# All Python objects and data structures are stored in a private heap.
# This heap is managed internally by the Python Memory Manager.

# Memory Manager :–
# Allocates and deallocates memory for objects.
# Works with the garbage collector to free unused memory.

# Garbage Collection :–
# Python uses automatic garbage collection to remove objects that are no longer in use.
# It mainly uses reference counting (tracking how many references point to an object).
# If the count becomes zero, the memory is freed.
# Also uses a cyclic garbage collector to detect and clean up objects involved in reference cycles.

# Dynamic Typing :–
# Memory is allocated dynamically at runtime based on the object type and size.

# 8) What is the purpose continuing statement in python? 

for i in range(5):
    if i == 2:
        continue
    print(i)
# 9) Write python program that swap two number with temp variable and without temp variable. 
 
 # Swap with temp variable
x = int(input("Enter x number: "))
y = int(input("Enter y number: "))

temp = x
x = y
y = temp
print(f"After swapping (with temp):x={x} and y={y}")

# 10) Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user. 
  

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is odd.")