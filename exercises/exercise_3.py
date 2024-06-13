# Your solution to Exercise 3
number = int(input("Enter the roulette number: "))

if number == 0:
  print("Green")
elif number > 0 and number <= 36:
  if number % 2 == 0:
    if number >= 11 and number <= 18 or number >= 29 and number <= 36:
      print("Red")
    else:
      print("Black")
  else:
    if number >= 1 and number <= 10 or number >= 19 and number <= 28:
      print("Red")
    else:
      print("Black")
else:
  print("The bet will not play!")
