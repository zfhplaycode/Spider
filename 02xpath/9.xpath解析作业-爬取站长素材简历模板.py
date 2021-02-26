import requests
from lxml import etree
import os

if __name__=="__main__":
	# if not os.path.exists('./简历'):
	# 	os.mkdir('./简历')
	# headers = {
	# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
	# }
	# url = 'https://sc.chinaz.com/jianli/free.html'
	# page_text = requests.get(url=url, headers=headers).text
	# tree = etree.HTML(page_text)

	# div_list = tree.xpath('//div[@class="sc_warp  mt20"]/div/div/div')

	# for div in div_list:
	# 	jianli_url ='https:' + div.xpath('./a/@href')[0]
	# 	jianli_page_text = requests.get(url=jianli_url, headers=headers).text
	# 	jianli_tree = etree.HTML(jianli_page_text)
	# 	download_url = jianli_tree.xpath('//div[@class="down_wrap"]/div[2]/ul/li/a/@href')[0]
	# 	jianli_data = requests.get(url=download_url, headers=headers).content
	# 	jianli_name = download_url.split('/')[-1]
	# 	jianli_path = './简历/' + jianli_name
	# 	with open(jianli_path, 'wb') as fp:
	# 		fp.write(jianli_data)
	#		print(jianli_name, '下载成功！')

	if not os.path.exists('./简历'):
		os.mkdir('./简历')
	headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
	}
	#通过基础url构建不同页面的url
	base_url = 'https://sc.chinaz.com/jianli/free'
	for index in range(1, 3):#更改range中的不同参数遍历不同页面数据
		if index==1:
			url = base_url + '.html'
		else:
			url = base_url + '_' + str(index) + '.html'
		page_text = requests.get(url=url, headers=headers).text
		tree = etree.HTML(page_text)

		#找到对应的div标签
		div_list = tree.xpath('//div[@class="bggray clearfix pt20"]/div[3]/div/div/div')		# for div in div_list:
		for div in div_list:
			#获取取每个简历对应的url
			jianli_url ='https:' + div.xpath('./a/@href')[0]
			#获取每个简历的下载页面
			jianli_page_text = requests.get(url=jianli_url, headers=headers).text
			jianli_tree = etree.HTML(jianli_page_text)
			#获取每个简历的下载链接
			download_url = jianli_tree.xpath('//div[@class="down_wrap"]/div[2]/ul/li/a/@href')[0]
			#获取简历
			jianli_data = requests.get(url=download_url, headers=headers).content
			#根据简历的下载链接构造每个简历的名字
			jianli_name = download_url.split('/')[-1]
			jianli_path = './简历/' + jianli_name
			#持久化存储
			with open(jianli_path, 'wb') as fp:
				fp.write(jianli_data)
				print(jianli_name, '下载成功！')	
				