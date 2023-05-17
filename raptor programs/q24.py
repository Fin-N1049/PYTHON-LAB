#GCD of two numbers(24)
a=int(input("enter the first number  "))
b=int(input("enter the second number "))
i=2
x=1
while i<b/2:
  if a%i==0 and b%i==0:
    a=a/i
    b=b/i
    x=x*i     
  else:
    i=i+1
print("GCD of the two numbers is",x)