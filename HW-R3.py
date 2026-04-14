#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: HW-R3
import random

#1. import random and print "Hello World!"
print("Helllo world!")
#2. Create three variables that each randomly generate an integer between 1 and 10, print each number on the same line.
varible1 = random.randint(1, 10)
varible2 = random.randint(1, 10)
varible3 = random.randint(1, 10)
print(varible1, varible2, varible3)
#3. Create a list containing 5 strings listing 5 colors.
colorlist = ["red", "blue", "green", "yellow", "pink"]

#4. Use a function to randomly choose one of the 5 colors from the list and print the result.
print(random.choice(colorlist))
#5. Create an if statement that determines which of the three variables from #2 is the lowest.
if varible3 > varible1 < varible2:
    print("varible1 is the lowest")
elif varible3 > varible2 < varible1:
    print("varible2 is the lowest")
else:
    print("varible1 is the lowest")