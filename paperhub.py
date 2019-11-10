# PaperHub - script to retrieve papers

import re
import sys

# Pyperclip is not built-in, check and download if needed
try:
    import pyperclip
except (ImportError, ModuleNotFoundError):
    print('Pyperclip module not found. Please download it.')
    exit()

# Check DOI / URL is in correct format
link_regex = re.compile('''
    http[s]?://
    (?:[a-zA-Z]|
    [0-9]|
    [$-_@.&+]|
    [!*\(\),]|
    (?:%[0-9a-fA-F][0-9a-fA-F]))+''',
    re.IGNORECASE|re.VERBOSE)

match = re.search(link_regex, paper_link)

# Get DOI or URL
# Option 1: clipboard
try:
    paper_link = pyperclip.paste()
except (#error):
    paper_link = input('Please input the paper DOI or URL here: > ')

# argument
# manual input


# URL
# Sci-hub automatic redirect

# file:
# download locally
# send via email
# send to evernote
