from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import json
output=[]

#############wesanahealth.com####################
#https://www.wesanahealth.com/  
press_url='https://wesanahealth.com/media-room/'
press_page = requests.get(press_url).text
press_doc=BeautifulSoup(press_page, 'html.parser')
items = press_doc.find_all(class_="elementor-post__text")
for item in items:
  link="https://wesanahealth.com/in-the-news/wesana-health-ceo-daniel-carcillo-to-keynote-charles-river-symposium-re-imagining-substance-abuse-addiction-and-mental-health-disorders-with-psychedelic-therapies/"
  headers={'User-Agent': 'XYZ/3.0'}
  response = requests.get(link, headers=headers).text
  detail_page = BeautifulSoup(response, 'html.parser')
  details=detail_page.find("div", {"itemprop": "articleBody"})
  title=detail_page.find("h1", {"itemprop": "headline"})
  news={}
  news["Title"]=title.text
  news["Description"]=details.text
  output.append(news) 
with open("wesanahealth-media-release-data.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
  
##wesana-health-news https://ir.wesanahealth.com/news-events/press-releases

req = Request('https://ir.wesanahealth.com/news-events/press-releases', headers={'User-Agent': 'XYZ/3.0'})
webpage = urlopen(req, timeout=10).read()
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
    details.find('div', class_="related-documents-line hidden-print").decompose()
    news={}
    news["Title"]=title.text
    news["Description"]=details.text
    output.append(news) 
    
with open("wesanahealth-news-events-releases.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
  

####Scraping FQA of wesanahealth
url_list="https://ir.wesanahealth.com/company-information/faq"
# empty list to store all results
headers={'User-Agent': 'XYZ/3.0'}
req = requests.get(url_list,headers=headers )
soup = BeautifulSoup(req.text, "html.parser")
#results=soup.find('div',class_="container w-container")
results=soup.find_all(['dt','dd'])
for result in results:
  output=result.text
  with open("wesanahealth-FAQ-data.txt", "a") as f:
    output=str(output)
    f.write(output)
    f.write('\n')


#Scraping Insights of vivihealth
url_list="https://www.vivihealth.com/coronavirus-update/"
# empty list to store all results
headers={'User-Agent': 'XYZ/3.0'}
req = requests.get(url_list,headers=headers )
soup = BeautifulSoup(req.text, "html.parser")
#results=soup.find('div',class_="container w-container")
title=soup.find('h1',class_="entry-title")
description=soup.find('div', class_="entry-content")
author=soup.find('p',class_="entry-meta")
output=[]
news={}
news["Title"]=title.text
news["Authored"]=author.text
news["Description"]=description.text
output.append(news) 
with open("vivihealth-news.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


#Scraping privacy policy of vivihealth
url_list="https://www.vivihealth.com/privacy-policy/"
# empty list to store all results
headers={'User-Agent': 'XYZ/3.0'}
req = requests.get(url_list,headers=headers )
soup = BeautifulSoup(req.text, "html.parser")
#results=soup.find('div',class_="container w-container")
title=soup.find('main',class_="content")
with open("vivihealth-privacy-policy.txt", "a") as f:
  output=str(title.text)
  f.write(output)
  f.write('\n')
  
###Scraping FQA of wesanahealth
url_list="https://ir.wesanahealth.com/company-information/faq"
# empty list to store all results
headers={'User-Agent': 'XYZ/3.0'}
req = requests.get(url_list,headers=headers )
soup = BeautifulSoup(req.text, "html.parser")
#results=soup.find('div',class_="container w-container")
results=soup.find_all(['dt','dd'])
for result in results:
  output=result.text
  with open("wesanahealth-FAQ-data.txt", "a") as f:
    output=str(output)
    f.write(output)
    f.write('\n')


# not-working
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
  req = Request(f"https://www.valant.io/blog/page/{page}/", headers={'User-Agent': 'XYZ/3.0'})

  webpage = urlopen(req,timeout=100).read()
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
    news["Blog Title"]=title.text
    news["Blog Description"]=details.text
    output.append(news)  
with open("valant-blog.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
#Valant-Webinars
for page in range(1, 3 ):
  req = Request(f"https://www.valant.io/webinars/page/{page}", headers={'User-Agent': 'XYZ/3.0'})

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
with open("valant-webinars.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  

Valant-case-studies

req = Request(f"https://www.valant.io/resources/white-papers/", headers={'User-Agent': 'XYZ/3.0'})

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
with open("valant-white-papers.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')

#https://blog.nview.com/
for page in range(1, 10 ):
  req = Request(f"https://blog.nview.com/page/{page}", headers={'User-Agent': 'XYZ/3.0'})

  webpage = urlopen(req,timeout=10).read()
  news_doc=BeautifulSoup(webpage, 'html.parser')
  items = news_doc.find_all("article", class_="blog-index__post blog-index__post--small")
  
  for item in items:
    title =item.find('h4', class_="blog-index-title")
    
    get_link = item.find('a')
    link=get_link.attrs['href']
    headers={'User-Agent': 'XYZ/3.0'}
    response = requests.get(link, headers=headers).text
    detail_page = BeautifulSoup(response, 'html.parser')
    details=detail_page.find("div",class_="blog-post__body")
    news={}
    news["Blog Title"]=title.text
    try:
      news["Blog Description"]=details.text
    except:
      pass
    output.append(news)  
with open("nview-blog.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
  

#############################blog.nview.com/tag/################################
req = Request(f"https://blog.nview.com/tag/nview-press-releases/page/3", headers={'User-Agent': 'XYZ/3.0'})

webpage = urlopen(req,timeout=10).read()
news_doc=BeautifulSoup(webpage, 'html.parser')
items = news_doc.find_all("article", class_="blog-index__post blog-index__post--small")

for item in items:
  title =item.find('h4', class_="blog-index-title")
  
  get_link = item.find('a')
  link=get_link.attrs['href']
  headers={'User-Agent': 'XYZ/3.0'}
  response = requests.get(link, headers=headers).text
  detail_page = BeautifulSoup(response, 'html.parser')
  details=detail_page.find("div",class_="blog-post__body")
  news={}
  news["Blog Title"]=title.text
  try:
    news["Blog Description"]=details.text
  except:
    pass
  output.append(news)  
with open("nview-press-releases.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  

####################https://www.nssbehavioralhealth.com/ website#################
req = Request(f"https://www.nssbehavioralhealth.com/nextstep-solutions-blog/", headers={'User-Agent': 'XYZ/3.0'})

webpage = urlopen(req,timeout=10).read()
news_doc=BeautifulSoup(webpage, 'html.parser')
items = news_doc.find_all("div", class_="q_masonry_blog_post_text")

for item in items:
  title =item.find('h5', class_="q_masonry_blog_title entry_title")
  
  get_link = title.find('a')
  link=get_link.attrs['href']
  headers={'User-Agent': 'XYZ/3.0'}
  response = requests.get(link, headers=headers).text
  detail_page = BeautifulSoup(response, 'html.parser')
  details=detail_page.find("div",class_="post_text_inner")
  news={}
  news["Blog Title"]=title.text
  try:
    news["Blog Description"]=details.text
  except:
    pass
  output.append(news)  
with open("nssbehavioralhealth-blogs.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


################https://www.neuroflow.com/BLOGS/#############################
for page in range(1, 10 ):
  req = Request(f"https://www.neuroflow.com/blog/page/{page}/", headers={'User-Agent': 'XYZ/3.0'})

  webpage = urlopen(req,timeout=10).read()
  news_doc=BeautifulSoup(webpage, 'html.parser')
  items = news_doc.find_all("div", class_="entry-content-wrap")
  
  for item in items:
    title =item.find('h3', class_="entry-post-title")
    print(title.text)
    
    get_link = title.find('a')
    link=get_link.attrs['href']
    headers={'User-Agent': 'XYZ/3.0'}
    response = requests.get(link, headers=headers).text
    detail_page = BeautifulSoup(response, 'html.parser')
    details=detail_page.find("div",class_="entry-content clearfix")
    news={}
    news["Blog Title"]=title.text
    try:
      news["Blog Description"]=details.text
    except:
      pass
    output.append(news)  
with open("neuroflow-blog.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
################https://www.neuroflow.com/PRESS/#############################
for page in range(1, 4 ):
  req = Request(f"https://www.neuroflow.com/press/page/{page}/", headers={'User-Agent': 'XYZ/3.0'})

  webpage = urlopen(req,timeout=10).read()
  news_doc=BeautifulSoup(webpage, 'html.parser')
  items = news_doc.find_all("div", class_="entry-content-wrap clearfix")
  
  for item in items:
    title =item.find('h3', class_="entry-post-title")
    print(title.text)
    
    get_link = title.find('a')
    link=get_link.attrs['href']
    headers={'User-Agent': 'XYZ/3.0'}
    response = requests.get(link, headers=headers).text
    detail_page = BeautifulSoup(response, 'html.parser')
    details=detail_page.find("div",class_="entry-content clearfix")
    news={}
    news["Press Title"]=title.text
    try:
      news["Press Description"]=details.text
    except:
      pass
    output.append(news)  
with open("neuroflow-Press.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
req = Request(f"https://www.neuroflow.com/research/", headers={'User-Agent': 'XYZ/3.0'})

webpage = urlopen(req,timeout=10).read()
news_doc=BeautifulSoup(webpage, 'html.parser')
items = news_doc.find_all("div", class_="vc_row wpb_row vc_row-fluid vc_column-gap-25") 
for item in items:
  details=item.find("div",class_="w-author-desc")
  title=item.find("h3")
  news={}
  news["Research Title"]=title.text
  try:
    news["Research Description"]=details.text
  except:
    pass
  output.append(news)  
with open("neuroflow-Research.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')



####################https://www.neuroblu.ai/ website#################
req = Request(f"https://www.neuroblu.ai/announcements/", headers={'User-Agent': 'XYZ/3.0'})

webpage = urlopen(req,timeout=10).read()
news_doc=BeautifulSoup(webpage, 'html.parser')
items = news_doc.find_all("div", class_="collection-item-4 w-dyn-item")

for item in items:
  title =item.find('h3', class_="heading-3 nrelease announcements")
  
  get_link = item.find('a')
  link='https://www.neuroblu.ai' + get_link.attrs['href']
  headers={'User-Agent': 'XYZ/3.0'}
  response = requests.get(link, headers=headers).text
  detail_page = BeautifulSoup(response, 'html.parser')
  details=detail_page.find("div",class_="rich-text-block w-richtext")
  news={}
  news["Announcement Title"]=title.text
  try:
    news["Announcement Description"]=details.text
  except:
    pass
  output.append(news)  
with open("neuroblu-announcements.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')

###Use Cases
link='https://www.neuroblu.ai/use-cases/analyzing-hospitalization-rate-treatment-switch-and-effectiveness-between-two-mdd-drugs'
headers={'User-Agent': 'XYZ/3.0'}
response = requests.get(link, headers=headers).text
detail_page = BeautifulSoup(response, 'html.parser')
title=detail_page.find("h2",class_="heading-29")
details=detail_page.find("div",class_="rich-text-block w-richtext")
news={}
news["Usecase Title"]=title.text
try:
  news["Usecase Description"]=details.text
except:
  pass
output.append(news)  
with open("neuroblu-usecases.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


################https://nndc.org/announcements/#############################
for page in range(1, 3):
  req = Request(f"https://nndc.org/category/announcements/page/{page}/", headers={'User-Agent': 'XYZ/3.0'})

  webpage = urlopen(req,timeout=10).read()
  news_doc=BeautifulSoup(webpage, 'html.parser')
  items = news_doc.find_all("div", class_="post_content clearfix")
  
  for item in items:
    title =item.find('h3', class_="post_title")
    print(title.text)
    
    get_link = title.find('a')
    link=get_link.attrs['href']
    headers={'User-Agent': 'XYZ/3.0'}
    response = requests.get(link, headers=headers).text
    detail_page = BeautifulSoup(response, 'html.parser')
    details=detail_page.find("section",class_="post_content")
    news={}
    news["Announcement Title"]=title.text
    try:
      news["Announcement Description"]=details.text
    except:
      pass
    output.append(news)  
with open("nndc-Announcement.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')

###############EVENTS################
for page in range(1, 7):
  req = Request(f"https://nndc.org/category/events/page/{page}/", headers={'User-Agent': 'XYZ/3.0'})

  webpage = urlopen(req,timeout=10).read()
  news_doc=BeautifulSoup(webpage, 'html.parser')
  items = news_doc.find_all("div", class_="post_content clearfix")
  
  for item in items:
    title =item.find('h3', class_="post_title")
    print(title.text)
    
    get_link = title.find('a')
    link=get_link.attrs['href']
    headers={'User-Agent': 'XYZ/3.0'}
    response = requests.get(link, headers=headers).text
    detail_page = BeautifulSoup(response, 'html.parser')
    details=detail_page.find("section",class_="post_content")
    news={}
    news["Event Title"]=title.text
    try:
      news["Event Description"]=details.text
    except:
      pass
    output.append(news)  
with open("nndc-Events.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


########################myoutcomes websit blogs########################
req = Request(f"https://www.myoutcomes.com/blog-feed", headers={'User-Agent': 'XYZ/3.0'})

webpage = urlopen(req,timeout=10).read()
news_doc=BeautifulSoup(webpage, 'html.parser')
items = news_doc.find_all("div", class_="items-grid__item-body")
  
for item in items:
  title =item.find('div', class_="items-grid__header h3")
  print(title.text)
  try:
    get_link = item.find('a',class_="sb-cta-small")
    link='https://www.myoutcomes.com' + get_link.attrs['href']
    headers={'User-Agent': 'XYZ/3.0'}
    response = requests.get(link, headers=headers).text
    detail_page = BeautifulSoup(response, 'html.parser')
    details=detail_page.find("div",class_="sb-item-view__body")
    news={}
    news["Blog Title"]=title.text
    
    news["Blog Description"]=details.text
  except:
    pass
  output.append(news)  
with open("myoutcomes-blogs.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')



########################mirah case-studies########################
req = Request(f"https://www.mirah.com/case-studies", headers={'User-Agent': 'XYZ/3.0'})

webpage = urlopen(req,timeout=10).read()
news_doc=BeautifulSoup(webpage, 'html.parser')
items = news_doc.find_all("div", class_="list-item-content")
  
for item in items:
  title =item.find('h2', class_="list-item-content__title")
  print(title.text)
  try:
    get_link = item.find('a')
    link=get_link.attrs['href']
    headers={'User-Agent': 'XYZ/3.0'}
    response = requests.get(link, headers=headers).text
    detail_page = BeautifulSoup(response, 'html.parser')
    details=detail_page.find("article",class_="section")
    news={}
    news["Title"]=title.text
    
    news["Description"]=details.text
  except:
    pass
  output.append(news)  
with open("mirah-blogs.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')



