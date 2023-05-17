class threeDShapes:
  volume=float
  area=float

  def print_volume(self,shape):
    print("the volume of the ",shape ," is ",round(self.volume,2))
  def print_area(self,shape):
    print("the area of the ",shape ," is ",round(self.area,2))

class cylinder(threeDShapes):
  height=float
  radius=float
  pi=3.14

  def __init__(self,r,h):
    self.height=h
    self.radius=r

  def cal_volume(self):
    threeDShapes.volume=self.pi*(self.radius**2)*self.height
  
  def cal_area(self):
    threeDShapes.area=(2*self.pi*self.radius*self.height) + (2*self.pi*(self.radius**2))


class sphere(threeDShapes):
  radius=float
  pi=3.14
  
  def __init__(self,r):
    self.radius=r
  
  def cal_volume(self):
    threeDShapes.volume=(4/3)*self.pi*(self.radius**3)
  def cal_area(self):
    threeDShapes.area=4*self.pi*(self.radius**2)



height=float(input("enter the height of cylinder : "))
radius=float(input("enter the radius of cylinder : "))
cylinder1=cylinder(radius,height)
cylinder1.cal_volume()
cylinder1.cal_area()
print("____________________________________________________")
cylinder1.print_volume("cylinder")
cylinder1.print_area("cylinder")
print("____________________________________________________")

radius1=float(input("\n enter the radius of sphere : "))
sphere1=sphere(radius1)
sphere1.cal_volume()
sphere1.cal_area()
print("____________________________________________________")
cylinder1.print_volume("sphere")
print("____________________________________________________")
