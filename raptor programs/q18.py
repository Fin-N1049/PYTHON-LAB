# reverse of the given number(18)
a=int(input("enter the number "))
q=a
b=0
while q>0:
  r=q%10
  q=int(q/10)
  b=b*10+r
print(b,"is the reverse of",a)