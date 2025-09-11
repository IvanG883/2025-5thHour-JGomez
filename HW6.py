#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: HW6


#1. Import the "random" library
import random

#2. print "Hello World!"
print("hellow world")
#3. Create three different variables that each randomly generate an integer between 1 and 10
d10 = random.randint(1,10)
d11 = random.randint(1,10)
d12 = random.randint(1,10)

#4. Print the three variables from #3 on the same line.
print(d10,d11,d12)

#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
d10 += 2
d11 -= 4
d12 *= 1.5

#6. Print each result from #5 on the same line.
print(d10,d11,d12)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
randomlist = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]

#8. Sort the list in #7 and print it.
randomlist.sort()
print(randomlist)
#9. Add together the highest three numbers in the list from #7 and print the result.
randomlist_sum = randomlist[0] + randomlist[1] + randomlist[2]
print(randomlist_sum)
#10. Create a list with 5 names of other students in this class and print the list.
Namelist = ["jack", "john", "jill", "roberto", "andrea", "ivan"]
print(Namelist)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(Namelist)
print(Namelist)
#12. Print a random choice from the list of names from #10.
Namelist = random.choice(Namelist)
print(Namelist)