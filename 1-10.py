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

#4 string methods   ----------------------------------------------------------------------------------------------------------------------------------------------------------
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
