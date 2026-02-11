#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: HW19
import random
#1. Import the def functions created in problem 1-4 from HW16
from HW16 import hello_world,average,animal_list,loop
hello_world()
average(2,3,4)
animal_list("frog",
    "dog",
    "cat",
    "bird",
    "rabbit",
    )
loop(69)

#2. Call the functions here and run HW19

#3. Delete all calls from HW15 and run HW19 again.

#4. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("Hello world!")
#5. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    num_div = int(input("Give me an integer: "))
    print(100/num_div)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Value Error. Needs to be an integer!")
except:
    print("Unknown error.")
#6. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.

#7. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.

j = 5
while j >= 0:
    print(j)
    j -= 1
raise Exception("Stops at Zero!")

