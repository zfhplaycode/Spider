#基本框架
#指定url
url = "xxx"
#在头信息中进行UA伪装
headers = {
	'User-Agent':'xxx',
}
#处理带参数的url(可选, get)
param = {
	'xxx':'xxx',
}
#处理带参数的url(可选, post)
data = {
	'xxx':'xxx',
}

#使用requests模块发起get请求(可携带参数), 获取响应数据
response = requests.get(url=url, params=param, headers=headers)

#使用代理
page_text = requests.get(url=url, headers=headers, proxies={'https':'49.70.95.102:9999'}).text

#使用requests模块发起post请求(通常会携带参数)
response = requests.post(url=post_url, data=data, headers=headers)

#获取响应数据(文本格式)
page_text = response.text
#持久化存储
with open(filename, 'w', encoding='utf-8') as fp:
	fp.write(page_text)

#获取响应数据(json格式)
dic_obj = response.json()
#json格式的持久化存储
fp = open(filename, 'w', encoding='utf-8')
json.dump(dic_obj, fp=fp, ensure_ascii=False)

#必要的信息提示
print('xxx')
