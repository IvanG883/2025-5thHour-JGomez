#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: HW12
import random
#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i = 5
while not i == -1:
    print (i)
    i = i - 1
print("hello world")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
J = 0
while J < 30:
    if J % 2 == 0:
        print (J)
        J += 1

    else: J += 1

#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
K = 0
while K < 30:
    if K % 3 == 0:
        K += 1
        continue
    else:
        print (K)
        K += 1
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
L = random.randint(1,6)
while True:
    print (L)
    if L ==1:
        break
    else:
        L = random.randint(1, 6)

#5. Create a while loop that asks for a number input until the user inputs the number 0.
M = int(input("input a number 0"))
while M != 0:
    M = int(input("input a number 0"))