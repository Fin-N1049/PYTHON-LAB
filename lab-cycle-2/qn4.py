import math
class box:
  length=int
  breadth=int
  height=int
  area=int
  volume=int
  ratio=float
  count=0
  def __init__(self,*arg:int):
    if len(arg)==1:
      self.length=arg[0]
      self.count=1
    elif len(arg)==2:
      self.length=arg[0]
      self.breadth=arg[1]
      self.count=2
    elif len(arg)==3:
      self.length=arg[0]
      self.breadth=arg[1]
      self.height=arg[2]
      self.count=3
    else:
      print("arg overflowed")

  def area_volume(self):
    if self.count==1:
      self.area=6*(self.length**2)
      self.volume=math.pow(self.length,3)
      print("-"*50)
      print("the area of cube is : ",self.area)
      print("the volume of cube is : ",self.volume)
      print("-"*50,"\n")
    elif self.count==2:
      self.area=2*(math.pow(self.length,2))+4*self.length*self.breadth
      self.volume=math.pow(self.length,2)*self.breadth
      print("-"*50)
      print("the  area of square prism is : ",self.area)
      print("the volume of square prism is : ",self.volume)
      print("-"*50,"\n")
    elif self.count==3:
      self.area=2*((self.length*self.breadth)+(self.height*self.length)+(self.height*self.breadth))
      self.volume=self.length*self.breadth*self.height
      print("-"*50)
      print("the area of rectangular prism is : ",self.area)
      print("the volume of rectangular prism is : ",self.volume)
      print("-"*50,"\n")

    



a=int(input("enter how many box to create : "))
a1=a
boxes=[]
ratio=[]
while a>0:
  value=input("enter which boxes to create without space and use  small letter  (cube , squareprism and rectangularprism) : ")
  boxes.append(value)
  a-=1
print("\n")
while a1>0:
  for i in boxes:
    print(i)
    if i=='cube':
      side=int(input("enter the side of cube : "))
      obj1=box(side)
      obj1.area_volume()
      ratio.append(obj1.volume/obj1.area)
    elif i=='squareprism':
      length=int(input("enter the length of square prism : "))
      heigth=int(input("enter the heigth of square prism : "))
      obj2=box(length,heigth)
      obj2.area_volume()
      ratio.append(obj2.volume/obj2.area)
    elif i=='rectangularprism':
      length=int(input("enter the length of rectangular prism : "))
      width=int(input("enter the width of rectangular prism : "))
      heigth=int(input("enter the heigth of rectangular prism : "))
      obj3=box(length,width,heigth)
      obj3.area_volume()
      ratio.append(obj3.volume/obj3.area)
    else:
      print("invalid statement")
    a1-=1
  print("the max volume area ratio in the given box is : ",round(max(ratio),2))
      
