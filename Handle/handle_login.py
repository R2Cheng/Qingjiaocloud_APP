from Page.page_login import PageLogin
import allure

class HandleLogin(PageLogin):

    # 引导页点击跳过
    @allure.step("点击跳过")
    def tap_skip(self):
        self.execute_tap(self.get_skip_ele())

    # 1 输入账号
    @allure.step("输入账号")
    def input_num(self, val):
        self.execute_input(self.get_num_ele(), val)

    # 3 输入密码
    @allure.step("输入密码")
    def input_pwd(self, val):
        self.execute_input(self.get_pwd_ele(), val)

    # 4 点击机房下拉框
    @allure.step("点击选择机房下拉框")
    def tap_machine_room(self):
        self.execute_tap(self.get_machine_room_ele())

    # 4 点击下拉框第一个机房
    @allure.step("点击第一个机房")
    def tap_room(self):
        self.execute_tap(self.get_room_ele())

    # 5 勾选协议
    @allure.step("勾选用户协议")
    def tap_agreement(self):
        self.execute_tap(self.get_agreement_ele())

    # 6 点击提交登录
    @allure.step("点击登录")
    def tap_enter(self):
        self.execute_tap(self.get_enter_ele())
