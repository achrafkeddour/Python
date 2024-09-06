#21 lists, sets, tuples 
# list = [] , ordered , you can change values
# tuple = () , ordered
# set = {} , unordered  , you can not change values

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

