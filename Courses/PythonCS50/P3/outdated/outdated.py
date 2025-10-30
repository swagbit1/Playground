validMonths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
    
        user = input("Date: ")

        if '/' in user:
            month,day,year = user.split("/")
            
            if int(month) > 12 or int(day) > 31: continue
            if len(month) < 2:
                month = '0' + month
            
            if len(day) < 2:
                day = '0' + day

            
            
            print(f"{year}-{month}-{day}")
            break

        else:
            if ',' not in user: continue

            month, day, year = user.split(" ")

            if month not in validMonths or int(day[0:-1]) > 31: continue

            print(f"{year}-{'0' + str(validMonths.index(month) + 1) if validMonths.index(month) + 1 < 10 else validMonths.index(month) + 1}-{'0' + day[0:-1] if len(day[0:-1]) < 2 else day[0:-1]}")
            break
    except (ValueError, EOFError):
        print()
        pass
