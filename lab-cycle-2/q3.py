class Box:
    length=None
    breadth=None
    height=None
    area=None
    volume=None
    def __init__(self,*arg):
        if(len(arg)==1):
            self.length=arg[0]
            self.breadth=arg[0]
            self.height=arg[0]
        elif(len(arg)==2):
            self.length=arg[0]
            self.breadth=arg[0]
            self.height=arg[1]
        elif(len(arg)==3):
            self.length=arg[0]
            self.breadth=arg[1]
            self.height=arg[2]

    def find_area(self):
        self.area=2*((self.length*self.breadth)+(self.breadth*self.height)+(self.height*self.length))
        # print("Area=",self.area)
        return self.area
    def find_volume(self):
        self.volume=self.length*self.breadth*self.height
        # print ("Volume=",self.volume)
        return self.volume
    
import random
n=int(input("Enter the number of boxes needed : "))
b=[Box(random.randint(1,100),random.randint(1,100),random.randint(1,100))for i in range (n)]
ar=[i.find_area()for i in  (b)]
vol=[i.find_volume()for i in (b)]
ratio=[]
for i in range (0,n):
    ratio.append(round(vol[i]/ar[i],3))
pos=ratio.index(max(ratio))
print("The box with maximum volume:area ratio is = ")
print("Area = ",ar[pos])
print("Volume =",vol[pos])
print("Ratio =",ratio[pos])  