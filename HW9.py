#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: HW9

import random
#1. Print "Hello World!"
print("hello world")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
Numberlist = (random.randint(1,100),random.randint(1,100),random.randint(1,100))
#3. Print the list.
print(Numberlist)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if Numberlist[0] > Numberlist[1] and Numberlist[0] > Numberlist[2]:
    print(Numberlist[0], "is the largest number")
    num = Numberlist[0]
elif Numberlist[1] > Numberlist[0] and Numberlist[1] > Numberlist[2]:
    print(Numberlist[1], "is the largest number")
    num = Numberlist[1]
else:
    print(Numberlist[2], "is the largest number")
    num = Numberlist[2]

#5. Tie the result (the largest number) from #4 to a variable called "num".
print(num)
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print(f"{num} is divisible by both 2 and 3")
    else:
     print(f"{num} is divisible by 2 but not 3")
else:
    if num % 3 == 0:
        print(f"{num} is divisible by 3 but not 2")
    else:
        print(f"{num} is not divisible by 2 or 3")