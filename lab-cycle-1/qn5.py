#to print all the substrings of a string numbers

def subStrings(string):
  for i in range(len(string)):
    for j in range(len(string)+1):
      print(string[i:j])


def stringLenK(string,length):
  for i in range(len(string)):
    for j in range(len(string)+1):
      sub_string=string[i:j]
      if len(sub_string)==length:
        print(sub_string)


def distinctString(string,No_of_Distinct_char):
  for i in range(len(string)):
    for j in range(len(string)+1):
      sub_string=string[i:j]
      distinct=set(sub_string)
      if len(distinct)==No_of_Distinct_char:
        print(sub_string)

def palindromeStrings(string):
  for i in range(len(string)):
    for j in range(len(string)+1):
      sub_string=string[i:j]
      if sub_string==sub_string[::-1]:
        print(sub_string)

def Distinct_Len_and_Char(string,len_of_string,Distinct_char):
  for i in range(len(string)):
    for j in range(len(string)+1):
      sub_string=string[i:j]
      if len(sub_string)==len_of_string:
        distinct=set(sub_string)
        if len(distinct)==Distinct_char:
          print(sub_string)

      
name=input("enter a string : " )
subStrings(name)

num1=int(input("enter length : "))
stringLenK(name,num1)

num2=int(input("enter number of distinct character :"))
distinctString(name,num2)

print("palendrome strings ")
palindromeStrings(name)

num3=int(input("enter the length : "))
num4=int(input("enter number of distinct character :"))
Distinct_Len_and_Char(name,num3,num4)