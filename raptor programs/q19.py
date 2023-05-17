#square of natural numbers between two numbers(19)
a=int(input("enter the first number"))
b=int(input("enter the last number"))
while a<b:
  c=a*a
  a=a+1
  print(c)
if a==b:
  print("there is no number between ",a,"and", b)
else:
  print("there is no number between", a,"and ",b)