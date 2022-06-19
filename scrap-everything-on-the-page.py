from unicodedata import category
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import json
output=[]
#https://www.wesanahealth.com/
#https://wesanahealth.com/media-room/
# press_page = requests.get(press_url).text
# press_doc=BeautifulSoup(press_page, 'html.parser')
# items = press_doc.find_all(class_="elementor-post__text")
# for item in items:
# link="https://wesanahealth.com/in-the-news/wesana-health-ceo-daniel-carcillo-to-keynote-charles-river-symposium-re-imagining-substance-abuse-addiction-and-mental-health-disorders-with-psychedelic-therapies/"
# headers={'User-Agent': 'XYZ/3.0'}
# response = requests.get(link, headers=headers).text
# detail_page = BeautifulSoup(response, 'html.parser')
# details=detail_page.find("div", {"itemprop": "articleBody"})
# title=detail_page.find("h1", {"itemprop": "headline"})
# news={}
# news["Title"]=title.text
# news["Description"]=details.text
# output.append(news) 
# with open("wesanahealth-media-release-data.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
  
#wesana-health-news
#https://ir.wesanahealth.com/news-events/press-releases

# req = Request('https://ir.wesanahealth.com/news-events/press-releases', headers={'User-Agent': 'XYZ/3.0'})
# webpage = urlopen(req, timeout=10).read()
for page in range(1, 5 ):
  req = Request(f"https://ir.wesanahealth.com/news-events/press-releases?page={page}", headers={'User-Agent': 'XYZ/3.0'})

  webpage = urlopen(req, timeout=100).read()
  news_doc=BeautifulSoup(webpage, 'html.parser')
  items = news_doc.find_all("div", class_="media-body")

  for item in items:
    title =item.find('a')
    get_link = item.find('a')
    link=get_link.attrs['href']
    headers={'User-Agent': 'XYZ/3.0'}
    response = requests.get(link, headers=headers).text
    detail_page = BeautifulSoup(response, 'html.parser')
    details=detail_page.find("article",class_="full-news-article")
    details.find('h1', class_="article-heading").decompose()
    details.find('h1', class_="related-documents-line hidden-print").decompose()
    news={}
    news["Title"]=title.text
    news["Description"]=details.text
    output.append(news) 
    
with open("wesanahealth-news-events-releases.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')

    
