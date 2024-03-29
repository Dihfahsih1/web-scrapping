'''
The imports are used to access the python library classes 
that are used to implement code reusability
importantly, use pip install bs4 from which we can access the BeautifulSoup class that is used 
for parsing the websites to be scrapped HTML document. We use it to extract data from the HTML of the
website we are scraping
Use pip install to install the following packages
bs4 -> Beautiful Soup is a python library used for pulling data out of HTML and XML files
pdfminer ->This is a python library used for extracting pdf documents from the web
PyPDF2 -> Used to transform the pafes of pdf files
requests -> Allows you to send HTTP/1.1 requests extremely easily

'''


from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from io import StringIO,BytesIO
import time
import requests

# # ssl._create_default_https_context = ssl._create_unverified_context

#This is an empty list from which scrapped text is append to be printed out
output=[]

'''
HOW TO LOCATE THE DATA FROM THE SOURCE CODE
We exclude unwanted data and scrap only the data you want from the webpage
We open the webpage and then inspect the page by doing this in the browser
  -Right click on the content on webpage that you want to scrap and select Inspect
  - or Ctr + Shift + i
  -Most times the content is in div, span, article, section, header html tags
  -check for a class on that tag that contains the content you want to scrap
  -put the tag and the class as parameters of the BeautifulSoup class
  
'''
#Betteroutcomenow
archive_url="https://blog.betteroutcomesnow.com/archive/2022"
press_urls=int(archive_url.split('/')[-1])#split is used to choose which part on the url we are to use while scraping that webpage

#we use the for loop to iterate through the url pages, we use the range to start from 2017 and increase by 1
for url in range(2017, press_urls +1 ):
  press_url=f"https://blog.betteroutcomesnow.com/archive/{url}/" #the url part is used to pass the increased value in the range starting from 2017, then 2018 untill all archived urls are looped
  press_page = requests.get(press_url).text#we use the requests that we installed so as to enable us to make HTTP request to the passed press_url variable as a parameter and get the text part of the HTTP request
  press_doc=BeautifulSoup(press_page, 'html.parser')# we use BeautifulSoup class that we imported from bs4 to get the HTML document structure of the webpage we are scraping, beautifulsoup the parses the page using the an HTML parser(html.parser) which is used to process data
  items = press_doc.find_all(class_="post-item")#from the parsed html page, we use a class find_all from beautifulsoup to get all html classes in the HTML page with a class post-item
  
  
  for item in items:#use the for loop to iterate through all items in the soup with class=post-item
    title =item.find(class_="post-header")#from each of the item in the soup, find an html tag with a class = post-header as a title
    get_link = item.find('a') #from the soup item, find the the anchor tag 'a'
    link=get_link.attrs['href'] #use the attrs class from the beautiful soup to slice out a link from the soup item
    get_details = requests.get(link).text #getting the response from the page using the get method of the requests package that we installed
    detail_page = BeautifulSoup(get_details, 'html.parser')# for each item link we process the data on that link or details page
    details=detail_page.find(class_="hs_cos_wrapper hs_cos_wrapper_meta_field hs_cos_wrapper_type_rich_text")# on the details page, we use find function to get a class of the data we want, this class is done by inspecting one of the details page
    press={} #we create an empty dictionary that will hold data from each item
    press["Title: "]=title.text # We get text data from the title variable we created and append it to a dictionary press
    press["Description: "]=details.text #we get all the text data from the details page and also append it to the press dictionary
    output.append(press)#we use the output list we declared prior and append to it all the data from the press dictionary

#this is used to open our disk where this scipt is located and create a name with .txt, we convert all the data into utf encoding style, the "a" stands for if file exists, then append to it data  
with open("betteroutcomesnow-archived-blogs-data.txt", "a",encoding='utf-8') as f:
  output=str(output) # we stringify the output variable
  f.write(output)# this writes and saves content to the .txt file
  f.write('\n')   #this moves to the next line 
  
#https://www.blueprint-health.com/
press_url="https://www.blueprint-health.com/blog"
press_page = requests.get(press_url).text
press_doc=BeautifulSoup(press_page, 'html.parser')

press_pages =int(press_doc.find(class_='w-pagination-wrapper').a['href'].split('=')[-1])#we split the url into 2 parts from the equal sign and take the first part immediately afetr the equal signs and then we convert the result int an integer

for page in range(1, press_pages + 1 ):
  press_url=f"https://www.blueprint-health.com/blog?cbb911e6_page={page}" #the {page} is used to pass the integer value to the url which is always the page number on a paginated webpage
  press_page = requests.get(press_url).text
  press_doc=BeautifulSoup(press_page, 'html.parser')
  items = press_doc.find_all(class_="collection-item-blog")
  for item in items:
    title =item.find(class_="title-post")
    get_link = item.find('a')
    link=get_link.attrs['href']
    link="https://www.blueprint-health.com" +link
    get_details = requests.get(link).text 
    detail_page = BeautifulSoup(get_details, 'html.parser')
    details=detail_page.find(class_="rich-text-blog")
    press={}
    press["Title"]=title.text
    press["Description"]=details.text
    output.append(press)    
with open("blueprint-health-blogs.txt", "a",encoding='utf-8') as f:
  output=str(output)
  f.write(output)
  f.write('\n')   
  
#the remaining code we use the same criteria as explained above

#https://www.greenspacehealth.com/en-ca/
press_url="https://www.greenspacehealth.com/en-ca/blog"
press_page = requests.get(press_url).text
press_doc=BeautifulSoup(press_page, 'html.parser')
items = press_doc.find_all(class_="collection-item-3")
for item in items:
  title =item.find(class_="blog-heading")
  get_link = item.find('a')
  link=get_link.attrs['href']
  link="https://www.greenspacehealth.com" +link
  get_details = requests.get(link).text 
  detail_page = BeautifulSoup(get_details, 'html.parser')
  details=detail_page.find(class_="container-9 w-container")
  press={}
  press["Title"]=title.text
  press["Description"]=details.text
  output.append(press)      
with open("greenspacehealth-blog-data.txt", "a",encoding='utf-8') as f:
  output=str(output)
  f.write(output)
  f.write('\n')   
  
#https://mdlogix.com
req = Request('https://mdlogix.com/mdlogix-news/', headers={'User-Agent': 'XYZ/3.0'})# headers are passed as a dictionary to help pass the request in the payload and to avoid being blocked as requests from bots
webpage = urlopen(req, timeout=10).read()# timeout is used to create an interval between requests so as not to overwhelm the server with too many requests.
for page in range(1, 4 ):
  req = Request(f"https://mdlogix.com/mdlogix-news/page/{page}/", headers={'User-Agent': 'XYZ/3.0'}) 
  
  webpage = urlopen(req, timeout=100).read()# urlopen is a python module used to fetch urls, in this case it has been used to fetch the url we have named req, the .read() is used to read the webpage content
  news_doc=BeautifulSoup(webpage, 'html.parser')
  items = news_doc.find_all(class_="entry-body")# entry-body is the class on the webpage with all the content we want to scrap. Items hold all contents found from the class entry-body
  
  for item in items: #to get individual item from the soup, we use the for loop to iterate through the items on the web page
    title =item.find(class_="entry-title") # for each item, we use find to locate the class for the title which is "entry-title"
    get_link = item.find('a')
    link=get_link.attrs['href']
    headers={'User-Agent': 'XYZ/3.0'}
    response = requests.get(link, headers=headers).text
    detail_page = BeautifulSoup(response, 'html.parser')
    details=detail_page.find(class_="entry-content")
    news={}
    news["Title"]=title.text
    news["Description"]=details.text
    output.append(news) 
    
with open("mdlogix-news-data.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')

#scrap greenspacehealth security data
url_list="https://www.greenspacehealth.com/en-ca/security"
req = requests.get(url_list)
soup = BeautifulSoup(req.text, "html.parser")
results=soup.find('div',class_="container w-container")
results=results.find_all('div', class_="column-grow-hover w-col w-col-4")
for result in results:
  question =result.find(class_="heading-8")
  answer = result.find(class_="paragraph")
  press={}

  press["Security Feature"]=question.text
  press["Description"]=answer.text
  output.append(press)  
with open("greenspacehealth-SecurityFeatures-data.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


#https://www.holmusk.com/publications
url="https://www.holmusk.com/news"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
results=soup.find('div',class_="collection-list _3-col _2-col-tablet w-dyn-items")
results=results.find_all('div', class_="w-dyn-item")
for result in results:
  link = result.find('a', class_="link-block-2 w-inline-block")
  link=link.attrs['href']
  
  test_cond = str(link)
  if "holmusk.com" in test_cond:#the link returned mixed links even those linking to external websites so we use if statement to weed them out and remain with only those of holmusk which we want to scrap
    req = requests.get(link)
    soup = BeautifulSoup(req.text, "html.parser")
    results=soup.find_all('div',class_="container news-template w-container")

    for result in results:
      title =result.find(class_="news-title")
      
      description = result.find("div",class_="w-richtext")
      press={}
      press["News Title"]=title.text
      press["Details"]=description.text
      output.append(press)
    
with open("holmusk-news-events-data.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


# #owl-health-blog data   
for page in range(1, 4): #we manually check the how many pages are in the pagination section and in this case they were 3, so we loop within that range starting from 1, in python the range does not include the last number so the range must contain a larger number than the desired so as to get correct results and that's why we used 4 instead of the 3
  blog_url=f"https://www.owl.health/blog/page/{page}/?et_blog" # each number in the range will be inserted in the {page} e.g {3}
  page = requests.get(blog_url).text
  doc=BeautifulSoup(page, 'html.parser')
  items = doc.find_all('div', class_="et_pb_salvattore_content")# get all the content we need from a given webpage in this case each of the 3 pages
  for item in items: # after getting all the contents from a given webpage, loop through the items to get individual item from the items
    title =item.find('h2',class_="entry-title")
    get_link = item.find('a')
    link=get_link.attrs['href']
    details=item.find('div',class_="post-content")
    get_details = requests.get(link).text 
    detail_page = BeautifulSoup(get_details, 'html.parser')
    details=detail_page.find(class_="et_pb_module et_pb_post_content et_pb_post_content_0_tb_body")
    blog={}
    try:#for this specific webpage, some blog articles were just images or pdfs and never had either a title or description, we use the try block to weed out such exceptions that would cause the script to break because of Nonetype errors
      blog["Blog Title: "]=title.text
      blog["Blog Description: "]=details.text
    except:
      pass #in case there is a blog without a title or description, we skip and move to the next blog.
    output.append(blog)
with open("owl-health-blogs-data.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


#tridiuum news data
for page in range(1, 6):
  time.sleep(3)
  blog_url=f"https://tridiuum.com/category/news/page/{page}/"
  headers = requests.utils.default_headers()
  headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})#The HTTP headers are used to allow our script to send additional information to the server and enable the server to provide additional information that we can scrap
  page = requests.get(blog_url, headers=headers).text
  doc=BeautifulSoup(page, 'html.parser')
  items = doc.find_all('div', class_="article-inner")
  for item in items:
    title =item.find('h2',class_="entry-title")
    get_link = title.find('a')
    link=get_link.attrs['href']
    news={}
    news["Newa Title: "]=title.text
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
    get_details = requests.get(link,headers=headers).text 
    detail_page = BeautifulSoup(get_details, 'html.parser')
    details=detail_page.find('div',class_="entry-content single-page")
    news["News Description: "]=details.text      
    output.append(news)
with open("tridiuum-news-data.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
  
#tridiuum news data
for page in range(1, 8):
  time.sleep(3)
  blog_url=f"https://tridiuum.com/category/blog/page/{page}/"
  headers = requests.utils.default_headers()
  headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
  page = requests.get(blog_url, headers=headers).text
  doc=BeautifulSoup(page, 'html.parser')
  items = doc.find_all('div', class_="article-inner")
  for item in items:
    title =item.find('h2',class_="entry-title")
    get_link = title.find('a')
    link=get_link.attrs['href']
    news={}
    news["News Title: "]=title.text
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
    get_details = requests.get(link,headers=headers).text 
    detail_page = BeautifulSoup(get_details, 'html.parser')
    details=detail_page.find('div',class_="entry-content single-page")
    news["News Description: "]=details.text      
    output.append(news)
with open("tridiuum-blog-data.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')

#Silver cloud health press releases
import time
for page in range(1, 13):
  time.sleep(5)
  blog_url=f"https://www.silvercloudhealth.com/uk/press_releases/page/{page}"
  headers = requests.utils.default_headers()#this helps us to send the value of a user agent such as the browser while requesting for a webpage using python requests module;
  
  
  headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})#we have explicitly set our user agent as Mozilla and this will update server whenever this script sends the request for the webpage.
  page = requests.get(blog_url, headers=headers).text#this returns the text document from the url instead of the HTML document with tags and other undesired elements from the webpage
  doc=BeautifulSoup(page, 'html.parser')
  items = doc.find_all('div', class_="blog-info-inner")
  for item in items:
    title =item.find('h2',class_="silver-heading")
    get_link = item.find('div',class_="excerpt").find('a')
    link=get_link.attrs['href']
    news={}
    news["Press Title"]=title.text
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
    get_details = requests.get(link,headers=headers).text 
    
    detail_page = BeautifulSoup(get_details, 'html.parser')
    details=detail_page.find('div',class_="section post-body")
    news["Press Description"]=details.text      
    output.append(news)
with open("silver-cloud-health-press-releases.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
#Silver cloud health blogs 
for page in range(1, 18):
  time.sleep(5)
  blog_url=f"https://www.silvercloudhealth.com/uk/blog/page/{page}"
  headers = requests.utils.default_headers()
  headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
  page = requests.get(blog_url, headers=headers, timeout=10).text # since we are scraping many pages from the website, this will send many requests to the server, to avoid our IP from being blocked, we use a timeout of 10s to put an interval between our requests and make the server happy and not stressed by too much requests at ago
  doc=BeautifulSoup(page, 'html.parser')
  items = doc.find_all('div', class_="blog-info-inner")
  for item in items:
    title =item.find('h2',class_="silver-heading")
    get_link = item.find('div',class_="excerpt").find('a')
    link=get_link.attrs['href']
    news={}
    news["Blog Title"]=title.text
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
    get_details = requests.get(link,headers=headers).text 
    detail_page = BeautifulSoup(get_details, 'html.parser')
    details=detail_page.find('div',class_="section post-body")
    news["Blog Description"]=details.text    
    output.append(news)
with open("silver-cloud-health-press-releases.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
  
#Silver Cloud health content library  
from PyPDF2 import PdfFileReader, PdfFileWriter # install pypdf2 and then import classes for reading and writing pdf content to the file
resource_url=f"https://www.silvercloudhealth.com/uk/resources"
headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
page = requests.get(resource_url, headers=headers).text
doc=BeautifulSoup(page, 'html.parser')
items = doc.find_all('div', class_="resource")
for item in items:
  title =item.find('div',class_="resource-heading")
  get_link = item.find('a')
  link=get_link.attrs['href']
  details=item.find('div',class_="resource-description")
  blog={}
  blog["Resource Title"]=title.text
  
 
  if "https://www.silvercloudhealth.com/" in link:# the resources had links to external websites, since we want to scrap on this website, we check if the url contains this specific website, then we can scrap its data
     
    if ".jpg" not in link:#for this specific url, some links returned images and pdfs instead of the desired content with titles and description, so we used the if statements to weed these out and remain with only textual data
      if ".pdf" not in link:
        page = requests.get(link, headers=headers).text
        doc=BeautifulSoup(page, 'html.parser')
        details = doc.find('span',class_="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_rich_text")
        blog["Resource Title"]=title.text
        blog["Resource Description"]=details.text
      else:
        # creating a pdf file object 
        pdfFileObj = requests.get(link)
        writer = PdfFileWriter()
        remoteFile = urlopen(Request(link)).read()
        memoryFile = BytesIO(remoteFile)
        pdfReader = PdfFileReader(memoryFile, strict=False)          
        # creating a page object 
        pageObj = pdfReader.getPage(0) 
            
        # extracting text from page 
        details=pageObj.extractText()
        blog["Resource Title"]=title.text
        blog["Resource Description"]=details
        blog["Resource Pdf Link"]=link 
        pdfFileObj.close() 
  else:
    blog["Resource Title"]=title.text
    blog["Resource Link"]=link
    blog["Resource Description"]=details.text
  output.append(blog)
with open("silver-cloud-health-resources.txt", "a") as f:
  output=str(output)
  f.write(output)


#oqmeasures-news
url="https://www.oqmeasures.com/category/oq-news/"
headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "html.parser")
main=soup.find('main',class_="site-main")
results=main.find_all('div', class_="card-body")
for result in results:
  title=result.find('h2', class_="entry-title card-title h3")
  link = title.find('a', class_="text-dark")
  link=link.attrs['href']
  req = requests.get(link, headers=headers)
  soup = BeautifulSoup(req.text, "html.parser")
  details=soup.find('div',class_="card-body")
  if details is not None:
    details.find('header', class_="entry-header").decompose()
    press={}
    press["News Title"]=title.text
    press["Details"]=details.text
    output.append(press)
  
with open("oqmeasures-news.text", "a") as f:
  output=str(output)
  f.write(output)


#############wesanahealth.com####################
#https://www.wesanahealth.com/  
press_url='https://wesanahealth.com/media-room/'
press_page = requests.get(press_url).text
press_doc=BeautifulSoup(press_page, 'html.parser')
items = press_doc.find_all(class_="elementor-post__text")
for item in items:
  #Due to sofisticated server blocking, this was done manually by passing the url to be scrapped in the script
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
 
results=soup.find_all(['dt','dd'])#We find all the instances of data in a table in the soup
for result in results:
  output=result.text
  with open("wesanahealth-FAQ-data.txt", "a") as f:
    output=str(output)
    f.write(output)
    f.write('\n')

#Valant-blogs
for page in range(1, 29 ):
  req = Request(f"https://www.valant.io/blog/page/{page}/", headers={'User-Agent': 'XYZ/3.0'})

  webpage = urlopen(req,timeout=100).read() # we use a timout of 100s to avoid bombarding the server with to much traffic at ago, this slows down our scraping speed and requires stable internet to maitain the hold time sice we are scrapping many pages
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

  webpage = urlopen(req, timeout=10).read()
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
  

#Valant-case-studies

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
    get_link = title.find('a')
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
 
###############Scrap neuroflow-research ########################### 
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

### scrap neuroblu Use Cases
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

############### Scrap nndc EVENTS################
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


#######################mirah case-studies########################
output=[]
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
    details=detail_page.find("article",class_="sections")
    news={}
    news["Title"]=title.text
    
    news["Description"]=details.text
  except:
    pass
  output.append(news)  
with open("mirah-case-studies.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
'''
Scrap Dynamic data from https://ksanahealth.com/mental-health-blog
The website uses dynamically loaded conetnt using javascript, so i didn't scrap it like previously did for the rest but used 
1: Right-click on page and select 'Inspect'.
2 - Select 'Network' tab. 
3: Click on the 'Show more' button. 
4: See the ajax call (url) appearing in network tab  then check the ajax that loads the content and manually pick the url and use it after determining the number of pages on count of show more loads in this case they were for counts:
'''                                    
######data scrapped on july 21 2022

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }

output = []

r = requests.get(f'https://ksanahealth.com/wp-admin/admin-ajax.php?id=&post_id=107&slug=mental-health-blog&canonical_url=https%3A%2F%2Fksanahealth.com%2Fmental-health-blog%2F&posts_per_page=10&page=4&offset=0&post_type=post&repeater=default&seo_start_page=1&preloaded=false&preloaded_amount=0&order=DESC&orderby=date&action=alm_get_posts&query_type=standard', headers=headers)#here we are passing in the url we got from the network tab after loading the dynamic page, this would better be done using selenium but we opted for beautiful soup to maintain the consistency of our scrap script
soup = BeautifulSoup(r.txt()['html'], 'html.parser')
for item in soup.select('div.post-item'): #using select here is the same as using find_all data in the soup
  title=item.select_one('h4').text.strip()
  get_link=item.select_one('a.more-link').get('href')# select_one is the same as using find
  
  response = requests.get(get_link, headers=headers).text
  detail_page = BeautifulSoup(response, 'html.parser')
  if 'https://ksanahealth.com/' in get_link:
    try:
      details=detail_page.select_one("div.blog-post__body")
      news={}
      news["Blog Title"]=title
      
      news["Blog Description"]=details.text
      output.append(news) 
    except:
      pass
with open("ksanahealth-blogs.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


#########Scrap the ksanahealth Announcements ###########
##data scrapped on july 21 2022      
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://ksanahealth.com/newsroom/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
data = soup.find('ul' ,class_='wp-block-latest-posts__list has-dates wp-block-latest-posts')
items = data.find_all('li')
for item in items:
  get_link=item.select_one('a.wp-block-latest-posts__post-title').get('href')
  if 'https://ksanahealth.com/' in get_link:
    response = requests.get(get_link, headers=headers).text
    detail_page = BeautifulSoup(response, 'html.parser')
    title=detail_page.select_one("h1.postmtitle")
    details=detail_page.select_one("div.blog-post__body")
    news={}
    news["Announcement Title"]=title.text
    news["Announcement Description"]=details.text
    output.append(news) 
with open("ksanahealth-Announcement.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  

######Scrap ksanahealth Product features - evidence part
#data scrapped on july 21 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://ksanahealth.com/evidence/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="hs-evdnce-pg-inner")
output=output.text

with open("ksanahealth-products-evidence.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
  
######Scrap ksanahealth Product features - evidence part
#data scrapped on july 21 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://ksanahealth.com/ears/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('main', class_="body-container-wrapper")
output=output.text

with open("ksanahealth-products-ears.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  

######Scrap ksanahealth Product features - evidence part
#data scrapped on july 21 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://ksanahealth.com/vira/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('main', class_="body-container-wrapper")
output=output.text

with open("ksanahealth-products-viral-management.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')

#########Scrap the futuresrecoveryhealthcare news pr ###########
#data scrapped on july 21 2022      
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://futuresrecoveryhealthcare.com/news-pr/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
items = soup.find_all('a', class_="content-pane")
for item in items:
  try:
    get_link=item.get('href')
    if 'https://futuresrecoveryhealthcare.com' in get_link:
      response = requests.get(get_link, headers=headers).text
      detail_page = BeautifulSoup(response, 'html.parser')
      title=detail_page.select_one("header.entry-header")
      details=detail_page.select_one("div.entry-content")
      news={}
      news["News Title"]=title.text
      news["News Description"]=details.text
      output.append(news) 
  except:
    pass
with open("futuresrecoveryhealthcare-news-pr.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


#########Scrap the futuresrecoveryhealthcare Blogs ###########
#data scrapped on july 21 2022      
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://futuresrecoveryhealthcare.com/blog/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
items = soup.find_all('a', class_="content-pane")
for item in items:
  try:
    get_link=item.get('href')
    if 'https://futuresrecoveryhealthcare.com' in get_link:
      response = requests.get(get_link, headers=headers).text
      detail_page = BeautifulSoup(response, 'html.parser')
      title=detail_page.select_one("h1.entry-title")
      dates=detail_page.select_one("div.entry-meta")
      details=detail_page.select_one("div.entry-content")
      news={}
      news["Blog Title"]=title.text
      news["Blog  Date"]=dates.text
      news["Blog Description"]=details.text
      output.append(news) 
  except:
    pass
with open("futuresrecoveryhealthcare-blogs.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  

######Scrap fit-outcomes Product features - evidence part
#data scrapped on july 21 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://blog.fit-outcomes.com/en/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="site-content")
output=output.text

with open("fit-outcomes-blog.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


#######Scrap fit-outcomes Product FAQ
#data scrapped on july 21 2022  
import urllib  
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 
url='https://www.fit-outcomes.com/help/faq'
output = []
request = urllib.request.Request(url,None,headers)
webpage = request.urlopen(request).read()
soup=BeautifulSoup(webpage, 'html.parser')
x =soup.find('div', class_="table-responsive vte3")
output=x.text

with open("fit-outcomes-FAQ.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')

######Scrap celesthealth News
#data scrapped on july 23 2022  
import urllib  
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

r = Request(f'https://www.celesthealth.com/news.asp', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output = []
x =soup.find('div', class_="main_content_subPage")
output=x.text

with open("celesthealth-news.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
######Scrap celesthealth Methods
#data scrapped on july 23 2022  
import urllib  
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

r = Request(f'https://www.celesthealth.com/method.asp', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output = []
x =soup.find('div', class_="main_content_body")
output=x.text

with open("celesthealth-methods.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


######Scrap celesthealth instruments
#data scrapped on july 23 2022  
import urllib  
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

r = Request(f'https://www.celesthealth.com/instruments.asp', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output = []
x =soup.find('div', class_="main_content_body")
output=x.text

with open("celesthealth-instruments.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
  
######Scrap celesthealth instruments
#data scrapped on july 23 2022  
import urllib  
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

r = Request(f'https://www.celesthealth.com/about.asp', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output = []
x =soup.find('div', class_="main_content_body")
output=x.text

with open("celesthealth-about.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
  
#mhoutcomes-Insights --> download brief description of the insights
output=[]
for page in range(1, 4 ):
  req = Request(f"https://mhoutcomes.com/insights/page/{page}/", headers={'User-Agent': 'XYZ/3.0'})

  webpage = urlopen(req,timeout=100).read()
  news_doc=BeautifulSoup(webpage, 'html.parser')
  items = news_doc.find_all("div", class_="blog-details-wrap clearfix")

  for item in items:
    try:
      
      title =item.find('h3', itemprop="name headline")
      get_link = item.find('a',class_="link-to-post")
      link=get_link.attrs['href']
      
      response = requests.get(link, {'User-Agent': 'XYZ/3.0'}).text
      soup = BeautifulSoup(response, 'html.parser')
      details=soup.find("section",class_="page-content clearfix container")
      news={}
      news["Insight Title"]=title.text
      news["Insight Description"]=details.text
      output.append(news)  
    except:
      pass
with open("mhoutcomes-Insights.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
  
  
  #######Scrap outcomereferrals -about-mission
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/about-us/mission', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="sub-page-content-wrapper")
output=output.text

with open("outcomereferrals-about-mission.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')



  ######Scrap outcomereferrals -about-history
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/about-us/history', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="sub-page-content-wrapper")
output=output.text

with open("outcomereferrals-about-history.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
######Scrap outcomereferrals -about-team
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/about-us/team', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="sub-page-content-wrapper")
output=output.text

with open("outcomereferrals-about-team.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')

######Scrap outcomereferrals top-assessment/top-assessment
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/top-assessment/top-assessment', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="main-content")
output=output.text

with open("outcomereferrals-top-assessment-top-assessment.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')  
  
  
  
######Scrap outcomereferrals top-assessment/top-assessment
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/outcome-measurement/outcome-measurement', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="main-content")
output=output.text

with open("outcomereferrals-outcome-measurement.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 
  
  
######Scrap outcomereferrals validation-articles
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/validation-research/validation-articles', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="main-content")
output=output.text

with open("outcomereferrals-validation-articles.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 
  
  
#######Scrap outcomereferrals validation-articles
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/child-welfare/child-welfare', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="main-content")
output=output.text

with open("outcomereferrals-child-welfare.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 


######Scrap outcomereferrals testimonies
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/child-welfare/testimonial-from-dr-drendel', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="main-content")
output=output.text

with open("outcomereferrals-testimonies.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 
  
  
######Scrap outcomereferrals joint-commission
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'http://www.outcomereferrals.com/main/sub-page/category/joint-commission', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="main-content")
output=output.text

with open("outcomereferrals-joint-commission.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 
  
  
######Scrap visiontree homepage
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://visiontree.com/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="flex-grow")
output=output.text

with open("visiontree-homepage.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 
  
  
######Scrap visiontree clinical
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://visiontree.com/solutions/clinical/patient-centered-outcomes/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="flex flex-col h-screen")
output=output.text

with open("visiontree-clinical.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 
  
#######Scrap visiontree outcomes
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://visiontree.com/solutions/research/patient-centered-outcomes/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="flex flex-col h-screen")
output=output.text

with open("visiontree-patient-centered-outcomes.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 
  
  
######Scrap visiontree solutions packages
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://visiontree.com/solutions/packages/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8")
output=output.text

with open("visiontree-solution-packages.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 
  
  
######Scrap visiontree solutions-patient-portal
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://visiontree.com/solutions/patient-portal/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8")
output=output.text

with open("visiontree-solutions-patient-portal.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 
  
######Scrap visiontree telehealth
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://visiontree.com/telehealth-and-covid19-toolkit/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8")
output=output.text

with open("visiontree-telehealth.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 
  
######Scrap visiontree provenchoice
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://visiontree.com/proven-choice/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8")
output=output.text

with open("visiontree-proven-choice.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 
  
  
######Scrap visiontree patients-reported-outcomes
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://visiontree.com/patient-reported-outcomes/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="mx-auto max-w-md px-4 sm:max-w-3xl sm:px-6 lg:max-w-7xl lg:px-8")
output=output.text

with open("visiontree-patient-reported-outcomes.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 


######Scrap visiontree macra-mips
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://visiontree.com/macra-mips/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="flex-grow")
output=output.text

with open("visiontree-highlights.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 
  
  
######Scrap visiontree macra-mips
#data scrapped on july 23 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://visiontree.com/vtoc-roi/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8")
output=output.text

with open("visiontree-return-on-investiments.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 


#########Scrap the visiontree press release ###########
#data scrapped on july 23 2022      
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://visiontree.com/press-releases/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
data=soup.find('tbody',)
items = data.find_all('tr')
for item in items:
  try:
    get_link = item.find('a', class_='link')
    Date=item.find('td', class_="px-6 py-4 align-top font-medium w-1/4")
    
    title=item.find('td', class_="px-6 py-4 text-gray-500")
    link='https://visiontree.com'+get_link.attrs['href']
    response = requests.get(link, headers=headers).text
    detail_page = BeautifulSoup(response, 'html.parser')
    details=detail_page.find("div", class_="pageWrap pageWrap--m")
     
    news={}
    news["Press Date"]=Date.text
    news["Press Title"]=title.text
    news["Press Description"]=details.text
    output.append(news) 
  except:
    pass
with open("visiontree-press-releases.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
#########visiontree case studies and patient voices are external links###########

######Scrap azzly homepage
#data scrapped on july 30 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://azzly.com/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="vc_row wpb_row vc_inner vc_row-fluid vc_column-gap-20 vc_row-o-equal-height vc_row-o-content-middle vc_row-flex")
output=output.text

with open("azzly-testimonies.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 


######Scrap about better outcomes
#data scrapped on july 30 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://betteroutcomesnow.com/about-bon/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="wrapper white")
output=output.text

with open("betteroutcomesnow-about.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 
  
#######Scrap about better outcomes-pcoms
#data scrapped on july 30 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://betteroutcomesnow.com/about-pcoms/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="wrapper white")
output=output.text

with open("betteroutcomesnow-about-pcoms.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 


######Scrap about better outcomes top tens
#data scrapped on july 30 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://betteroutcomesnow.com/about-pcoms/top-ten/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="wrapper white")
output=output.text

with open("betteroutcomesnow-about-top-tens.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 




#######Scrap about better outcomes pcoms-implementation
#data scrapped on july 30 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://betteroutcomesnow.com/about-pcoms/pcoms-implementation/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="wrapper white")
output=output.text

with open("betteroutcomesnow-about-pcoms-implementation.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 


######Scrap about better outcomes pcoms-evidence-based-practic
#data scrapped on july 30 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://betteroutcomesnow.com/about-pcoms/pcoms-implementation/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="wrapper white")
output=output.text

with open("betteroutcomesnow-about-pcomsevidence-based-practic.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 
  
#######Scrap about better outcomes taam
#data scrapped on july 30 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://betteroutcomesnow.com/about-bon/our-team/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="wrapper white")
output=output.text

with open("betteroutcomesnow-team.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n') 


#######Scrap about better outcomes pcoms-training
#data scrapped on july 30 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://betteroutcomesnow.com/resources/pcoms-training/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="wrapper white")
output=output.text

with open("betteroutcomesnowp-coms-training.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')

#######Scrap bhworks-page
#data scrapped on july 30 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f' https://mdlogix.com/bhworks-page/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="elementor-section-wrap")
output=output.text

with open("mdlogix-bhworks.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


#######Scrap bhworks-for-schools
#data scrapped on july 30 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://mdlogix.com/for-schools/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="elementor-section-wrap")
output=output.text

with open("mdlogix-for-schools.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')

######Scrap bhworks-for-healthcare-providers
#data scrapped on july 30 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://mdlogix.com/for-healthcare-providers/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="elementor-section-wrap")
output=output.text

with open("mdlogix-for-healthcare-providers.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
  
#######Scrap bhworks-for-employers
#data scrapped on july 30 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://mdlogix.com/for-employers/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="elementor-section-wrap")
output=output.text

with open("mdlogix-for-employers.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')

#######Scrap bhworks-for-community
#data scrapped on july 30 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://mdlogix.com/community/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="elementor-section-wrap")
output=output.text

with open("mdlogix-for-community.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


#######Scrap bhworks-for-collaboration-partners-advisor
#data scrapped on july 30 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://mdlogix.com/collaboration-partners-advisors/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="elementor-section-wrap")
output=output.text

with open("mdlogix-for-collaboration-partners-advisors.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')

#######Scrap bhworks-for-crms-page
#data scrapped on july 30 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://mdlogix.com/crms-page/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="elementor-section-wrap")
output=output.text

with open("mdlogix-crms-page.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')

######Scrap blueprint-health-who-we-serve
# #data scrapped on july 31 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://www.blueprint-health.com/who-we-serve/clients', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="section new gray wf-section")
output=output.text

with open("blueprint-health-who-we-serve.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


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
  
# #######Scrap Mirah homepage
# # # #data scrapped on july 31 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://www.mirah.com/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('article', class_="sections")
output=output.text

with open("mirah-homepage-content.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


# #######Scrap Mirah mbc
# # # #data scrapped on july 31 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://www.mirah.com/mbc/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('article', class_="sections")
output=output.text

with open("mirah-mbc.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


# #######Scrap Mirah for-providers
# # # #data scrapped on july 31 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://www.mirah.com/for-providers/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('article', class_="sections")
output=output.text

with open("mirah-for-providers.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


#######Scrap Mirah product
# # #data scrapped on july 31 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://www.mirah.com/product/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('article', class_="sections")
output=output.text

with open("mirah-for-product.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


#######Scrap Mirah Team
# # #data scrapped on july 31 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://www.mirah.com/our-team/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('article', class_="sections")
output=output.text

with open("mirah-for-our-team.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


###############################REMAINING WEBSITES TO BE SCRAPPED#############################
#scrapped on 1 August
for page in range(1, 11 ):
  req = Request(f"https://blog.nview.com/page/{page}", headers={'User-Agent': 'XYZ/3.0'})

  webpage = urlopen(req,timeout=10).read()
  news_doc=BeautifulSoup(webpage, 'html.parser')
  items = news_doc.find_all("article", class_="blog-index__post blog-index__post--small")
  
  for item in items:
    title =item.find('h4', class_="blog-index-title")    
    get_link = title.find('a')
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
with open("nview-blog.txt", "a",encoding='utf-8') as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  

#owl-health-media-hits
for page in range(1, 9):
    req = Request(f"https://www.owl.health/newsroom/page/{page}/?et_blog", headers={'User-Agent': 'XYZ/3.0'})

    webpage = urlopen(req,timeout=10).read()
    news_doc=BeautifulSoup(webpage, 'html.parser')
    items = news_doc.find_all("div", class_="column size-1of2")
    print(items)
    for item in items:
      title =item.find(class_="entry-title")
      
      get_link = title.find('a')
      link=get_link.attrs['href']
      print(link)
      headers={'User-Agent': 'XYZ/3.0'}
      response = requests.get(link, headers=headers).text
      soup = BeautifulSoup(response, 'html.parser')
      details=soup.find("div",class_="et_pb_module et_pb_post_content et_pb_post_content_0_tb_body")
      news={}
      news["News Title: "]=title.text
      try:
        news["News Description: "]=details.text
      except:
        pass
      output.append(news)  
with open("nview-blog.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')



#######Scrap owl-health
# # #data scrapped on augut 1 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://www.owl.health/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="et_builder_inner_content et_pb_gutters3")
output=output.text

with open("owl-health-homepage.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
  
# #######Scrap owl-health-offers
# # # #data scrapped on augut 1 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://www.owl.health/what-owl-offers/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="et_builder_inner_content et_pb_gutters3")
output=output.text

with open("owl-health-offers.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
  
# #######Scrap owl-health-communnity
# # # #data scrapped on augut 1 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://www.owl.health/community-mental-health-centers/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="et_builder_inner_content et_pb_gutters3")
output=output.text

with open("owl-health-community.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
# #######Scrap owl-health-system
# # # #data scrapped on augut 1 2022    
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','accept': 'application/json' }
output = []
r = Request(f'https://www.owl.health/health-systems/', headers=headers)
webpage = urlopen(r,timeout=10).read()
soup=BeautifulSoup(webpage, 'html.parser')
output =soup.find('div', class_="et_builder_inner_content et_pb_gutters3")
output=output.text

with open("owl-health-system.txt", "a") as f:
  output=str(output)
  f.write(output)
  f.write('\n')


#media-hits data of owl-health  
import time
for page in range(1, 32):
  time.sleep(3)
  blog_url=f"https://www.owl.health/newsroom/page/{page}/?et_blog"
  headers = requests.utils.default_headers()
  headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
  page = requests.get(blog_url, headers=headers, timeout=10).text
  doc=BeautifulSoup(page, 'html.parser')
  items = doc.find_all('div', class_="et_pb_salvattore_content")
  for item in items:
    title =item.find('h2',class_="entry-title")
    get_link = item.find('a')
    link=get_link.attrs['href']
    external_details=item.find('div',class_="post-content")
    blog={}
    blog["News Title: "]=title.text
    if "https://www.owl.health" in link:
      get_details = requests.get(link).text 
      detail_page = BeautifulSoup(get_details, 'html.parser')
      details=detail_page.find(class_="et_pb_module et_pb_post_content et_pb_post_content_0_tb_body")
      if details is not None:
        blog["News Description: "]=details.text
    else:
      blog['Description: '] = external_details.text
      blog['External Link: '] = link
      
    output.append(blog)
with open("owl-health-media-hits-data.txt", "a",encoding='utf-8') as f:
  output=str(output)
  f.write(output)
  f.write('\n')



# ################https://azzly.com/blog/#############################
for page in range(1, 16):
  req = Request(f"https://azzly.com/blog/page/{page}/", headers={'User-Agent': 'XYZ/3.0'})

  webpage = urlopen(req,timeout=10).read()
  news_doc=BeautifulSoup(webpage, 'html.parser')
  items = news_doc.find_all("div", class_="blog-entry-content entry-details clr")
  for item in items:
    title =item.find('h2', class_="blog-entry-title entry-title")
    get_link = title.find('a')
    link=get_link.attrs['href']
    headers={'User-Agent': 'XYZ/3.0'}
    response = requests.get(link, headers=headers).text
    detail_page = BeautifulSoup(response, 'html.parser')
    details=detail_page.find("div",class_="single-blog-content entry clr")
    news={}
    news["Blog Title"]=title.text
    try:
      news["Blog Description"]=details.text
    except:
      pass
    output.append(news)  
with open("azzly-Blogs.txt", "a",encoding='utf-8') as f:
  output=str(output)
  f.write(output)
  f.write('\n')
  
################## RESOURCE REFERENCES########################

'''
In due course of web scrapping, we might face several challenges, but these problems have been faced by many other people in scrapping community and have provided solutions to how they fixed these problems,
below are some of the challenges faced and the resources that helped to fix them

 1. To get started with beautiful soup documentation use the link below
      Solution: https://www.crummy.com/software/BeautifulSoup/bs3/documentation.html
    
 2. Problem, how to open pdf webpages:
      solution: https://stackoverflow.com/questions/9751197/opening-pdf-urls-with-pypdf
    
 3. How to use the PyPDF2 module to read and write content
      solution: https://pypi.org/project/PyPDF2/
    
 4. Passing additional information using headers
      solution: https://www.geeksforgeeks.org/python-requests-post-request-with-headers-and-body/
    
 5. Several websites were blocking our requests to their servers
      Solution: https://stackoverflow.com/questions/43440397/requests-using-beautiful-soup-gets-
    
 6. Choosing the proper python encoding for the scraped data to be written to a file or being saved
      Solution: https://stackoverflow.com/questions/491921/unicode-utf-8-reading-and-writing-to-files-in-python
    
 7. Writing or saving to file that content that has been scrapped using beautiful soup package
    Solution: https://stackoverflow.com/questions/65815005/beautifulsoup-4-python-web-scraping-to-txt-file
  
 8. How to efficiently scrap data from dynamic websites using Selenium?
  
   " You don't need selenium for this. When a page is loaded dynamically, you can look up in Network tab which urls are being accessed. The following code will get you started - returning a dataframe with blog title & url. You can further access those urls. Do tell if you need guidance."...answer by https://stackoverflow.com/users/19475185/platipus-on-fire
    
    Solution: https://stackoverflow.com/questions/73056468/how-to-efficiently-scrap-data-from-dynamic-websites-using-selenium  
    
 9. Creatig a pdf object
      Solution: https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
    
 10. Scraping paginated pages
    paginated pages can be tricky to scrap because most of them hide their implementation from the html by using javascript to load their pages with the links to the content.
    For this project we manually had to get the number of paginated pages with the content we want and then pass the maximum number using the range python class
    
      Link to pagination implementation in beautiful soup: https://stackoverflow.com/questions/54096972/scraping-paginated-results-using-python-beautifulsoup-3
    
 11. How to append beautiful soup data to a list so that it is saved as a single file
      Solution: https://www.anycodings.com/1questions/114656/how-to-append-my-web-scraping-data-into-a-list

 12. How to fix the error "'page' is not defined"
      Solution: https://stackoverflow.com/questions/65500904/web-scraping-using-python-and-beautiful-soup-error-page-is-not-defined
      
 13. How to fix urllib.request 403 Forbidden  when accessing a webpage through a script
      Solution: https://stackoverflow.com/questions/41214965/python-3-5-urllib-request-403-forbidden-error
      
 14. Fixing the attributeerror when the script is run
      Solution: https://www.geeksforgeeks.org/beautifulsoup-error-handling/#:~:text=The%20AttributeError%20in%20BeautifulSoup%20is,that%20function%20then%20AttributeError%20occurs.
      
 15. Solving the Nonetype error when accessing itemes of class on a soup
      Solutions: https://stackoverflow.com/questions/33774409/beautifulsoup-error-handling-when-find-returns-nonetype 
'''
################## End of the Script ########################