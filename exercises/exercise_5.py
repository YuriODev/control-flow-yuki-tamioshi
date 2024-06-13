a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
discriminant = b**2 - 4 * a * c
if discriminant > 0:
  root1 = (-b + discriminant**0.5) / (2 * a)
  root2 = (-b - discriminant**0.5) / (2 * a)
  print(f"{root1:.2f} and {root2:.2f}")
elif discriminant == 0:
  root = (-b + discriminant**0.5) / (2 * a)
  print(f"{root:.2f}")
else:
  print("No roots.")

