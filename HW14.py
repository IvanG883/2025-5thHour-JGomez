#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: HW14
import time

#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end. for b in range(10,0,-1):
for i in range(5,0,-1):
    time.sleep(0.7)
    print(i)
else:
    print("Hello world")

#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for j in range(0,30,2):
    print(j)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for k in range(0,31,2):
    if k % 3 == 0:
        continue
    else:
        print(k)
#4. Create a for loop that prints 5 different animals from a list.
animals = ['cat', 'dog', 'rabbit', 'rat','bat']
for a in animals:
    print(a)

#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
revers_string = ""
for x in input("Enter a word"):
    revers_string = x + revers_string
print(revers_string)
#6. Create a list containing 10 integers of your choice and print the list.
numlist = [1,2,3,4,5,6,7,8,9,10]
print(numlist)
#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = 0
oddNumbers = 0

#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
for num in numlist:
    if num % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1
    print(evenNumbers, oddNumbers)
#9. Create a variable that asks the user for an integer and an empty integer variable.
numinput = int(input("Enter a number: "))
factorial = 1
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
for h in range(1,numinput+1):
    factorial *= h
print(f"the factorial of, {numinput}, is, {factorial} ")