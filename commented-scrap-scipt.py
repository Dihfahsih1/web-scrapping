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
from urllib.request import urlretrieve
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO,BytesIO
from PyPDF2 import PdfFileReader, PdfFileWriter
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