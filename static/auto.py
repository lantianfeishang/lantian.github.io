import time,os,re,threading
from selenium import webdriver
from selenium.webdriver.common.by import By
"""
手册：

若此上import或from后的英文为灰色，则自行搜索xxx导包。from优先级大于import

url:为课程地址
number:为学习通账号
password:为学习通密码
请填写

至此，可使用
"""
url = ''
number=""
password=""

os.system('cls')
browser = webdriver.Firefox()
browser.get(url)
time.sleep(3)
def login(number,password):
   browser.find_element(By.ID,'phone').send_keys(number)#输入手机号码
   browser.find_element(By.ID,'pwd').send_keys(password)#输入密码
   browser.find_element(By.ID,'loginBtn').click()
#开始视频
def videoOpen():
   time.sleep(1)
   frame1 = browser.find_element(By.XPATH,'//*[@id="iframe"]')
   browser.switch_to.frame(frame1)
   frame2 = browser.find_element(By.XPATH,'/html/body/div[2]/div/p/div/iframe')
   browser.switch_to.frame(frame2)
   browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[3]/div[2]/div/button').click()
   browser.switch_to.default_content()
   browser.switch_to.default_content()
#视频结束
def videoOver():
   time.sleep(1)
   browser.find_element(By.ID,'prevNextFocusNext').click()
   time.sleep(1)
   browser.find_element(By.ID,'prevNextFocusNext').click()
#已经看过
def videoHadOver():
   time.sleep(1)
   frame1 = browser.find_element(By.XPATH,'//*[@id="iframe"]')
   browser.switch_to.frame(frame1)
   s = browser.find_element(By.XPATH,'/html/body/div[2]/div/p/div/div[1]').get_attribute("aria-label")
   p = '.+\S?'
   word = re.findall(p, s, re.S)[0]
   browser.switch_to.default_content()
   if word == "任务点已完成":
      return True
   else:False
#问题弹窗
def is_exist():
   while True:
      try:
         browser.switch_to.frame('tmDialog_iframe')#答题窗口在另一个frame里面，要切换
         box=browser.find_elements(By.CLASS_NAME,'answerOption')#答题列表
         radio=box[0].find_element(By.TAG_NAME,'input')#找到第一个选项
         radio.click()#选择
         browser.find_element(By.LINK_TEXT,'关闭').click()#关闭答题窗口
         browser.switch_to.default_content()
      except:
         browser.switch_to.parent_frame()#没有弹出，切换回本来的frame
      time.sleep(5)
#视频主程序
def watch():
   a = 0
   while True:
      time.sleep(2)#2秒检测一次
      if videoHadOver():
         videoOver()
         a=0
      if a == 0:
         videoOpen()
         time.sleep(1)
         a=1

login(number,password)
watch()
t = threading.Thread(target=is_exist())
t.start()
t.join()