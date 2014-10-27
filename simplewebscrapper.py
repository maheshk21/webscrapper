# Simple Python Web Scrapping program to print all the links in a particular web page
# Author : Mahesh Kumar K


from bs4 import BeautifulSoup
import requests

def webscrap():
	url = raw_input("Enter the url:\t")  # accepts the url
	link = requests.get('http://'+url)   # it requests for that particular url
	data = link.text                     # converting into into
	soup = BeautifulSoup(data)           # Parsing the data using BeautifulSoup
	for link in soup.find_all('a'):
		print(link.get('href'))

if __name__=="__main__":
	webscrap()
