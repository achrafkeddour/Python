#11 logical operators : and , or , not 
is_student = False
if not is_student:
    print("you are not a studnet ")
else :
    print("you're student")
#you are not a studnet
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#12, conditional expressions : 'Action1 if condition else Action2' 
access_level = "admin" #i can change it
print("full_access" if access_level == "admin" else "limited access")
a = 12 ; b = 5
print(f"the maximun is {a if a > b else b}")

#another example 
temperature = float(input("enter the temperature today : "))
is_sunny = "it is sunny today" if temperature > 23 else "it is not sunny be carefull bro"
print(is_sunny)
# 13 : count and replace methods -----------------------------------------------------------------------------------------------------------------------------------------
value = input("enter a value : ")
num_of_a = value.count("a") + value.count("A") 
print(f"a has appeared {num_of_a} times")

newname = value.replace("a","")
print(f"if we deleted it, we'll have : {newname}")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#14 #indexing [start : end : step]
ach = "hello everyone"
print(ach[2]) #l
print(ach[1:8]) #ello ev (only from 1 to 7) (the last mafihach)
# print(ach[:4]) same result as print(ach[0:4]) start from the beginnig to 3
print(ach[4:]) #o everyone from the fifth (5) letter to the end
#print(ach[start : end : step])
print(ach[::3]) #hlern (ysoti b 3 steps)

#megative indexes means starting from the last 
#-1 the last one ; -2 before the last one ; -3 the third last one
print(ach[-4]) #y

credit_num = "1234-5678-9012-3456" #i must have string not int

lastdegits = credit_num[-4:]
print(F" your credit num is : XXXX-XXXX-XXXX-{lastdegits}")

inverse_num = credit_num[::-1]
print(f"the inverse is {inverse_num}")

same = ach[::]
print(same)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#15 : format spicifiers {x:flags}
import math 

p = math.pi 
a =2222222.56585
n = -10012.45
print(f"{p:.2f}") #.Nf : Round to N decimal places (fixed point). 
print(f"{p:40}") #:(N) : Allocate N spaces (default is right-justified). '                       3.141592653589793'
print(f"{p:040}")                                                      # '000000000000000000000003.141592653589793'
print(f"{a:,}") #2,222,222.56585
print(f"{p:+}")
print(f"{n:+}") # :+ : shows the sign (whatever it is + or -)
print(f"{a:<030,}") #2,222,222.56585000000000000000      justify left
print(f"{a:>030,}") #0000000000000002,222,222.56585      justify right
print(f"{a:^030}") #000000002222222.56585000000000       center align
print(f"{a:=030,}") #0,000,000,000,002,222,222.56585

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#16 while
nom = ""
while nom == "" :
    nom = input("please enter your name : ")
print(f"Hello {nom}") 

#2nd example
age = int(input("how old are you ? "))
while age <0 :
    print("age can't be negative")
    age = int(input("how old are you ? "))

print(f"you are {age} !")

#3rd example
food = input("please enter you fav food ")
while not food == "q":
    print(f"{food} is a good choice")
    food = input("please enter another fav food (q to quit)") 

print("bye")

#4th example
num = float(input("enter a number between 1 and 20 : "))

while num < 1 or num > 20 :
    print(f"\n{num} is not valid \n")
    num = float(input("a num between 1 & 20 : "))
print(f"i like it {num}")

#5th example
i = 0
while i < 10 :
    t = float(input(f"enter the {i}(th) : "))
    print(f"you entered {t} ! good")
    i +=1
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#18 for loops
for x in range(20,100,5):
    print(x) #result from 20 to 100 (step is 5)
print("----------------------------------------------------")
for x in reversed(range(20,30)):
    print(x)

something = "hello everyone"
for i in reversed(something) :
    print(i)

mylist = ['achraf','second' , 'third','brocode']
for i in mylist:
    print(i)

#other example
for i in range(1,9):
    if i == 5: #sauter
        continue
    elif i ==7: #stop at 6
        break
    else:
        print(i)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#20 nested loops 
mylist = ['blue','red','yellow','white']

for y in range(1,10):
    for x in mylist:
        print(f"{y} - {x}   ",end='|') # number - colors
    
    print()# by default end='\n'

print("\n------------------------------------------------------------\n")


for y in range(10):
    for x in range(4):
        print('$',end=' ')

print("\n------------------------------------------------------------\n")

for y in range(10):
    for x in range(4):
        print('$',end=' ')
    print()
