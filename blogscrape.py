import requests
from bs4 import BeautifulSoup
from csv import writer
import numpy as np

response = requests.get('https://www.foxnews.com/')

soup = BeautifulSoup(response.text,features="html.parser")# features for error in virtual enviroment

name = {soup.find(class_='logo')}
link = {'<a>https://www.foxnews.com/</a>'}

# title ={"Fox News"}
foxData ={}

#get top 5 articles
# title = soup.find(class_='info-header').find_next('a').get_text()
# print(title)

title = soup.select('a')
print(title)

