import pickle
import tabulate
from fpdf import FPDF
vehiclelist=[[324942,'Polo_GT','Rahul','Hatchback',19.3,'volkswagen',2456],#
[452313, 'XZ_Plus_LUX', 'Anju', 'SUV', 31.2, 'Tata_Motors', 8734]]
with open('vehicledata.pkl','wb') as vehiclepickle:
   pickle.dump(vehiclelist,vehiclepickle)
class Vehicle:
  def __init__(self,EN,MO,ON,TV,MI,V,RN):
    self.enginenumber=EN
    self.model=MO
    self.ownername=ON
    self.type_v=TV
    self.mileage=MI
    self.vendor=V
    self.registrationNumber=RN
  def display(self):
    s = "{:<9} {:^11} {:^11} {:^10} {:^15} {:^15} {:^15}".format(self.enginenumber,self.model,self.ownername,self.type_v,self.mileage,self.vendor,self.registrationNumber)
    print(s) 

class SeveralVehicles(Vehicle):
  def __init__(self):
      self.vehiclelist=list()
      self.vehicledetails=list()
  
  def readfile(self,filename):
      vehicledata=open(filename,'rb')
      vehiclereaddata=pickle.load(vehicledata)
      for i in vehiclereaddata:
         vehicle=Vehicle(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
         self.vehiclelist.append(vehicle)
         self.vehicledetails.append(i)
      vehicledata.close()
      
  def addvehicle(self,vehicle):
      self.vehiclelist.append(vehicle)
      
  def displaydetails(self):
      print("No.\tEngNo.\t  Model\t\tOwner\t   Type\t\tMileage\t\tVendor\t\tRegNo.\n")
      No = 1
      for vehicleardetail in self.vehiclelist:
            print(No,end = "\t")
            No+=1
            vehicleardetail.display()
            print()
            
  def mileagesort(self):
        S_list = sorted(self.vehicledetails,key = lambda x : x[3])
        vehiclelistindex = 0
        self.vehicledetails = S_list
        for i in S_list:
            A = Vehicle(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
            self.vehiclelist[vehiclelistindex] = A
            vehiclelistindex+=1
            
  def Delete(self,RegNo):
        check = False
        del_index = 0
        for i in self.vehiclelist:
            if i.registrationNumber == RegNo:
                self.vehiclelist.pop(del_index)
                check = True
            del_index+=1
        if not check:
            print(RegNo,"Does not Exist")
            
  def Modify(self,RegNo,Detail_name,Change_value):
        check = False
        for i in self.vehiclelist:
            if i.registrationNumber == RegNo:
                check = True
                if i.Detail_name:
                    self.vehiclelist[i].Detail_name = Change_value
                else:
                    print(Detail_name,"is not a valid detail")
        if not check:
            print(RegNo,"is not a valid parameter")     
            
  def Save(self,filename):
        Details = open(filename,"wb")
        Details.truncate()
        print(self.vehiclelist)
        pickle.dump(self.vehiclelist,Details)
        Details.close()
  
  def filter(self):
    print("1.Owner Name\n2.Vendor name \n3.Model Name \n4.Type\n5.Mileage\n")
    option = int(input("Choose a Data to filter : "))
    filteredList = list()
    if(option==1):
      filterKey = (input("Enter the name you want to filter"))
      filteredList = [i for i in self.vehiclelist if i['ownerName']== filterKey]
      self.display("Filtered List",filteredList)
    elif (option==2):
      filterKey = (input("Enter the Vendor name you want to filter"))
      filteredList = [i for i in self.vehiclelist if i['vendor']== filterKey]
      self.display("Filtered List",filteredList)
    elif (option==3):
      filterKey = (input("Enter the Model name you want to filter"))
      filteredList = [i for i in self.vehiclelist if i['model']== filterKey]
      self.display("Filtered List",filteredList)
    elif (option==4):
      filterKey = (input("Enter the type you want to filter"))
      filteredList = [i for i in self.vehiclelist if i['type']== filterKey]
      self.display("Filtered List",filteredList)
    elif(option==5):
      filterKey = float(input("Enter the mileage you want to filter"))
      filteredList = [i for i in self.vehiclelist if i['mileage']== filterKey]
      self.display("Filtered List",filteredList)
 
  def report(self,filename):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial",size = 10)
        pdf.cell(200,10,ln = 2,align = "C",txt = "No.\tEngNo.\tModel\tType\tMileage\tVendor\tRegNo.\tOwner\n")
        
        for entries in self.vehiclelist:
            add_text = ""
            print(entries)
            add_text+=str(entries)
            add_text+="\t"
            pdf.cell(200,10,ln = 2,align = "C",txt = add_text)
        pdf.output(filename)
        
def main():
     vehicle=SeveralVehicles()
     Key=True
     while Key:
       print("\n\tVEHICLE DETAILS COLLECTION\n1.Display \n2.Sort the mileage\n3.Add \n4. Delete \n5.Modify \n6.Store as a pickle file\n7.Load the pickle file \n8.Filter the data\n9.Export it as a pdfreport\n10.Exit\n")
       choice=int(input("Enter the choice : "))
       if choice == 1:
           vehicle.displaydetails()
       elif choice == 2:
            vehicle.mileagesort()
            vehicle.displaydetails()
       elif choice == 3:
            print("Enter the details : ")
            d1 = int(input("Engine No  :"))
            d2 = input("Model : ")
            d3 = input("Type  : ")
            d4 = int(input("Mileage : "))
            d5 = input("Vendor : ")
            d6 = int(input("Registration No. :"))
            d7 = input("Owner Name : ")
            to_add_vehicle = Vehicle(d1,d2,d7,d3,d4,d5,d6)
            vehicle.addvehicle(to_add_vehicle)
       elif choice == 4:
            to_delete_RegNo = int(input("Enter Reg No to delete : "))
            vehicle.Delete(to_delete_RegNo)
       elif choice == 5:
            to_modify_RegNo = int(input("Enter Reg No to Modify : "))
            to_modify_detail = int(input("Enter Model name : "))
            to_modify_CV = int(input("Enter Change Value to Modify : "))
            vehicle.Modify(to_modify_RegNo,to_modify_detail,to_modify_CV)
       elif choice == 6:
            vehicle.Save("vehicledata.pkl")
       elif choice == 7:
            vehicle.readfile("vehicledata.pkl")
       elif choice ==8:
            vehicle.filter()
       elif choice == 9:
            vehicle.report("report.pdf")
       elif choice == 10:
            Key = False
       else:
            print("Invalid option try again...")      
            
            
main()