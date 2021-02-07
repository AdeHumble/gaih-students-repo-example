# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:14:26 2021

@author: MUJEEB ADEYANJU SUNMOLA
ORGANISATION: GLOBAL AI PYTHON HUB
"""

#HOMEWORK 2a: A program to swap the second half of an even list with its first half
count=0
items=input("Please, enter an even list of items\nNOTE: Each item must be separated by a comma: ").split(",")

#The while loop below will counts the number of wrong entries and also termnates the whole program at excatly 3 wrong triers.
while len(items)%2!=0:
    count+=1
    if count<=2:
        items=input("Error!\nYou entered an odd list of items...try again!\n\nPlease, enter an even list of items, each separated by a comma: ").split(",")
    else:
        print("You have made 3 incorrect entries...Bye!")
        break
    
else:
    first_half=items[:int(len(items)/2)]       #slices the first half of the even list
    second_half=items[int(len(items)/2):]      #slices the second half of the even list
    print('\nYour new(swapped) list is: ',second_half+first_half)           #joins and prints the two lists together in a reversed order
