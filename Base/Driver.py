from appium import webdriver

def appium_desired():
        desired_caps = dict()

        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = '11'
        desired_caps["deviceName"] = "*******"
        desired_caps["appPackage"] = "com.qingjiaocloud"
        desired_caps["appActivity"] = "com.qingjiaocloud.guide.WelcomeActivity"
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        desired_caps["noReset"] = True

        return webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

