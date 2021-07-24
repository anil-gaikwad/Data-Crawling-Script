import requests
from bs4 import BeautifulSoup
import json


r = requests.get('https://en.wikipedia.org/wiki/Wikipedia:Featured_pictures/People/Science_and_engineering')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.findAll('li', class_='gallerybox')

formatted_links = []
base = 'https:'
for link in links:
    data = {
        "name": link.find_all('div', class_='gallerytext')[0].a.text.strip(),
        "organization": link.find_all('div', class_='gallerytext')[0].a.findNext().text.strip(),
        "image_url": base + link.find_all('div', class_='thumb')[0].img.get('src').strip(),
    }
    formatted_links.append(data)

print(formatted_links)
with open('problem1/data.json', 'w') as file:
    json.dump(formatted_links, file)