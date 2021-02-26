import requests
import re
import os
#爬取糗事百科中糗图板块下所有的糗图图片
if __name__=="__main__":
	#创建一个文件夹保存所有的图片
	if not os.path.exists('./qiutuLibs'):
		os.mkdir('./qiutuLibs')
	url = 'https://www.qiushibaike.com/imgrank/'
	#UA伪装
	headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
	}
	#设置通用的url模板
	url = 'https://www.qiushibaike.com/imgrank/page/%d/'
	for pageNum in range(1, 3):
		new_url = format(url%pageNum)
		#使用通用爬虫对url对应的一整张页面进行爬取
		page_text = requests.get(url=new_url, headers=headers).text
		#构造正则表达式(***)，使用聚焦爬虫将页面中所有的糗图进行解析/爬取
		ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'
		image_src_list = re.findall(ex, page_text, re.S)
		#print(image_url)
		for src in image_src_list:
			#拼接出一个完整的图片url
			src = 'https:' + src
			#请求图片的二进制数据
			image_data = requests.get(src, headers=headers).content
			#生成图片名称
			image_name = src.split('/')[-1]
			#构造图片的存储路径
			imgPath = './qiutuLibs/' + image_name
			with open(imgPath, 'wb') as fp:
				fp.write(image_data)
				print(image_name, '下载成功！')
