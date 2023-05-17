#whether a number is the multiple of another(6)
a=int(input("enter the first number"))
b=int(input("enter the second number"))
if a%b==0:
  print("a is the multiple of b")
else:    
  print("a is not the multiple of b")
if b%a==0:
  print("b is the multiple of a")
else:
  print("b is not the multiple of a")
