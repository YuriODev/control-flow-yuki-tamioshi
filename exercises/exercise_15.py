day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
  days_in_month[1] = 29

if day < days_in_month[month - 1]:
  day += 1
elif day == days_in_month[month - 1] and month < 12:
  day = 1
  month += 1
else:
  day = 1
  month = 1
  year += 1

print(f"{day:02}.{month:02}.{year}")

