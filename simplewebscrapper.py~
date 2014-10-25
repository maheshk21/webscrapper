# Simple Python Web Scrapping program to print all the links in a particular web page
# Author : Mahesh Kumar K


from bs4 import BeautifulSoup
import requests

def webscrap():
	url = raw_input("Enter the url:\t")
	link = requests.get('http://'+url)
	data = link.text
	soup = BeautifulSoup(data)
	for link in soup.find_all('a'):
		print(link.get('href'))

if __name__=="__main__":
	webscrap()
