import pytest
import Base
import Handle
import logging
import allure

class TestLogin:

    @classmethod
    def setup_class(cls):
        cls.driver = Base.DriverUtil().get_driver()
        cls.handle = Handle.HandleTotal(cls.driver)


    @allure.feature("登录模块")
    # allure标题-title
    @allure.story("用例--登录测试")
    # allure描述信息
    @allure.description("该用例是针对登录的测试")
    @pytest.mark.parametrize("info", Base.get_data("login","login_success"))
    def test_login_success(self, info):
        logging.info('-' * 15+"test case login start"+ '-' *15)
        # 1 点击跳过
        self.handle.init_login.tap_skip()
        logging.info("点击跳过")

        # 2 输入账号
        self.handle.init_login.input_num(info["num"])
        logging.info("青椒云登录账号输入为'{}'".format(info["num"]))

        # 3 输入密码
        self.handle.init_login.input_pwd(info["pwd"])
        logging.info("青椒云登录密码输入为'{}'".format(info["pwd"]))

        # 4 选择机房
        self.handle.init_login.tap_machine_room()
        self.handle.init_login.tap_room()
        logging.info("选择登录机房")

        # 5 勾选协议
        self.handle.init_login.tap_agreement()
        logging.info("勾选并同意用户协议")

        # 6 点击登录
        self.handle.init_login.tap_enter()
        logging.info("点击登录")
        logging.info('-' * 15 + "test case login stop" + '-' * 15)

# 项目根目录执行生成报告
# 生成allure报告：allure generate report/xml -o report/html --clean

if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])