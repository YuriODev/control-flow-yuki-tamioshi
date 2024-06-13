grade = int(input("Enter the school grade: "))

if grade >= 1 and grade <= 3:
  print("initial level")
elif grade >= 4 and grade <= 6:
  print("average level")
elif grade >= 7 and grade <= 9:
  print("sufficient level")
elif grade >= 10 and grade <= 12:
  print("high level")
else:
  print("level is absent")

