#编码流程：
#1.验证码的识别，获取验证码图片的文字数据
#2.对post请求进行发送（处理请求参数）
#3.对响应数据进行持久化存储

import requests
from lxml import etree
from cnocr import CnOcr

#1.对验证码图片进行捕获和识别
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
	}
url = 'http://www.renren.com/SysHome.do'
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
code_img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
code_img_data = requests.get(url=code_img_src, headers=headers).content
with open('./code.jpg', 'wb') as fp:
	fp.write(code_img_data)
#使用人工识别方法
result = input('请输入验证码:')

login_url = 'http://www.renren.com/ajaxLogin/login71=1&uniqueTimestamp-201934939288'

data = {
	'emall':'www.zhangbowudi@qq.com',
	'lcode':result,
	'orlgURL':'http://www.renren.com/home',
	'domain':'renren.com',
	'key_ld':'1',
	'captcha_type':'web_login',
	'password':'6cc43fc30ade20f0748892610fad005c9696c9809329279c1985dc4cd8ab591f',
	'rkey':'3d1f9abdaae1f018a49d38069fe743c8',
}
# login_page_text = requests.post(url=login_url, headers=headers, data=data).text
# with open('renren.html', 'w', encoding='utf-8') as fp:
# 	fp.write(login_page_text)
response = requests.post(url=url, headers=headers, data=data)
print(response.status_code)
