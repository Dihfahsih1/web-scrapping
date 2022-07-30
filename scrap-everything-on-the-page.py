from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# from email.policy import strict
# from unicodedata import category
# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup
# import requests
# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context

# import json
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
# import time
# from io import StringIO,BytesIO
# from PyPDF2 import PdfFileReader, PdfFileWriter
# resource_url=f"https://www.silvercloudhealth.com/uk/resources"
# headers = requests.utils.default_headers()
# headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
# page = requests.get(resource_url, headers=headers).text
# doc=BeautifulSoup(page, 'html.parser')
# items = doc.find_all('div', class_="resource")
# for item in items:
#   time.sleep(3)
#   title =item.find('div',class_="resource-heading")
#   get_link = item.find('a')
#   link=get_link.attrs['href']
#   details=item.find('div',class_="resource-description")
#   blog={}
#   blog["Resource Title"]=title.text
#   if "https://www.silvercloudhealth.com/" in link:
#     if ".jpg" not in link:
#       if ".pdf" not in link:
#         page = requests.get(link, headers=headers).text
#         doc=BeautifulSoup(page, 'html.parser')
#         details = doc.find('span',class_="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_rich_text")
#         blog["Resource Title"]=title.text
#         blog["Resource Description"]=details.text
#       else:
#         # creating a pdf file object 
#         pdfFileObj = requests.get(link)
#         writer = PdfFileWriter()
#         remoteFile = urlopen(Request(link)).read()
#         memoryFile = BytesIO(remoteFile)
#         pdfReader = PdfFileReader(memoryFile, strict=False)          
#         # creating a page object 
#         pageObj = pdfReader.getPage(0) 
            
#         # extracting text from page 
#         details=pageObj.extractText()
#         blog["Resource Title"]=title.text
#         blog["Resource Description"]=details
#         blog["Resource Pdf Link"]=link 
#         pdfFileObj.close() 
#   else:
#     blog["Resource Title"]=title.text
#     blog["Resource Link"]=link
#     blog["Resource Description"]=details.text
#   output.append(blog)
# with open("silver-cloud-health-resources.txt", "a") as f:
#   output=str(output)
#   f.write(output)


#oqmeasures-news
# url="https://www.oqmeasures.com/category/oq-news/"
# headers = requests.utils.default_headers()
# headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
# req = requests.get(url, headers=headers)
# soup = BeautifulSoup(req.text, "html.parser")
# main=soup.find('main',class_="site-main")
# results=main.find_all('div', class_="card-body")
# for result in results:
#   title=result.find('h2', class_="entry-title card-title h3")
#   link = title.find('a', class_="text-dark")
#   link=link.attrs['href']
#   req = requests.get(link, headers=headers)
#   soup = BeautifulSoup(req.text, "html.parser")
#   details=soup.find('div',class_="card-body")
#   if details is not None:
#     details.find('header', class_="entry-header").decompose()
#     press={}
#     press["News Title"]=title.text
#     press["Details"]=details.text
#     output.append(press)
  
# with open("oqmeasures-news.text", "a") as f:
#   output=str(output)
#   f.write(output)

# ssl._create_default_https_context = ssl._create_unverified_context
# import json
# output=[]

# #############wesanahealth.com####################
# #https://www.wesanahealth.com/  
# press_url='https://wesanahealth.com/media-room/'
# press_page = requests.get(press_url).text
# press_doc=BeautifulSoup(press_page, 'html.parser')
# items = press_doc.find_all(class_="elementor-post__text")
# for item in items:
#   link="https://wesanahealth.com/in-the-news/wesana-health-ceo-daniel-carcillo-to-keynote-charles-river-symposium-re-imagining-substance-abuse-addiction-and-mental-health-disorders-with-psychedelic-therapies/"
#   headers={'User-Agent': 'XYZ/3.0'}
#   response = requests.get(link, headers=headers).text
#   detail_page = BeautifulSoup(response, 'html.parser')
#   details=detail_page.find("div", {"itemprop": "articleBody"})
#   title=detail_page.find("h1", {"itemprop": "headline"})
#   news={}
#   news["Title"]=title.text
#   news["Description"]=details.text
#   output.append(news) 
# with open("wesanahealth-media-release-data.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
  
# ##wesana-health-news https://ir.wesanahealth.com/news-events/press-releases

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
  
  

# ####Scraping FQA of wesanahealth
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
  
# ###Scraping FQA of wesanahealth
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


# # not-working
# # req = Request(f"https://visiontree.com/press-releases/", headers={'User-Agent': 'XYZ/3.0'})
# # webpage = urlopen(req, timeout=100).read()
# # news_doc=BeautifulSoup(webpage, 'html.parser')
# # items = news_doc.find_all("tbody")
# # for item in items:
# #   data =item.find('td', class_="px-6 py-4 text-gray-500")
# #   get_link = data.find('a')
# #   link="https://visiontree.com/press-releases"+ get_link.attrs['href']
# #   headers={'User-Agent': 'XYZ/3.0'}
# #   response = requests.get(link, headers=headers).text
# #   detail_page = BeautifulSoup(response, 'html.parser')
# #   print(detail_page.text)
# #   details=detail_page.find("div",class_="pageWrap pageWrap--m")
  
# #   title=detail_page.find('div',class_="relative")
# #   detail_page.find('div', class_="flex items-center justify-between mb-6").decompose()
# #   news={}
# #   news["Title"]=title.text
# #   news["Description"]=details.text
# #   output.append(news) 
  
# # with open("visiontree-press-releases.txt", "a") as f:
# #   output=str(output)
# #   f.write(output)
# #   f.write('\n')


# #Valant-blogs
# for page in range(1, 29 ):
#   req = Request(f"https://www.valant.io/blog/page/{page}/", headers={'User-Agent': 'XYZ/3.0'})

#   webpage = urlopen(req,timeout=100).read()
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
#     news["Blog Title"]=title.text
#     news["Blog Description"]=details.text
#     output.append(news)  
# with open("valant-blog.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
# #Valant-Webinars
# for page in range(1, 3 ):
#   req = Request(f"https://www.valant.io/webinars/page/{page}", headers={'User-Agent': 'XYZ/3.0'})

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
  

# Valant-case-studies

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

# #https://blog.nview.com/
# for page in range(1, 10 ):
#   req = Request(f"https://blog.nview.com/page/{page}", headers={'User-Agent': 'XYZ/3.0'})

#   webpage = urlopen(req,timeout=10).read()
#   news_doc=BeautifulSoup(webpage, 'html.parser')
#   items = news_doc.find_all("article", class_="blog-index__post blog-index__post--small")
  
#   for item in items:
#     title =item.find('h4', class_="blog-index-title")
    
#     get_link = item.find('a')
#     link=get_link.attrs['href']
#     headers={'User-Agent': 'XYZ/3.0'}
#     response = requests.get(link, headers=headers).text
#     detail_page = BeautifulSoup(response, 'html.parser')
#     details=detail_page.find("div",class_="blog-post__body")
#     news={}
#     news["Blog Title"]=title.text
#     try:
#       news["Blog Description"]=details.text
#     except:
#       pass
#     output.append(news)  
# with open("nview-blog.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
  

# #############################blog.nview.com/tag/################################
# req = Request(f"https://blog.nview.com/tag/nview-press-releases/page/3", headers={'User-Agent': 'XYZ/3.0'})

# webpage = urlopen(req,timeout=10).read()
# news_doc=BeautifulSoup(webpage, 'html.parser')
# items = news_doc.find_all("article", class_="blog-index__post blog-index__post--small")

# for item in items:
#   title =item.find('h4', class_="blog-index-title")
  
#   get_link = item.find('a')
#   link=get_link.attrs['href']
#   headers={'User-Agent': 'XYZ/3.0'}
#   response = requests.get(link, headers=headers).text
#   detail_page = BeautifulSoup(response, 'html.parser')
#   details=detail_page.find("div",class_="blog-post__body")
#   news={}
#   news["Blog Title"]=title.text
#   try:
#     news["Blog Description"]=details.text
#   except:
#     pass
#   output.append(news)  
# with open("nview-press-releases.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  

# ####################https://www.nssbehavioralhealth.com/ website#################
# req = Request(f"https://www.nssbehavioralhealth.com/nextstep-solutions-blog/", headers={'User-Agent': 'XYZ/3.0'})

# webpage = urlopen(req,timeout=10).read()
# news_doc=BeautifulSoup(webpage, 'html.parser')
# items = news_doc.find_all("div", class_="q_masonry_blog_post_text")

# for item in items:
#   title =item.find('h5', class_="q_masonry_blog_title entry_title")
  
#   get_link = title.find('a')
#   link=get_link.attrs['href']
#   headers={'User-Agent': 'XYZ/3.0'}
#   response = requests.get(link, headers=headers).text
#   detail_page = BeautifulSoup(response, 'html.parser')
#   details=detail_page.find("div",class_="post_text_inner")
#   news={}
#   news["Blog Title"]=title.text
#   try:
#     news["Blog Description"]=details.text
#   except:
#     pass
#   output.append(news)  
# with open("nssbehavioralhealth-blogs.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')


# ################https://www.neuroflow.com/BLOGS/#############################
# for page in range(1, 10 ):
#   req = Request(f"https://www.neuroflow.com/blog/page/{page}/", headers={'User-Agent': 'XYZ/3.0'})

#   webpage = urlopen(req,timeout=10).read()
#   news_doc=BeautifulSoup(webpage, 'html.parser')
#   items = news_doc.find_all("div", class_="entry-content-wrap")
  
#   for item in items:
#     title =item.find('h3', class_="entry-post-title")
#     print(title.text)
    
#     get_link = title.find('a')
#     link=get_link.attrs['href']
#     headers={'User-Agent': 'XYZ/3.0'}
#     response = requests.get(link, headers=headers).text
#     detail_page = BeautifulSoup(response, 'html.parser')
#     details=detail_page.find("div",class_="entry-content clearfix")
#     news={}
#     news["Blog Title"]=title.text
#     try:
#       news["Blog Description"]=details.text
#     except:
#       pass
#     output.append(news)  
# with open("neuroflow-blog.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
# ################https://www.neuroflow.com/PRESS/#############################
# for page in range(1, 4 ):
#   req = Request(f"https://www.neuroflow.com/press/page/{page}/", headers={'User-Agent': 'XYZ/3.0'})

#   webpage = urlopen(req,timeout=10).read()
#   news_doc=BeautifulSoup(webpage, 'html.parser')
#   items = news_doc.find_all("div", class_="entry-content-wrap clearfix")
  
#   for item in items:
#     title =item.find('h3', class_="entry-post-title")
#     print(title.text)
    
#     get_link = title.find('a')
#     link=get_link.attrs['href']
#     headers={'User-Agent': 'XYZ/3.0'}
#     response = requests.get(link, headers=headers).text
#     detail_page = BeautifulSoup(response, 'html.parser')
#     details=detail_page.find("div",class_="entry-content clearfix")
#     news={}
#     news["Press Title"]=title.text
#     try:
#       news["Press Description"]=details.text
#     except:
#       pass
#     output.append(news)  
# with open("neuroflow-Press.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
# req = Request(f"https://www.neuroflow.com/research/", headers={'User-Agent': 'XYZ/3.0'})

# webpage = urlopen(req,timeout=10).read()
# news_doc=BeautifulSoup(webpage, 'html.parser')
# items = news_doc.find_all("div", class_="vc_row wpb_row vc_row-fluid vc_column-gap-25") 
# for item in items:
#   details=item.find("div",class_="w-author-desc")
#   title=item.find("h3")
#   news={}
#   news["Research Title"]=title.text
#   try:
#     news["Research Description"]=details.text
#   except:
#     pass
#   output.append(news)  
# with open("neuroflow-Research.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')



# ####################https://www.neuroblu.ai/ website#################
# req = Request(f"https://www.neuroblu.ai/announcements/", headers={'User-Agent': 'XYZ/3.0'})

# webpage = urlopen(req,timeout=10).read()
# news_doc=BeautifulSoup(webpage, 'html.parser')
# items = news_doc.find_all("div", class_="collection-item-4 w-dyn-item")

# for item in items:
#   title =item.find('h3', class_="heading-3 nrelease announcements")
  
#   get_link = item.find('a')
#   link='https://www.neuroblu.ai' + get_link.attrs['href']
#   headers={'User-Agent': 'XYZ/3.0'}
#   response = requests.get(link, headers=headers).text
#   detail_page = BeautifulSoup(response, 'html.parser')
#   details=detail_page.find("div",class_="rich-text-block w-richtext")
#   news={}
#   news["Announcement Title"]=title.text
#   try:
#     news["Announcement Description"]=details.text
#   except:
#     pass
#   output.append(news)  
# with open("neuroblu-announcements.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')

# ###Use Cases
# link='https://www.neuroblu.ai/use-cases/analyzing-hospitalization-rate-treatment-switch-and-effectiveness-between-two-mdd-drugs'
# headers={'User-Agent': 'XYZ/3.0'}
# response = requests.get(link, headers=headers).text
# detail_page = BeautifulSoup(response, 'html.parser')
# title=detail_page.find("h2",class_="heading-29")
# details=detail_page.find("div",class_="rich-text-block w-richtext")
# news={}
# news["Usecase Title"]=title.text
# try:
#   news["Usecase Description"]=details.text
# except:
#   pass
# output.append(news)  
# with open("neuroblu-usecases.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')


# ################https://nndc.org/announcements/#############################
# for page in range(1, 3):
#   req = Request(f"https://nndc.org/category/announcements/page/{page}/", headers={'User-Agent': 'XYZ/3.0'})

#   webpage = urlopen(req,timeout=10).read()
#   news_doc=BeautifulSoup(webpage, 'html.parser')
#   items = news_doc.find_all("div", class_="post_content clearfix")
  
#   for item in items:
#     title =item.find('h3', class_="post_title")
#     print(title.text)
    
#     get_link = title.find('a')
#     link=get_link.attrs['href']
#     headers={'User-Agent': 'XYZ/3.0'}
#     response = requests.get(link, headers=headers).text
#     detail_page = BeautifulSoup(response, 'html.parser')
#     details=detail_page.find("section",class_="post_content")
#     news={}
#     news["Announcement Title"]=title.text
#     try:
#       news["Announcement Description"]=details.text
#     except:
#       pass
#     output.append(news)  
# with open("nndc-Announcement.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')

# ###############EVENTS################
# for page in range(1, 7):
#   req = Request(f"https://nndc.org/category/events/page/{page}/", headers={'User-Agent': 'XYZ/3.0'})

#   webpage = urlopen(req,timeout=10).read()
#   news_doc=BeautifulSoup(webpage, 'html.parser')
#   items = news_doc.find_all("div", class_="post_content clearfix")
  
#   for item in items:
#     title =item.find('h3', class_="post_title")
#     print(title.text)
    
#     get_link = title.find('a')
#     link=get_link.attrs['href']
#     headers={'User-Agent': 'XYZ/3.0'}
#     response = requests.get(link, headers=headers).text
#     detail_page = BeautifulSoup(response, 'html.parser')
#     details=detail_page.find("section",class_="post_content")
#     news={}
#     news["Event Title"]=title.text
#     try:
#       news["Event Description"]=details.text
#     except:
#       pass
#     output.append(news)  
# with open("nndc-Events.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')


# ########################myoutcomes websit blogs########################
# req = Request(f"https://www.myoutcomes.com/blog-feed", headers={'User-Agent': 'XYZ/3.0'})

# webpage = urlopen(req,timeout=10).read()
# news_doc=BeautifulSoup(webpage, 'html.parser')
# items = news_doc.find_all("div", class_="items-grid__item-body")
  
# for item in items:
#   title =item.find('div', class_="items-grid__header h3")
#   print(title.text)
#   try:
#     get_link = item.find('a',class_="sb-cta-small")
#     link='https://www.myoutcomes.com' + get_link.attrs['href']
#     headers={'User-Agent': 'XYZ/3.0'}
#     response = requests.get(link, headers=headers).text
#     detail_page = BeautifulSoup(response, 'html.parser')
#     details=detail_page.find("div",class_="sb-item-view__body")
#     news={}
#     news["Blog Title"]=title.text
    
#     news["Blog Description"]=details.text
#   except:
#     pass
#   output.append(news)  
# with open("myoutcomes-blogs.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')


########################mirah case-studies########################
# output=[]
# req = Request(f"https://www.mirah.com/case-studies", headers={'User-Agent': 'XYZ/3.0'})

# webpage = urlopen(req,timeout=10).read()
# news_doc=BeautifulSoup(webpage, 'html.parser')
# items = news_doc.find_all("div", class_="list-item-content")
  
# for item in items:
#   title =item.find('h2', class_="list-item-content__title")
#   print(title.text)
#   try:
#     get_link = item.find('a')
#     link=get_link.attrs['href']
#     headers={'User-Agent': 'XYZ/3.0'}
#     response = requests.get(link, headers=headers).text
#     detail_page = BeautifulSoup(response, 'html.parser')
#     details=detail_page.find("article",class_="section")
#     news={}
#     news["Title"]=title.text
    
#     news["Description"]=details.text
#   except:
#     pass
#   output.append(news)  
# with open("mirah-blogs.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
########################################################################
# Scrap Dynamic data from https://ksanahealth.com/mental-health-blog
# /The website uses dynamically loaded conetnt using javascript, so i didn't scrap it like previously did for the rest but used 
# 1: Right-click on page and select 'Inspect'.
# 2 - Select 'Network' tab. 
# 3: Click on the 'Show more' button. 
# 4: See the ajax call (url) appearing in network tab  then check the ajax that loads the content and manually pick the url and use it after determining the number of pages on count of show more loads in this case they were for counts     

#data scrapped on july 21 2022                                     
#####################################################################

# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }

# output = []

# r = requests.get(f'https://ksanahealth.com/wp-admin/admin-ajax.php?id=&post_id=107&slug=mental-health-blog&canonical_url=https%3A%2F%2Fksanahealth.com%2Fmental-health-blog%2F&posts_per_page=10&page=4&offset=0&post_type=post&repeater=default&seo_start_page=1&preloaded=false&preloaded_amount=0&order=DESC&orderby=date&action=alm_get_posts&query_type=standard', headers=headers)
# soup = BeautifulSoup(r.json()['html'], 'html.parser')
# for item in soup.select('div.post-item'):
#   title=item.select_one('h4').text.strip()
#   get_link=item.select_one('a.more-link').get('href')
  
#   response = requests.get(get_link, headers=headers).text
#   detail_page = BeautifulSoup(response, 'html.parser')
#   if 'https://ksanahealth.com/' in get_link:
#     try:
#       details=detail_page.select_one("div.blog-post__body")
#       news={}
#       news["Blog Title"]=title
      
#       news["Blog Description"]=details.text
#       output.append(news) 
#     except:
#       pass
# with open("ksanahealth-blogs.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')


##########Scrap the ksanahealth Announcements ###########
#data scrapped on july 21 2022      
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://ksanahealth.com/newsroom/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# data = soup.find('ul' ,class_='wp-block-latest-posts__list has-dates wp-block-latest-posts')
# items = data.find_all('li')
# for item in items:
#   get_link=item.select_one('a.wp-block-latest-posts__post-title').get('href')
#   if 'https://ksanahealth.com/' in get_link:
#     response = requests.get(get_link, headers=headers).text
#     detail_page = BeautifulSoup(response, 'html.parser')
#     title=detail_page.select_one("h1.postmtitle")
#     details=detail_page.select_one("div.blog-post__body")
#     news={}
#     news["Announcement Title"]=title.text
#     news["Announcement Description"]=details.text
#     output.append(news) 
# with open("ksanahealth-Announcement.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  

#######Scrap ksanahealth Product features - evidence part
#data scrapped on july 21 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://ksanahealth.com/evidence/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="hs-evdnce-pg-inner")
# output=output.text

# with open("ksanahealth-products-evidence.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
  
#######Scrap ksanahealth Product features - evidence part
#data scrapped on july 21 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://ksanahealth.com/ears/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('main', class_="body-container-wrapper")
# output=output.text

# with open("ksanahealth-products-ears.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  

#######Scrap ksanahealth Product features - evidence part
#data scrapped on july 21 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://ksanahealth.com/vira/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('main', class_="body-container-wrapper")
# output=output.text

# with open("ksanahealth-products-viral-management.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')

##########Scrap the futuresrecoveryhealthcare news pr ###########
#data scrapped on july 21 2022      
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://futuresrecoveryhealthcare.com/news-pr/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# items = soup.find_all('a', class_="content-pane")
# for item in items:
#   try:
#     get_link=item.get('href')
#     if 'https://futuresrecoveryhealthcare.com' in get_link:
#       response = requests.get(get_link, headers=headers).text
#       detail_page = BeautifulSoup(response, 'html.parser')
#       title=detail_page.select_one("header.entry-header")
#       details=detail_page.select_one("div.entry-content")
#       news={}
#       news["News Title"]=title.text
#       news["News Description"]=details.text
#       output.append(news) 
#   except:
#     pass
# with open("futuresrecoveryhealthcare-news-pr.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')


##########Scrap the futuresrecoveryhealthcare Blogs ###########
#data scrapped on july 21 2022      
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://futuresrecoveryhealthcare.com/blog/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# items = soup.find_all('a', class_="content-pane")
# for item in items:
#   try:
#     get_link=item.get('href')
#     if 'https://futuresrecoveryhealthcare.com' in get_link:
#       response = requests.get(get_link, headers=headers).text
#       detail_page = BeautifulSoup(response, 'html.parser')
#       title=detail_page.select_one("h1.entry-title")
#       dates=detail_page.select_one("div.entry-meta")
#       details=detail_page.select_one("div.entry-content")
#       news={}
#       news["Blog Title"]=title.text
#       news["Blog  Date"]=dates.text
#       news["Blog Description"]=details.text
#       output.append(news) 
#   except:
#     pass
# with open("futuresrecoveryhealthcare-blogs.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  

#######Scrap fit-outcomes Product features - evidence part
#data scrapped on july 21 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://blog.fit-outcomes.com/en/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="site-content")
# output=output.text

# with open("fit-outcomes-blog.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')


# #######Scrap fit-outcomes Product FAQ
# #data scrapped on july 21 2022  
# import urllib  
# user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
# headers={'User-Agent':user_agent,} 
# url='https://www.fit-outcomes.com/help/faq'
# output = []
# request = urllib.request.Request(url,None,headers)
# webpage = request.urlopen(request).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# x =soup.find('div', class_="table-responsive vte3")
# output=x.text

# with open("fit-outcomes-FAQ.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')

#######Scrap celesthealth News
#data scrapped on july 23 2022  
# import urllib  
# user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
# headers={'User-Agent':user_agent,} 

# r = Request(f'https://www.celesthealth.com/news.asp', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output = []
# x =soup.find('div', class_="main_content_subPage")
# output=x.text

# with open("celesthealth-news.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
#######Scrap celesthealth Methods
#data scrapped on july 23 2022  
# import urllib  
# user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
# headers={'User-Agent':user_agent,} 

# r = Request(f'https://www.celesthealth.com/method.asp', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output = []
# x =soup.find('div', class_="main_content_body")
# output=x.text

# with open("celesthealth-methods.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')


#######Scrap celesthealth instruments
#data scrapped on july 23 2022  
# import urllib  
# user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
# headers={'User-Agent':user_agent,} 

# r = Request(f'https://www.celesthealth.com/instruments.asp', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output = []
# x =soup.find('div', class_="main_content_body")
# output=x.text

# with open("celesthealth-instruments.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
  
#######Scrap celesthealth instruments
#data scrapped on july 23 2022  
# import urllib  
# user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
# headers={'User-Agent':user_agent,} 

# r = Request(f'https://www.celesthealth.com/about.asp', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output = []
# x =soup.find('div', class_="main_content_body")
# output=x.text

# with open("celesthealth-about.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
  
# #mhoutcomes-Insights --> download brief description of the insights
# output=[]
# for page in range(1, 4 ):
#   req = Request(f"https://mhoutcomes.com/insights/page/{page}/", headers={'User-Agent': 'XYZ/3.0'})

#   webpage = urlopen(req,timeout=100).read()
#   news_doc=BeautifulSoup(webpage, 'html.parser')
#   items = news_doc.find_all("div", class_="blog-details-wrap clearfix")

#   for item in items:
#     try:
      
#       title =item.find('h3', itemprop="name headline")
#       get_link = item.find('a',class_="link-to-post")
#       link=get_link.attrs['href']
      
#       response = requests.get(link, {'User-Agent': 'XYZ/3.0'}).text
#       soup = BeautifulSoup(response, 'html.parser')
#       details=soup.find("section",class_="page-content clearfix container")
#       news={}
#       news["Insight Title"]=title.text
#       news["Insight Description"]=details.text
#       output.append(news)  
#     except:
#       pass
# with open("mhoutcomes-Insights.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
  
  
#   #######Scrap outcomereferrals -about-mission
# #data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/about-us/mission', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="sub-page-content-wrapper")
# output=output.text

# with open("outcomereferrals-about-mission.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')



  #######Scrap outcomereferrals -about-history
#data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/about-us/history', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="sub-page-content-wrapper")
# output=output.text

# with open("outcomereferrals-about-history.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
#######Scrap outcomereferrals -about-team
#data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/about-us/team', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="sub-page-content-wrapper")
# output=output.text

# with open("outcomereferrals-about-team.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')

#######Scrap outcomereferrals top-assessment/top-assessment
#data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/top-assessment/top-assessment', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="main-content")
# output=output.text

# with open("outcomereferrals-top-assessment-top-assessment.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')  
  
  
  
#######Scrap outcomereferrals top-assessment/top-assessment
#data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/outcome-measurement/outcome-measurement', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="main-content")
# output=output.text

# with open("outcomereferrals-outcome-measurement.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 
  
  
#######Scrap outcomereferrals validation-articles
#data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/validation-research/validation-articles', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="main-content")
# output=output.text

# with open("outcomereferrals-validation-articles.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 
  
  
# #######Scrap outcomereferrals validation-articles
# #data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/child-welfare/child-welfare', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="main-content")
# output=output.text

# with open("outcomereferrals-child-welfare.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 


#######Scrap outcomereferrals testimonies
#data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/child-welfare/testimonial-from-dr-drendel', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="main-content")
# output=output.text

# with open("outcomereferrals-testimonies.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 
  
  
#######Scrap outcomereferrals joint-commission
#data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/joint-commission', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="main-content")
# output=output.text

# with open("outcomereferrals-joint-commission.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 
  
  
#######Scrap visiontree homepage
#data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://visiontree.com/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="flex-grow")
# output=output.text

# with open("visiontree-homepage.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 
  
  
#######Scrap visiontree clinical
#data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://visiontree.com/solutions/clinical/patient-centered-outcomes/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="flex flex-col h-screen")
# output=output.text

# with open("visiontree-clinical.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 
  
# #######Scrap visiontree outcomes
# #data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://visiontree.com/solutions/research/patient-centered-outcomes/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="flex flex-col h-screen")
# output=output.text

# with open("visiontree-patient-centered-outcomes.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 
  
  
#######Scrap visiontree solutions packages
#data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://visiontree.com/solutions/packages/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8")
# output=output.text

# with open("visiontree-solution-packages.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 
  
  
#######Scrap visiontree solutions-patient-portal
#data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://visiontree.com/solutions/patient-portal/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8")
# output=output.text

# with open("visiontree-solutions-patient-portal.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 
  
#######Scrap visiontree telehealth
#data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://visiontree.com/telehealth-and-covid19-toolkit/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8")
# output=output.text

# with open("visiontree-telehealth.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 
  
#######Scrap visiontree provenchoice
#data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://visiontree.com/proven-choice/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8")
# output=output.text

# with open("visiontree-proven-choice.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 
  
  
#######Scrap visiontree patients-reported-outcomes
#data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://visiontree.com/patient-reported-outcomes/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="mx-auto max-w-md px-4 sm:max-w-3xl sm:px-6 lg:max-w-7xl lg:px-8")
# output=output.text

# with open("visiontree-patient-reported-outcomes.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 


#######Scrap visiontree macra-mips
#data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://visiontree.com/macra-mips/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="flex-grow")
# output=output.text

# with open("visiontree-highlights.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 
  
  
#######Scrap visiontree macra-mips
#data scrapped on july 23 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://visiontree.com/vtoc-roi/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8")
# output=output.text

# with open("visiontree-return-on-investiments.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 


##########Scrap the visiontree press release ###########
#data scrapped on july 23 2022      
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://visiontree.com/press-releases/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# data=soup.find('tbody',)
# items = data.find_all('tr')
# for item in items:
#   try:
#     get_link = item.find('a', class_='link')
#     Date=item.find('td', class_="px-6 py-4 align-top font-medium w-1/4")
    
#     title=item.find('td', class_="px-6 py-4 text-gray-500")
#     link='https://visiontree.com'+get_link.attrs['href']
#     response = requests.get(link, headers=headers).text
#     detail_page = BeautifulSoup(response, 'html.parser')
#     details=detail_page.find("div", class_="pageWrap pageWrap--m")
     
#     news={}
#     news["Press Date"]=Date.text
#     news["Press Title"]=title.text
#     news["Press Description"]=details.text
#     output.append(news) 
#   except:
#     pass
# with open("visiontree-press-releases.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
##########visiontree case studies and patient voices are external links###########

#######Scrap azzly homepage
#data scrapped on july 30 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://azzly.com/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="vc_row wpb_row vc_inner vc_row-fluid vc_column-gap-20 vc_row-o-equal-height vc_row-o-content-middle vc_row-flex")
# output=output.text

# with open("azzly-testimonies.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 


#######Scrap about better outcomes
#data scrapped on july 30 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://betteroutcomesnow.com/about-bon/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="wrapper white")
# output=output.text

# with open("betteroutcomesnow-about.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 
  
# #######Scrap about better outcomes-pcoms
# #data scrapped on july 30 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://betteroutcomesnow.com/about-pcoms/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="wrapper white")
# output=output.text

# with open("betteroutcomesnow-about-pcoms.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 


#######Scrap about better outcomes top tens
#data scrapped on july 30 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://betteroutcomesnow.com/about-pcoms/top-ten/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="wrapper white")
# output=output.text

# with open("betteroutcomesnow-about-top-tens.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 




# #######Scrap about better outcomes pcoms-implementation
# #data scrapped on july 30 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://betteroutcomesnow.com/about-pcoms/pcoms-implementation/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="wrapper white")
# output=output.text

# with open("betteroutcomesnow-about-pcoms-implementation.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 


#######Scrap about better outcomes pcoms-evidence-based-practic
#data scrapped on july 30 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://betteroutcomesnow.com/about-pcoms/pcoms-implementation/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="wrapper white")
# output=output.text

# with open("betteroutcomesnow-about-pcomsevidence-based-practic.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 
  
# #######Scrap about better outcomes taam
# #data scrapped on july 30 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://betteroutcomesnow.com/about-bon/our-team/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="wrapper white")
# output=output.text

# with open("betteroutcomesnow-team.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n') 


# #######Scrap about better outcomes pcoms-training
# #data scrapped on july 30 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://betteroutcomesnow.com/resources/pcoms-training/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="wrapper white")
# output=output.text

# with open("betteroutcomesnowp-coms-training.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')

# #######Scrap bhworks-page
# #data scrapped on july 30 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f' https://mdlogix.com/bhworks-page/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="elementor-section-wrap")
# output=output.text

# with open("mdlogix-bhworks.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')


# #######Scrap bhworks-for-schools
# #data scrapped on july 30 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://mdlogix.com/for-schools/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="elementor-section-wrap")
# output=output.text

# with open("mdlogix-for-schools.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')

#######Scrap bhworks-for-healthcare-providers
#data scrapped on july 30 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://mdlogix.com/for-healthcare-providers/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="elementor-section-wrap")
# output=output.text

# with open("mdlogix-for-healthcare-providers.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')
  
  
# #######Scrap bhworks-for-employers
# #data scrapped on july 30 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://mdlogix.com/for-employers/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="elementor-section-wrap")
# output=output.text

# with open("mdlogix-for-employers.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')

# #######Scrap bhworks-for-community
# #data scrapped on july 30 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://mdlogix.com/community/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="elementor-section-wrap")
# output=output.text

# with open("mdlogix-for-community.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')


# #######Scrap bhworks-for-collaboration-partners-advisor
# #data scrapped on july 30 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://mdlogix.com/collaboration-partners-advisors/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="elementor-section-wrap")
# output=output.text

# with open("mdlogix-for-collaboration-partners-advisors.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')

# #######Scrap bhworks-for-crms-page
# #data scrapped on july 30 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://mdlogix.com/crms-page/', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="elementor-section-wrap")
# output=output.text

# with open("mdlogix-crms-page.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')

#######Scrap blueprint-health-who-we-serve
# # #data scrapped on july 31 2022    
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
# output = []
# r = Request(f'https://www.blueprint-health.com/who-we-serve/clients', headers=headers)
# webpage = urlopen(r,timeout=10).read()
# soup=BeautifulSoup(webpage, 'html.parser')
# output =soup.find('div', class_="section new gray wf-section")
# output=output.text

# with open("blueprint-health-who-we-serve.txt", "a") as f:
#   output=str(output)
#   f.write(output)
#   f.write('\n')


#######Scrap blueprint-solutions-assessments
# # #data scrapped on july 31 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://www.blueprint-health.com/solutions/assessments', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="feature-columns w-row")
output=output.text

with open("blueprint-solutions-assessments.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')



