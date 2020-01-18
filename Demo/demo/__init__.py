class Lakewood:
    Rating = 4
    Rewarded_C_Weekday = 80
    Rewarded_C_Weekend = 80
    Regular_C_weekday = 110
    Regular_C_weekend = 90
class Bridgewood:
    Rating = 5
    Rewarded_C_Weekday = 110
    Rewarded_C_Weekend = 50
    Regular_C_weekday = 160
    Regular_C_weekend = 60
class Ridgewood:
    Rating = 5
    Rewarded_C_Weekday = 100
    Rewarded_C_Weekend = 40
    Regular_C_weekday = 220
    Regular_C_weekend = 150

weekday = ["mon","tues","wed","thur","fri"]
weekend = ["sat","sun"]
str1,str3 = [x for x in input("Please enter: ").split(":")]
str4 = [x for x in str3.split(",")]
str2=[]

for i in str4:
    temp=i[10:]
    str2.append(temp[0:len(temp)-1])
price1,price2,price3=0,0,0
for i in str2:
    if i in weekday and str1=="Regular":
        price1 = price1+ Lakewood.Regular_C_weekday
        price2 = price2+ Bridgewood.Regular_C_weekday
        price3 = price3+ Ridgewood.Regular_C_weekday
    elif i in weekend and str1 == "Regular":
        price1 = price1 + Lakewood.Rewarded_C_Weekend
        price2 = price2 + Bridgewood.Rewarded_C_Weekend
        price3 = price3 + Ridgewood.Regular_C_weekend
    elif i in weekday and str1 == "Rewarded":
        price1 = price1 + Lakewood.Rewarded_C_Weekday
        price2 = price2 + Bridgewood.Rewarded_C_Weekday
        price3 = price3 + Ridgewood.Regular_C_weekday
    elif i in weekend and str1 == "Rewarded":
        price1 = price1 + Lakewood.Rewarded_C_Weekend
        price2 = price2 + Bridgewood.Rewarded_C_Weekend
        price3 = price3 + Ridgewood.Regular_C_weekend
dict1 = {price1:"Lakewood",price2:"Bridgewood",price3:"Ridgewood"}
val = min(dict1)
print(dict1[val])
if price1==price2:
    print("Bridgewood",price1)
elif price2==price3:
    print("Ridgewood",price2)
elif price1==price3:
    print("Ridgewood",price3)