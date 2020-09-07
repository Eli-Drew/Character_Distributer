"""
=======================================
Author:    Drew Rinker
Date:      09/06/20

This is an update to the original
character assigner program. This version
will utilize numpy and make a more efficient
version. Extra functionality being added will
be decided as the program is being built.
This program will address the input validation
issues that the first program had.
=======================================
"""
import random
import numpy as np

#================================================================
def readfile():
    """Reads a text file to populate characters.
        The text file has a certain format to adhere to."""
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

#================================================================
def character_assigner(lyst1, lyst2):
    """This function uses assigns charactes to people."""
    user_lyst = []
    
    

#================================================================
def print_list(lst):
    """Prints list in a desirable way."""
    delimiter = ""
    for x in lst:
        print(delimiter, x, end= " ")

#================================================================
def main():
    """Main function of program. Starting point."""
    char_list_A, char_list_B, char_list_C = readfile()
    
    random.shuffle(char_list_A)
    random.shuffle(char_list_B)
    random.shuffle(char_list_C)

    lenA = len(char_list_A)
    lenB = len(char_list_B)
    lenC = len(char_list_C)

    trackA = np.zeros(lenA)
    trackB = np.zeros(lenB)
    trackC = np.zeros(lenC)

    y = True
    while(y)
        try: 
            users = int(input("How many people are reading?: "))
            y = False
        except:
            print("That wasn't an integer. Please try again.\n")

    
        
    
