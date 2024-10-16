def add_substitution(dictionary_name): #save the subsitutions in the input dictionary
    word1 = input("Please enter the word that will be replaced \n").lower()
    word2 = input("Please enter the word that will replace it. \n").lower()
    dictionary_name[word1] = word2

def describe_subsitutions(dictionary_name):
    for original in dictionary_name: # print out the key and value of the substitution dictionary for each substitution
        print(f"{original} => {dictionary_name[original]}")
    
def run_subsitutions(dictionary_name):
    user_input = str(input("Enter a sentence: \n")).lower() #gather the input string that will be replaced
    replace_list = user_input.split(" ") #turn the sentence into a list 
    for position, word in enumerate(replace_list): 
        #for each value in the list, if that value is in the substitution dictionary then replace that item in the list at the position with the value at the word key in the dictionary
        if word in dictionary_name:
            replace_list[position] = dictionary_name[word]
    return " ".join(replace_list) # turn the modified list back into a string and return it

replacement = {}

while True: #will loop through the options until the user types exit where we will break out of the loop and the program will end
    choice = input("Enter a command (add, describe, run, or exit): \n").lower()
    if choice == "add":
        add_substitution(replacement)
    elif choice == "describe":
        describe_subsitutions(replacement)
    elif choice == "run":
        print(f"The resulting sentence is: {run_subsitutions(replacement)}")
    elif choice == "exit":
        break
    else:
        print("Invalid option!")

