from static.pan import static_pan
from urllib.parse import quote
import re

class rufen(static_pan):
    url = 'http://www.rufengso.net/'

    def run(self,p):
        self.__url = 'http://www.rufengso.net/s/name/%s/'%quote(p)
        self.lis = []

    def __next__(self):
        if self.now != True:return None
        resp = self.get_data(
            url=self.__url+str(self.num),
            headers = self.headers,
        )
        self.num += 1
        com = re.compile('<h3.*?<a.*?title="(.*?)".href="(.*?)"')
        if resp != None and resp.status_code == 200:
            lis = [
                (re.sub('\s','',_t),'http://pdd.19mi.net'+re.sub('r','go',_u)) for _t,_u in com.findall(resp.text,re.S) if 'http://www.rufengso.net'+re.sub('r','go',_u) not in self.lis
            ]
            self.lis.extend(
                [i[-1] for i in lis]
            )
            if len(lis) == 0:self.now = False
            yield lis
        else:
            self.now = False
            yield None