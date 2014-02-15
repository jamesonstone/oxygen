#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup


def get_links(url):
	connector = urllib2.urlopen(url)
	html = connector.read()
	soup = BeautifulSoup(html)
	links = soup.find_all('a')
	for html_tag in links:
		link = html_tag.get('href', None)
		if link != None:
			print link


def main():
	url = raw_input('What url would you like to run the crawler against? ')
	get_links('http://www.' + url + '/')




# run main when called
if __name__ == "__main__":
	main()