# Retrieve pdf file URL 

from bs4 import BeautifulSoup
import requests
import input

# test_url = https://www.sciencedirect.com/science/article/pii/S1364032119307270

# Automatically redirect to active scihub domain
domain_finder = 'https://whereisscihub.now.sh/go'

# Default local download path
download_path = '..\\Tests\\Papers\\paper.pdf' # TODO automatically name file

# Open active scihub domain
scihub = requests.get(domain_finder)

# Search paper on scihub
paper_url = requests.get(scihub.url + '/' + input.url)

# Find the pdf file URL inside the page
soup_txt = paper_url.text
soup = BeautifulSoup(soup_txt, 'html.parser')
article = soup.find('iframe') # tag

# Retrieve tag attribute (our pdf ) 
try:
    attr = article.attrs['src'] # attribute
except AttributeError:
    print("Attr 'src' not found. Check that the URL is correct.")
    exit()

pdf_url = 'https:' + attr.split('#', 1)[0]