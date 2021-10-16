# 这个模块只负责完成 me 界面的元素动作
from Page.page_me import PageMe
import allure


class HandleMe(PageMe):

    # 我的页点击退出账号
    @allure.step("点击退出账号")
    def tap_logout(self):
        self.execute_tap(self.get_logout_ele())

    # 我的页-是否退出点击确定
    @allure.step("点击确定")
    def tap_confirm(self):
        self.execute_tap(self.get_confirm_ele())

    # 我的页-是否退出点击取消
    @allure.step("点击取消")
    def tap_cancel(self):
        self.execute_tap(self.get_cancel_ele())
