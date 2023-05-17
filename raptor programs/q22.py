#Sum upto Series of 1-4+9-16...(22)
a=int(input("enter the number of terms"))
i=1
sum=1
while i<a:
  i=i+1
  x=i*i
  if i%2==0:
    sum=sum-x
  else:
    sum=sum+x
print(sum)
  

  

  