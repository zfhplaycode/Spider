from selenium import webdriver
from lxml import etree

#实例化一个浏览器对象（传入浏览器的驱动程序）
bro = webdriver.Chrome(executable_path='./chromedriver')
#让浏览器发起一个指定url对应请求
bro.get('https://www.taobao.com/')


#page_source获取浏览器当前页面的源码数据
page_text = bro.page_source

#解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
	name = li.xpath('./dl/a/@title')
	print(name)

bro.quit()