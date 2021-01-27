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
    valid_input = False

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

def assign_characters(character_list, num_chars, remainder):
    """This evenly distributes characters to users."""
    assigned_list = []
    
    #removes characters from original list once they're added to
    #the user. both lists are sent back.
    for x in range(num_chars):
        characters_left = len(character_list)
        if characters_left <= 0:
            break
        pop_index = random.randint(1,characters_left)
        character = character_list.pop(pop_index - 1)
        assigned_list.append(character)

    #handling uneven distribution of characters. 
    if remainder != 0:
        character = character_list.pop()
        assigned_list.append(character)
        remainder -= 1
            

    return assigned_list, character_list, remainder

def print_list(lst):
    """Prints list in a desirable way."""
    delimiter = ""
    for x in lst:
        print(delimiter, x)
        

def main():

    tier_A_characters, tier_B_characters, tier_C_characters = readfile()

    #shuffles list of characters
    random.shuffle(tier_A_characters)
    random.shuffle(tier_B_characters)
    random.shuffle(tier_C_characters)

    #keeps track of remainder and how many characters
    #each user gets. handles uneven distribution.
    users = int(input("How many people are reading?: "))
    amount_chars_A = (len(tier_A_characters)) // users
    remainder_A = (len(tier_A_characters)) % users
    index_A = 0
    
    amount_chars_B = (len(tier_B_characters)) // users
    remainder_B = (len(tier_B_characters)) % users
    index_B = 0
    
    amount_chars_C = (len(tier_C_characters)) // users
    remainder_C = (len(tier_C_characters)) % users
    index_C = 0
    

    #this for loop with give character lists for users
    for x in range(users):

        print("=" * 50)
        user_name = input("Enter the player's name: ")

        #sends orignial list and remainder number. returns user list and remainder
        user_list_A, tier_A_characters, remainder_A = assign_characters(tier_A_characters,
                                                           amount_chars_A,
                                                           remainder_A)
        print_list(user_list_A)

        
        #sends orignial list and remainder number. returns user list and remainder
        user_list_B, tier_B_characters, remainder_B = assign_characters(tier_B_characters,
                                                           amount_chars_B,
                                                           remainder_B)
        print_list(user_list_B)

        
        #sends orignial list and remainder number. returns user list and remainder
        user_list_C, tier_C_characters, remainder_C = assign_characters(tier_C_characters,
                                                           amount_chars_C,
                                                           remainder_C)
        print_list(user_list_C)
                                    

main()
