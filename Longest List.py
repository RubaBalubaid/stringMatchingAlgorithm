# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 10:13:00 2023

@author: shade
"""
#importing pandas library 
import pandas as pd 
import time 


df = pd.read_csv("both_covid_data.csv")
df = df.astype(str)


df["joined_row"] = df.apply(lambda row: ''.join(row), axis=1)



start_time = time.perf_counter()

def lcs(X, Y): 
    
    m = len(X) 
    n = len(Y) 
  
    
    L = [[None]*(n+1) for i in range(m+1)] 
  
   
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 

    

    index = L[m][n]  


    lcs=[""] * (index+1)  

    lcs[index] = ""  


    i=m; j=n;  

    while i > 0 and j > 0:  


        if X[i - 1] == Y[j - 1]:  

            lcs[index - 1]=X[i - 1];  

            i -= 1; j -= 1; index -= 1;      

        

        elif L [i - 1][j] > L [i][j - 1]:  

            i -= 1;     

        else:               j -= 1;     

    print ("LCS of " + X + " and " + Y + " is " + "".join(lcs))
    
end_time = time.perf_counter()
    
    
print("Time taken for implementing (Longest String Matching algorithm) using Array:",end_time-start_time)

