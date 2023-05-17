#sum of factors of a number(20)
a=int(input("enter the number"))
i=1
sum=0
while i<=a:
  if a%i==0:
    sum=sum+i
    i=i+1
  else:
    i=i+1
print("sum is ",sum)