# Web Scrapping program to access all the courses and the universities available in Coursera	
# Author : Mahesh Kumar K

import requests
import json

def courseradata():
	# api links
	courseurl = 'https://api.coursera.org/api/catalog.v1/courses'
	universitiesurl='https://api.coursera.org/api/catalog.v1/universities'
	
	# access the corresponding links	
	cresponse = requests.get(courseurl)
	uresponse = requests.get(universitiesurl)

	# loading the data into json format	
	cjsondata = json.loads(cresponse.text)
	ujsondata = json.loads(uresponse.text)
	
	# for loop to print available courses
	for item in cjsondata['elements']:
		print "Course ID:",item['id']
		print "Course Short Name:",item['shortName']
		print "Course Name:",item['name']
		print "\n"

	# for loop to print participating universities	
	for item in ujsondata['elements']:
		print "University ID:", item['id']
		print "University Name:", item['shortName']
		print "\n"

if __name__=="__main__":
	courseradata()
