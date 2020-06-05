import re
from static.pan import static_pan

class qzhou(static_pan):

    url = 'https://www.qzhou.com.cn/'

    def run(self, p):
        self.__url = 'https://www.qzhou.com.cn/search?'
        self.title = p
        self.lis = []

    def __next__(self):
        def ret_title(title):
            title = re.sub('\s','',title)
            title = re.sub('\s','',title)
            title = re.sub('、|-','',title)
            if len(title) > 10:
                return title[:10]
            else:
                return title
        if self.now != True:return None
        resp = self.get_data(
            url=self.__url, headers=self.headers,
            params={
                'keyword':self.title,
                'p':self.num,
            },
        )
        self.num += 1
        com = re.compile('result-title.*?href..(.*?)".*?"(.*?)"')
        if resp != None and resp.status_code == 200:
            lis = [
                (ret_title(_t),'https://www.qzhou.com.cn/redirect/' + _u.rsplit('/',1)[-1]) for _u,_t in com.findall(resp.text,re.S) if _u.rsplit('/',1)[-1] not in self.lis
            ]
            self.lis.append(
                i[1] for i in lis
            )
            yield lis
        else:
            self.now = False
            yield None