# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import webbrowser
import re

base_url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
r = requests.get(base_url) 
soup = BeautifulSoup(r.text, "html.parser")

for words in soup.find_all(text = re.compile("student")):
	letter = str(words)
	letter = letter.replace("student", "AMAZING student")
	words.replaceWith(letter)#Replaces all words with student to AMAZING student

for img in soup.find_all('img'):
	if img['src'] == "https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg":
		img['src'] = "Jonny.jpg" #Replaces main picture with a picture of me
	else:
		img['src'] = "Media/logo.png" #Replaces rest of pictures with School of Info Pic

my_string = str(soup)


txtfile = open("HW3_BSI_Page.html", "w") #Saves it to a html file
txtfile.write(str(soup))
txtfile.close()

#References: http://stackoverflow.com/questions/1579133/replace-src-of-all-img-elements-using-parser
             #https://www.crummy.com/software/BeautifulSoup/bs4/doc/
             #https://docs.python.org/2/library/re.html#re.compile