#Import libraries
import requests
from bs4 import BeautifulSoup

# URL from which pdfs to be downloaded
url = "https://www.m3information.com/resources/"

# Requests URL and get response object
response = requests.get(url)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')

# Find all hyperlinks present on webpage
links = soup.find_all('a')

i = 0

# From all links check for pdf link and
# if present download file
for link in links:
  if ('.pdf' in link.get('href', [])):
    i += 1
    #("Downloading file: ", i)
    response = requests.get(link.get('href'))
    file_name = link.get('href')
    file_name = file_name.replace("https://www.m3information.com/wp-content/uploads/",'/').split('/')[-1]

    pdf = open(file_name, 'wb')
    pdf.write(response.content)
    pdf.close()
    print("File ", i, " downloaded")
print("All PDF files downloaded")



