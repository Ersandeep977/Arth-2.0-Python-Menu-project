import os 
import time
import calendar
import datetime
from time import gmtime, strftime
print("*"*80)
print("*"*20,"Task-1 by Sandeep Kumar Patel","*"*20)
print("*"*80)
print("Welcome to my Menu")
print("*"*80)
while True:
    c = input('do you want Continu plz type "y/n" :- ')
    print('''
Enter 1 for date Print
Enter 2 for calender Print
Enter 3 for Text Editer Open
Enter 4 for Firefox Open
Enter 5 for Minikube launch
Enter 6 for launch Google
Enter 7 for launch Python
Enter 8 for Create EC2 instances in us-east-1 resion
Enter 9 for launch Apache server for hosting the webpage
Enter 10 to launch docker

''')
    if c == "y" :
        ch = int(input('Enter your choice :- '))    
        if ch == 1:
        # for date Print     
            print("*"*80)
            print("Current System date is :- ",strftime("%d/%m/%y", gmtime()))
            print("Current System day is :- ",strftime("%d", gmtime()))
            print("Current System Month is :- ",strftime("%m", gmtime()))
            print("Current System Year is :- ",strftime("%y", gmtime()))
            print("*"*80)
            print("thank you for using")
            print("*"*80)
            
        elif ch == 2:
        # Enter 2 for calender Print    
            month = datetime.date.today().month
            year = datetime.date.today().year
            print("*"*80)
            print (calendar.month(year,month))
            print("*"*80)
            print("thank you for using")
            print("*"*80)
            
        elif ch == 3:
        # Enter 3 for NotePad Open    
            print(os.system('gedit'))
            print("*"*80)
            print("thank you for using")
            print("*"*80)
        elif ch == 4:
            print(os.system('firefox'))
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
        # Enter 8 for Create EC2 instances in us-east-1 resion    
            print('terrafrom file copy in main folder')
            os.system('cp ./terraform/main.tf main.tf')
            print('python file copy in main folder')
            os.system('cp ./terraform/terraform.py terraform.py')
            os.system('python terraform.py')
            ch= input((' do you went to clear  terrafrom and python file type "yes/no" : '))
            if ch == "yes":
                print('file delete ......')
                os.system('rm -rf main.tf terraform.py .terraform.lock.hcl terraform.tfstate terraform.tfstate.backup')
                os.system('rd /s .terraform')
            else:
                print('thank you using terraform')
                exit()
            print("*"*80)
            print("thank you for using")
            print("*"*80)
        elif ch == 9:
            print('''
                fast you are sure this linx server other vies this is not work
                if you are sure them type "yes"
                if not sure then type "no"
            ''')
            c = input('Are you Sure this linx type "yes/no" :- ')
            if c == "yes":
                os.system('chmod +x shell.sh')
                os.system('sh shell.sh')
                print("*"*80)
                print("thank you for using")
                print("*"*80)
            else:
                print("This work only Redhat linux server not foe windows sever")
                print("*"*80)
                print("thank you for using")
                print("*"*80)   
        elif ch == 11:
            pass         
    else:
        print("Plz chocse Right Option")
        print("Thank you for using my Menu python program.")
        break
