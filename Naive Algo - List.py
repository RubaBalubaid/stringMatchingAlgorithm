# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 07:32:07 2023

@author: itzha
"""

#importing the necessary libraries 
import time
import pandas as pd 

#creating a dataframe that read data from the given file.
df = pd.read_csv("both_covid_data.csv")
df = df.astype(str)
# Join all the elements in each row with no separator.
df["joined_row"] = df.apply(lambda row: ''.join(row), axis=1)

 

 #Naive string matching algorithm to find patterns in data stored in a frame. 
start_time = time.perf_counter() 
def naive_string_match(dataframe, pattern): 

    # Initialize the matches list  
    matches = []  

    # Iterate over each row of the dataframe  
    for index, row in dataframe.iterrows():  

        # Iterate over each column of the row  
        for col in row:  

            # If pattern is found in the column value add it to matches list.  
            if pattern in str(col):  

                matches.append(index) 

    return matches 

#Pattern: 
pattern = '0010'    

matches = naive_string_match(df, pattern)    
print("Matches found at positions:", matches)   #Print the matches indices.

end_time = time.perf_counter()

#Calculating and printing the run time needed to search for a pattern match.
print("Time taken for implementing (Naive String Matching algorithm) using Array: ", end_time - start_time)
