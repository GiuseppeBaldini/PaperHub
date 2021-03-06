# Input DOI / URL

import re
import sys

# Pyperclip is not built-in, check and download if needed
try:
    import pyperclip
except (ImportError, ModuleNotFoundError):
    print('Pyperclip module not found. Please download it.')
    sys.exit(0)

# Regex for links
link_regex = re.compile(r'''(
    http[s]?://
    (?:[a-zA-Z]|
    [0-9]|
    [$-_@.&+]|
    [!*\(\),]|
    (?:%[0-9a-fA-F][0-9a-fA-F]))+
    )''', re.IGNORECASE | re.VERBOSE)

# Get DOI / URL using different methods

# Method 1: argument
try:
    input_link = sys.argv[1]
# Method 2: clipboard
except IndexError:
    input_link = pyperclip.paste()

# Method 3: manual input
def regex_check(regex, link):
    """
    Check using regex. If DOI/URL are not in the right format,
    require manual input until correct or Enter to quit.
    """
    while True:
        match = re.match(regex, link)
        if match == None:
            link = str(input('''Enter valid DOI / URL or press Enter to quit: > '''))
            if link == '':
                exit()
            else:
                continue
        else:
            return link

url = regex_check(link_regex, input_link)