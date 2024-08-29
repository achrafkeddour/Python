#11 logical operators : and , or , not 
is_student = False
if not is_student:
    print("you are not a studnet ")
else :
    print("you're student")
#you are not a studnet
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#12, conditional expressions : 'Action1 if condition else Action2' 
age = 19
print("Adult" if age >= 18 else "child")
access_level = "admin" #i can change it
print("full_access" if access_level == "admin" else "limited access")
a = 12 ; b = 5
print(f"the maximun is {a if a > b else b}")
