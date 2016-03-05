#!/usr/bin/env python3

import requests
import json
from bs4 import BeautifulSoup

'''
从豆瓣获取电影信息
'''

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag='

def get_movies(url, new=False, tag='最新', page_limit=20, page_start=0, sort = 'time'):
	movie_list = []
	if tag == '最新':
		url = (url + '{}&page_limit={}&page_start={}').format(tag, page_limit, page_start)
	else:
		url = (url + '{}&sort={}&page_limit={}&page_start={}').format(tag, sort, page_limit, page_start)

	wb_data = requests.get(url)
	movies = json.loads(wb_data.text)['subjects']
	for movie in movies:
		if new and not movie['is_new']:
			continue
		else:
			movie_data = requests.get(movie['url'])
			movie_soup = BeautifulSoup(movie_data.text, 'lxml')
			last = movie_soup.select('span[property="v:runtime"]') #时长
			movie['last'] = last[0].text
			dates = movie_soup.select('span[property="v:initialReleaseDate"]') # 上映时间
			movie['date'] = [item.text for item in dates]
			summary = movie_soup.select('span[property="v:summary"]')
			movie['summary'] = summary[0].get_text().strip()
			for k,v in movie.items():
				print(k+': '+str(v))
			print('-----------------------------------\n')
	
# 获取最新的电影
def get_newest_movies():
	get_movies(url,True,tag='最新',page_limit=20)

# 获取热门电影
def get_hot_movies(page_limit=20, sort='recommend'):
	get_movies(url,False,'热门',page_limit, 0, sort)


# 获取科幻电影
def get_sciencefiction_movies(page_limit=2, sort='recommend'):
	get_movies(url, False, '科幻', page_limit, 0, sort)

get_sciencefiction_movies(5)
