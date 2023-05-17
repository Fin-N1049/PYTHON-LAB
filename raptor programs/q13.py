#binary to decimal(13)
a=int(input("enter a binary number"))
q=a
i=0
n=0
while q>0:
  r=int(q%10)
  q=int(q/10)
  n=n+r*(2**i)
  i=i+1
print("decimal equalent to ",a,"is",n)
  
  
