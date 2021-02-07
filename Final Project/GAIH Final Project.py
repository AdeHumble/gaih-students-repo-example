# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 07:11:31 2021

@author: MUJEEB ADEYANJU SUNMOLA

ORGANISATION: GLOBAL AI PYTHON HUB
 
"""
#Final Project
class employee:
    def __init__(self,name,age,lang):
        self.name=name
        self.age=age
        self.lang=lang
        self.name_lang={}
        self.name_age={}
        
        self.name_age.update({self.name:age})
        self.name_lang.update({self.name:self.lang})
        
        print(self.name_lang)
        
        print(self.name_age)
        
           
    def update_lang(self,name,*lang): #update the language information for an existing employee
                    
        if name==self.name:
            print('Updating language information for', name)
            self.name_lang.update({name:self.lang})
            print(self.name_lang)
        
       
class manager(employee):
    pass
    
    
emp1=employee("Bukky",30,'Spanish')
print()
mngr1=manager("Mr Godfrey", 55,'French')


emp1.update_lang('Bukky', 'German')
print()
mngr1.update_lang('Mr Godfrey', 'Yoruba')