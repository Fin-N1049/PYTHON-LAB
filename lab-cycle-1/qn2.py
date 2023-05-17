#creating a function to get inputs and output the area of triangle
def AreaOfTriangle(a,b,c):
  import math
  s=(a+b+c)/2
  area=math.sqrt(s*(s-a)*(s-b)*(s-c))
  return area

count=0
i=2
area1=0
area2=0
total_area=area1+area2


def contribution():
  total_area=area1+area2
  contribution_tri1=(100*area1)/total_area
  contribution_tri2=(100*area2)/total_area

  print("the area contribution of first triangle is ",contribution_tri1)
  print("the area contributuon of second triangle is ",contribution_tri2)
    
print("TRIANGLE:- AREAS AND ITS CONTRIBUTION")
while i>0:

  a=int(input('enter the side of triangle :'))
  b=int(input('enter the side of triangle :'))
  c=int(input('enter the side of triangle :'))
  i=i-1
  count+=1
  if count==1:
    area1=(AreaOfTriangle(a,b,c))
    print(' area of first triangle is ',area1)

  elif count==2:
    area2=AreaOfTriangle(a,b,c)
    print('area of second triangle is',area2)

contribution() 