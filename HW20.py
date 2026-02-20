#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: HW20

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class items:
    def __init__(self, Stock, Cost, weight):
        self.Stock = Stock
        self.Cost = Cost
        self.weight = weight

    def Double(self):
            self.Cost *= 2

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
Chips = items(10, 25 , 17 )
DrPepper = items(50, 45 , 37 )
chocolate = items(100, 90 , 95 )
#3. Print the stock of all three objects and the cost of the second store item.
print(f"Stock: {Chips.Stock}, DrPepper: {DrPepper.Stock}, Chocolate: {chocolate.Stock},")
print(DrPepper.Cost)
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
DrPepper.Double()
print(DrPepper.Cost)
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
chocolate.Stock *= 1/4
print(chocolate.Stock)
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del Chips
try :
    print(Chips.Stock)
except :
    print("Something went wrong no more Chips")