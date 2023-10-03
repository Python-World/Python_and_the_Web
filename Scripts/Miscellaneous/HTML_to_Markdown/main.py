# Importing required libraries/modules
import os

import html2text

# Empty string to add html source to it
html = ""

# Reading index.html file line by line
for line in open("index.html").readlines():
    # Adding lines of html file to 'html'
    html += line.strip()

# Using 'html2text' function in 'html2text'
markdown = html2text.html2text(html)

# Created the README file for this project using index.html and main.py files

# Opening a new file
with open("README.md", "w") as file:
    # Writing into the README.md file
    file.write(markdown)
