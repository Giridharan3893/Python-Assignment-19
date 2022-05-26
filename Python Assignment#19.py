#!/usr/bin/env python
# coding: utf-8

# In[3]:


##Answer1:

import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def check(email):

    if(re.fullmatch(regex, email)):
        print("Valid Email")
 
    else:
        print("Invalid Email")

if __name__ == '__main__':

    email = "giridaranp@gmail.com"

    check(email)
 
    email = "cricbuzz.com"
    check(email)
 
    email = "giri.com"
    check(email)


# In[5]:


##Answer2:

import re

filenames = ["giri.html", "giri.xml", 
            "giri.txt", "giri.jpg"]
  
for file in filenames:
 
    match = re.search("\.xml$", file)

    if match:
        print("The file ending with .xml is:",
             file)


# In[ ]:


##Answer3:

import sys, re

f = open(sys.argv[1],'r')
text = f.read()
ips = [] 
regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',text)
if regex is not None:
    for match in regex:
        if match not in ips:
            ips.append(match)
            print(match)


# In[11]:


##Answer4:

import re
password = "R@m@_f0rtu9e$"
flag = 0
while True:  
    if (len(password)<8):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break
  
if flag ==-1:
    print("Not a Valid Password")


# In[14]:


##Answer5:

import re

def password(v):

    if v == "\n" or v == " ":
        return "Password cannot be a newline or space!"

    if 9 <= len(v) <= 20:

        if re.search(r'(.)\1\1', v):
            return "Weak Password: Same character repeats three or more times in a row"

        if re.search(r'(..)(.*?)\1', v):
            return "Weak password: Same string pattern repetition"
   
        else:
            return "Strong Password!"
   
    else:
        return "Password length must be 9-20 characters!"

def main():

    print(password("Qggf!@ghf3"))
    print(password("titfortat"))
    print(password("apr@3893"))
    print(password("Aasd!feasn"))
    print(password("772*hd897"))
    print(password(" "))

if __name__ == '__main__':
    main()


# In[18]:


##Answer6:

with open('GFG.txt','r') as file:
   
    for line in file:
      
        for word in line.split():

            print(word) 


# In[20]:


##Answer7:

file = open('file.txt', 'r')
 
while 1:

    char = file.read(1)         
    if not char:
        break
         
    print(char)
      
file.close()


# In[22]:


##Answer8:

def counter(fname):

    num_words = 0

    num_lines = 0

    num_charc = 0

    num_spaces = 0

    with open(fname, 'r') as f:

        for line in f:

            num_lines += 1

            word = 'Y'

            for letter in line:

                if (letter != ' ' and word == 'Y'):

                    num_words += 1

                    word = 'N'

                elif (letter == ' '):

                    num_spaces += 1

                    word = 'Y'

                for i in letter:

                    if(i !=" " and i !="\n"):

                        num_charc += 1

    print("Number of words in text file: ", num_words)

    print("Number of lines in text file: ", num_lines)

    print('Number of characters in text file: ', num_charc)

    print('Number of spaces in text file: ', num_spaces)

if __name__ == '__main__': 
    fname = 'File1.txt'
    try: 
        counter(fname) 
    except: 
        print('File not found')


# In[23]:


##Answer9:

f = open("file.txt", "r")
d = dict()
  
for res in f:

    res = res.strip()

    res = res.lower()

    lines = res.split()
  
    for line in lines:
  
        if line in d:
        
            d[line] = d[line]+1
        else:

            d[line] = 1
    
f.close()

for key in list(d.keys()):
    print("The count of {} is {}".format(key,d[key]))


# In[26]:


##Answer10:

number_of_words = 0

with open(r'SampleFile.txt','r') as file:

    data = file.read()

    lines = data.split()

    for word in lines:

        if not word.isnumeric():         

            number_of_words += 1
print(number_of_words)


# In[ ]:




