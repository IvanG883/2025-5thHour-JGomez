#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: HW-R2


#1. Print "Hello World!"
print("Hello world!")
#2. Create an empty list.
emptylist = []

#3. Create a list that contains the names of everyone in the classroom.
classroomlist = ["Dylan", "Bryson", "Aiden", "Ivan", "Ashton", "Hogan", "Brennlyn", "Sam"]
#4. Print the list from #3, sort the list, then print the list again.
print(classroomlist)
classroomlist.sort()
print(classroomlist)
#5. Append 5 different integers into the empty list from #2 and print the list.
emptylist.append(5)
emptylist.append(7)
emptylist.append(6)
emptylist.append(2)
emptylist.append(9)
#6. Add together the middle three numbers in the list from #2 and print the result.
listsum = emptylist[1] + emptylist[2] + emptylist[3]
print(listsum)
#7. Remove the very first number in the list from #2. Print the new first number.
emptylist.pop(0)
print(emptylist[0])
#8. Create a dictionary with three keys with respective values: your name, your grade, and your favorite color.
infodict = {
    "Name": "Ivan ",
    "Grade": 12,
    "Favorite color": "purple"
}
#9. Using the update function, add a fourth key and value determining your favorite candy.
infodict.update({"favorite candy": "Jolly Rancher"})

#10. Print ONLY the values of the dictionary from #8.
print(infodict.values())