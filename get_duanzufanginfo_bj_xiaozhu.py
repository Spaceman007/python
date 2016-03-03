from bs4 import BeautifulSoup
import requests

'''
从bj.xiaozhu.com获取短租房信息
'''

urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(0,13)]
house_number = 0

# 获取单个房子的详细信息
def get_house_info(url):
	wb_data = requests.get(url)
	soup = BeautifulSoup(wb_data.text, 'lxml')

	imgs = soup.select('img#curBigImage')
	titles = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
	addrs = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span.pr5')
	prices = soup.select('#pricePart > div.day_l > span')
	owner_imgs  = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
	owner_names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
	owner_genders = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span')

	for title,addr,price,img,owner_img,ownder_name,owner_gender in zip(titles,addrs,prices,imgs,owner_imgs,owner_names,owner_genders):
		gender = 'M'

		if owner_genders[0].get('class')[0] == 'member_girl_ico':
			gender = 'F'

		data = {
				'title': title.get_text(),
				'addr' : addr.get_text().strip(),
				'price': price.get_text(),
				'img'  : img.get('src'),
				'owner_img': owner_img.get('src'),
				'ownder_name': ownder_name.get_text(),
				'owner_gender': gender
		}
		for k,v in data.items():
			print(k+':'+v)
		print('----------------------------')

for url in urls:
	wb_data = requests.get(url)
	soup = BeautifulSoup(wb_data.text, 'lxml')
	house_urls = soup.select('#page_list > ul > li > a[target="_blank"]')

	for house_url in house_urls:
		get_house_info(house_url.get('href'))
		house_number += 1
		if house_number > 10:
			break
	if house_number > 10:
		break
