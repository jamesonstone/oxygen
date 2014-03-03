#!/usr/bin/python
import urllib2
import httplib
from bs4 import BeautifulSoup

# global link set
linkset = []


def get_links(url):
	connector = urllib2.urlopen(url)
	html = connector.read()
	soup = BeautifulSoup(html)
	links = soup.find_all('a')
	
	for html_tag in links:
		link = html_tag.get('href', None)
		linkset.append(link)
		if link != None:
			print link

def get_status(url):
	conn = httplib.HTTPConnection(url)
	conn.request("GET", link)
	resp = conn.getresponse()
	print r1.status, r1.reason

def find_the_status():
	for linkers in linkset:
		get_status(linkers)


def main():
	url = raw_input('What url would you like to run the crawler against? ')
	get_links('http://www.' + url + '/')
	find_the_status()




# run main when called
if __name__ == "__main__":
	main()