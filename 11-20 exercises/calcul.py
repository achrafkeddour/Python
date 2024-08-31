p = float(input("enter the value of p : "))
t = 100
n = float(input("enter the value of n : "))
r= float(input("enter the value of r : "))

while p < 0 :
    print("p must be > 0 (more than 0)")
    p = float(input("enter the value of p : "))

while n <= 0 :
    print("n must be > 0 (more than 0)")
    n = float(input("enter the value of n : "))

while r < 0 :
    print("r must be > 0 (more than 0)")
    r = float(input("enter the value of r : "))

A = p * pow((1 + r/n),t)

print(f"the A is {A:.2f}") #round 2 nums after the ","
