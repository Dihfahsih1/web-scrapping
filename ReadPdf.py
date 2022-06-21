from io import StringIO,BytesIO
from PyPDF2 import PdfFileReader, PdfFileWriter
import requests
from urllib.request import Request, urlopen
link="example.com"
pdfFileObj = requests.get(link)
writer = PdfFileWriter()
remoteFile = urlopen(Request(link)).read()
memoryFile = BytesIO(remoteFile)
pdfReader = PdfFileReader(memoryFile, strict=False)          
# creating a page object 
pageObj = pdfReader.getPage(0) 
    
# extracting text from page 
details=pageObj.extractText()