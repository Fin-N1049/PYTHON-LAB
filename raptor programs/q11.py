# check whether a number is armstrong number(11)
a=int(input("enter the number to be checked"))
i=0
q=a
while q>0:
  q=int(q/10)
  i=i+1
q=a
b=0
while q>0: 
  r=int(q%10)
  q=int(q/10)
  b=b+r**i
if a==b:
  print(a,"is an armstrong number")
else :
  print(a,"is not an armstrong number")