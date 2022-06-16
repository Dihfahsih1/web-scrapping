from unicodedata import category
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

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

# #blog data   
# blog_url="https://www.owl.health/blog/"
# blog_page = requests.get(blog_url).text
# blog_doc=BeautifulSoup(blog_page, 'html.parser')
# blog_pages = int(blog_doc.find(class_='alignleft').a['href'].split('/')[-2])
   
# for page in range(1, blog_pages + 1 ):
#   blog_url=f"https://www.owl.health/blog/page/{page}/?et_blog"
#   page = requests.get(blog_url).text
#   doc=BeautifulSoup(page, 'html.parser')
#   items = doc.find_all(class_="et_pb_post")
#   for item in items:
#     title =item.find(class_="entry-title")
#     get_link = item.find('a')
#     link=get_link.attrs['href']
#     get_details = requests.get(link).text 
#     detail_page = BeautifulSoup(get_details, 'html.parser')
#     details=detail_page.find(class_="et_pb_post_content")
#     description=item.find(class_="post-content-inner")
    
#     blog={}
#     blog["Blog Title: "]=title.text
#     try:
#       blog["Blog Description: "]=details.text
#     except:
#       pass
#     output.append(blog)

#https://azzly.com/blog/
# press_url="https://azzly.com/blog/"
# press_page = requests.get(press_url).text
# press_doc=BeautifulSoup(press_page, 'html.parser')
# press_pages =int(press_doc.find(class_='page-numbers').a['href'].split('/')[-2])

# for page in range(1, press_pages + 1 ):
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
    
# with open("press-data.json", "w") as f:
#   f.write(json.dumps(output))
  
  
  
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
# news_doc=BeautifulSoup(webpage, 'html.parser')
# news_pages = int(news_doc.find(class_='posts-page-links').a['href'][-2]) 
# for page in range(1, news_pages + 1 ):
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
# with open("mdlogix-news-data.json", "w") as f:
#   f.write(json.dumps(output))   

url_list="https://www.greenspacehealth.com/en-ca/patients"

# empty list to store all results

req = requests.get(url_list)
soup = BeautifulSoup(req.text, "html.parser")
results=soup.find('div',class_="w-dyn-items")
results=results.find_all('div', class_="w-dyn-item")
for result in results:
  question =result.find('div', class_="accordion-title")
  answer = result.find('div', class_="accordion-content w-richtext")
  press={}

  press["Question"]=question.text
  press["Answer"]=answer.text
  output.append(press)
with open("greenspacehealth-FAQ-data.json", "a") as f:
  json.dump(output, f, indent=2)
  
    

  