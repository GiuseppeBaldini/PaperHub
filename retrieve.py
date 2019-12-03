# Retrieve paper

# Open browser > SciHub
# Sci-hub automatic redirect
# Retrieve PDF file

import requests
import input


# test_url = https://www.sciencedirect.com/science/article/pii/S1364032119307270
domain_finder = 'https://whereisscihub.now.sh/go'
download_path = '..\\Tests\\Papers\\paper.pdf'

# get the most recent scihub domain
scihub = requests.get(domain_finder)

# find our paper on scihub
paper = scihub.url + '/' + input.url

# find pdf url
# location.href
# pdf = 

# download pdf file in download path
# file = requests.get(pdf)
# open(download_path, 'wb').write(file.content)