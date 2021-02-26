import requests
from lxml import etree
import re
from multiprocessing.dummy import Pool
#需求：爬取梨视频的视频数据(由于梨视频的前端代码发生变化，暂时还没有解析出正确的
#视频下载地址,但已构建出正确的应用框架)
#原则：线程池处理的是阻塞且较为耗时的操作
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
#获取视频首页
url = 'https://www.pearvideo.com/category_5'
page_text = requests.get(url=url, headers=headers).text

#解析出存放视频详情页的名字和url
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@id="listvideoList"]/ul/li')

#热门视频的url and name作为字典存入urls中
urls = []
#视频详情页的url(含参数)
detail_url = 'https://www.pearvideo.com/videoStatus.jsp'
for li in li_list:
	#解析出每个视频的名字及视频真实连接的参数
	video_url = li.xpath('./div/a/@href')[0]
	video_name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
	contId = video_url[6:]

	#请求获取视频详情页所需的头信息and参数
	video_headers = {
	'Referer':video_url,
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
	}
	param = {
	'contId': contId,
	}
	#解析出采用AJAX方法所接受的信息
	res = requests.get(url=detail_url, params=param, headers=video_headers).json()

	#得到伪装的的视频下载地址
	down_url = res['videoInfo']['videos']['srcUrl']

	#创建真实的视频下载地址
	ex = 'mp4/.*?/.*?/(.*?)-.*?'
	need_replace = re.findall(ex, down_url)[0]
	replaced = 'cont-' + contId
	down_url = down_url.replace(need_replace, replaced)

	#存入urls中
	dic = {
	'url':down_url,
	'name':video_name,
	}
	urls.append(dic)

def get_content(dic):
	print(dic['name'], '正在下载。。。。')
	video_data  = requests.get(url=dic['url'], headers=headers).content
	with open(dic['name'], 'wb') as fp:
		fp.write(video_data)
		print(dic['name'], '下载成功')

pool = Pool(4)
pool.map(get_content, urls)
pool.close()
pool.join()



