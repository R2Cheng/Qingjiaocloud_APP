from selenium.webdriver.common.by import By
from Base.Action import BaseAction


class PageLogin(BaseAction):

    #定位
    #引导页-跳过
    skip_feature = By.ID, "com.qingjiaocloud:id/tv_skip"
    #登录页-账号
    num_feature = By.ID, "com.qingjiaocloud:id/ed_phone"
    #登录页-密码
    pwd_feature = By.ID, "com.qingjiaocloud:id/ed_password"
    #登录页-机房下拉框
    machine_room_feature = By.ID, "com.qingjiaocloud:id/img_up_down"
    #登录页-用户协议&隐私协议
    agreement_feature = By.ID, "com.qingjiaocloud:id/iv_user_agreement"
    #登录页-登录
    enter_feature = By.ID, "com.qingjiaocloud:id/phone_login_sure"
    #登录页-机房下拉框内容
    first_room_feature = By.XPATH, "//*[@text='华南']"
    second_room_feature = By.XPATH, "//*[@text='华北']"
    third_room_feature = By.XPATH, "//*[@text='华东']"

    # 1 跳过
    def get_skip_ele(self):
        return self.get_element(self.skip_feature)

    # 2 获取账号输入框
    def get_num_ele(self):
        return self.get_element(self.num_feature)

    # 3 密码输入框
    def get_pwd_ele(self):
        return self.get_element(self.pwd_feature)

    # 4 机房下拉框
    def get_machine_room_ele(self):
        return self.get_element(self.machine_room_feature)

    # 5 选择机房
    def get_room_ele(self):
        return self.get_element(self.second_room_feature)

    # 5 勾选协议
    def get_agreement_ele(self):
        return self.get_element(self.agreement_feature)

    # 5 提交登录按钮
    def get_enter_ele(self):
        return self.get_element(self.enter_feature)