# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 22:27:54 2023

@author: itzha
"""

import pandas as pd 
import time 

#Pattern : 
pattern = '0010' 

#Class to create nodes that hold the data element, and a pointer to the next node.
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None  
  
# Linked List class contains a node object, to create a linked list.
class LinkedList: 
    def __init__(self):  
        self.head = None

    # method to add new node to the linked list    
    def append(self, new_data): 

        # create a new node using the given data and assign it to the head of the linked list if it is empty.    
        if self.head is None: 
            self.head = Node(new_data) 

        # else, traverse till the last node and insert the new_node there.  
        else: 

            last = self.head 

            while (last.next): 

                last = last.next

            last.next = Node(new_data)  

    # method to print all nodes of the linked list    
    def printList(self): 

        temp = self.head 

        while (temp): 

            print (temp.data)  

            temp = temp.next  
    #method to traverse data element in each node.         
    def extract(self): 

        temp = self.head 

        while (temp): 
  #each data element in the linked list will be send as an argument to the naive string match method, to search for a pattern match.    
           naive_string_match(pattern, temp.data) 
           
           #next element..
           temp = temp.next

start_time = time.perf_counter() 

   # method to apply Naive String Matching algorithm on the data stored in Linked List 
def naive_string_match(pat, txt):
       M = len(pat)
       N = len(txt)
  
    #A loop to slide pat[] one by one.
       for i in range(N - M + 1):
         j = 0
  
        # For current index i, check for pattern match.
         while(j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1
  
            if (j == M):
             print("Pattern found at index ", i)  #Print the 1st index in which a pattern match has been found.


  
                           
mylist=LinkedList() 

#creating a dataframe that read data from the given file.
df = pd.read_csv("both_covid_data.csv")
df = df.astype(str)
#Join all the elements in each row with no separator
df["joined_row"] = df.apply(lambda row: ''.join(row), axis=1)
for i,s in enumerate(df["joined_row"]):
   #Store the data in the linked list. 
   mylist.append(s) 
   
   
#search for a pattern match for each linked list element.   
mylist.extract()
end_time = time.perf_counter()

#Calculating and printing the run time needed to search for a pattern match.
print("Time taken for implementing (Naive String Matching algorithm) using Linked List:", end_time - start_time)

