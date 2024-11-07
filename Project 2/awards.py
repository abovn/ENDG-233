# awards.py
# ENDG 233 F21
# Fadi Haider
# A terminal-based program for analyzing movie awards data.
# You must include the code listed below. You may add your own additional functions, variables, etc. 
# You may not import any modules.
# You may only use built-in functions that directly support strings, lists, dictionaries, sets, and tuples.
# Remember to include docstrings for your functions and comments throughout your code.

# ******************************************************************************************************
# Data is imported from the included awards_data.py file. Both files must remain in the same directory.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any other data.
from awards_data import SAG, oscars, NBR, ISA, GLAAD, NAACP
award_list_names = ['sag', 'oscars', 'nbr', 'isa', 'glaad', 'naacp']
award_list_options = [SAG, oscars, NBR, ISA, GLAAD, NAACP]
# ******************************************************************************************************


# ******************************************************************************************************
# DEFINE FUNCTIONS HERE

def count_awards(movie_title):                                          # 
    """
    Counts the number of times a given movie title appears in a nested list of award options.

    Args:
        movie_title (str): The movie title to be counted.

    Returns:
        int: The number of times the given movie title appears in the award_list_options nested list.
    """
    win_count = 0                                                       # Creates a variable which allows me to count and output the total amount of awards won by the input
    for i in range(len(award_list_options)):                            # For an input nested list, the outer loop iterates over the list using the range function
        for k in range(len(award_list_options[i])):                     # The inner loop iterates over the indices of the nested lists within award_list_options using the range function. The code snippet accesses the elements of award_list_options using the indices i and k
            simplified_movie_title = award_list_options[i][k].lower()   # By lowering the movie title in the list, I can match the input with the titles in the list
            if movie_title == simplified_movie_title:                   # Therefore if the simplified (input) movie title matches a simplified name in awards_data.py, the count will add 1 to the total awards won
                win_count += 1
    return win_count                                                    # Returns an integer output for the total amount of awards won for an input movie (movie_title)


def print_award_winners(award_choice):
    '''
    Print the movie titles in the chosen award category.

    Args:
        award_choice (str): The chosen award category.

    Returns:
        None
    '''
    if award_choice in award_list_names:                                                # If the user inputted list is valid (included in awards_data.py), then continue
        for movie_title in award_list_options[award_list_names.index(award_choice)]:    # Searches for the chosen movie in the awards list
            print(movie_title)                                                          # Prints what it has found in list
                                      
# ******************************************************************************************************
print("ENDG 233 Awards Data Program")

# Prompt the user to input the following information
menu_option = int(input('\nSelect 1 to search a specific movie, 2 to print specific rewards results, 0 to end: '))                              # Assigns int and variable name to usre input, allowing them to navigate the menu

while menu_option != 0:                                                                                                                         # Creates a while loop, looping the function until 0 is inputted
    if menu_option == 1:                                                                                                                        
        movie_title = input('Please enter the movie title you would like to search: ').strip().lower()                                          # Removes external spaces, assigns a variable name and lowers the user input so that it can be matched with list
        print(f'--Number of Awards Won--\n{count_awards(movie_title)}')                                                                         # Large blanket print statement which calls function count_awards, and applies it to the input for the 
    
    elif menu_option == 2:
        award_choice = input('\nPlease choose one of the following awards lists:\nOscars\nSAG\nNBR\nISA\nGLAAD\nNAACP\n\n').strip().lower()     # Assigns the input to a variable and strips and lowers the string so it can match with the given list in awards_data.py
        if award_choice in award_list_names:                                                                                                    # If statement that carries out function if there is a match
            print('--Requested Award Winners--')
            print_award_winners(award_choice)                                                                                                   # Carries out the print_award_winners function, which prints all the winners in a given category, which is inputted by the user
        else:
            print('Awards list not found.')                                                                                                     # Catch-all for invalid input
    
    else:
        print('You must select either 1, 2, or 0.')                                                                                             # Catch-all for invalid input
    menu_option = int(input('\nSelect 1 to search a specific movie, 2 to print specific rewards results, 0 to end: '))                          # Loops back to the main menu, sending the user back to the start of the while loop

print('Thank you for using the awards data program.')                                                                                           # Final print statement when input = 0

exit
