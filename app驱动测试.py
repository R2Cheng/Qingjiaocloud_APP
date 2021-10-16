from appium import webdriver
from time import sleep

# 前置代码、
# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = '********'

# app信息
desired_caps['appPackage'] = 'com.qingjiaocloud'
desired_caps['appActivity'] = 'com.qingjiaocloud.guide.WelcomeActivity'
#获取完整的activity，https://www.cnblogs.com/nimantou/p/12486788.html

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 暂停3秒
sleep(3)
# 关闭 设置
driver.close_app()

# 关闭所有
driver.quit()
