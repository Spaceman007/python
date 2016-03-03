#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import time
import urllib.request, re

"""
下载http://weheartit.com/inspirations/taylorswift上的图片
"""

localSavePath = '/Users/Long/Downloads/girls/'
url = 'http://weheartit.com/inspirations/taylorswift?scrolling=true&page='
pic_number = 1

def download_file(url):
	global pic_number
	pattern = r'(?<=[^\.])\.\w+$'
	match = re.search(pattern, url)
	if match:
		filename = localSavePath + str(pic_number) + match.group()
		print(filename)
		pic_number += 1
		with open(filename, 'wb') as f:
			r = requests.get(url)
			f.write(r.content)

def download_single_page(url):
	wb_data = requests.get(url)
	soup = BeautifulSoup(wb_data.text, 'lxml')
	imgs = soup.select('div > a > img.entry_thumbnail')

	for img in imgs:
		download_file(img.get('src'))

def download(start, end):
	for i in range(start, end):
		download_single_page(url + str(i))

download(0, 2)
