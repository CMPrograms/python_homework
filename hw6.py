import math 
import random

def get_number(str):
  user_number = None
  while user_number == None:
    try:
      user_number = int(input(str))
      return user_number
    except ValueError:
      print("Invalid Input!")



def factorize(number): 
  factors = []
  i = 1
  while i <= number:
    if number % i == 0:
      factors.append(i)
      i += 1
    else:
      i += 1
  return factors
  

def is_square(number):
    result = math.sqrt(number)
    if number % result == 0:
      return True
    else:
      return False

def increment(number):
  number += 1
  return number

numbers = []

for i in range(20):
  numbers.append(random.randrange(100))

print("The list of numbers is", numbers)


choice = None
while choice != "done":
  choice = input("Enter a command(factorize/square/quartile/increment/append/done): ").lower()
  if choice == "factorize":
    # Print out the prime factors of the number.
    number = get_number("Enter a number: ")
    print("The factors of the number are ", factorize(number))
  elif choice == "square":
    number = get_number("Enter a number: ")
    if is_square(number):
      print("The number is square")
    else:
      print("The number is not square")
  elif choice == "quartile":
    # Check what quartile the number fits into. (1-25, 25-50, 50-75, 75-100)
    x = get_number("Enter a number 1-100: ")
    if x > 100:
      print("Invalid Input")
    elif x >= 75:
      print("The number is in the fourth quartile")
    elif x >= 50:
      print("The number is in the third quartile")
    elif x >= 25:
      print("The number is in the second quartile")
    else:
      print("The number is in the first quartile")
  elif choice == "increment":
    # Increase the value of the number by 1.
    print(increment(get_number("Enter a number: ")))
  elif choice == "append":
    # Add a new number to the end of the list.
    numbers.append(get_number("Enter a number to add to the end of the list: "))
  elif choice != "done":
    print("Command not recognized.")
