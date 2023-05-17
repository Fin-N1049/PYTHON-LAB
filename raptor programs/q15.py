#fibonacci series(15)
a=int(input("enter the number of terms"))
if a==1:
  print("0")
elif a==2:
  print("0 1")
else:
  i=0
  num1=0
  num2=1
  print("0 1",end=" ")
  while i<(a-2):
    sum=num2+num1
    print(sum,end=" ")
    num1=num2
    num2=sum
    i=i+1


  