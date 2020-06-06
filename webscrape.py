from bs4 import BeautifulSoup
html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>website</title>
</head>
<body>
    <div id="section1">
        <h3 data-hello="hi">Hello</h3>
        <p>asdfsadsadfasdsaddfsaddf</p>
    </div>
    <div id="section2">
        <ul class="items">
            <li class="item"><a href="#">Item 1</a></li>
            <li class="item"><a href="#">Item 2</a></li>
            <li class="item"><a href="#">Item 3</a></li>
            <li class="item"><a href="#">Item 4</a></li>
        </ul>
    </div>
</body>
</html>
"""
soup = BeautifulSoup(html_doc,'html.parser')

#Direct
#print(soup.title)

#find
# el = soup.find_all('div')

# el = soup.find(id='section1')
# el = soup.find(class_='item')

# select
#el = soup.select('#section1')[0]

#get text()
# el= soup.find(class_='item').get_text()


# for item in soup.select('.item'):
#     print(item.get_text())


#navigation
# el = soup.body.contents[3].find_next_sibling

# el = soup.find(class_='item').find_parent()
# el=soup.find('h3').find_next_sibling('p')


#print(el)

