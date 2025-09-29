# Project_2: Password Generator in python
import random
import string
Alphabets = list(string.ascii_letters)
Numbers = ['1','2','3','4','5','6','7','8','9','0']
Special_Characters = ["!","@","#","$","%","^","&","*","(",")","_","+","=","/",";",":","<",">","?","."]
print("Welcome to the password generator...!")
n_Alphabets = int(input("Enter the n.of alphabets you want in your password !\n"))
n_Numbers = int(input("Enter the n.of numbers you want in your password !\n"))
n_Symbols = int(input("Enter the n.of symbols you want in your password !\n"))
Password=[]
for i in range(1,n_Alphabets+1):
    alph = random.choice(Alphabets)
    Password += alph
#print(Password)
for i in range(1,n_Numbers+1):
    nums = random.choice(Numbers)
    Password += nums
#print(Password)
for i in range(1,n_Symbols+1):
    symb = random.choice(Special_Characters)
    Password += symb
random.shuffle(Password)
#print(Password)
Pswd=""
for j in Password:
    Pswd += j
#print(Pswd)
print(f"your generated password is: {Pswd}")
