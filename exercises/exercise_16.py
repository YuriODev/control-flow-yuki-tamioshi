day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
if day > 1:
    day -= 1
else:
    if month > 1:
        month -= 1
        if month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                day = 29
            else:
                day = 28
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            day = 31
        else:
            day = 30
    else:
        month = 12
        day = 31
        year -= 1
print(f"{day:02}.{month:02}.{year}")

