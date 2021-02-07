# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 21:17:55 2021

@author: MUJEEB ADEYANJU SUNMOLA

ORGANISATION: GLOBAL AI PYTHON HUB

"""
#HOMEWORK 5: A program to demostrates the use of PPython class and inheritance using Animals( Dogs and Cats) as a case-study
class Animals:
    breed='domestic'
    legs=4
        
    def best_food(self,food):
        return f"{self.name} is enjoying {food}"
    
    def profile(self):
        print(f'My name is {self.name}\nI am a a very cute {self.breed} animal with {self.legs} legs and {self.toes} toes\nI am {self.age} years old and i lobe ')
        
class Dogs(Animals):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.toes=16
      
class Cats(Animals):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.toes=18
    
    
#Instances of the Dog and Cat's class resPectively   
watson1=Dogs('Jilly',12)
watson2=Cats('Billy', 10)



print(watson1.best_food('rice'))
print()
print(watson1.profile())
