#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be given a number as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

#Code Here:

height = int(input("Input your height here (In inches)"))
weight = int(input("Input your weight here (In pounds)"))

print(f"your height is {height} inches")
print(f"your weight is {weight} pounds")

BMI = weight / (height**2) * 703
print(f"Your BMI is {BMI}")

if BMI < 18.5:
    print("You are under weight")
elif BMI >= 18.5 and BMI <= 25:
    print("You are normal weight")
elif BMI >= 25 and BMI <= 29.9:
    print("You are over weight")
else:
    print("You are very obese")
