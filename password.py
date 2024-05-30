import random

letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','_','+','?']

print("Welcome To The Password Generator!!!!!")

nl=int(input("How many letters you want in password:"))
nn=int(input("How many numbers you want in password:"))
ns=int(input("How many symbols you want in password:"))

password_list=[]

for i in range(1,nl+1):
    char= random.choice(letters)
    password_list += char

for x in range(1,nn+1):
    num= random.choice(numbers)
    password_list += num

for a in range(1,ns+1):
    sym= random.choice(symbols)
    password_list += sym


random.shuffle(password_list)

password=''

for char in password_list:
    password += char

print(" ")

print("Here is your password:",password)







P_
