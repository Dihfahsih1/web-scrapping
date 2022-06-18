
import requests
from bs4 import BeautifulSoup as bs

page = 0

with requests.Session() as s:
  s.headers = {'User-Agent':'Mozilla/5.0'}
  while True:
    page+=1
    r = s.get(f'https://www.realestate.co.nz/residential/sale/auckland?by=latest&oad=true&page={page}&pm=1')
    soup = bs(r.content, 'lxml')
    next_page = soup.select_one('[data-test=next-link]')
    
    if next_page is None:
        break
    print(page)



# def get_content(page: int) -> str:
#     url = f"https://horizonhealth.com/blog/page/{page}"
#     headers={'User-Agent': 'XYZ/3.0'}
#     news_page = requests.get(url, headers=headers).text
#     news_doc=BeautifulSoup(news_page, 'html.parser')
#     items = news_doc.find_all('a', class_="sl_card sl_card--blog sl_blog")
#     for item in items:
#       print(item.text)
#       return item.getText(strip=True)


# print(" ".join(get_content(page) for page in range(1, 5)))

