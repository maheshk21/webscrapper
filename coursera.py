# Web Scrapping program to access all the courses available in Coursera	
# Author : Mahesh Kumar K

import requests
import json

def nyscrapper():
	url = 'https://api.coursera.org/api/catalog.v1/courses'
	response = requests.get(url)
	#response.text	
	jsondata = json.loads(response.text)
	for item in jsondata['elements']:
		print "Course ID:",item['id']
		print "Course Short Name:",item['shortName']
		print "Course Name:",item['name']
		print "\n"

if __name__=="__main__":
	nyscrapper()
