foods = []
prices = []
total = 0

while True:
    food = input("enter a food that you wanna buy (q to quit) : ")
    if food.lower() == 'q':
        break
    else:
        price = float(input("enter its price : $"))
        foods.append(food)
        prices.append(price)


print("your cart shop : ")
for food in foods:
    print(food,end=' , ')

print()

for price in prices:
    print(price,end=' , ')

print()

for price in prices:
    total+=price

print(f"the total price is : ${total}")
