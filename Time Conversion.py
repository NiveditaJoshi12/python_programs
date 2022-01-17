# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

current_time = input("Enter current time in 12 hr format: ")

if current_time[:2] == "12" and current_time[-2:] == "AM":
      print("00:" + current_time[3:8])

elif current_time[-2:] == "AM":
    print(current_time[:-2])

elif current_time[-2:] == "PM" and current_time[:2] != "12":
    print(str(int(current_time[:2])+12) + current_time[2:8])

else:
    print(current_time[:-2])




