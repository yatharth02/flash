#import datetime functionality for date function
from datetime import *

#main method which executes the code
def hotels(type,date):
    if type=='Regular':
        return Regular(date) #invoking regular method as date list argument
    else:
        return Rewards(date) #invoking rewards method as date list argument

#calculate rates for regular customer and return hotel name
def Regular(date):
    DayList=Days(date)
    Lakewood_sum=HotelPrice(DayList,110,90) #checking price as per the days for specific hotel
    Bridgewood_sum=HotelPrice(DayList,160,60) #checking price as per the days for specific hotel
    Ridgewood_sum=HotelPrice(DayList,220,150) #checking price as per the days for specific hotel
    return HotelName(Lakewood_sum, Bridgewood_sum, Ridgewood_sum) #returning hotel name as per the lowest price and rating format

#calculate rates for rewards customer and return hotel name    
def Rewards(date):
    DayList=Days(date)
    Lakewood_sum=HotelPrice(DayList,80,80) #checking price as per the days for specific hotel
    Bridgewood_sum=HotelPrice(DayList,110,50) #checking price as per the days for specific hotel
    Ridgewood_sum=HotelPrice(DayList,100,40) #checking price as per the days for specific hotel
    return HotelName(Lakewood_sum, Bridgewood_sum, Ridgewood_sum) #returning hotel name as per the lowest price and rating format

#check the min price for the hotels and return its name
def HotelName(Lakewood_sum,Bridgewood_sum,Ridgewood_sum):
    dict={'Ridgewood':Ridgewood_sum,'Bridgewood':Bridgewood_sum,'Lakewood':Lakewood_sum} #forming dictionary as per the rating order
    Min_price=min(Lakewood_sum,Bridgewood_sum,Ridgewood_sum) #calculating min price for hotels
    return (list(dict.keys())[list(dict.values()).index(Min_price)]) #with min price known, getting hotel name

#calculate the sum for the each hotel as per the days
def HotelPrice(DayList,num1,num2):
    return num1*int(DayList[0])+num2*int(DayList[1]) #calculating the sum as per the inputs

#checking the weekend and weekday days 
def Days(date):
    weekDay=0
    weekEnd=0
    DayList=[]
    for i in date: #iterating dates
        i=i[1:10] #getting date part as a string, ex 16Mar2019
        i=datetime.strptime(i, '%d%b%Y') #converting date string to datetime part i.e. 2019-03-16 00:00:00
        if i.isoweekday() in [1,2,3,4,5]: #checking is given date is weekend or weekday i.e. 1:monday, 2:tuesday.......7:sunday
            weekDay+=1
        else:
            weekEnd+=1
    DayList.append(weekDay) #appending weekday into the list
    DayList.append(weekEnd) #appending weekend into the list
    return(DayList)

#input format by customer and splitting into list by ':' as a delimiter
data=input("Enter the details").split(':')
#list at index 0 has customer type and trimming spaces
#list at index 1 has booking dates and splitting into list by ',' as a delimiter
print(hotels(data[0].strip(),data[1].split(',')))