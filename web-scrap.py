import requests
from bs4 import BeautifulSoup

import json
output=[]

# #news data
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

#press release data
press_url="https://azzly.com/"
press_page = requests.get(press_url).text
press_doc=BeautifulSoup(press_page, 'html.parser')
press_pages = int(press_doc.find(class_='page-numbers').a['href'].split('/')[-2])

for page in range(1, press_pages + 1 ):
  press_url=f"https://www.owl.health/category/media-hits/page/{page}/?et_blog"
  press_page = requests.get(press_url).text
  press_doc=BeautifulSoup(press_page, 'html.parser')
  items = press_doc.find_all(class_="blog-entry")
  for item in items:
    title =item.find(class_="entry-title")
    get_link = item.find('a')
    link=get_link.attrs['href']
    get_details = requests.get(link).text 
    detail_page = BeautifulSoup(get_details, 'html.parser')
    details=detail_page.find(class_="field-name-body")
    press={}
    press["Press Title: "]=title.text
    try:
      press["Press Description: "]=details.text
    except:
      pass
    
    output.append(press)    
    
with open("press-data.json", "w") as f:
  f.write(json.dumps(output))
  


