#UA：User-Agent(请求载体的身份标识)
#UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测
#到载体为某一款浏览器的说明该请求是一个正常的请求。但是，如果检测
#到请求的载体身份表示不是基于某一款浏览器的，则表示该请求为不正常
#的请求（爬虫），则服务器很有可能会拒绝本次请求。

#UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
import requests
if __name__=="__main__":
	#指定url
	url = 'https://www.baidu.com/s?'
	#UA伪装：将对应的User-Agent封装到一个字典中
	headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
	}
	kw = input('input a word:')
	#处理url携带的参数：封装到字典中
	param = {
		'wd':kw
	}
	#对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
	response = requests.get(url=url, params=param, headers=headers)
	
	page_text = response.text
	fileName=kw+'.html'
	with open(fileName, 'w', encoding='utf-8') as fp:
		fp.write(page_text)
	print(fileName, '保存成功！')
