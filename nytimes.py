# Web Scrapping program to access news on The New York Times
# Author : Mahesh Kumar K

import requests
import lxml.html as lh

def nyscrapper():
	url = str(raw_input("Enter the NY Times link :\t")) # visit the new york website and paste the corresponding link for better results.
	response = requests.get(url)
	document = lh.fromstring(response.content)
	text = document.xpath('//p[@itemprop="articleBody"]')
	nynews = str()

	for details in text:
		nynews += details.text_content()

	print nynews

if __name__=="__main__":
	nyscrapper()
