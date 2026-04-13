#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: HW-R6


#1. Create a def function that prints out "Hello World!". Call the function.
def hello_world():
    print("Hello World!")
hello_world()
#2. Create a def function that prints your name. Call the function with the name as the argument.
def print_name(name):
    print(name)
print_name("Ivan")

#3. Create a def function that calculates the average of a list. Call the function with the list as the argument.

def average_list(*num_list):
    avg = sum(num_list)/len(num_list)
    print(avg)
average_list(1,2,3,4,5)
#4. Call the function from #3 but with a new list of different numbers.
average_list(5,4,3,2,1)
#5. Create a def function that takes two numbers as arguments, x and y. Inside the function, create a for loop
#with a range of 10. Inside the loop, make z equal the sum of x and y, make x equal y, then y equal z.
def function(x,y):
    for i in range(10):
        z=x+y
        x=y
        y=z
        print(x)
#6. Call the function from #5 with the arguments for x and y being 0 and 1.
function(0,1)