#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import time

'''
打印深圳二手平板电脑信息
'''

origin_url = 'http://sz.58.com/pbdn/'

def get_views_from(url):
	id = url.split('/')[-1].strip('x.shtml')
	api = 'http://jst1.58.com/counter?infoid={}'.format(id)
	js = requests.get(api)
	views = js.text.split('=')[-1]
	return views

def get_product_info(url, who=0):
	wb_data = requests.get(url)
	soup = BeautifulSoup(wb_data.text, 'lxml')

	title = soup.title.text
	date = soup.select('.time')
	price = soup.select('#content span.price')
	condition = soup.select('div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(2) > div.su_con > span')
	area = soup.select('.c_25d')

	data = {
			'category': '个人' if who == 0 else '商家',
			'title': title,
			'date': date[0].text,
			'price': price[0].text,
			'condition': condition[0].text.strip(),
			'area': list(area[0].stripped_strings) if soup.find_all('span', 'c_25d') else None,
			'view': get_views_from(url)
	}

	for k,v in data.items():
		print(str(k)+': '+str(v))
	print('---------------------------------------------\n')

def get_product_links(origin_url, who=0):
	urls = [(origin_url + str(who) + '/pn{}/').format(str(i)) for i in range(1, 3)]
	links = []
	for url in urls:
		wb_data = requests.get(url)
		soup = BeautifulSoup(wb_data.text, 'lxml')
		product_urls = soup.select('td.t > a.t')
		for i in product_urls:
			link = i.get('href').split('?')[0]
			if link.split('/')[2] == 'sz.58.com':
				links.append(link)

	return links

# who: 0 - '个人', else, '商家'
def show_all_products(origin_url, who):
	for url in get_product_links(origin_url, who):
		get_product_info(url, who)
		#time.sleep(1)

show_all_products(origin_url, 0)
