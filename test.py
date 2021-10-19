import os 
import time
import calendar
import datetime
from time import gmtime, strftime
print("*"*80)
print("*"*20,"Task-1 by Sandeep kumar Patel","*"*20)
print("*"*80)
print("Welcome to my Menu")
print('''
Enter 1 for date Print
Enter 2 for calender Print
Enter 3 for NotePad Open
Enter 4 for Chrome Open
Enter 5 for minikube launch
Enter 6 for launch Google
Enter 7 for launch Python
Enter 8 for Create EC2 instances in us-east-1 resion
''')
print("*"*80)
ch = int(input('Enter your choces :- '))
if ch == 1:
    print("*"*80)
    print("Current System date is :- ",strftime("%d/%m/%y", gmtime()))
    print("Current System day is :- ",strftime("%d", gmtime()))
    print("Current System Month is :- ",strftime("%m", gmtime()))
    print("Current System Year is :- ",strftime("%y", gmtime()))
    print("*"*80)
    print("thank you for using")
    print("*"*80)
elif ch == 2:
    # yy = int(input("Enter year: "))
    # mm = int(input("Enter month: "))
    # print(calendar.month(yy, mm))
    month = datetime.date.today().month
    year = datetime.date.today().year
    print("*"*80)
    print (calendar.month(year,month))
    print("*"*80)
    print("thank you for using")
    print("*"*80) 
elif ch == 3:
    print(os.system('notepad'))
    print("*"*80)
    print("thank you for using")
    print("*"*80)
elif ch == 4:
    print(os.system('chrome'))
    print("*"*80)
    print("thank you for using")
    print("*"*80)
elif ch == 5:
    os.system('start cmd /c "python minikube_start.py"')
elif ch == 6:
    import webbrowser
    webbrowser.open('http://www.google.com')
    print("*"*80)
    print("thank you for using")
    print("*"*80)
elif ch == 7:
    os.system('start cmd /c "python"')
    print("*"*80)
    print("thank you for using")
    print("*"*80)  
elif ch == 8:
    os.system('start cmd /c "python C://Users//Sandeep//Desktop//Arth-2.0//terraform//terraform.py"')
   # os.system('start cmd /c "python ./terraform/terraform.py"')
    print("*"*80)
    print("thank you for using")
    print("*"*80)
elif ch == 9:
    os.system('')
        
else:
    print("Plz chocse Right Option")
