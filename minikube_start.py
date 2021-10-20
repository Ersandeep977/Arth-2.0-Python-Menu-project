import os
import time
print("..."*80)
print("hello....WELCOME TO 'KUBERNESTES WORLD'...by SANDEEP KUMAR Patel..")
print("..."*80)
print(" ..Minikube to launch.... ")
print("#"*150)
time.sleep(1)
os.system('minikube start')
print("#"*150)
print("NEXT ..Show the minikube status.... ")
print("#"*150)
time.sleep(1)
os.system('minikube status')
print("#"*150)
print("NEXT ..Show the minikube local ip.... ")
print("...."*150)
time.sleep(1)
print("#"*150)
os.system('minikube ip')
print("#"*150)
print("NEXT ..Show pods.... ")
print("...."*150)
time.sleep(1)
print("#"*150)
os.system('kubectl get pods')
print("#"*150)
print("NEXT ..Show DASHBOARD.... ")
print("...."*150)
time.sleep(1)
print("#"*150)
os.system('start cmd /c "minikube dashboard"')
print("#"*150)
print("NEXT ..create deployment.... ")
print("...."*150)
time.sleep(1)
print("#"*150)
os.system('kubectl create deployment hello-node --image=k8s.gcr.io/echoserver:1.4')
print("#"*150)
print("NEXT ..View the Deployment: .... ")
print("...."*150)
time.sleep(5)
print("#"*150)
os.system('kubectl get deployments')
print("#"*150)
print("NEXT ..Show pods.... ")
print("...."*150)
time.sleep(1)
print("#"*150)
os.system('kubectl get pods')
print("#"*150)
print("NEXT ..Delete all the deployments.... ")
print("...."*150)
time.sleep(5)
print("#"*150)
os.system('kubectl delete deploy hello-node')
print("#"*150)
print("NEXT ..Show DASHBOARD.... ")
print("...."*150)
time.sleep(10)
print("#"*150)
os.system('minikube stop')



