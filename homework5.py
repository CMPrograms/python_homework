def add_substitution(dictionary_name):
    word1 = input("Please enter the word that will be replaced \n").lower()
    word2 = input("Please enter the word that will replace it. \n").lower()
    dictionary_name[word1] = word2

def describe_subsitutions(dictionary_name):
    for original in dictionary_name:
        print(f"{original} => {dictionary_name[original]}")
    
def run_subsitutions(dictionary_name):
    user_input = str(input("Enter a sentence: \n")).lower()
    replace_list = user_input.split(" ")
    for position, word in enumerate(replace_list):
        if word in dictionary_name:
            replace_list[position] = dictionary_name[word]
    return " ".join(replace_list)

replacement = {}

while True:
    choice = input("Enter a command (add, describe, run, or exit): \n").lower()
    if choice == "add":
        add_substitution(replacement)
    elif choice == "describe":
        describe_subsitutions(replacement)
    elif choice == "run":
        print(run_subsitutions(replacement))
    elif choice == "exit":
        break
    else:
        print("Invalid option!")

