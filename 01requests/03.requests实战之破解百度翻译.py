import requests
import json

if __name__=="__main__":
	#1.指定url
	post_url = 'https://fanyi.baidu.com/langdetect'
	#2.进行UA伪装
	headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
	}
	#3.post请求参数处理（同get请求一致）
	word = input('Enter a word:')
	data = {
	'query': word,
	}
	#4.请求发送(url+params+headers)
	response = requests.post(url=post_url, data=data, headers=headers)
	#5.获取响应数据：json()方法返回的是obj（如果确认响应数据是json类型才可以使用该方法）
	dict_obj = response.json()
	#持久化存储
	fileName = word+'.json'
	fp=open(fileName, 'w', encoding='utf-8')
	json.dump(dict_obj, fp=fp, ensure_ascii=False)
	print('Over!')
