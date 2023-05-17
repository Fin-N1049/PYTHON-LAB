#find the nature of quadratic equation(9)
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
d=(b*b)-4*a*c
if d>0:
  print("the quadratic equation has 2 real solutions")
elif d==0:
  print("the quadratic equation has 1 real solution")
else :
  print("the quadratic equation has 2 imaginary solution")