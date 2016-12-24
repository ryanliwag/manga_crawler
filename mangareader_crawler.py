#!/usr/bin/python3

import requests
import cfscrape
import os
import argparse
from bs4 import BeautifulSoup

print("mangareader webscraper")

parser = argparse.ArgumentParser()
parser.add_argument("mangareader_url", help="input manga url ex: http://www.mangareader.net/bleach")
args = parser.parse_args()
scraper = cfscrape.create_scraper() # CloudflareScraper instance 

def download_img(page_url):
	soup_img = BeautifulSoup(scraper.get(page_url).content, 'html.parser')
	imgurl = scraper.get(soup_img.find('img')['src']).content
	text_test = str(soup_img.find('img')['alt'])
	with open( title.string + '/' + text_test,'wb') as image:
		image.write(imgurl)
		print(text_test + ' download complete')


url = str(args.mangareader_url)
site = ('http://www.mangareader.net')
soup = BeautifulSoup(scraper.get(url).content, 'html.parser')
title = soup.find('h1') # finds the h1 tag, which is the manga title

os.makedirs(title.string)# creates folder named after the manga title

#variables
iterate = True
jump_url = (url + '/1') #takes the first chapter in the manga series

while (iterate == True): #finds the "href" tag to the next manga page and concatenates it to the site link
	new_soup = BeautifulSoup(scraper.get(jump_url).content, 'html.parser')
	for new_links in new_soup.find_all('a'):
		string_1 = str(new_links)
		if string_1.find('Next') > 0:
			new_word = new_links	
	jump_url2 = jump_url
	new_href = str(new_word.get('href'))
	jump_url = site + new_href
	if jump_url2 == jump_url:
		iterate = False
	else:
		print(jump_url2)
	
	


		
	
	




	











		
	
	




	










