from static.pan import static_pan
import time,re
from urllib.parse import quote

class verypan(static_pan):

    url = 'http://www.verypan.com/'

    def run(self, p):
        if ' ' in p:
            _p = ''
            for i in p.split(' '):
                _p += quote(i) + '+'
            else:
                _p = _p[:-1]
        else:
            _p = quote(p)
        self.__url = 'http://www.verypan.com/index/index/baidusearch/r/1591319035/keyword/%s/page/'%_p
        self.lis = []

    def __next__(self):
        if self.now != True:return None
        resp = self.get_data(
            url=self.__url+str(self.num),headers=self.headers
        )
        self.num += 1
        com = re.compile('<h2.*?href="(.*?)".*?title="(.*?)"')
        if resp != None and resp.status_code == 200:
            lis = [
                (title,'http://www.verypan.com'+re.sub('baiducontent','baidudown',_u)) for _u,title in com.findall(resp.text) if ('http://www.verypan.com'+re.sub('baiducontent','baidudown',_u)) not in self.lis
            ]
            self.lis.extend(
                [i[-1] for i in lis]
            )
            if len(lis) == 0:self.now =False
            yield lis
        else:
            self.now = False
            yield None