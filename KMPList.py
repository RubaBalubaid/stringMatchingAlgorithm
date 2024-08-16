# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 21:30:34 2023

@author: ruba balubaid
"""


"""
Definition for variables and methods in code:
    
- myFile: is a file to read
- text: array to store information from a file
- readlist(): to read a txt file
- KMP(text, pattern): to take array and pattren
- n,m: to calculate length
- lps: longest proper prefix will hold the longest prefix suffix values for pattern 
- read_csv(): to convert csv file to data frame and read it

"""

# we use array data strcture in KMP algorithm

import time;
import pandas as pd;


start_time = time.perf_counter()

# Code to be timed


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


def KMP(pat, txt):
    M = len(pat)
    N = len(txt)
 
    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0]*M
    j = 0  # index for pat[]
 
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
 
    i = 0  # index for txt[]
    while (N - i) >= (M - j):
        if pat[j] == txt[i]:
            i += 1
            j += 1
 
        if j == M:
            print("Found pattern at index " + str(i-j))
            j = lps[j-1]
 
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
                
 
def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix
 
    lps[0] = 0 # lps[0] is always 0
    i = 1
 
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]
 
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
 
      
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
    
        col=KMP(target, s)
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

print("Time taken in KMP list:", end_time - start_time)
              

"""
other way to calculate time and read a data

start = time.process_time_ns()                 

KMP(text, "1,1,0,0,1,1,1,1,0,1,1")

print(time.process_time())

"""


