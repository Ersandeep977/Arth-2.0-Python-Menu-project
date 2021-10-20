import os
import time
print("...."*80)
print("hello....WELCOME TO 'terraform WORLD'...by SANDEEP KUMAR Patel..")
print("...."*80)
print('''
Enter "yes" for run terraform command
or
Enter "No" for exit terraform
''')
while True:
    ch = input('Enter your choice "yes/no" :- ')
    if ch == 'yes': 
        print(" ..terrafrom init launch.... ")
        print("#"*150)
        time.sleep(1)
        os.system('terraform init')
        print("#"*150)
        print("...."*80)
        print("NEXT ..Show the validate.... ")
        print("...."*80)
        print("#"*150)
        time.sleep(5)
        os.system('terraform validate')
        print("#"*150)
        print("...."*80)
        print("NEXT ..Show the plan.... ")
        print("...."*80)
        print("#"*150)
        time.sleep(5)
        os.system('terraform plan')
        print("NEXT ..Show the apply.... ")
        print("...."*80)
        print("#"*150)
        time.sleep(5)
        os.system('terraform apply -auto-approve')
        print("NEXT ..Show the destroy.... ")
        print("...."*80)
        print("#"*150)
        time.sleep(5)
        os.system('terraform destroy -auto-approve')
    elif ch =='no':
        print('Thank you for using this application \n wait 5 second and press "Enter" buton')
        time.sleep(3)
        break  
    