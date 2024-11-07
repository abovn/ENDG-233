# spotify_program.py
# Fadi Haider, ENDG 233 F23
# A terminal-based application to process and plot data based on given user input and provided data values.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

import numpy as np
import matplotlib.pyplot as plt
import math

# ******************************************************************************************************
# Data is imported from the included csv file. You may not modify the content, order, or location of the csv file.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any other data.
column_names = ['title', 'artist(s)', 'release', 'num_of_streams', 'bpm', 'key', 'mode', 'danceability', 'valence', 'energy', 'acousticness', 'instrumentalness', 'liveness', 'speechiness']
data = np.genfromtxt(r'C:\Users\haide\OneDrive\Desktop\University\Fall 2023\ENDG 233\Portofolio Project 3\spotify_data.csv', delimiter = ',', skip_header = True, dtype = str)
# ******************************************************************************************************

# ******************************************************************************************************
# DEFINE BONUS CLASS HERE (optional)
class Song: 
    """
    A class representing a song object.
    
    Args:
        data_row (list): A list containing the data for a song, including the title, artist, date, number of streams, BPM, key, mode, danceability, valence, energy, acousticness, instrumentalness, liveness, and speechiness.
    
    Attributes:
        title (str): The title of the song.
        artist (str): The artist of the song.
        date (str): The date of the song.
        num_of_streams (float): The number of streams of the song.
        bpm (float): The BPM (beats per minute) of the song.
        key (str): The key of the song.
        mode (float): The mode of the song.
        danceability (float): The danceability score of the song.
        valence (float): The valence score of the song.
        energy (float): The energy score of the song.
        acousticness (float): The acousticness score of the song.
        instrumentalness (float): The instrumentalness score of the song.
        liveness (float): The liveness score of the song.
        speechiness (float): The speechiness score of the song.
        percentages (list): A list of percentages related to the song attributes.
    """
    def __init__(self, data_row):
        self.title = str(data_row[0])
        self.artist = str(data_row[1])
        self.date = float(data_row[2])
        self.num_of_streams = float(data_row[3])
        self.bpm = float(data_row[4])
        self.key = str(data_row[5])
        self.mode = str(data_row[6])
        self.danceability = float(data_row[7])
        self.valence = float(data_row[8])
        self.energy = float(data_row[9])
        self.acousticness = float(data_row[10])
        self.instrumentalness = float(data_row[11])
        self.liveness = float(data_row[12])
        self.speechiness = float(data_row[13])

# ******************************************************************************************************
# DEFINE FUNCTIONS HERE

def feature_stats(input_value):
    """
    Calculate the highest value, lowest value, and mean value of a desired song feature from a given dataset.

    Args:
        input_value (int): An integer representing the index of the desired song feature in the dataset.

    Returns:
        int: The index of the maximum value in the converted data.

    Example:
        feature_stats(3)
        This code will calculate the highest value, lowest value, and mean value of the song feature at index 3 in the dataset.
    """
    converted_data = np.array([row[input_value] for row in data], dtype='float')        # Assigns name converted_data to array created from csv

    list_min = converted_data.min()                                                     # Finds min value from given column
    list_max = converted_data.max()                                                     # Finds max value from given column
    mean_value = math.floor(np.mean(converted_data))                                    # Finds the avg value from given column, and uses (math.floor) to round down 
    
    print(f'Highest Value: {list_max:.0f}')                                             # Prints Highest Value
    print(f'Lowest Value: {list_min:.0f}')                                              # Prints Lowest Value
    print(f'Mean Value: {mean_value}')                                                  # Prints Mean Value
    
    max_value = converted_data.argmax()                                                 # Finds Index of the max value from given column
    top_song = data[max_value][0]                                                       # Uses the Index to find title from cloumn 0
    
    print(f'Top song in selected feature: {top_song}')                                  # Prints from referenced variable

    return max_value

def age_stats(input_value):
    """
    Calculate the span of years between the release of the oldest and newest songs in a dataset.
    Identify the artist, key, and mode of the oldest song.

    Parameters:
    input_value (int): The column index of the dataset to analyze.

    Returns:
    None

    Example Usage:
    age_stats(2)

    This code will calculate the span of years, artist, key, and mode of the oldest song in the dataset based on the input value of 2.
    """

    converted_data = np.array([row[input_value] for row in data], dtype='float')

    min_year = converted_data.min()                                                     # Finds min in column
    max_year = converted_data.max()                                                     # Finds max in column
    
    min_value = converted_data.argmin()                                                 # Finds Index of min (oldest song)
    
    year_span = max_year - min_year                                                     # Calculates the difference between the release years of the newest and oldest songs
    
    oldest_artist = data[min_value][1]                                                  # Uses the index value and column of the artist to find the artist of the oldest song 
    oldest_key = data[min_value][5]                                                     # Uses the index value and column of the key to find the key of the oldest song
    oldest_mode = data[min_value][6]                                                    # Uses the index value and column of the mode to find the mode of the oldest song
    
    print(f'Span of years: {year_span:.0f}')                                            # Prints the difference between the release years of the oldest and newest songs   
    print(f'Artist of the oldest song: {oldest_artist}')                                # Prints the artist of the oldest song
    print(f'Keys and mode of the oldest song: {oldest_key} {oldest_mode}')              # Prints the mode and key of the oldest song in the same line
                                                                                  
# ******************************************************************************************************
# DEFINE MAIN CODE
# Add your code within the main function. A docstring is not required for this function.

# You may find the following hints helpful:
# A list comprehension can be used to convert data values in a column and create a new array
# e.g. converted_data = np.array([row[column_value] for row in data], dtype='float')
# NumPy has many built-in functions/methods, including those for finding the index location of a value (e.g. argmax(), argmin(), etc.)
# Refer to the NumPy and Matplotlib documentation for more


def main():
    print("ENDG 233 Spotify Statistics\n")
    print("Song analysis options: ")
    for menu, option in enumerate(column_names):
        print(menu, option)
    print("Choose -1 to end the program.")

# Continue main code below
    process_list = [3,4,7,8,9,10,11,12,13]                                              # List of inputs to process using function feature_stats
    nothing_list = [0,1,5,6]                                                            # List of inputs to pass
    
    menu_boolean = 1                                                                    # Sets the menu boolean to 1 (true)
    # Utilize variable instead of (while menu_boolean != to avoid redundancy and use of excess repetition of input statement
    while menu_boolean == 1:                                                            # Creates a while loop that repeats until the value of the variable is changed (therefore ending the loop)
        menu_option = int(input('\nPlease enter a song feature to analyze: '))          # Request user input, casts as int, and assigns to variable
        
        if menu_option in nothing_list:                                                 # If input is in invalid column     
            pass                                                                        # Skips, goes back to loop, as menu_boolean remains unchanged
        elif menu_option == 2:                                                          # If input is 2, execute following
            age_stats(menu_option)                                                      # Utilize the age_stats to find the oldst song
        elif menu_option in process_list:                                               # If menu option is to be processed by feature_stats (in list process_list)
            feature_stats(menu_option)                                                  # Uses the feature_stats function to output values for the details of songs and print them based on input
        elif menu_option == -1:                                                         # If user inputs -1
            menu_boolean = 0                                                            # Change menu_boolean to false, exiting the while loop and going to the next part of the code
        else:
            print('You must enter a valid menu option.')                                # Catch-all for invalid input

    #Create and print danceability vs. bpm plot

    x = np.array([row[4] for row in data], dtype = int)                                 # Assigns x and casts int to a 1-D numpy array created from coumn 4 
    y = np.array([row[7] for row in data], dtype = int)                                 # Assigns y and casts int to a 1-D numpy array created from coumn 7

    plt.scatter(x, y, color='b', label='Song stats')                                    # Plots the data points
    plt.title('Danceability vs Beats per Minute')                                       # Set the title
    plt.xlabel('BPM')                                                                   # Label for the x-axis
    plt.ylabel('Danceability')                                                          # Label for the y-axis
    plt.legend()                                                                        # Show legend
    plt.grid(False)                                                                     # Set grid to false
    plt.show()                                                                          # Show the plot

    # Create bonus Song object (optional)

    input_int = int(input('Bonus - Enter any row number: '))                            # Takes input from user, assigns int
    input_row_title = data[input_int][0]                                                # Locates title in csv, assings variable
    input_row = data[input_int]                                                         # Finds the row for the provided song

    input_song = Song(input_row)                                                        # Uses class to find values from list, assigns input_song

    # Defines the x and y axes
    categories = ['danceability','valence','energy','acousticness','instrumentalness','liveness','speechiness']
    percentages = [input_song.danceability, input_song.valence, input_song.energy, input_song.acousticness, input_song.instrumentalness, input_song.liveness, input_song.speechiness]

    # Create and print bonus plot (optional)
    plt.bar(categories, percentages, color='b')                                         # Creates a bar graph using matplotlib with x and y axes assignes, and colour blue
    plt.title(f'Song Stats for {input_row_title}')                                      # Creates a title based on the title of the song from the input row
    plt.xlabel('Features')                                                              # Assign x-label
    plt.ylabel('Values')                                                                # Assign y-label
    plt.ylim(0, 100)                                                                    # Scales the graph from 0-100 (shows percent score)
    plt.yticks([0,10,20,30,40,50,60,70,80,90,100])                                      # Sets the scale for the y-axis from 0-100 in increments of 10
    plt.show()                                                                          # Shows plot

if __name__ == '__main__':
    main()
