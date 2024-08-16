# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 07:24:49 2023

@author: ruba balubaid
"""

"""
Definition for variables and methods in code:
    
- myFile: is a file to read
- text: array to store information from a file
- readlist(): to read a txt file
- KMP(text, pattern): to take array and pattren
- n,m: to calculate length
- lps: will hold the longest prefix suffix values for pattern 
"""

# linked list data strcture code
import time
import pandas as pd;

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
# Python program for KMP Algorithm using Linked List 
  
# A linked list node 
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
  
def KMPSearch(pat, txt): 
    M = len(pat) 
    N = len(txt) 

    # create linked list of pattern characters  
    head1 = Node(None) # dummy node to mark beginning 
    prev = head1 

    for i in range(M):  

        # create a new node for every character of pattern  
        curr = Node(pat[i])  

        # append the new node at the end of linked list  
        prev.next = curr  

        # update previous pointer to current node  
        prev = curr

    # create linked list of text characters  
    head2 = Node(None) # dummy node to mark beginning 
    prev = head2 

    for i in range(N):  

        # create a new node for every character of text  
        curr = Node(txt[i])  

        # append the new node at the end of linked list  
        prev.next = curr  

        # update previous pointer to current node  
        prev = curr

    i, j, count= 0, 0, 0

    while i < N: 
        # if characters match then move ahead in both lists 
        if (head2.data == head1.data):
            count += 1 
            i += 1 
            j += 1
            head2=head2.next 
            head1=head1.next 
        else: 
            if (j != 0): 
                j=0 
            else: 
                i+=1 
                head2=head2.next 
            if (count == M): 
                return True 
            return False 
    count += 1    

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
    
        col=KMPSearch(s,target)
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

print("Time taken in KMP Linked list:", end_time - start_time)
print()

""" 
KMPSearch("1,0,1,0", text)
                                                        
print("Time for Linked list in KMP Algorithm:")
print(time.process_time())
"""