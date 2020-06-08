import requests
from bs4 import BeautifulSoup
from csv import writer
import numpy as np

response = requests.get('https://www.foxnews.com/')

soup = BeautifulSoup(response.text,features="html.parser")# features for error in virtual enviroment

name={'Fox News'}
link = {'<a>https://www.foxnews.com/</a>'}

lines = soup.find_all(class_='info-header')

with open('posts.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['title']
    csv_writer.writerow(headers)

    titles =[]
    for line in lines:

        title = line.find(class_='title').get_text()
        titles.append(title)
        csv_writer.writerow(title)

for title in titles:
    print(title)

