#爬取单张糗图图片
import requests

if __name__=="__main__":
	#如何爬取图片数据
	url = 'https://pic.qiushibaike.com/system/pictures/12393/123933419/medium/JMONJGP52IXHG3E0.jpg'
	#content返回的是二进制形式的图片数据
	#text(字符串) content(二进制) json()(对象)
	image_data = requests.get(url=url).content
	with open('./image.jpg', 'wb') as fp:
		fp.write(image_data)