import re
import sys


def main():
    print(convert(input("Hours: ")))

#00:00
#9:00 AM to 5:00 PM
#9 AM to 5 PM
#9:00 AM to 5 PM
#9 AM to 5:00 PM

def convert(s):
    match = re.search(r"^(1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM)$",s)
        # the hours are 10-12 or 1-9 respectively, above restrics values like 13 for a 12 hr clock
        # next is getting minuts, since : is outside, not caputred in group, but minuts is () inside so caputred as group
        #that whole thing also is optional hence ? outside it all
        # AM an PM directly instead of [A-Z][A-Z] which allows for valies like ZZ, extra check we have to do
        # the ^ $ only caputres the exact syntax we seek for 
    convertedTime = ""

    if not match:
        raise ValueError("Invalid Input")

    first, last = match.group().strip().split('to')
    first = first.strip().replace(" ", "")
    last = last.strip().replace(" ", "")

    if 'AM' in first:
        if ':' in first:
            hr, min = first.split(":") # split if colon included to mins and hrs
            if hr == "12": #12 AM means 00 for 24 hrs
                hr = "00"
            #convertedTime += hr + ":" + min[0:-2] # remove the AM
            convertedTime += f"{int(hr):02}:{int(min[0:-2]):02}" 
            # format values so that 9 am becomes 09:00 am, ensures leading zeros for single values

        else:
            hr = first[0:-2]
            if hr == "12":
                hr = "00"
            #convertedTime += hr + ":00"
            convertedTime += f"{int(hr):02}:00"
    elif "PM" in first:
        if ':' in first:
            hr, min = first.split(":")
            if not hr == "12": # add only if hr is not 12 other since 12 Pm is 12 in 24 hr
                hr = int(hr) + 12
            convertedTime += str(hr) + ":" + min[0:-2]
        else:
            if last[0:-2] == "12": # same thing here, 12 is a edge case
                convertedTime += str(int(last[0:-2])) + ":00"
            else:
                convertedTime += str(int(last[0:-2]) + 12) + ":00"

    convertedTime += " to "

    if 'AM' in last:
        if ':' in last:
            hr, min = last.split(":")
            if hr == "12":
                hr = "00"
            #convertedTime += hr + ":" + min[0:-2] # remove the AM
            convertedTime += f"{int(hr):02}:{int(min[0:-2]):02}"
        else:
            hr = last[0:-2]
            if hr == "12":
                hr = "00"
            #convertedTime += hr + ":00"
            convertedTime += f"{int(hr):02}:00"
    elif "PM" in last:
        if ':' in last:
            hr, min = last.split(":")
            if not hr == "12":
                hr = int(hr) + 12
            convertedTime += str(hr) + ":" + min[0:-2]
        else:
            if last[0:-2] == "12":
                convertedTime += str(int(last[0:-2])) + ":00"
            else:
                convertedTime += str(int(last[0:-2]) + 12) + ":00"

    return convertedTime





if __name__ == "__main__":
    main()

# Bettter way of doing it using regex and it's groups
# reduces redudentent code

# import re

# def convert(s):
#     # Regex: capture start and end hours, optional minutes, and AM/PM
#     pattern = r"^(1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM)$"
#     match = re.search(pattern, s)

#     if not match:
#         raise ValueError("Invalid time format")

#     def to_24_hour(hour_str, minute_str, ampm):
#         hour = int(hour_str)
#         minute = int(minute_str) if minute_str else 0

#         # Convert AM/PM to 24-hour format
#         if ampm == "AM":
#             hour = 0 if hour == 12 else hour
#         else:  # PM
#             hour = hour if hour == 12 else hour + 12

#         # Format with leading zeros
#         return f"{hour:02}:{minute:02}"

#     # Start time (groups 1,2,3)
#     start_time = to_24_hour(match.group(1), match.group(2), match.group(3))
#     # End time (groups 4,5,6)
#     end_time = to_24_hour(match.group(4), match.group(5), match.group(6))

#     return f"{start_time} to {end_time}"
