#0506170835023100
#MoDyYrHrMnBinCap
#bin = "1106171335023035"
#Input
bin = input("Ready to recieve bin updates...")
                                                                                                                                #Slices out the dates
month = bin[0:2:1]
day = bin[2:4:1]
year = bin[4:6:1]
hour = bin[6:8:1]
minute = bin[8:10:1]
bin_num = bin[10:13:1]
capacity = bin[13:16:1]                                                                                                   #Creating the notification

#Time
hour = int(hour)
if hour < 12:
     time = str(hour) + ":" + str(minute) + " AM"
else:
    hour = hour - 12
    time = str(hour) +  ":" + str(minute) + " PM"

#Greeting
if "AM" in time:
    greeting = "Good morning!"
elif "PM" in time:
    greeting = "Good afternoon!"

#Date
    #Month Conversion
if int(month) == 1:
    month_word = "January"
elif int(month) == 2:
    month_word = "Febuary"
elif int(month) == 3:
    month_word = "March"
elif int(month) == 4:
    month_word = "April"
elif int(month) == 5:
    month_word = "May"
elif int(month) == 6:
    month_word = "June"
elif int(month) == 7:
    month_word = "July"
elif int(month) == 8:
    month_word = "August"
elif int(month) == 9:
    month_word = "September"
elif int(month) == 10:
    month_word = "October"
elif int(month) == 11:
    month_word = "November"
elif int(month) == 12:
    month_word = "December"
    
#CompleteYear
complete_year = "20" + str(year)
#Date in word form
if int(day) < 10:
    dayth = str(day).strip("0") + "th"
else:
    dayth = str(day) + "th"
#Set date
date = month_word + ", " + dayth + " " + complete_year

#Set bin locations
bin_num = str(bin_num).strip("0")
bin_num = int(bin_num)
if bin_num == 23:
    location = "2346 Rose Park"
#Available Capacity
if int(capacity) != 100:           #If not 100
    capacity = capacity[1:3:1]#Remove zeros before number

if int(capacity) != 100:
    available_capacity = 100 - int(capacity)
else:
    available_capacity = capacity

available_capacity = str(available_capacity) + "%"

#Status
status = available_capacity.strip("%")
if int(status) >50:
    status = " Time to pick up donations!"
else:
    status = " No need to pick up donations right now."

#Notification
notification = "{} Today is {}. The donation bin located at {}, has reported {} available capacity.{}".format(greeting, date,  location, available_capacity, status)
print(notification)


