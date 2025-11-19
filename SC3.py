#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: SC3
import random

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
import random
x = 0
while 5>3:
    players = int(input("Enter number of players:"))
    if players < 1:
        print("Please enter a positive integer")
        continue
    count = players
    while not players == 0:
        print("Enter your score 1-5")
        score = int(input())
        if score > 5 or score < 1:
            print("Please enter a score between 1 and 5")
            continue
        players -= 1
        x += score
        print(score)
    y = x / count
    print(y)