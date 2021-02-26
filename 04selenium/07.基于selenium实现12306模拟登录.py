import requests
from hashlib import md5

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

#模拟真实滑动轨迹
def get_track(distance):
    track = []
    current = 0
    mid = distance * 3 / 4
    t = 0.2
    v = 0
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        v = v0 + a * t
        move = v0 * t + 1 / 2 * a * t * t
        current += move
        track.append(round(move))
    return track

from selenium import webdriver
import time
from PIL import Image
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(1)


count_log = bro.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')
count_log.click()

#确保验证码图片能够加载出来
time.sleep(5)

#save_screenshot：将当前get打开的页面进行截图保存
bro.save_screenshot('aa.png')

#确定验证码图片对应的左上角和右下角的坐标（确定需要裁剪的区域）
code_img_ele = bro.find_element_by_xpath('//*[@id="J-loginImg"]')
#验证码左上角的坐标x, y
location = code_img_ele.location
#验证码标签对应的长和宽
size = code_img_ele.size
#左上角和右下角的坐标， 确定验证码图片的区域
print(location, size)
rangle = (
    location['x']-20, location['y'], location['x']+size['width']-40, location['y']+size['height'])

i = Image.open('./aa.png')
code_img_name = 'code.png'
#crop根据指定区域进行图片裁剪
frame = i.crop(rangle)
frame.save(code_img_name)

#将验证码图片提交给超级鹰进行识别
chaojiying = Chaojiying_Client('zfh12332', 'zfh12332', '911612')
im = open('code.png', 'rb').read()
print ('超级鹰返回的位置坐标：', chaojiying.PostPic(im, 9004)['pic_str'])
result = chaojiying.PostPic(im, 9004)['pic_str']
all_list = [] #存储即将被点击的点的坐标 [[x1, y1], [x2, y2]]
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append((xy_list))
print('解析出超级鹰返回的数据并存放在列表中：', all_list)

for l in all_list:
    x = l[0]
    y = l[1]
    ActionChains(bro).move_to_element_with_offset(code_img_ele, x, y).click().perform()

bro.find_element_by_id('J-userName').send_keys('xxxxxxx')
time.sleep(2)
bro.find_element_by_id('J-password').send_keys('xxxxxxx')
time.sleep(2)
bro.find_element_by_id('J-login').click()


#进行滑动验证（这里不能很好的实现滑动验证）
#防止加载不出来滑动验证的页面
time.sleep(0.5)
#确定滑块位置
span = bro.find_element_by_xpath('//*[@id="nc_1_n1z"]')

#动作链
action = ActionChains(bro)
#点击长按指定的标签
action.click_and_hold(span)

track = get_track(300)
for d in track:
    action.move_by_offset(150, 0).perform()

# for i in range(2):
#     #perform()立即执行动作链操作
#     #move_by_offset(x, y):x:水平方向，y：竖直方向
#     action.move_by_offset(150, 0).perform()

#释放动作链
action.release()

time.sleep(3)
bro.quit()

