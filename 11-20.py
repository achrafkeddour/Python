#11 logical operators : and , or , not 
is_student = False
if not is_student:
    print("you are not a studnet ")
else :
    print("you're student")
#you are not a studnet
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
--------------------------------------------------------------------------------------------------------------------------------------------------------
