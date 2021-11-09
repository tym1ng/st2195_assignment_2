from bs4 import BeautifulSoup
import requests

csv_wiki = requests.get("https://en.wikipedia.org/wiki/Comma-separated_values")
soup = BeautifulSoup(csv_wiki.text, 'html.parser')
    
ths = soup.find(id='Example')
table = ths.findNext('pre').text
print(table)

f = open('car.csv', 'w')
f.write(table)
f.close()