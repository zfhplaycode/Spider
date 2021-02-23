import requests
import json

if __name__=="__main__":
	url='https://movie.douban.com/j/search_subjects'
	movie_type=input("Enter a moive type:")
	movie_tag=input("Enter a moive tag:")
	param={
	'type':movie_type,
	'tag':movie_tag,
	'sort':'recommend',
	'page_limit':'20',
	'page_start':'0',
	}
	headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
	}

	response = requests.get(url=url, params=param, headers=headers)
	dict_obj = response.json()

	fileName = movie_tag+'(豆瓣).json'
	fp = open(fileName, 'w', encoding='utf-8')
	json.dump(dict_obj, fp=fp, ensure_ascii=False)

	print('Over!')