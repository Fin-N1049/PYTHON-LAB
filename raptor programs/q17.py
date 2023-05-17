# check whether a number is a paliandrome(17)
a=int(input("enter the number to be checked "))
q=a
b=0
while q>0:
  r=q%10
  q=int(q/10)
  b=b*10+r
if a==b:
  print(a,"is an paliandrome number")
else :
  print(a,"is not an paliandrome number")