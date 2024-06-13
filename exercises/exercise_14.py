number = int(input("Enter the four-digit number: "))

digit1 = number // 1000
digit2 = (number % 1000) // 100
digit3 = (number % 100) // 10
digit4 = number % 10

if digit1 == digit4 and digit2 == digit3:
  print(True)
else:
  print(False)

