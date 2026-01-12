#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: HW15
import random
#1. import the "random" library

#2. print "Hello World!"
print("hello world!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Enter first number: "))
b = int(input("Enter  second number: "))
c = int(input("Enter third number: "))
#4. Add a and b together, then divide the sum by c. Print the result.
d = a + b
e = d/c
print(e)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
e=round(e)
if e % 2 == 0:
    print("Even")
else:
    print("Odd")
#6. Create a list of five different random integers between 1 and 10.
randomlist = [
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10),]
#7. Print the 4th number in the list.
print(randomlist[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
randomlist.append(random.randint(1, 10))
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
randomlist.sort()
print(randomlist[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i <= 101:
    print(i)
    i = i+i
#11. Create a list containing the names of five other students in the classroom.
namelist = [
    "Dylan",
    "Sam",
    "Aidan",
    "Jude",
    "Brenlen",
]
#12. Create a for loop that individually prints out the names of each student in the list.
for l in namelist:
    print(l)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for j in range(1,101):
    if j % 10 == 0:
        break
    else:
        print(j)
#14. Free space. Do something creative. :)
player = input("Rock, Paper, Scissor?")
Rps = [
    "Rock",
    "Paper",
    "Scissor",
]
print(f"I chose {(random.choice(Rps))} You chose {(player)}")