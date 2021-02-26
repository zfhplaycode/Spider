import requests
from lxml import etree
#单行注释 ctrl+/
#多行注释 ctrl+shift+/
#知识点：xpath同时爬取多个层级关系的数据

if __name__=="__main__":
	# headers = {
	# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
	# }
	# url = 'https://www.aqistudy.cn/historydata/'
	# page_text = requests.get(url=url, headers=headers).text
	# tree = etree.HTML(page_text)
	# hot_city_list = tree.xpath('//div[@class="bottom"]/ul/li')
	# all_city_names = []
	# for li in hot_city_list:
	# 	hot_city_name = li.xpath('./a/text()')[0]
	# 	all_city_names.append(hot_city_name)
	# all_city_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
	# for li in all_city_list:
	# 	city_name = li.xpath('./a/text()')[0]
	# 	all_city_names.append(city_name)
	# print(all_city_names, len(all_city_names))
	
	headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
	}
	url = 'https://www.aqistudy.cn/historydata/'
	page_text = requests.get(url=url, headers=headers).text
	tree = etree.HTML(page_text)
	city_names = []
	#//div[@class="bottom"]/ul/li/        热门城市a标签的层级关系
	#//div[@class="bottom"]/ul/div[2]/li/ 全部城市a标签的层级关系
	city_list = tree.xpath('//div[@class="bottom"]/ul/li | //div[@class="bottom"]/ul/div[2]/li')
	for li in city_list:
		city_name = li.xpath('./a/text()')[0]
		city_names.append(city_name)

	print(city_names, len(city_names))