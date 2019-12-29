# PaperHub
A Python script to download scientific papers from scihub using DOI / URL.

### Introduction

For convenience (and learning), the script is split into three parts:

**1. Input**
* Argument to the script `paperhub.py [DOI / URL]` (default)
* Most recent copied content stored in clipboard 
* User input (if both the above fail)

_The input text is validated through a simple regex to make sure it is a valid URL._

**2. Retrieve**
Using the URL from step 1, it finds the corresponding scihub page of the paper and returns the pdf file URL.

**3. Download**
It downloads the pdf file. Currently only storing locally in the default Downloads folder.

### Dependencies

* [Pyperclip](https://github.com/asweigart/pyperclip) (clipboard functions)
* [Requests](https://2.python-requests.org//en/latest/) (HTTP library)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (library to parse HTTP / XML)

### Improvements

**1. Exception handling**  
Make script more resilient to edge cases errors 

**2. Output**  
Optional arguments to send download file via email / store in Evernote

**3. GUI**   
Improve input experience and output choice using a simple graphic interface
