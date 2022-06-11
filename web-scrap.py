import requests

from bs4 import BeautifulSoup
url="https://www.owl.health/blog/"
page = requests.get(url).text
doc=BeautifulSoup(page, 'html.parser')
page_text = doc.find(class_='alignleft').a['href'].split('/')[-2]

print(page_text)

# src=result.content
# soup=BeautifulSoup(src, 'lxml')
# urls = []

# for h2_tag in soup.find_all("h2"):
#   a_tag = h2_tag.find("a")
#   urls.append(a_tag.attrs['href'])
# print(urls)