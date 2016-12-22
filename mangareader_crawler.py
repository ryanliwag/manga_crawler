#!/usr/bin/python3

import requests
import cfscrape

from bs4 import BeautifulSoup


print("mangareader web scraper")

scraper = cfscrape.create_scraper() # CloudflareScraper instance 

def download_img(page_url):
	soup_img = BeautifulSoup(scraper.get(page_url).content, 'html.parser')
	imgurl = scraper.get(soup_img.find('img')['src']).content
	text_test = str(soup_img.find('img')['alt'])
	with open(text_test,'wb') as image:
		image.write(imgurl)
		print(text_test + ' download complete')

url = ("http://www.mangareader.net/magi/331") #change url to download different manga 
site = ("http://www.mangareader.net")

#variables
iterate = True
jump_url2 = ('')
jump_url = url

while (iterate == True):
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
		download_img(jump_url2)
	
	


		
	
	




	










