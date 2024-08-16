# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 22:45:24 2023

@author: itzha
"""

#importing pandas library 
import pandas as pd 
import time 

#creating a dataframe that read data from the given file.
df = pd.read_csv("both_covid_data.csv")
df = df.astype(str)
#Join all the elements in each row with no separator
df["joined_row"] = df.apply(lambda row: ''.join(row), axis=1)


  
#creating a hash table, and storing the data from the dataframe in.
hash_table = {df.index[i] : df.joined_row[i] for i in range(len(df))}



#creatin a hash table (for the pattern.)
table = {}

#method to create a hash table of all the substrings of the pattern.
def createHashTable(pattern): 
    m = len(pattern) 
    for i in range(m): 
        table[pattern[i:i+1]] = i 
  
 
start_time = time.perf_counter() 

#method to search for all occurrences of the pattern in the given text (data in the hash table) using Naive String Matching Algorithm.
def searchPattern(text, pattern): 
    n = len(text) 
    m = len(pattern)  

    #Create a hash table for pattern  
    createHashTable(pattern)  

    # Traverse through the text (data from the hash table) 
    for i in range(n-m+1):  

        # For current index i, check for pattern match  
        j = 0;  

        while j < m:  

            # If characters don't match, break the loop and move to next index in text.  
            if text[i + j] != pattern[j]:  

                break;  

            j += 1;  

            # If *all* characters are matched, print the index at which it is found.    
            if j == m:    

                print("Pattern found at index", i);    



#Pattern: 
pattern = '0010'

#A loop to traverse the data elements in the hash table, and search in each for a pattern matching.
for key, value in hash_table.items():
    searchPattern(value, pattern)



end_time = time.perf_counter()

#Calculating and printing the run time needed to search for a pattern match.
print("Time taken for implementing (Naive String Matching algorithm) using Hash Table:", end_time - start_time)
  



    