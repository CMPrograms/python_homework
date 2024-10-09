import math 

def equation(): #Create a function called equation that we can call.
    solvingFor = input("What side are you solving for? Please enter a/b/c: ") #Ask what side the user needs to solve for and store it in a variable
    
    if solvingFor.lower() == "a": #check the variable to see if the user needs to solve for A then ask for the values of B and C.
        b = float(input("Please enter the number for B: "))
        c = float(input("Please enter the number for C: "))
        if b > c:   # Make sure code doesn't crash for mathematical impossibilities
            print("B cannot be greater than C")
            equation()
        elif b < 0: # only want to calculate positive numbers
            print("Please provide a positive number")
            equation()
        else:
            a = math.sqrt((c*c) - (b*b)) # Calculate side a by finding the square root of C squared minus B squared
            print("A = " + str(a)) 
            continueProgram()

    elif solvingFor.lower() == "b": #check the variable to see if the user needs to solve for B then ask for the values of A and C.
        a = float(input("Please enter the number for A: "))
        c = float(input("Please enter the number for C: "))
        if a > c: # mathmatical impossibility
            print("A cannot be greater than C")
            equation()
        elif a < 0: # only want to calculate positive numbers
            print("Please provide a positive number")
            equation()
        else:
            b = math.sqrt((c*c) - (a*a)) # Calculate side B by finding the square root of C squared minus A squared
            print("B = " + str(b)) 
            continueProgram()
    
    elif solvingFor.lower() == "c": #check the variable to see if the user needs to solve for C then ask for the values of A and B.
        a = float(input("Please enter the number for A: "))
        b = float(input("Please enter the number for B: "))
        if a < 0 or b < 0: # Only want to calculate in positive numbers
            print("Please provide a positive number.")
        else:
            c = math.sqrt((a*a)+(b*b))  # Calculate hypotenuse C by finding the square root of A squared plus B squared
            print("C = " + str(c)) 
            continueProgram()
    
    else : # If the variable solvingFor isn't a,b,c then run the the code.
        print("Error: Side", solvingFor, "is not a valid side. Please choose a,b,c") #error message if they don't choose a valid side for the equation
        equation() # Call the function again to receive a proper side.(This will continue until they choose A,B,C)
    
def continueProgram():
    continuePythag = input("Would you like to use this program again? (Y/N) ")
    if continuePythag.lower() == "y":
        equation()
    elif continuePythag.lower() == "n":
        exit()
    else:
        print("Please enter Y/N")
        continueProgram()

equation() # Call the function to begin the program.
