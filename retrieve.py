# Retrieve paper

# Open browser > SciHub
# Sci-hub automatic redirect
# Retrieve PDF file

from bs4 import BeautifulSoup
import requests
import input


# test_url = https://www.sciencedirect.com/science/article/pii/S1364032119307270
domain_finder = 'https://whereisscihub.now.sh/go'
download_path = '..\\Tests\\Papers\\paper.pdf'

# Get the most recent scihub domain
scihub = requests.get(domain_finder)

# Find paper on scihub
paper = scihub.url + '/' + input.url
paper_url = requests.get(paper)

soup_txt = paper_url.text
soup = BeautifulSoup(soup_txt, 'html.parser')

article = soup.find('iframe')
attr = article.attrs['src']

# pdf url
pdf_url = 'https:' + attr.split('#', 1)[0]

# download pdf file
r = requests.get(pdf_url, stream=True)

with open(download_path, 'wb') as f:
    for chunk in r.iter_content(1024):
        f.write(chunk)