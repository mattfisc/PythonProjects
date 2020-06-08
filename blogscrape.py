import requests
from bs4 import BeautifulSoup
from csv import writer
import numpy as np

response = requests.get('https://www.foxnews.com/')

soup = BeautifulSoup(response.text,features="html.parser")# features for error in virtual enviroment

name={'Fox News'}
link = {'<a>https://www.foxnews.com/</a>'}


#get top 5 articles
# title = soup.find(class_='info-header').find_next('a').get_text()
# print(title)

lines = soup.find_all(class_='info-header')

for line in lines:
    #title = line.find()
    title = line.find(class_='title').get_text()
    #title = line.find('a').get_text()
    print(title)
