from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
# import requests
# import ssl
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

#######Scrap visiontree homepage
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
