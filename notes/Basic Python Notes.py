"""
print("Hello World!")

# Apparently I'm going to slow, so I will speed up
# This is a comment
# This has no effect on the code
# This is used for a variety of things, such as
# 1. Making personal notes about my code
# 2. Commenting out code that does not work

print("Notice what is happening here.")
print()  # This creates a new line
print()  # Do you notice the underline here?
# Hover over top it to see what is wrong.

# Math
print(5 + 3)
print(5 - 3)
print(4 * 5)
print(6 / 5)

# Semi-advanced math
print("Figure this out...")
print(6 // 4)
print(12 // 3)
print(9 // 4)  # This will only give me a whole number
print()

print("Figure this out too...")
print(6 % 4)
print(5 % 3)
print(9 % 4)

# Defining Variables
car_name = "Wiebe Mobile"  # String
car_type = "Tesla"  # String
car_cylinders = 16  # Integer
car_mile_per_gallon = 0.01  # Float

print("I have a car called %s. I's pretty nice" % car_name)
print("It has %d cylinder, but gets %f mpg" % (car_cylinders, car_mile_per_gallon))

# Taking Input
name = input("What is your name?")
print("Hello %s" % name)

age = input("How old are you?")
print("%s? You belong in a museum!" % age)

# Recasting
real_age = int(input("How old are you again?"))
hidden_age = real_age + 5
print(hidden_age)
"""

# Multi-line comments

"""
This ia a multi-line comment
anything in between them is automatically commented out.
"""


# Defining Functions
def say_it():
    print("Hello World!")


say_it()
say_it()
say_it()


# f(x) = 2x + 3
def f(x):
    print(2*x + 3)


f(1)
f(5)
f(5000)


def distance(x1, y1, x2, y2):
    dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12)

# For loops
for i in (1, 2, 3):
    say_it()

for i in range(5):  # Range(5) gives the number 0-4
    f(i)

for i in range(5):
    print(i**2)

# While loops
a = 0
while a < 10:
    print(a)
    a += 1  # This is the same as a = a + 1


"""
Hints for loops:
For loops - Use when you know EXACTLY how many iterations
While - Use when you DON'T know how many iterations
"""

# Control Statements (If Statements)
sunny = False
if sunny:
    print("Go outside")


def grade_calc(precentage):
    if precentage >= 90:
        return "A"
    elif precentage >= 80:
        return "B"
    elif precentage >= 70:
        return "C"
    elif precentage >= 60:
        return "D"
    else:
        return "F"


your_grade = grade_calc(82)
print(your_grade)

# Random numbers
import random  # This should be on line 1
print(random.randint(0, 100))

# Equality Statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)
print(3 != 4)  # is not equal to
"""
a = 3 # a is set to 3
a == 3 # Is a equal to 3?
"""

# Creating a list
fruit = ['apples', 'oranges', 'blackberries', 'strawberries', 'blueberries', 'raspberries', 'pineapple',
         'mango', 'coconut']
print(fruit)


# Pulling items from a list
print(fruit[1])

# Getting from the length of a list
print(len(fruit))
print("The length of the list is %d" % len(fruit))

# Modify Lists
fruit[8] = 'Banana'
print(fruit)

# Looping through lists
for item in fruit:
    print(item)

words = ['computer', 'mouse', 'apples', 'battery', 'touchscreen', 'files']
words[2] = 'keyboard'
print(words[2])
print(words)
print("The last thing in the list is %s" % words[len(words)-1])
