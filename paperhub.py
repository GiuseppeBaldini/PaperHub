# PaperHub - script to retrieve papers

import pyperclip
import sys

# Pyperclip is not built-in, check and download if needed
try:
    import pyperclip
except (ImportError, ModuleNotFoundError):
    print('Pyperclip module not found. Please download it.')
    exit()

# Get DOI or link:
# clipboard
# argument
# manual input

# By default get DOI / URL from clipboard
try:
    paper_id = pyperclip.paste()
except ():
    paper_id = input('Please input the paper DOI or URL here: > ')


# URL
# Sci-hub automatic redirect

# file:
# download locally
# send via email
# send to evernote
