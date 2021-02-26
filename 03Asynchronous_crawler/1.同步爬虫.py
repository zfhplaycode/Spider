import requests
headers = {}
urls = []

def get_content(url):
	print('正在爬取：', url)
	response = requests.get(url=url, headers=headers)
	if resposne.status_code == 200 :
		return resposne.content

def parse_content(content):
	print('响应数据的长度为：', len(content))

for url in urls:
	content = get_content(url)
	parse_content(content)