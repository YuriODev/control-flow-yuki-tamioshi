number = int(input("Enter the three-digit number: "))

digit1 = number // 100
digit2 = (number % 100) // 10
digit3 = number % 10

sum_first_last = digit1 + digit3

if sum_first_last > digit2:
  print(">")
elif sum_first_last < digit2:
  print("<")
else:
  print("=")

