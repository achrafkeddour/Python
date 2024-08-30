#validate inputs entered by user
#not less than 12 characters
#we dont accept symbols like @
#no spaces no numbers we accept only charaters

username = input("Enter your username ")
if len(username) < 12 :
    print("please enter a username made from 12 characters and more ")
elif username.find("@") != -1: # If find returns any value other than -1, it means "@" is found
    print("we dont accept @ ")
elif not username.isalpha() :
    print("no spaces no numbers we accept only charaters")
else :
    print(f"Welcome {username} .. you have a good name ")


print(username.find("@")) #if i dont find @ i got -1 .. if i find it i got another value (the index of @)

