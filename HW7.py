#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: HW7

#1. Print Hello World!
print ("hello world!")

#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
keydictonary = {
"name":"johny",
"year":[17,19,16],
"sports": True,
}
#3. Print the keys of the dictionary from #2.
print(keydictonary.keys())
#4. Print the values of the dictionary from #2
print(keydictonary.values())
#5. Print one of the three numbers from the list by itself
print(keydictonary["year"][1])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
keydictonary.update({"nickname": "john"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(keydictonary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
fifth_hour_class = {
    "student_1" : {
        "Name" : "dylan",
        "Grade" : 12,
        "Sports" : False
    },
    "student_2" : {
        "Name" : "sam",
        "Grade" : 10,
        "Sports" : False
    },
    "student_3" : {
        "Name" : "Diana",
        "Grade" : 12,
        "Sports" : True
    },
}
#9. Print the names of all three classmates on the same line.
print (fifth_hour_class["student_1"]["Name"])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
fifth_hour_class["student_1"].pop("Name")
print(fifth_hour_class["student_1"])