import re
from static.pan import static_pan

class pansou(static_pan):

    url = 'http://m.pansou.com'

    def run(self, p):
        if ' ' in p:
            _p = ''
            for i in p.split(' '):
                _p += i + '+'
            else:
                self.p = _p[:-1]
        else:
            self.p = p
        self.lis = []

    def __next__(self):
        if self.now != True:return None
        resp = self.get_data(
            url = 'http://106.15.195.249:8011/search_new',
            headers = self.headers,
            params = {
                'callback':'jQuery172028731124917333895_1591326382988',
                'q':self.p,
                'p':self.num,
            }
        )
        self.num += 1
        com = re.compile('title.."(.*?)"..link.."(.*?)"')
        if resp != None and resp.status_code == 200:
            data = resp.content.decode('utf8')
            lis = [
                (_t,_u) for _t,_u in com.findall(data,re.S) if _u not in self.lis
            ]
            self.lis.extend(
                [i[-1] for i in lis]
            )
            if len(lis) == 0:self.now = False
            yield lis
        else:
            self.now = False
            yield None