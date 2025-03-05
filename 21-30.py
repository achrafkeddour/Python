#21 lists, sets, tuples 
# list = [] , ordered , you can change values
# tuple = () , ordered
# set = {} , unordered  , you can not change values

#What Does "Mutable" Mean?

#    Mutable means you can change the object after it’s created—add, remove, or modify its elements.
#    Immutable means once it’s created, it’s locked; you can’t change it.

#What Does "Ordered" Mean?

#    Ordered means the items have a specific, predictable sequence, and you can access them by their position (like item[0] for the first item).
#    Unordered means there’s no guaranteed sequence, and you can’t rely on positions.

#lists 
mylist = ["apple", "orange","banana", "ak"]

print(mylist[::-1]) #the inverse ['orange', 'banana', 'apple']

#the different methods that we can use with collections
print(dir(mylist))

#see the explanation of each method that we may apply
#print(help(mylist))

print(mylist.sort())
print(mylist)


mylist.append("space") #add in the last
mylist.insert(1,"woowowowowowow") #add in the position that i want
mylist.remove('banana')
for element in mylist:
    print(element)


print(mylist.index("orange")) #the index of orange in the list

print(mylist.count("orange")) #1 kayna mara whda
print(mylist.count("notexistent")) #0

mylist.clear() #make it [] (clear)
print(mylist)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Sets {} : same for dir() and help() methods ,
# we can not have myset[0] because there is no order

myset = {'achraf','gogo','qq'}
print(myset) # {'qq', 'gogo', 'achraf'} (no order)
myset.add('newhaha') # or remove('existing_element')
print(myset) #'achraf', 'newhaha', 'qq', 'gogo'}
# pop() remove randomly because no order 
#clear()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#23 2D-collections:
coll = [
    ['days/times','9:00','11:00','13:00','14:00'],
    ['sunday','mathematics','arabic','french','english'],
    ['monday','geology','biology'],
    ['thuesday','sports','science','history']
]
print('\n\t\tOur Work Plan ! \n')
for row in coll:
    for column in row:
        print(f"{column:<15}", end=' | ')
    print(); print()

print('\n\nphone numbers :\n\n')
nums = ((1,2,3),
        (4,5,6),
        (7,8,9),
        ('*',0,'#')
        )
for row in nums:
    for column in row:
        print(f"{column:^3}",end=' ')

    print()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#25 dictionaries
menu = {
    "simple": 200,
    "napolitano": 300,
    "4 seasons": 600,
    "margherita": 400,
    "tacos": 500,
    "hamburger": 250
}

cart = []
total =0

print("--------------------------------MENU--------------------------------")

for k , v in menu.items():
    print(f"{k:10} : ${v}")
print("--------------------------------------------------------------------")

while True:
    food = input("what do you want (q to quit) : ")
    if food.lower() == "q":
        break
    elif food in menu.keys():
        cart.append(food)

print()
for food in cart:
    total += menu.get(food)
    print(food,end=' ')

print()
print(f"total is : {total:.2f}")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
