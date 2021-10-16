import pytest
import Base
import Handle
import logging
import allure
from time import sleep
from Base.Action import BaseAction
class TestLogout:

    @classmethod
    def setup_class(cls):
        cls.driver = Base.DriverUtil().get_driver()
        cls.handle = Handle.HandleTotal(cls.driver)

    def teardown_class(self):
        # 暂停3秒
        sleep(3)

        # 关闭app应用
        self.driver.close_app()
        logging.info("关闭应用")

        # 关闭所有
        self.driver.quit()
        logging.info("关闭驱动")

    @allure.feature("登出模块")
    # allure标题-title
    @allure.story("用例--登出测试")
    # allure描述信息
    @allure.description("该用例是针对登出的测试")
    def test_logout_success(self):
        logging.info('-' * 15+"test case logout start"+ '-' *15)
        sleep(2)

        # 实例化工具方法
        bo = BaseAction(self.driver)
        # 向右滑动
        bo.swipe_left()
        logging.info("从右向左滑动")
        # 向上滑动
        bo.swipe_top()
        logging.info("从下向上滑动")

        # 1 点击退出账号
        self.handle.init_me.tap_logout()
        logging.info("点击退出账号")

        # 2 点击确定
        self.handle.init_me.tap_confirm()
        logging.info("点击确定")

        logging.info('-' * 15 + "test case logout stop" + '-' * 15)

if __name__ == '__main__':
    pytest.main(["-s", "test_logout.py"])