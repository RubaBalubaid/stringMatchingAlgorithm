# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 12:34:29 2023

@author: shade
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 06:56:04 2023

@author: shade
""" 
import pandas as pd 
import time 


df = pd.read_csv("both_covid_data.csv")
df = df.astype(str)


df["joined_row"] = df.apply(lambda row: ''.join(row), axis=1)
              
 

start_time = time.perf_counter()

class Node: 
  
   
    def __init__(self, data): 
        self.data = data   
        self.next = None   
  

class LinkedList: 
 
    def __init__(self): 
        self.head = None
 
    def printList(self):  

        temp = self.head  

        while (temp):  

            print (temp.data)  

            temp = temp.next

    def getLength(self):  

        temp = self.head  

        count = 0;  

        while (temp):  

            count += 1;  

            temp = temp.next;  

        return count;    

    def lcs(self, X, Y, m, n):     

        if m == 0 or n == 0:     

            return 0;     

          
        elif X[m-1] == Y[n-1]:     

            node = Node(X[m-1])     

            if self.head is None:     

                self.head = node     

            else:     

                current_node = self.head     

                while current_node.next is not None:   
                    current_node=current_node.next                     
                    current_node=current_node.next               
                    current_node.next=node    
                    return 1 + self.lcs(X, Y, m-1, n-1);      
                else:     
                    
                    return max(self.lcs(X, Y, m, n-1), self.lcs(X, Y, m-1, n));
                
               
                   
                       
end_time = time.perf_counter()
  
print("Time taken for implementing (Longest String Matching algorithm) using Linked List:",end_time-start_time)