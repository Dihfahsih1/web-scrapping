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
# for page in range(1, 5 ):
#   req = Request(f"https://ir.wesanahealth.com/news-events/press-releases?page={page}", headers={'User-Agent': 'XYZ/3.0'})

#   webpage = urlopen(req, timeout=100).read()
#   news_doc=BeautifulSoup(webpage, 'html.parser')
#   items = news_doc.find_all("div", class_="media-body")

#   for item in items:
#     title =item.find('a')
#     get_link = item.find('a')
#     link=get_link.attrs['href']
#     headers={'User-Agent': 'XYZ/3.0'}
#     response = requests.get(link, headers=headers).text
#     detail_page = BeautifulSoup(response, 'html.parser')
#     details=detail_page.find("article",class_="full-news-article")
#     details.find('h1', class_="article-heading").decompose()
#     details.find('div', class_="related-documents-line hidden-print").decompose()
#     news={}
#     news["Title"]=title.text
#     news["Description"]=details.text
#     output.append(news) 
    
# with open("wesanahealth-news-events-releases.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
  

#Scraping FQA of wesanahealth
# url_list="https://ir.wesanahealth.com/company-information/faq"
# # empty list to store all results
# headers={'User-Agent': 'XYZ/3.0'}
# req = requests.get(url_list,headers=headers )
# soup = BeautifulSoup(req.text, "html.parser")
# #results=soup.find('div',class_="container w-container")
# results=soup.find_all(['dt','dd'])
# for result in results:
#   output=result.text
#   with open("wesanahealth-FAQ-data.txt", "a") as f:
#     output=str(output)
#     f.write(output)
#     f.write('\n')


# #Scraping Insights of vivihealth
# url_list="https://www.vivihealth.com/coronavirus-update/"
# # empty list to store all results
# headers={'User-Agent': 'XYZ/3.0'}
# req = requests.get(url_list,headers=headers )
# soup = BeautifulSoup(req.text, "html.parser")
# #results=soup.find('div',class_="container w-container")
# title=soup.find('h1',class_="entry-title")
# description=soup.find('div', class_="entry-content")
# author=soup.find('p',class_="entry-meta")
# output=[]
# news={}
# news["Title"]=title.text
# news["Authored"]=author.text
# news["Description"]=description.text
# output.append(news) 
# with open("vivihealth-news.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')


# #Scraping privacy policy of vivihealth
# url_list="https://www.vivihealth.com/privacy-policy/"
# # empty list to store all results
# headers={'User-Agent': 'XYZ/3.0'}
# req = requests.get(url_list,headers=headers )
# soup = BeautifulSoup(req.text, "html.parser")
# #results=soup.find('div',class_="container w-container")
# title=soup.find('main',class_="content")
# with open("vivihealth-privacy-policy.txt", "a") as f:
#   output=str(title.text)
#   f.write(output)
#   f.write('\n')
  
#Scraping FQA of wesanahealth
# url_list="https://ir.wesanahealth.com/company-information/faq"
# # empty list to store all results
# headers={'User-Agent': 'XYZ/3.0'}
# req = requests.get(url_list,headers=headers )
# soup = BeautifulSoup(req.text, "html.parser")
# #results=soup.find('div',class_="container w-container")
# results=soup.find_all(['dt','dd'])
# for result in results:
#   output=result.text
#   with open("wesanahealth-FAQ-data.txt", "a") as f:
#     output=str(output)
#     f.write(output)
#     f.write('\n')


#not-working
# req = Request(f"https://visiontree.com/press-releases/", headers={'User-Agent': 'XYZ/3.0'})
# webpage = urlopen(req, timeout=100).read()
# news_doc=BeautifulSoup(webpage, 'html.parser')
# items = news_doc.find_all("tbody")
# for item in items:
#   data =item.find('td', class_="px-6 py-4 text-gray-500")
#   get_link = data.find('a')
#   link="https://visiontree.com/press-releases"+ get_link.attrs['href']
#   headers={'User-Agent': 'XYZ/3.0'}
#   response = requests.get(link, headers=headers).text
#   detail_page = BeautifulSoup(response, 'html.parser')
#   print(detail_page.text)
#   details=detail_page.find("div",class_="pageWrap pageWrap--m")
  
#   title=detail_page.find('div',class_="relative")
#   detail_page.find('div', class_="flex items-center justify-between mb-6").decompose()
#   news={}
#   news["Title"]=title.text
#   news["Description"]=details.text
#   output.append(news) 
  
# with open("visiontree-press-releases.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')


#Valant-blogs
for page in range(1, 29 ):
  req = Request(f"https://www.valant.io/blog/{page}", headers={'User-Agent': 'XYZ/3.0'})

  webpage = urlopen(req, timeout=100).read()
  news_doc=BeautifulSoup(webpage, 'html.parser')
  items = news_doc.find_all("div", class_="post-content-wrap")

  for item in items:
    
    title =item.find('h3', class_="title")
    get_link = item.find('a')
    link=get_link.attrs['href']
    headers={'User-Agent': 'XYZ/3.0'}
    response = requests.get(link, headers=headers).text
    detail_page = BeautifulSoup(response, 'html.parser')
    details=detail_page.find("div",class_="content-inner")
    news={}
    news["Title"]=title.text
    news["Description"]=details.text
    output.append(news)  
with open("valant-blog.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
#Valant-Webinars
# for page in range(1, 3 ):
#   req = Request(f"https://www.valant.io/webinars/{page}", headers={'User-Agent': 'XYZ/3.0'})

#   webpage = urlopen(req, timeout=100).read()
#   news_doc=BeautifulSoup(webpage, 'html.parser')
#   items = news_doc.find_all("div", class_="post-content-wrap")

#   for item in items:
    
#     title =item.find('h3', class_="title")
#     get_link = item.find('a')
#     link=get_link.attrs['href']
#     headers={'User-Agent': 'XYZ/3.0'}
#     response = requests.get(link, headers=headers).text
#     detail_page = BeautifulSoup(response, 'html.parser')
#     details=detail_page.find("div",class_="content-inner")
#     news={}
#     news["Title"]=title.text
#     news["Description"]=details.text
#     output.append(news)  
# with open("valant-webinars.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  

#Valant-case-studies

# req = Request(f"https://www.valant.io/resources/white-papers/", headers={'User-Agent': 'XYZ/3.0'})

# webpage = urlopen(req, timeout=100).read()
# news_doc=BeautifulSoup(webpage, 'html.parser')
# items = news_doc.find_all("div", class_="post-content-wrap")

# for item in items:
  
#   title =item.find('h3', class_="title")
#   get_link = item.find('a')
#   link=get_link.attrs['href']
#   headers={'User-Agent': 'XYZ/3.0'}
#   response = requests.get(link, headers=headers).text
#   detail_page = BeautifulSoup(response, 'html.parser')
#   details=detail_page.find("div",class_="content-inner")
#   news={}
#   news["Title"]=title.text
#   news["Description"]=details.text
#   output.append(news)  
# with open("valant-white-papers.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')

