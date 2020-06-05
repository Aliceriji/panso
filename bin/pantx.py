from urllib.parse import quote
from static.pan import static_pan
import re

class pantx(static_pan):

    url = 'https://www.pantianxia.com/'

    def run(self, p):
        self.__url = 'https://www.pantianxia.com/zh/%s?page='%quote(p)
        self.lis = []

    def __next__(self):
        if self.now != True: return None
        resp = self.get_data(
            url=self.__url+str(self.num),
            headers = self.headers,
        )
        self.num += 1
        com = re.compile('class="l".*?href="(.*?)".*?title="(.*?)"')
        if resp != None and resp.status_code == 200:
            lis = [
                (_t,'https://www.pantianxia.com'+re.sub('s','go',_u,1)) for _u,_t in com.findall(resp.text) if 'https://www.pantianxia.com'+re.sub('s','go',_u,1) not in self.lis
            ]
            self.lis.extend(
                [i[-1] for i in lis]
            )
            if len(lis) == 0:self.now = False
            yield lis
        else:
            self.now = False
            yield None