number = int(input("Enter the three-digit number: "))
digit = int(input("Enter the digit: "))

digit1 = number // 100
digit2 = (number % 100) // 10
digit3 = number % 10

if digit == digit1 or digit == digit2 or digit == digit3:
  print(True)
else:
  print(False)
