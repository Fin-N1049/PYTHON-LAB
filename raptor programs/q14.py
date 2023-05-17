#factorial to a given number(14)
def fact (x):
  i=1
  n=1
  while i<x+1:
    n=n*i
    i=i+1
  return(n)
a=int(input("enter the n th term"))
fact(a)
print("factorial of",a, "is",fact(a))

