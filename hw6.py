import math 
import random

def get_number():
  user_number = None
  while user_number == None:
    try:
      user_number = int(input(f"Enter an integer: "))
      return user_number
    except ValueError:
      print("Invalid Input!")

def get_index(list1):
  while True:
    try:
     index = get_number()
     list1[index] = list1[index]
     return index
    except IndexError:
      print("Invalid Index Number")

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


def increment(list1):
  choice = get_index(list1)
  list1[choice] += 1
  return list1[choice]

numbers = []

for i in range(20):
  numbers.append(random.randrange(100))




choice = None
while choice != "done":
  print("The list of numbers is", numbers)
  choice = input("Enter a command(factorize/square/quartile/increment/append/done): ").lower()

  if choice == "factorize":
    # Print out the prime factors of the number.
    factors =  factorize(numbers[get_index(numbers)])
    print(f"The factors of the number are {factors}")

  elif choice == "square":
    number = numbers[get_index(numbers)]
    if is_square(number):
      print("The number is square")
    else:
      print("The number is not square")

  elif choice == "quartile":
    # Check what quartile the number fits into. (1-25, 25-50, 50-75, 75-100)
    x = numbers[get_index(numbers)]
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
    increment(numbers)

  elif choice == "append":
    # Add a new number to the end of the list.
    numbers.append(get_number())

  elif choice != "done":
    print("Command not recognized.")
