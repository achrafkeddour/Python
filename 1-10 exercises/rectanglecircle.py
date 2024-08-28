#rectangle calc
height = input("what is height : ")
width = input("what is width : ")


if bool(height) and bool(width):
    height = float(height)
    width = float(width)

    area = height*width
    perimeter = (height+width)*2

    q = int(input("what do you wanna calculate ? (enter a number) \n 1. area \n 2. perimeter \n 3. both \n"))
    
    if q == 1:
        print(f"the area is {area}")
    elif q==2:
        print(f"the perimeter is {perimeter}")
    elif q==3:
        print(f"the area is {area} and the perimeter is {perimeter}")
    else:
        print("please enter 1 or 2 or 3")
else: 
    print("please enter both height and width values")


------------------------------------------------------------------------------------------------------------------------------------------------------
#circle
import math

D = float(input("what is the diameter of the circle : "))
R = D/2
area = math.pi * pow(R,2)
perimeter = math.pi * R * 2

print(f"the area is {round(area,2)}")
print(f"the perimeter is {round(perimeter,2)}")
---------------------------------------------------------------------------------------------------------------------------------
#triangle
c = math.sqrt(pow(A,2)+pow(B,2)) #watr ta3 triangle (khati circle w rectangle)
