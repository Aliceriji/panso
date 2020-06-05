import time
import requests
from static.pan import pan
from urllib.parse import quote
import re

pan51_url = 'https://m.51caichang.com/search/ajax?keyword=%s&page={}&site=&cat=&order=&feed_time=0&m=0&url_path=so&_=1591253500090'

class pan51(pan):

    url = 'https://m.51caichang.com/'

    def run(self,p):
        if ' ' in p:
            _p = ''
            for i in p.split(' '):
                _p += quote(i) + '+'
            else:
                _p = _p[:-1]
        else:
            _p = quote(p)
        self.__url = pan51_url % _p
        self.driver.get('https://m.51caichang.com/so?keyword=%s&page=1&url_path=so'%_p)
        title = ''
        for cookie in self.driver.get_cookies():
            title += cookie.get('name') + '=' + cookie.get('value') + ';'
        self.headers = {
            'cookie': title,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        }
        self.driver.close()
        self.num = 1
        self.url_lis = []
        self.now = True

    def close(self):
        pass

    def __next__(self):
        def get_data(num=0):
            if num == 3:return None
            try:
                resp = requests.get(self.__url.format(str(self.num)), headers=self.headers,timeout=3)
                time.sleep(2)
                self.num += 1
                return resp
            except Exception as err:
                print(type(err))
                return get_data(num+1)
        if self.now == False:return None
        resp = get_data()
        if resp and resp.status_code == 200:
            lis = []
            for i in resp.json().get('list'):
                title = re.sub('<.*?>|\s','',i.get('filename'))
                url = i.get('dir_share_url')
                if url not in self.url_lis:
                    self.url_lis.append(url)
                    lis.append(
                        (title,url)
                    )
            if len(lis) == 0:self.now = False
            yield lis
        else:
            self.now = False
            yield None
