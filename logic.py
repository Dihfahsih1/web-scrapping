from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

import json
output=[]

url = 'https://www.blueprint-health.com/blog'
while True:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    pages = soup.find_all('div', class_="w-pagination-wrapper pagination")
    for page in pages:
        nextpage = page.find('a', {'aria-label': 'Next Page'})
        uu = nextpage.get('href')
        url = 'https://www.blueprint-health.com/blog' + str(uu)
        press_page = requests.get(url).text
        press_doc=BeautifulSoup(press_page, 'html.parser')
        items = press_doc.find_all(class_="collection-item-blog")
        for item in items:
          title =item.find(class_="title-post")
          get_link = item.find('a')
          link=get_link.attrs['href']
          link="https://www.blueprint-health.com" +link
          get_details = requests.get(link).text 
          detail_page = BeautifulSoup(get_details, 'html.parser')
          details=detail_page.find(class_="rich-text-blog")
          press={}
          press["Title"]=title.text
          press["Description"]=details.text
          print(title.text)
        