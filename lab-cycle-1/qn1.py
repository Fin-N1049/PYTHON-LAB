#creating a function to extract digits
def Sum_Of_Digits(number):
  sum=0
  rev=0
  while number>0:
    sum=sum+(number%10)
    number=number//10
  print('Sum : ',sum)



# creating a function to reverse a number
def ReverseOfNumber(number):
  reverse=0
  while number>0:
    reverse=reverse*10+(number%10)
    number=number//10
  print("Reverse : ",reverse)



#creating a functiom to calulate the difference between the product of digits at the odd and even pos
def diff(number):
  count=0
  OddProduct=1
  EvenProduct=1
  digit=0
  while number>0:
    digit=number%10
    number=number//10
    count+=1
    if count%2==0:
      OddProduct=OddProduct*digit
    else:
      EvenProduct=EvenProduct*digit
  print("difference : ",OddProduct-EvenProduct)


number=int(input("enter a four digit number : "))
Sum_Of_Digits(number)
ReverseOfNumber(number)
diff(number)