#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: HW_R8
import random

#1. Import all of HW_R7 into this assignment using the from/import function.
from HWR7 import *


#2. Create an object of three students in the classroom. Ask for their name, grade, and favorite color as need be.
Dylan = info("dylan", 12, "red")
Sam = info("sam", 10, "prettiest of pinks")
Aiden = info("aiden", 10, "Green")
#3. Print the name of the first student.
print(Dylan.name)
#4. Use the def function from HW_R7 to bump the grade level of the second student up by 1. Print the new grade.
info.add_grade_attribute(Sam)
print(Sam.grade)
#5. Use the def function from HW_R7 to ask the third student to change their favorite color to something else.
#Print the new color.
info.add_color_attribute(Aiden)
print(Aiden.color)