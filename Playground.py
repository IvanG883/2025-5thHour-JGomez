import random

print("number guessing game")
number = (random.randint(1,50))
random = (int(input("your number")))
print (random)
print (number)

if random > number:
    print ("you win")
else:
    print ("you lose")

