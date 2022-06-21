from io import StringIO,BytesIO
from PyPDF2 import PdfFileReader, PdfFileWriter
import requests
from urllib.request import Request, urlopen
headers = requests.utils.default_headers()
link="https://www.oqmeasures.com/wp-content/uploads/2018/07/History-and-Science-behind-the-OQ-Family-of-Instruments-1.pdf"
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
pdfFileObj = requests.get(link, headers=headers)
writer = PdfFileWriter()
remoteFile = urlopen(Request(link)).read()
memoryFile = BytesIO(remoteFile)
pdfReader = PdfFileReader(memoryFile, strict=False)          
# creating a page object 
pageObj = pdfReader.getPage(0) 
    
# extracting text from page 
details=pageObj.extractText()
print(details)