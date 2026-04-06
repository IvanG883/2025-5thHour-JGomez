#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: HW-R5

#1. Create a list of the names of all the students in the classroom.
namelist = ["Dylan", "Bryson", "Aiden", "Ivan", "Ashton", "Hogan", "Brennlyn", "Sam"]
#2. Create a for loop that prints the names of every student in the list.
for n in namelist:
    print(n)
#3. Using the "in" operator (hint: Google), create a for loop that only prints
#the name of a student if the letter "e" is in it.

for name in namelist:
    if "e" in name.lower():
        print(name)