#arithmetic sequence upto n terms(10)
n=int(input("enter the n th term"))
a=int(input("enter the first term"))
d=int(input("enter the common difference"))
print("arithmetic sequence upto",n,"terms are")
i=0
while (i<n):
  term=a+(i*d)
  print(term)
  i=i+1