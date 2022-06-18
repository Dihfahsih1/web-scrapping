
import requests
from bs4 import BeautifulSoup as bs

page = 0
pages=[]
with requests.Session() as s:
  s.headers = {'User-Agent':'Mozilla/5.0'}
  while True:
    page+=1
    r = s.get(f'https://mdlogix.com/mdlogix-news/page/{page}')
    soup = bs(r.content, 'lxml')
    next_page = soup.find('div', class_="posts-page-links")
    
    if next_page is None:
      break    
    pages.append(page)
  new_value = pages[-1] +1
  pages.append(new_value)
  print(pages)
  

