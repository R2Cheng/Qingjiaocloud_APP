# 此模块只负责去定位 me 界面上的元素pytest框架app自动化执行用例只打开一次app
from selenium.webdriver.common.by import By
from Base.Action import BaseAction


class PageMe(BaseAction):


    #我的页-退出账号
    logout_feature = By.ID, "com.qingjiaocloud:id/tv_loginout"
    #我的页-确认退出
    confirm_feature = By.ID, "com.qingjiaocloud:id/tv_dialog_yes"
    #我的页-取消退出
    cancel_feature = By.ID, "com.qingjiaocloud:id/tv_dialog_no"


    # 1 退出账号
    def get_logout_ele(self):
        return self.get_element(self.logout_feature)

    # 2 确认退出
    def get_confirm_ele(self):
        return self.get_element(self.confirm_feature)

    # 3 取消退出
    def get_cancel_ele(self):
        return self.get_element(self.cancel_feature)
