import re
from static.pan import static_pan

fast_url = 'https://www.fastsoso.cn/search'

class fastsoso(static_pan):
    url = 'https://www.fastsoso.cn/'

    def run(self, p):
        self.title = p
        self.lis = []

    def __next__(self):
        if self.now != True: return None
        resp = self.get_data(
            url=fast_url,
            headers=self.headers,
            params={
                'page':self.num,
                'k':self.title,
                's':0,
                't':-1,
            }
        )
        self.num += 1
        com = re.compile('content-title.*?<a.*?surl=(.*?)".*?>(.*?)</a',re.S)
        if resp != None and resp.status_code == 200:
            lis = [
                (''.join(re.findall('>(.*?)<',i,re.S)).strip(),'https://pan.baidu.com/s/'+_u,) for _u,i in com.findall(resp.text,re.S) if _u not in self.lis
            ]
            self.lis.extend(i[1] for i in lis)
            yield lis
        else:
            self.now = False
            yield None