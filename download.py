# Download paper 

import requests
from retrieve import download_path, pdf_url

# Open connection
r = requests.get(pdf_url, stream=True)

# Check connection status
if r.status_code == 200:
    print('Downloading paper from: ' + pdf_url) 
else:
    print('Connection failed. Try a different URL / DOI.')
    exit()

# Save pdf file locally
with open(download_path, 'wb') as f:
    for chunk in r.iter_content(1024):
        f.write(chunk)

# Send via email


# Send to evernote