# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 20:47:28 2021

@author: MUJEEB ADEYANJU SUNMOLA

ORGANISATION: GLOBAL AI PYTHON HUB
"""
#Homework 3a: A program to verify a user login information
#If there is anything i must add, this program is very dynamic

user_name='adeyanju'
pass_word='blessing'
count=0
count1=0

username=input('Enter your username: ').lower().strip()
while username==user_name:
    print('\nWelcome', username, "\nPLease enter your pasword to further verify your identity")
    password=input('Enter your password: ').lower().strip()
    
    if password==pass_word:
        print('You have succesfully logged in into your account')
        break
    
    elif password!=pass_word:
        count+=1
        if count<=2:
            print('Incorrect password. Please, try entering your password again')
            continue
        
        else:
            print('\nYou have exceeded your trial limits\nThis software is shutting down now....!')
            break

while username!=user_name:   
    if count<=2:
        username=input('That was a wrong username. Please try again: ').strip().lower()
        
        if username==user_name:
            print('\nWelcome', username, "\nPLease enter your pasword to further verify your identity")
            count1=0
            pass_word=='blessing'
            password=input('Enter your password: ').lower().strip()
            
            while pass_word!=password:
                password=input('Enter your password: ').lower().strip()
                count1+=1
                if count1<=2:
                    continue
                else:
                    print('\nYou have exceeded your trial limits\nThis software is shutting down now....!')
                    break

            else:
                print('\nYou have succesfully logged in into your account')
                         
    else:
        print('\nYou have exceeded your trial limits\nThis software is shutting down now....!')
        break







#HOMEWORK 3b (EXTRA): This is purposely commented. it can be uncommented when its time to test it

# profile={user_name: 'adeyanju', pass_word: 'blessing'}

# count=0
# count1=0

# username=input('Enter your username: ').lower().strip()
# while username==profile[user_name]:
#     print('\nWelcome', username, "\nPLease enter your pasword to further verify your identity")
#     password=input('Enter your password: ').lower().strip()
    
#     if password==profile[pass_word]:
#         print('You have succesfully logged in into your account')
#         break
    
#     elif password!=profile[pass_word]:
#         count+=1
#         if count<=2:
#             print('Incorrect password. Please, try entering your password again')
#             continue
        
#         else:
#             print('\nYou have exceeded your trial limits\nThis software is shutting down now....!')
#             break

# while username!=profile[user_name]:
    
#     if count<=2:
#         username=input('That was a wrong username. Please try again: ').strip().lower()
#         if username==profile[user_name]:
#             print('\nWelcome', username, "\nPLease enter your pasword to further verify your identity")
#             count1=0
#             profile[pass_word]=='blessing'
#             password=input('Enter your password: ').lower().strip()
#             while password!=profile[pass_word]:
#                 password=input('Enter your password: ').lower().strip()
#                 count1+=1
#                 if count1<=2:
#                     continue
#                 else:
#                     print('\nYou have exceeded your trial limits\nThis software is shutting down now....!')
#                     break

#             else:
#                 print('\nYou have succesfully logged in into your account')
                
           
#     else:
#         print('\nYou have exceeded your trial limits\nThis software is shutting down now....!')
#         break
