#fibanocci series
fterm=0
lterm=1
sum=1

Input=int(input(" enter months : " ))
print("","_"*20)
print("   month  |  pairs\n",("_"*20))

if Input==1:
  print(lterm)
elif Input==2:
  print("  ",1,"     |  ",1,"\n",("_"*20))
  print("  ",2,"     |  ",1,"\n",("_"*20))
else:
  for i in range(1,Input+1):
    sum=fterm+lterm
    print("  ",i ,"     |  ",sum,"\n",("_"*20))
    lterm=fterm
    fterm=sum
{\rtf1}