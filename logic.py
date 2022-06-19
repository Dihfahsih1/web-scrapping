from unicodedata import category
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import json
output=[]
# for page in range(1, 6):
#   req = Request(f"https://horizonhealth.com/blog/page{page}", headers={'User-Agent': 'XYZ/3.0'})
#   webpage = urlopen(req, timeout=100).read()
#   news_doc=BeautifulSoup(webpage, 'html.parser')
#   items = news_doc.find_all('a',class_="sl_card sl_card--blog sl_blog",href=True)
#   for item in items:
#     link=item['href']
#     title =item.find('h2')
    
#     headers={'User-Agent': 'XYZ/3.0'}
#     response = requests.get(link, headers=headers).text
#     detail_page = BeautifulSoup(response, 'lxml')
#     details=detail_page.find(class_="sl_main")
#     news={}
#     news["Title: "]=title.text
#     news["Description: "]=details.text
#     output.append(news) 
# with open("text.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
  

#horizonhealth-white-papers/
# req = Request(f"https://horizonhealth.com/education/white-papers/", headers={'User-Agent': 'XYZ/3.0'})
# webpage = urlopen(req, timeout=100).read()
# news_doc=BeautifulSoup(webpage, 'html.parser')
# items = news_doc.find_all('a',class_="sl_callout-link",href=True)
# for item in items:
#   link=item['href']
#   if "https://horizonhealth.com" not in link:
#     link="https://horizonhealth.com"+link
#   else:
#     link
#   title =item.find('h3')
  
#   headers={'User-Agent': 'XYZ/3.0'}
#   response = requests.get(link, headers=headers).text
#   detail_page = BeautifulSoup(response, 'lxml')
#   details=detail_page.find(class_="sl_main")
#   news={}
#   news["Title"]=title.text
#   news["Description"]=details.text
#   output.append(news) 
# with open("horizonhealth-white-papers.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  

from contextlib import closing
from selenium.webdriver import Chrome # pip install selenium

url = "https://ksanahealth.com/mental-health-blog/"

# use firefox to get page with javascript generated content
with closing(Chrome()) as browser:
  n = 1
  while n < 10:
    browser.get(url) # load page
    link = browser.find_element(str(n))
    while link:
      browser.get(link.get_attribute("href")) # get individual 1,2,3,4 pages
      #### save(browser.page_source)
      browser.back() # return to page that has 1,2,3,next -like links
      n += 1
      link = browser.find_element(str(n))

    link = browser.find_element("next")
    if not link: break
    url = link.get_attribute("href")
    print(url)
    
    

      
