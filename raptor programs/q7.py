#find the smallest digit in a two digit number(7)
a=int(input("enter the number"))
q=int(a/10)
r=int(a%10)
if q<r:
  print(q,"is the smallest")
elif q==r:
  print("both numbers are equal")
else:
  print(r,"is the smallest")

