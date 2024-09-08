name = input("enter your name : ")
mymoney = float(input("how much do you have : $"))

books = []
prices = []
total = 0

while True:
    book = input("which book do you want to buy (q to quit) : ")
    if book.lower() =='q':
        break
    else: 
        price = float(input("enter its price : $"))
        books.append(book)
        prices.append(price)

for price in prices:
    total += price

if mymoney < total :
    print(f"sorry , you can not buy all these books , the total is ${total} , and you have only ${mymoney}")
elif mymoney == total :
    print(f"haha ! total is {total} , as your money !")
elif mymoney > total :
        print(f"total is {total} , it will stay with you only {mymoney-total}")
