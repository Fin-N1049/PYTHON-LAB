
def Below10k(name,code,Bpay):
  DA=Bpay*(5/100)
  HRA=Bpay*(2.5/100)
  MA=500
  PT=20
  PF=Bpay*(8/100)
  GS=Bpay+DA+MA
  D=PT+PF
  salary=GS-D
  print("---------EMPLOYEE PAY LIST-------")
  print(' NAME :',name)
  print(' CODE  :',code)
  print(' BASIC PAY :',Bpay)
  print(' DEARNESS ALLOWANCE  :',DA)
  print(' HOUSE RENT ALLOWANCE  :',HRA)
  print(' MEDICAL ALLOWANCE  :',MA)
  print(' PROFESSIONAL TAX  :',PT)
  print(' PROVIDENT FUND  :',PF)
  print(' INCOME TAX  : 0 ')
  print(' GROSS SALARY : ',GS)
  print(' DEDUCTION  :',D)
  print(' NET SALARY :  ',salary)


def Below30k(name,code,Bpay):
  DA=Bpay*(7.5/100)
  HRA=Bpay*(5/100)
  MA=2500
  PT=60
  PF=Bpay*(8/100)
  GS=Bpay+DA+MA
  D=PT+PF
  salary=GS-D
  print("---------EMPLOYEE PAY LIST-------")
  print(' NAME :',name)
  print(' CODE  :',code)
  print(' BASIC PAY :',Bpay)
  print(' DEARNESS ALLOWANCE  :',DA)
  print(' HOUSE RENT ALLOWANCE  :',HRA)
  print(' MEDICAL ALLOWANCE  :',MA)
  print(' PROFESSIONAL TAX  :',PT)
  print(' PROVIDENT FUND  :',PF)
  print(' INCOME TAX  : 0 ')
  print(' GROSS SALARY : ',GS)
  print(' DEDUCTION  :',D)
  print(' NET SALARY :  ',salary)

def Below50k(name,code,BPay):
  DA=Bpay*(11/100)
  HRA=Bpay*(7.5/100)
  MA=5000
  PT=60
  PF=Bpay*(11/100)
  IT=Bpay*(11/100)
  GS=Bpay+DA+MA
  D=PT+PF+IT
  salary=GS-D
  print("---------EMPLOYEE PAY LIST-------")
  print(' NAME :',name)
  print(' CODE  :',code)
  print(' BASIC PAY :',Bpay)
  print(' DEARNESS ALLOWANCE  :',DA)
  print(' HOUSE RENT ALLOWANCE  :',HRA)
  print(' MEDICAL ALLOWANCE  :',MA)
  print(' PROFESSIONAL TAX  :',PT)
  print(' PROVIDENT FUND  :',PF)
  print(' INCOME TAX  : ' ,IT)
  print(' GROSS SALARY : ',GS)
  print(' DEDUCTION  :',D)
  print(' NET SALARY :  ',salary)

def Else(name,code,Bpay):
  DA=Bpay*(25/100)
  HRA=Bpay*(11/100)
  MA=7000
  PT=80
  PF=Bpay*(12/100)
  IT=Bpay*(20/100)
  GS=Bpay+DA+MA
  D=PT+PF+IT
  salary=GS-D
  print("---------EMPLOYEE PAY LIST-------")
  print(' NAME :',name)
  print(' CODE  :',code)
  print(' BASIC PAY :',Bpay)
  print(' DEARNESS ALLOWANCE  :',DA)
  print(' HOUSE RENT ALLOWANCE  :',HRA)
  print(' MEDICAL ALLOWANCE  :',MA)
  print(' PROFESSIONAL TAX  :',PT)
  print(' PROVIDENT FUND  :',PF)
  print(' INCOME TAX  :',IT)
  print(' GROSS SALARY : ',GS)
  print(' DEDUCTION  :',D)
  print(' NET SALARY :  ',salary)



name=input("Enter the employee's name : ")
code=input("Enter the employee's code : ")
Bpay=int(input("Enter the basic pay :"))

if Bpay>1000:
  Below10k(name,code,Bpay)

elif Bpay>10000 and Bpay<30000:
  Below30k(name,code,Bpay)

elif Bpay>30000 and Bpay<50000:
  Below50k(name,code,Bpay)

else:
  Else(name,code,Bpay)