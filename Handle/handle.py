# 这个模块负责管理Handle下的所有动作
import Handle


class HandleTotal:

    def __init__(self, driver):
        self.driver = driver

    @property
    def init_home(self):
        return Handle.HandleHome(self.driver)

    @property
    def init_me(self):
        return Handle.HandleMe(self.driver)

    @property
    def init_login(self):
        return Handle.HandleLogin(self.driver)

    @property
    def init_logout(self):
        return Handle.HandleLogout(self.driver)

