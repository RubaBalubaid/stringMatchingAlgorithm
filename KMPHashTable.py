# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 18:24:23 2023

@author: rubah
"""


import time
import pandas as pd;

#start = time.process_time_ns() 
start_time = time.perf_counter()


"""
def readlist():   
    #opening the file in read mode
    myFile = open("both_covid_data.txt","r")
    text = []
    for i in myFile:
        text.append(str(i))  
    myFile.close()
    return text

text = readlist()
  """
  

def KMP(text, pattern): 
    n = len(text) 
    m = len(pattern) 

    # create a hash table to store the index of pattern 
    hash_table = [0] * 256

    # fill the hash table 
    for i in range(m): 
        hash_table[ord(pattern[i])] = i + 1

    # initialize lps array and variables 
    lps = [0] * m 
    j, i = 0, 0

    while i < n: 

    # if characters match, increment both pointers 
      if text[i] == pattern[j]: 
          i += 1
          j += 1

        # if j is equal to length of pattern, we have found a match.  
      if j == m:  
            print("Pattern found at index " + str(i-j))  

            # reset j to lps value  
            j = lps[j-1]  

        # mismatch after j matches  
      elif i < n and text[i] != pattern[j]:  

            # Do not match lps[0..lps[j-1]] characters, they will match anyway  
            if j != 0:  
                j = lps[j-1]  

            else:  
                i += 1

      return -1


def read_csv():                
    # Read the CSV file into a DataFrame
    df = pd.read_csv("both_covid_data.csv")
    df = df.astype(str)
    #print(len(df))
    # Join all the elements in each row with no separator
    df["joined_row"] = df.apply(lambda row: ''.join(row), axis=1)

    # Define the target string
    target = "0010"

    # Initialize a variable to store the result
    result = -1

    # Iterate through the joined_row column of the DataFrame
    for i, s in enumerate(df["joined_row"]):
    
        col=KMP(s,target)
        if col!=-1:
        # If a match is found, store the index in the result variable
            result = i
            break

    # Print the result
    if result != -1:
        print("Match found at index", result," at col",col)
    else:
        print("No match found.")
    
read_csv()



  
end_time = time.perf_counter()

print("Time taken in KMP hash table:", end_time - start_time)                

