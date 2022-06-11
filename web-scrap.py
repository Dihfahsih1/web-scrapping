import requests
from bs4 import BeautifulSoup

import json
url="https://www.owl.health/blog/"
page = requests.get(url).text
doc=BeautifulSoup(page, 'html.parser')
pages = int(doc.find(class_='alignleft').a['href'].split('/')[-2])
output=[]
for page in range(1, pages + 1 ):
  url=f"https://www.owl.health/blog/page/{page}/?et_blog"
  page = requests.get(url).text
  doc=BeautifulSoup(page, 'html.parser')
  items = doc.find_all(class_="et_pb_post")
  for item in items:
    title =item.find(class_="entry-title")
    get_link = item.find('a')
    link=get_link.attrs['href']
    get_details = requests.get(link).text 
    detail_page = BeautifulSoup(get_details, 'html.parser')
    details=detail_page.find(class_="et_pb_post_content")
    description=item.find(class_="post-content-inner")
    
    blog={}
    blog["Blog Title"]=title.text
    try:
      blog["Blog Description"]=details.text
    except:
      pass
    
    output.append(blog)
print(json.dumps(output))
with open("outfile.json", "w") as f:
  f.write(json.dumps(output))
  

# src=result.content
# soup=BeautifulSoup(src, 'lxml')
# urls = []

# for h2_tag in soup.find_all("h2"):
#   a_tag = h2_tag.find("a")
#   urls.append(a_tag.attrs['href'])
# print(urls)