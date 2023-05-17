def readUser():
  a=str(input("enter string and integer with space : "))
  return a

def rotate(a):
  b=a.split()
  c=[]
  k=int(input("enter element to rotate : "))
  for i in range(k,len(b)):
   c.append(b[i])
  for i in range(0,k):
    c.append(b[i])
  return c

def converting_tuple(a):
  b=tuple(i for i in a)
  return b

def removing_duplicate(a):
  a=set(a)
  b=list(a)
  return b

def fun(b):
  c=[]
  for i in b:
    i=int(i)
    c.append((i*i)-i)
  print("after converting into given function : ",c)
  return c

def merg(a,b):
  a.sort()
  b.sort()
  a.extend(b)
  return a

list1=readUser()
rList=rotate(list1)
tup=converting_tuple(rList)
remove=removing_duplicate(tup)
list2=list(input("enter the numbers :"))


print("the rotated list is : ",rotate)
print("list after converting to tuple : ",tup)
print("after removing duplicate : ",remove)
func=fun(list2)
mergList=merg(func,remove)
print("merging given two list : ",mergList)
