# currency swap  
it is a project that support currency swap  

![alt text](https://i.imgur.com/E8Qlh9h.png)

# how to run in terraform:  
git clone https://github.com/mohamedgalia/currency_swap.git  
cd currency_swap  
go to main.tf file  
terraform init  
terraform apply
  
**you will find the app in "instance-ip:8000"**  

#how to run in k8s:
git clone https://github.com/mohamedgalia/currency_swap.git  
cd currency_swap/k8s  
kubectl apply -f backend-dp.yml -f backend-sr.yml -f frontend-dp.yml -f frontend-sr.yml -f auti-dp.yml -f auti-sr.yml  

**you will find the app in "127.0.0.1:30037"**  

# using:  
python  
flask  
docker  
docker compose  
aws  
k8s  
html  
