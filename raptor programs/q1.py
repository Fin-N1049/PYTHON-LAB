#converting seconds into hours,minutes and seconds(1)
s=int(input("enter time in seconds"))
hours=int(s/3600)
rh=s%3600
minutes=int(rh/60)
rm=int(rh%60)
print("hours=",hours)
print("minutes=",minutes)
print("seconds=",rm)