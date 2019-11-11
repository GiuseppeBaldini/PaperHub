# PaperHub - script to retrieve papers

import re
import sys

# Pyperclip is not built-in, check and download if needed
try:
    import pyperclip
except (ImportError, ModuleNotFoundError):
    print('Pyperclip module not found. Please download it.')
    exit()

# Regex for links
link_regex = re.compile(r'''(
    http[s]?://
    (?:[a-zA-Z]|
    [0-9]|
    [$-_@.&+]|
    [!*\(\),]|
    (?:%[0-9a-fA-F][0-9a-fA-F]))+
    )''', re.IGNORECASE | re.VERBOSE)

# Get DOI or URL
# Option 1: argument
# Option 2: clipboard
try:
    link = sys.argv[1]
except IndexError:
    link = pyperclip.paste()

# Option 3: manual input
def regex_check(regex, link):
    """
    Check using regex. If no good, input manually until correct.
    """
    while True:
        match = re.match(link_regex, link)
        if match == None:
            link = str(input('Input not valid. Enter valid DOI or URL: > '))
            continue
        else:
            break

# Check DOI / URL is in correct format
regex_check(link_regex, link)

# Open browser > SciHub

# Sci-hub automatic redirect

# file:
# download locally
# send via email
# send to evernote
