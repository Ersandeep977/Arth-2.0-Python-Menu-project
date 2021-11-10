# this for internal testing used this file is not a part of this program
import os
import time
import calendar
import datetime
from time import gmtime, strftime

def menu():
    print('''
    Enter 1 for date print
    Enter 2 for cal print
    Enter 3 for notepad
    Enter 4 for chore
    ''')
    ch = int(input('Enter Your choces :'))
    if ch == 1 :
        date()
        
    elif ch == 2 :
        cal()
    
    elif ch == 3:
        notepad()
    
    elif ch == 4:
        chrome()   
    else:
        print('Right one..')
menu() 

def date():
    print("Curent date is ")
    print("*"*80)
    print("Current System date is :- ",strftime("%d/%m/%y", gmtime()))
    print("Current System day is :- ",strftime("%d", gmtime()))
    print("Current System Month is :- ",strftime("%m", gmtime()))
    print("Current System Year is :- ",strftime("%y", gmtime()))
    print("*"*80)
    print("thank you for using")
    print("*"*80) 
date()
def cal() :
    month = datetime.date.today().month
    year = datetime.date.today().year
    print("*"*80)
    print (calendar.month(year,month))
    print("*"*80)
    print("thank you for using")
    print("*"*80) 
cal() 
def notepad():
    print(os.system('notepad'))
    print("*"*80)
    print("thank you for using")
    print("*"*80)
notepad() 

def chrome():
    print(os.system('chrome'))
    print("*"*80)
    print("thank you for using")
    print("*"*80) 
chrome()

main()

print("hello")