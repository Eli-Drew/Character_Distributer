"""
======================================
Author:     Drew Rinker
Date:       09/04/20

This program assings characters to
readers. It still needs some input
validation and testing. (Min number
of characters, numbers vs strings, etc)

======================================
"""
import random
    

def readfile():
    """Reads a text file to populate characters."""

    character_lists = [[],[],[]]
    
    file = input("Enter the movie text file you want to use: ")
    f = open(file + ".txt" , 'r')

    list_name = 0
    
    for line in f:
        line = line.strip()
        if line == "Tier A":
            continue
        elif line == "Tier B":
            list_name = 1
            continue
        elif line == "Tier C":
            list_name = 2
            continue
        elif line == '':
            continue
        else:
            character_lists[list_name].append(line)

    return character_lists[0], character_lists[1], character_lists[2]
        

def create_character_list(tier_letter):
    """This function populates a list with characters
        with user input."""
    
    print("This is for tier " + tier_letter)
    user_continue = True
    character_list = []
    
    while(user_continue):
        new_character = input("Enter the character's name: ")

        character_list.append(new_character)
        print(character_list)
        
        user_answer = input("Any more characters? (y/n): ")

        #input validation
        while (user_answer not in ["y","n"]):
            print("Invalid input. Please enter 'y' or 'n'")
            user_answer = input("Any more characters? (y/n): ")
        
        if (user_answer == "y"):
            user_continue = True
        else:
            user_continue = False

        
    print()
    return character_list

def assign_characters(character_list, users):
    """This evenly distributes characters to users"""
    assigned_list = []
    #random.shuffle(character_list)
    
    num_of_characters = len(character_list) // users
    remainder = len(character_list) % users
    if remainder != 0:
        num_of_characters += 1

    for x in range(num_of_characters):
        pop_index = random.randint(0,len(character_list) -1)
        character = character_list.pop(pop_index)
        assigned_list.append(character)

    return assigned_list, character_list

def print_list(lst):
    """Prints list in a desirable way."""
    delimiter = ""
    for x in lst:
        print(delimiter, x)
        

def main():

    tier_A_characters, tier_B_characters, tier_C_characters = readfile()

##    tier_A_characters = create_character_list("Tier A")
##    tier_B_characters = create_character_list("Tier B")
##    tier_C_characters = create_character_list("Tier C")
##    print(tier_A_characters)
##    print()
##
##    print(tier_B_characters)
##    print()
##
##    print(tier_C_characters)
##    print()

    users = int(input("How many people are reading?: "))


    #this for loop with give character lists for users
    for x in range(users):

        print("=" * 50)
        user_name = input("Enter the player's name: ")
        #fix math for character distribution
        user_list_A, tier_A_characters = assign_characters(tier_A_characters, users)
        print_list(user_list_A)

        user_list_B, tier_B_characters = assign_characters(tier_B_characters, users)
        print_list(user_list_B)

        user_list_C, tier_C_characters = assign_characters(tier_C_characters, users)
        print_list(user_list_C)
                                    

main()
