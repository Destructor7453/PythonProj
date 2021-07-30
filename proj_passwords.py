#!/usr/bin/env python
# coding: utf-8

# # Password Project
# #### Kimberly Kokado

# In[1]:


import numpy as np
import pandas as pd
import os
import re


# First we need to import the dataframe:

# In[2]:


df = pd.read_csv(r"C:\Users\juggl\OneDrive\Documents\rockyou.txt", delimiter= "\n", header=None, names = ["Passwords"], encoding = "ISO-8859-1")


# In[3]:


df.head() #gives the header


# In[4]:


#drop duplicates from the dataframe
df.drop_duplicates(subset=["Passwords"], keep=False, inplace =True)


# In[5]:


df.info() #gives us info on the dataframe


# In[6]:


df = df.reset_index(drop=True) #reset index after dropping duplicates
print(df)


# In[7]:


#function to check password
def password_check(password):
    
    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # overall result
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error)
    
    if password_ok ==True:
        return "Password ok"
    if length_error == True:
        return "Length error"
    if uppercase_error == True:
        return "Uppercase error"
    if lowercase_error == True:
        return "Lowercase error"
    if digit_error == True:
        return "Digit error"


# In[8]:


def remove_specialchar(password):
    
    #search for special characters
    symbol_error = re.search(r"\W", password) is not None
    
    #search for spaces
    space_error = re.search(r" ", password) is not None
    
    if symbol_error == True:
        return "Symbol included"
    if space_error == True:
        return "Space included"


# first half of the above function is from stackoverflow: https://stackoverflow.com/questions/16709638/checking-the-strength-of-a-password-how-to-check-conditions

# In[9]:


df['Error'] = df['Passwords'].apply(remove_specialchar)


# In[12]:


print(df)


# In[13]:


#take the symbol and spaces out of the dataframe
clutter = df[(df['Error']=="Symbol included") | (df['Error'] == "Space included")].index
df.drop(clutter, inplace=True)


# In[14]:


df = df.reset_index(drop=True) #reset index after dropping clutter
print(df)


# In[15]:


df["Error"] = df['Passwords'].apply(password_check) #input error into a new column for password


# In[16]:


df.head()


# In[17]:


nist_pwd = df[ df['Error']== "Password ok"].index
print (nist_pwd)


# In[18]:


print(len(nist_pwd))


# This is the number of passwords in the 'rockyou.txt' that pass the partial NIST parameters for passwords. 

# In[ ]:




