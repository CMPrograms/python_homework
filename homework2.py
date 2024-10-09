# define the starting variables to use in the code, there is no average or sum at the start
sum = 0
average = 0

while sum < 100: # loop unless the sum is < 100
    try: # try to run this code as long as there is no error - ensure non-numeric values are dealt with
        user_number = float(input("Enter a number\n"))
        sum += user_number
        average += 1 # record the amount of loops the program has gone through to divide by later
        if sum >= 100: #if the sum >= 100 run this if statement, the loop will end after.
            print(f"Sum of all numbers is {sum}")
            num_avg = sum / average
            print(f"Average of all numbers is {num_avg}")
        else: # if we haven't met the 100 sum condition we print the current sum and loop again
           print(f"Current sum is {sum}")
    except ValueError: #if a non-number is entered as the user number then we inform them and rerun the code 
        print("Please enter a valid number!")
