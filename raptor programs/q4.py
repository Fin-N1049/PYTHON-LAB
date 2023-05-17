#greatest among 3 numbers(4)
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int (input("enter the third number"))
if a<b<c or b<a<c:
  print(c,"is the greatest")
elif a<c<b or c<a<b:
  print(b,"is the greatest")
else :
  print(a,"is the greatest")