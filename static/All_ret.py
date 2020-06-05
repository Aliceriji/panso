import threading
import time
from static.pro import time_sleep
from copy import copy

lis = []
lock = threading.Lock()
driver_lis = []

times = 0

close = False

def del_driver():
    global close
    for driver in driver_lis:
        driver.close()
        del driver
    driver_lis.clear()
    close = True
    time.sleep(time_sleep)

def run(pro,title,num=None):
    def inner():
        global times
        while not close:
            if times > 0:
                __lis = [i for i in next(p) if i != None]
                lock.acquire()
                if len(__lis) and __lis:
                    lis.extend(__lis)
                times -= 1
                lock.release()
                if times == 0: times = -1
            time.sleep(time_sleep)
    global close
    close = False
    p = pro(title)
    if num != None:p.num = num
    driver_lis.append(p)
    t = threading.Thread(target=inner)
    t.setDaemon(True)
    t.start()

def ret_lis():
    global times
    times = len(driver_lis)
    while 1:
        if len(driver_lis) == 0:return [[('未开启后台程序','#')]]
        if times == -1:
            _lis = copy(lis)
            lis.clear()
            return _lis
        time.sleep(1)

if __name__ == '__main__':
    from bin.rufengso import rufen
    from bin.pansou import pansou
    run(rufen,'火影')
    run(pansou, '火影')
    while 1:
        input('>>')
        print(ret_lis())