#2 variables ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

name = "achraf" ; last_name = "kdr" ; age = 21 ; b = True 
# same as :     name , last_name , age , b = "achraf" , "kdr" , 21 , True
print("my name is " + name) #it gives : my name is achraf 
print(type(name)) # it gives <class 'str'>
print(type(age))  #it gives <class 'int'>
print(type(b))     #it gives <class 'bool'>
full_name = name + " " + last_name
print(full_name) # achraf kdr

#name1 = name + 1 FALSE because we can only concatenate str (not "int") to str
name1 = name + "1"
print(name1) #achraf1
age = age +1
print(age) #22 and not 21
print("my age is "+ str(age)) # and not print("my age is "+ age) (concatenation is for str)
#float is a decimal number 
floatnum = 25.2 ; print (floatnum) #25.2
print(type(floatnum)) #<class 'float'>

naame = (input("enter your name: "))
if bool(naame): #True if name exits and False it not
    print(f"you are welcome {naame}")
else: 
    print("please enter a name ")
  
#4 string methods   -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
nom = "narUto sho "
print(len(nom)) #length
print(nom.find("o")) #only the index of the first o
print(nom.capitalize()) 
print(nom.upper())
print(nom.lower())
print(nom.isdigit()) #true if nom = "123"
print(nom.isalpha()) #true if there is no space .. only strings (koulech lase9)
print(nom.count("o")) # it's 2
print(nom.replace("o","A")) 
nom = nom.replace("o","A")
print(nom*5)

#5 type cast : str() , int() ,  float()  ---------------------------------------------------------------------------------------------------------------------------------------------------------------
x = 3; p = 120.165
x = float(x) ; p = int(p)
print(x) #3.0
print(p) #120
#anything i wanna print with a sentence must be inside str()
#print ("X is : "+ x) ..Error
print ("X is : "+ str(x)) #true one

#4 user input ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ism = input(" what is your name please ") #i will accept it as a string by default
age = int(input("how old are you ")) # value entered by the user must be an integer
height = float(input("what is your height ")) # value can be integer or float (because every int is a float , 44 = 44.0)
print("\n")
print("hello "+ ism)
print("you are " +str(age)+" years old" ) 
print("your height is " + str(height) +" cm")
print(f"hello {ism}, you are {age} years old , your height is {height} cm ") 

#The f before the string tells Python to look for expressions inside {} and replace them with their values.
age = 30
name = "john" 
print(f"Hello {name} you are {age} years old.")

#6 math --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import math
t = 9.9
print(math.pi) #3.141592653589793
print(math.e) #2.718281828459045
print(math.ceil(t)) #10
print(math.floor(t)) #9
print(math.sqrt(9)) #3.0
print(round(math.e ,2)) #2.72

