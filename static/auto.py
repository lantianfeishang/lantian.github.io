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
url = 'https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=906471136&courseId=246167166&clazzid=105956415&cpi=353007561&enc=d74465392df862b8366bfcb913e7f433&mooc2=1&openc=2eea01aabc52c4de414bfc9672588e7a'
number="13536376323"
password="ltz673718601"

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
   try:
      browser.switch_to.frame('iframe')
      frame2 = browser.find_element(By.XPATH,'/html/body/div[2]/div/p/div/iframe')
      browser.switch_to.frame(frame2)
      browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[3]/div[2]/div/button').click()
      print("尝试开始视频")
   except:
      print("视频开启失败")
      return 0
   else:
      print("视频开启成功")
      return 1
   finally:
      browser.switch_to.default_content()
      browser.switch_to.default_content()
#视频结束
def videoOver():
   try:
      time.sleep(1)
      browser.find_element(By.ID,'prevNextFocusNext').click()
      time.sleep(1)
      browser.find_element(By.ID,'prevNextFocusNext').click()
      print("跳过视频")
   except:
      pass
   finally:
      return 0
#已经看过
def videoHadOver():
   time.sleep(1)
   try:
      browser.switch_to.frame('iframe')
      s = browser.find_element(By.XPATH,'/html/body/div[2]/div/p/div/div[1]').get_attribute("aria-label")
      p = '.+\S?'
      word = re.findall(p, s, re.S)[0]
      browser.switch_to.default_content()
      if word == "任务点已完成":
         print("视频已经看过")
         return True
      else:return False
   except:pass
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
         browser.switch_to.default_content()
      time.sleep(5)
#视频主程序
def watch():
   a = 0
   while True:
      time.sleep(2)#2秒检测一次
      if videoHadOver():
         a = videoOver()
      if a == 0:
         a = videoOpen()

login(number,password)
watch()
t = threading.Thread(target=is_exist())
t.start()
t.join()