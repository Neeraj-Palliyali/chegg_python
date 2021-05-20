import pandas as pd 
import numpy as numpy
from bs4 import BeautifulSoup
import re 
import requests as req
import matplotlib.pyplot  as plt


# asking for response
resp = req.get("https://en.wikipedia.org/wiki/University_of_Maryland,_College_Park",)


# Q1) response object
print(resp)

# Q2) response code ONLY
print(resp.status_code)

# Q3) response header
print(resp.headers)

# Q4) First 500 characters of data in bytes 
print(resp._content[:500])

# getting only 500 characters 
k=resp._content[:500]

# getting output to unicode
soup = BeautifulSoup(k.decode('utf-8'), "html.parser")

# Q5) Printing the first 500 characteers of the html in unicode
print(soup)

# Q6) Printing the elapsed time 
print(resp.elapsed)

# Q7) Printing the cookies
print(resp.cookies)