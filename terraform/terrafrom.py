import os
import time
print("...."*80)
print("hello....WELCOME TO 'terraform WORLD'...by SANDEEP KUMAR Patel..")
print("...."*80)
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