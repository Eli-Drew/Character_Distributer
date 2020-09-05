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
##from random import randint, shuffle
import random

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
def main():

    tier_A_characters = create_character_list("Tier A")
    tier_B_characters = create_character_list("Tier B")
    tier_C_characters = create_character_list("Tier C")

    users = int(input("How many people are reading?: "))


    #this for loop with give character lists for users
    for x in range(users):
        user_name = input("Enter the player's name: ")
        user_list_A, tier_A_characters = assign_characters(tier_A_characters, users)
        print(user_list_A)
        print()

        user_list_B, tier_B_characters = assign_characters(tier_B_characters, users)
        print(user_list_B)
        print()

        user_list_C, tier_C_characters = assign_characters(tier_C_characters, users)
        print(user_list_C)
        print()
                                    
        

main()
