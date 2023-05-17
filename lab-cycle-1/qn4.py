def HappyCheck(num1):
  num2=num1

  for i in range(101):
    sum=0
    while num1>0:
      sum=sum+(num1%10)**2
      num1=num1//10
    
    num1=num2

    if sum==1:#checking if the input is happy or not
      print(num1,'is happy ')
      return True
      break  
    else:
      num1=sum

      
    if i==100:
      return False
      

  
#defining a function to produce happy numbers upto n limit
def produceUptoN(num):
  for i in range(1,num+1):
    HappyCheck(i)
      


#defining a function to produce happy numbers between the the two limits
def ProduceHappyNumbers(L_limit,U_limit):
  for i in range(L_limit,U_limit):
    HappyCheck(i)
    

print("******NUMBER HAPPY CHECK*****")
num=int(input('enter a number you want to check :'))
output=HappyCheck(num)
if output==False:
    print('not happy')

print("*****PRODUCING HAPPY NUMBER WITHIN A RANGE*****")
num1=int(input('enter the lower limit : '))
num2=int(input('enter the upper limit : '))
ProduceHappyNumbers(num1,num2)

print("*****PRODUCING UPTO A LIMIT*****")
num=int(input('enter a limit : '))
produceUptoN(num)