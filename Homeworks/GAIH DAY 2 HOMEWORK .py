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





#HOMEWORK 2b: A program to prints out all even numbers from 0 to any SINGLE DIGIT of the user_input(user_input inclusive)
even=[]
while True:
   #The try-except block below tries/tests/corrects for any invalid inputs

    try:
        num=abs(int(float(input("\nEnter your number: "))))
        break
    except:
        print("That was a wrong input! You must enter an integer value. Please, try again!")
    
    
#Even if the try-except block accepts the user inputs, the if-statements block below will make sure the input is a single digit   
if len(str(num))==1:
    for i in range(num+1):
        if i%2==0:
            even.append(i)

    print(f'The even numbers from to {num} ({num} inclusive) are: {even}')
else:
    print("Invalid input!\nNOTE:You must enter a single digit...Please, try again") #...and if not, it will prompts an error 
    