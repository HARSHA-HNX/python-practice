# Menu Driven Program

while True:
  print("\n1. Sum")
  print("2. Even/Odd")
  print("3. Factorial")
  print("4. Table")
  print("5. Reverse")
  print("6. Exit")

  choice = int(input("Enter your choice: "))

  if choice == 1:
      a = int(input("Enter first number: "))
      b = int(input("Enter second number: "))
      print("Sum is:", a + b)

  elif choice == 2:
      num = int(input("Enter number: "))
      if num % 2 == 0:
          print("Even")
      else:
          print("Odd")

  elif choice == 3:
      num = int(input("Enter number: "))
      fact = 1
      for i in range(1, num + 1):
        fact *= i
      print("Factorial:", fact)

  elif choice == 4:
      num = int(input("Enter number: "))
      for i in range(1, 11):
          print(num, "x", i, "=", num * i)

  elif choice == 5:
      num = int(input("Enter number: "))
      rev = 0
      while num > 0:
          digit = num % 10
          rev = rev * 10 + digit
          num //= 10
      print("Reverse:", rev)

  elif choice == 6:
      break

  else:
      print("Invalid choice")
