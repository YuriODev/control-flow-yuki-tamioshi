day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
  days_in_month[1] = 29
if day > 1:
  day -= 1
elif month > 1:
  day = days_in_month[month - 2]
  month -= 1
else:
  day = 31
  month = 12
  year -= 1
print(f"{day:02}.{month:02}.{year}")

