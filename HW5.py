#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.
Numlist = [1,2,3,4,5,6,7,8,9]
#2. Sort the list from highest to lowest.
Numlist.sort(reverse = True)
#3. Create an empty list.
Emptylist = []
#4. Remove the median number from the first list and add it to the second list.
Emptylist.append(Numlist[4])
Numlist.pop(4)
#5. Remove the first number from the first list and add it to the second list.
Emptylist.append(Numlist.pop(0))
Numlist.pop(0)
#6. Print both lists.
print(Numlist)
print(Emptylist)
#7. Add the two numbers in the second list together and print the result.
Emptylist= [Emptylist[0] + Emptylist[1]]
print(Emptylist)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).

Numlist.append(Emptylist[0])
Emptylist.pop(0)
#9. Sort the first list from lowest to highest and print it.
Numlist.sort()
print(Numlist)