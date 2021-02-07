# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:26:54 2021

@author: MUJEEB ADEYANJU SUNMOLA

ORGANISATION: GLOBAL AI PYTHON HUB

"""

#HOMEWORK 4: A program to prints out all prime numbers between 0 and 100

def prime():
    prime_list=[] #saves the list of prime numbers
    
    #The two for-loops below iterates between 0 and 100 and takes count of any number that is divisible from 1 to that number inclusive
    for i in range(0,100):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
            else:
                continue
            
        #Hence if a number has exactly two divisors(i.e. 1 and itself), only then will it be appended to the list of prime numbers above....    
        if count==2:
            prime_list.append(i)
            
    print('The prime numbers between 0 and 100 are:\n',prime_list,'\n\nThere are 25 of them')
    
prime() #calls the function to action





