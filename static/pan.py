# from DRIVER import PREFS_DRIVER as Driver
import requests
import time
from static.pro import time_sleep

# 所有云盘的主类文件

class pan:
    def __init__(self,p):
        self.d = Driver()
        self.driver = self.d.Ret_driver()
        self.num = 1
        self.run(p)

    def close(self):
        self.d.del_driver()

    def run(self, p):
        pass

    def btn(self,title):
        try:
            self.num += 1
            for i in range(1, 11):
                if self.driver.find_element_by_xpath(title % i).text.isdecimal():
                    if int(self.driver.find_element_by_xpath(title % i).text) == self.num:
                        btn1 = self.driver.find_element_by_xpath(title % i)
                        break
            btn1.click()
        except Exception as err:
            return False

class static_pan(pan):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    }
    sleep = 2

    def __init__(self,p):
        self.num = 1
        self.run(p)
        self.now = True

    def close(self):
        pass

    def run(self, p):
        pass

    def btn(self,title):
        pass

    def get_data(self,num=1,**kwargs):
        if num == 3:return None
        try:
            resp = requests.get(timeout=time_sleep,**kwargs)
            time.sleep(self.sleep)
            return resp
        except Exception as err:
            time.sleep(1)
            return self.get_data(num+1)

    def reboot(self,p):
        self.num = 1
        self.now = True
        self.run(p)