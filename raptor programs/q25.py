#area and perimeter of triangle(25) 
import math
a=int(input("enter the length of first side"))
b=int(input("enter the length of second side"))
c=int(input("enter the length of third side"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
p=2*s
print(p,"is the perimeter of the triangle")
print(area,"is the area of the triangle")
