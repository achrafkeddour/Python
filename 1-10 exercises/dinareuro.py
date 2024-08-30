# while 1 euro = 150 DA
print("\n\twe convert euro to DA and DA to euro\n ")
Quantity = float(input("How much do you have : "))
unit = input("Enter the unit (D for Dinar and E for Euro) : ") 

if unit == 'D' or unit =='d' :
    result = Quantity / 150
    print(f"{Quantity} DA = {result} euro")
elif unit == 'E' or unit == 'e' :
    result = Quantity * 150
    print(f"{Quantity} euro = {result} DA")
else:
    print("press only D or E ")
