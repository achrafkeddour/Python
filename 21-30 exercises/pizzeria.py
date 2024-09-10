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
print(f"total is : {total:2f}")
