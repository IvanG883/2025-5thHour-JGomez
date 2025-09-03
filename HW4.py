#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: HW4


#1. Print Hello World!
print("hello world")
#1. Create a list with 5 strings containing 5 different names in it.
Namelist = ["Bob","Joe","Jack", "john", "billy"]

#2. Append a new name onto the Name List.
Namelist.append("jeff")
print(Namelist)
#3. Print out the 4th name on the list.
print(Namelist[3])
#4. Create a list with 4 different integers in it.
Numberlist = ["1","2","3", "4"]

#5. Insert a new integer into the 2nd spot and print the new list.
Numberlist.insert(3,"7")
#6. Sort the list from lowest to highest and print the sorted list.
Numberlist.sort()
print(Numberlist)
#7. Add the 1st three numbers on the sorted list together and print the sum.
Numberlist_subsum = Numberlist[0] + Numberlist[1] + Numberlist[2]
print(Numberlist_subsum)
#8. Create a list with two strings, two variables, and too boolean values.
mixlist = [ "bob", "joe", 1, 2, True, False]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(mixlist[int(input("enter Index value"))])