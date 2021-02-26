from selenium import webdriver
from time import sleep
#实现无可视化页面
from selenium.webdriver.chrome.options import Options
#实现规避检测
from selenium.webdriver import ChromeOptions

#实现无可视化界面的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#实现规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

bro = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options,options=option)
bro.get('https://www.baidu.com')
page_text = bro.page_source
with open('无头浏览器+规避检测.html', 'w', encoding='utf-8') as fp:
	fp.write(page_text)
sleep(3)
bro.quit()