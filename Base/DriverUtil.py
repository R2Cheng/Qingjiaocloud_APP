import threading
from Base.Driver import appium_desired


class DriverUtil(object):

    __instance = None
    __instance_lock = threading.Lock()

    @classmethod
    def get_driver(cls):
        with DriverUtil.__instance_lock:
            if not DriverUtil.__instance:
                DriverUtil.__instance = appium_desired()
        return DriverUtil.__instance