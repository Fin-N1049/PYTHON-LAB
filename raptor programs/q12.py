#check whether a number is an automorphic number(12)
a=int(input("enter the number to be checked"))
b=int(a*a)
q=b
n=0 
i=0
while q>0:
  r=(q%10)
  q=int(q/10)
  n=n+r*(10**i)
  if n==a:
    print(a,"is an automorphic number")
    break
  else:
    i=i+1
if q==0:
  print(a,"is not an automorphic number")
  