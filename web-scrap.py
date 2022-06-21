from unicodedata import category
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import json
output=[]

# #https://www.owl.health
# news_url="https://www.owl.health/category/media-hits/"
# news_page = requests.get(news_url).text
# news_doc=BeautifulSoup(news_page, 'html.parser')
# news_pages = int(news_doc.find(class_='alignleft').a['href'].split('/')[-2])

# for page in range(1, news_pages + 1 ):
#   new_url=f"https://www.owl.health/category/media-hits/page/{page}/?et_blog"
#   news_page = requests.get(news_url).text
#   news_doc=BeautifulSoup(news_page, 'html.parser')
#   items = news_doc.find_all(class_="et_pb_post")
#   for item in items:
#     title =item.find(class_="entry-title")
#     get_link = item.find('a')
#     link=get_link.attrs['href']
#     get_details = requests.get(link).text 
#     detail_page = BeautifulSoup(get_details, 'html.parser')
#     details=detail_page.find(class_="field-name-body")
#     news={}
#     news["News Title: "]=title.text
#     try:
#       news["News Description: "]=details.text
#     except:
#       pass
    
#     output.append(news)

#https://azzly.com/blog/

# for page in range(1, 16):
#   press_url=f"https://azzly.com/blog/page/{page}"
#   press_page = requests.get(press_url).text
#   press_doc=BeautifulSoup(press_page, 'html.parser')
#   items = press_doc.find_all(class_="blog-entry")
#   for item in items:
#     title =item.find(class_="blog-entry-title")
#     get_link = item.find('a')
#     link=get_link.attrs['href']
#     get_details = requests.get(link).text 
#     detail_page = BeautifulSoup(get_details, 'html.parser')
#     details=detail_page.find(class_="single-blog-content")
#     press={}
#     press["Press Title: "]=title.text
#     try:
#       press["Press Description: "]=details.text
#     except:
#       pass
    
#     output.append(press)    
    
# with open("azzly-new-blog-data.json", "w") as f:
#   json.dump(output, f, indent=2)
  
  
  
#Betteroutcomenow
# archive_url="https://blog.betteroutcomesnow.com/archive/2022"
# press_urls=int(archive_url.split('/')[-1])


# for url in range(2017, press_urls +1 ):
#   press_url=f"https://blog.betteroutcomesnow.com/archive/{url}/"
#   press_page = requests.get(press_url).text
#   press_doc=BeautifulSoup(press_page, 'html.parser')
#   items = press_doc.find_all(class_="post-item")
  
#   for item in items:
#     title =item.find(class_="post-header")
#     get_link = item.find('a')
#     link=get_link.attrs['href']
#     get_details = requests.get(link).text 
#     detail_page = BeautifulSoup(get_details, 'html.parser')
#     details=detail_page.find(class_="hs_cos_wrapper hs_cos_wrapper_meta_field hs_cos_wrapper_type_rich_text")
#     press={}
#     press["Title: "]=title.text
#     press["Description: "]=details.text
#     output.append(press)    
    
# with open("betteroutcomesnow-archived-blogs-data.json", "w") as f:
#   f.write(json.dumps(output))
 
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage
# from io import StringIO
# output_string = StringIO()
# def convert_pdf_to_txt(path):
#     rsrcmgr = PDFResourceManager()
#     device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
#     fp = open(path, 'rb')
#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     password = ""
#     maxpages = 0
#     caching = True
#     pagenos=set()

#     for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
#         interpreter.process_page(page)

#     text = output_string.getvalue()

#     fp.close()
#     device.close()
#     output_string.close()
#     return text 
  
# import re
# from urllib.request import urlopen
# from urllib.request import urlretrieve

# html = urlopen("https://betteroutcomesnow.com/resources/articles-handouts/")
# html_doc = html.read()

# match = re.search(b'\"(.*?\.pdf)\"', html_doc)
# pdf_url = "" + match.group(1).decode('utf8')
# urlretrieve(pdf_url, "download.pdf")
# text = convert_pdf_to_txt("download.pdf")
# print(text)

# print(pdf_url)



#https://www.blueprint-health.com/
# press_url="https://www.blueprint-health.com/blog"
# press_page = requests.get(press_url).text
# press_doc=BeautifulSoup(press_page, 'html.parser')
# press_pages =int(press_doc.find(class_='w-pagination-wrapper').a['href'].split('=')[-1])

# for page in range(1, press_pages + 1 ):
#   print(page)
#   press_url=f"https://www.blueprint-health.com/blog?cbb911e6_page={page}"
#   press_page = requests.get(press_url).text
#   press_doc=BeautifulSoup(press_page, 'html.parser')
#   items = press_doc.find_all(class_="collection-item-blog")
#   for item in items:
#     title =item.find(class_="title-post")
#     get_link = item.find('a')
#     link=get_link.attrs['href']
#     link="https://www.blueprint-health.com" +link
#     get_details = requests.get(link).text 
#     detail_page = BeautifulSoup(get_details, 'html.parser')
#     details=detail_page.find(class_="rich-text-blog")
#     press={}
#     press["Title"]=title.text
#     press["Description"]=details.text
    
    
#     output.append(press)    
    
# with open("blueprint-health-blogs.json", "a") as f:
#   json.dump(output, f, indent=2)


#https://www.greenspacehealth.com/en-ca/
# press_url="https://www.greenspacehealth.com/en-ca/blog"
# press_page = requests.get(press_url).text
# press_doc=BeautifulSoup(press_page, 'html.parser')
# items = press_doc.find_all(class_="collection-item-3")
# for item in items:
#   title =item.find(class_="blog-heading")
#   get_link = item.find('a')
#   link=get_link.attrs['href']
#   link="https://www.greenspacehealth.com" +link
#   get_details = requests.get(link).text 
#   detail_page = BeautifulSoup(get_details, 'html.parser')
#   details=detail_page.find(class_="container-9 w-container")
#   press={}
#   press["Title"]=title.text

#   press["Description"]=details.text

  
#   output.append(press)    
    
# with open("greenspacehealth-blog-data.json", "a") as f:
#   json.dump(output, f, indent=2)
  
 #https://mdlogix.com
# req = Request('https://mdlogix.com/mdlogix-news/', headers={'User-Agent': 'XYZ/3.0'})
# webpage = urlopen(req, timeout=10).read()
# for page in range(1, 4 ):
#   req = Request(f"https://mdlogix.com/mdlogix-news/page/{page}/", headers={'User-Agent': 'XYZ/3.0'})
  
#   webpage = urlopen(req, timeout=100).read()
#   news_doc=BeautifulSoup(webpage, 'html.parser')
#   items = news_doc.find_all(class_="entry-body")
  
#   for item in items:
#     title =item.find(class_="entry-title")
#     get_link = item.find('a')
#     link=get_link.attrs['href']
#     headers={'User-Agent': 'XYZ/3.0'}
#     response = requests.get(link, headers=headers).text
#     detail_page = BeautifulSoup(response, 'html.parser')
#     details=detail_page.find(class_="entry-content")
#     news={}
#     news["Title"]=title.text
#     news["Description"]=details.text
#     output.append(news) 
    
# with open("mdlogix-news-data.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')

#Simple url scraping
# url_list="https://www.greenspacehealth.com/en-ca/security"
# # empty list to store all results
# req = requests.get(url_list)
# soup = BeautifulSoup(req.text, "html.parser")
# results=soup.find('div',class_="container w-container")
# results=results.find_all('div', class_="column-grow-hover w-col w-col-4")
# for result in results:
#   question =result.find(class_="heading-8")
#   answer = result.find(class_="paragraph")
#   press={}

#   press["Security Feature"]=question.text
#   press["Description"]=answer.text
#   output.append(press)
# with open("greenspacehealth-SecurityFeatures-data.json", "a") as f:
#   json.dump(output, f, indent=2)



#https://www.holmusk.com/publications
# url="https://www.holmusk.com/news"
# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")
# results=soup.find('div',class_="collection-list _3-col _2-col-tablet w-dyn-items")
# results=results.find_all('div', class_="w-dyn-item")
# for result in results:
#   link = result.find('a', class_="link-block-2 w-inline-block")
#   link=link.attrs['href']
  
#   test_cond = str(link)
#   if "holmusk.com" in test_cond:
#     req = requests.get(link)
#     soup = BeautifulSoup(req.text, "html.parser")
#     results=soup.find_all('div',class_="container news-template w-container")

#     for result in results:
#       title =result.find(class_="news-title")
      
#       description = result.find("div",class_="w-richtext")
#       press={}
#       press["News Title"]=title.text
#       press["Details"]=description.text
#       output.append(press)
  
# with open("holmusk-news-events-data.json", "a") as f:
#   json.dump(output, f, indent=2)


# # #owl-health-blog data   
# for page in range(1, 4):
#   blog_url=f"https://www.owl.health/blog/page/{page}/?et_blog"
#   page = requests.get(blog_url).text
#   doc=BeautifulSoup(page, 'html.parser')
#   items = doc.find_all('div', class_="et_pb_salvattore_content")
#   for item in items:
#     title =item.find('h2',class_="entry-title")
#     get_link = item.find('a')
#     link=get_link.attrs['href']
#     details=item.find('div',class_="post-content")
#     get_details = requests.get(link).text 
#     detail_page = BeautifulSoup(get_details, 'html.parser')
#     details=detail_page.find(class_="et_pb_module et_pb_post_content et_pb_post_content_0_tb_body")
    
#     blog={}
    
#     try:
#       blog["Newa Title: "]=title.text
#       blog["News Description: "]=details.text
#     except:
#       pass
#     output.append(blog)
# with open("owl-health-blogs-data.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')

# #media-hits data of owl-health  
# import time
# for page in range(1, 32):
#   time.sleep(3)
#   blog_url=f"https://www.owl.health/newsroom/page/{page}/?et_blog"
#   headers = requests.utils.default_headers()
#   headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
#   page = requests.get(blog_url, headers=headers).text
#   doc=BeautifulSoup(page, 'html.parser')
#   items = doc.find_all('div', class_="et_pb_salvattore_content")
#   for item in items:
#     title =item.find('h2',class_="entry-title")
#     get_link = item.find('a')
#     link=get_link.attrs['href']
#     external_details=item.find('div',class_="post-content")
#     blog={}
#     blog["Newa Title: "]=title.text
#     if "https://www.owl.health" in link:
#       get_details = requests.get(link).text 
#       detail_page = BeautifulSoup(get_details, 'html.parser')
#       details=detail_page.find(class_="et_pb_module et_pb_post_content et_pb_post_content_0_tb_body")
#       if details is not None:
#         blog["News Description: "]=details.text
#     else:
#       blog['Description: '] = external_details.text
#       blog['External Link: '] = link
      
#     output.append(blog)
# with open("owl-health-media-hits-data.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')

#tridiuum news data
# import time
# for page in range(1, 6):
#   time.sleep(3)
#   blog_url=f"https://tridiuum.com/category/news/page/{page}/"
#   headers = requests.utils.default_headers()
#   headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
#   page = requests.get(blog_url, headers=headers).text
#   doc=BeautifulSoup(page, 'html.parser')
#   items = doc.find_all('div', class_="article-inner")
#   for item in items:
#     title =item.find('h2',class_="entry-title")
#     get_link = title.find('a')
#     link=get_link.attrs['href']
#     news={}
#     news["Newa Title: "]=title.text
#     headers = requests.utils.default_headers()
#     headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
#     get_details = requests.get(link,headers=headers).text 
#     detail_page = BeautifulSoup(get_details, 'html.parser')
#     details=detail_page.find('div',class_="entry-content single-page")
#     # details.find('header',class_="entry-header").decompose()
#     # details.find('nav', class_="navigation-post").decompose()
#     news["News Description: "]=details.text      
#     output.append(news)
# with open("tridiuum-news-data.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
  
# #tridiuum news data
# import time
# for page in range(1, 8):
#   time.sleep(3)
#   blog_url=f"https://tridiuum.com/category/blog/page/{page}/"
#   headers = requests.utils.default_headers()
#   headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
#   page = requests.get(blog_url, headers=headers).text
#   doc=BeautifulSoup(page, 'html.parser')
#   items = doc.find_all('div', class_="article-inner")
#   for item in items:
#     title =item.find('h2',class_="entry-title")
#     get_link = title.find('a')
#     link=get_link.attrs['href']
#     news={}
#     news["Newa Title: "]=title.text
#     headers = requests.utils.default_headers()
#     headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
#     get_details = requests.get(link,headers=headers).text 
#     detail_page = BeautifulSoup(get_details, 'html.parser')
#     details=detail_page.find('div',class_="entry-content single-page")
#     news["News Description: "]=details.text      
#     output.append(news)
# with open("tridiuum-blog-data.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')

#Silver cloud health press releases
# import time
# for page in range(1, 13):
#   time.sleep(5)
#   blog_url=f"https://www.silvercloudhealth.com/uk/press_releases/page/{page}"
#   headers = requests.utils.default_headers()
#   headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
#   page = requests.get(blog_url, headers=headers).text
#   doc=BeautifulSoup(page, 'html.parser')
#   items = doc.find_all('div', class_="blog-info-inner")
#   for item in items:
#     title =item.find('h2',class_="silver-heading")
#     get_link = item.find('div',class_="excerpt").find('a')
#     link=get_link.attrs['href']
#     news={}
#     news["Press Title"]=title.text
#     headers = requests.utils.default_headers()
#     headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
#     get_details = requests.get(link,headers=headers).text 
    
#     detail_page = BeautifulSoup(get_details, 'html.parser')
#     details=detail_page.find('div',class_="section post-body")
#     news["Press Description"]=details.text      
#     output.append(news)
# with open("silver-cloud-health-press-releases.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
#Silver cloud health blogs 
# import time
# for page in range(1, 18):
#   time.sleep(5)
#   blog_url=f"https://www.silvercloudhealth.com/uk/blog/page/{page}"
#   headers = requests.utils.default_headers()
#   headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
#   page = requests.get(blog_url, headers=headers).text
#   doc=BeautifulSoup(page, 'html.parser')
#   items = doc.find_all('div', class_="blog-info-inner")
#   for item in items:
#     title =item.find('h2',class_="silver-heading")
#     get_link = item.find('div',class_="excerpt").find('a')
#     link=get_link.attrs['href']
#     news={}
#     news["Blog Title"]=title.text
#     headers = requests.utils.default_headers()
#     headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
#     get_details = requests.get(link,headers=headers).text 
#     detail_page = BeautifulSoup(get_details, 'html.parser')
#     details=detail_page.find('div',class_="section post-body")
#     news["Blog Description"]=details.text    
#     output.append(news)
# with open("silver-cloud-health-press-releases.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
  
#Silver Cloud health content library  
import time
import io
from PyPDF2 import PdfFileReader
resource_url=f"https://www.silvercloudhealth.com/uk/resources"
headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
page = requests.get(resource_url, headers=headers).text
doc=BeautifulSoup(page, 'html.parser')
items = doc.find_all('div', class_="resource")
for item in items:
  time.sleep(3)
  title =item.find('div',class_="resource-heading")
  get_link = item.find('a')
  link=get_link.attrs['href']
  details=item.find('div',class_="resource-description")
  blog={}
  blog["Resource Title"]=title.text
  if "https://www.silvercloudhealth.com/" in link:
    
    if ".pdf" in link:
      page = requests.get(link, headers=headers).text
      doc=BeautifulSoup(page, 'html.parser')
      details = doc.find('div',class_="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_rich_text")
      
      
    else:
      # creating a pdf file object 
      pdfFileObj = open('link', 'rb') 
          
      # creating a pdf reader object 
      pdfReader = PdfFileReader.PdfFileReader(pdfFileObj) 
          
      # printing number of pages in pdf file 
      print(pdfReader.numPages) 
          
      # creating a page object 
      pageObj = pdfReader.getPage(0) 
          
      # extracting text from page 
      print(pageObj.extractText()) 
          
      # closing the pdf file object 
      pdfFileObj.close() 
      
    blog["Resource Description"]=details.text
  else:
    blog["Resource Title"]=title.text
    blog["Resource Link"]=link
    blog["Resource Description"]=details.text
  output.append(blog)
  print(output)
# with open("silver-cloud-health-resources.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')