import requests
from lxml import etree
import os

if __name__=="__main__":
	url = 'http://pic.netbian.com/4kmeinv'
	headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
	}
	page_text = requests.get(url=url, headers=headers).text
	#response = requests.get(url=url, headers=headers)
	#response.encoding = 'utf-8'
	#page_text = response.text
	tree = etree.HTML(page_text)
	li_list = tree.xpath('//div[@class="slist"]//li')
	if not os.path.exists('./picLibs'):
		os.mkdir('./picLibs')
	for li in li_list:
		img_url = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
		img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
		#通用处理中文乱码的方案
		img_name = img_name.encode('iso-8859-1').decode('gbk')
		img_data = requests.get(url=img_url, headers=headers).content
		img_path = './picLibs/' + img_name
		with open(img_path, 'wb') as fp:
			fp.write(img_data)
			print(img_name, '下载成功！')