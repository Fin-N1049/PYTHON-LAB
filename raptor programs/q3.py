#converting days to years ,months and days(3)
d=int(input("enter the no of days"))
years=int(d/360)
ry=d%360
month=int(ry/30)
days=int(ry%30)
print("years are",years)
print("months are",month)
print("days are",days)


