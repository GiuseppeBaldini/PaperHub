# Retrieve pdf file URL 

from bs4 import BeautifulSoup as bs
import requests
import input

# Automatically redirect to active scihub domain
domain_finder = 'https://whereisscihub.now.sh/go'

# Open active scihub domain
scihub = requests.get(domain_finder)

# Search paper on scihub
paper_url = requests.get(scihub.url + '/' + input.url)

# Find the pdf file URL inside the page
soup_txt = paper_url.text
soup = bs(soup_txt, 'html.parser')
article = soup.find('iframe') # tag

# Retrieve tag attribute (our pdf ) 
try:
    attr = article.attrs['src'] # attribute
except AttributeError:
    print("Attr 'src' not found. Check that the URL is correct.")
    exit()

pdf_url = 'https:' + attr.split('#', 1)[0]

# We can use part of the DOI as file name
pdf_title = pdf_url.split('@', 1)[1] # includes .pdf

# Default local download path
download_path = '..\\..\\..\\..\\downloads\\' + pdf_title