from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('https://qzone.qq.com')

bro.switch_to.frame('login_frame')
a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()

userName_tag = bro.find_element_by_id('u')
passWord_tag = bro.find_element_by_id('p')
sleep(1)
userName_tag.send_keys('1505688484')
sleep(1)
passWord_tag.send_keys('Sn.zfh.123')
sleep(1)
btn = bro.find_element_by_id('login_button')
btn.click()

sleep(10)
bro.quit()