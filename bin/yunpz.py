import re

from static.pan import static_pan
from urllib.parse import quote,unquote

class yunpz(static_pan):

    url = 'http://www.yunpz.net/'

    def run(self, p):
        self.__url = 'http://www.yunpz.net/all/s-%s.html'%quote(p)
        self.lis = []

    def __next__(self):
        if self.now != True:return None
        if self.num == 1:
            resp = self.get_data(url=self.__url,headers=self.headers)
        else:
            resp = self.get_data(url=self.__url, headers=self.headers,params={'paging':self.num})
        self.num += 1
        com = re.compile('<h3.*?href="(.*?)"^[>]*?class="(.*?)|<h3.*?href="(.*?)".*?</h3>.*?<p.*?"(.*?)"')
        if resp != None and resp.status_code == 200:
            lis = []
            for _u,_t in list(com.findall(resp.text,re.S))[:-1]:
                url = 'http://www.yunpz.net/redirect/' + _u.rsplit('/',1)[-1].rsplit('.',1)[0] + '.go'
                value = unquote(re.search('key:.{}.*?value..(.*?)..,'.format(_t),resp.text,re.S).group(1))
                title = re.sub('\s','',''.join(re.findall('>(.*?)<',value,re.S)).strip())
                if url not in self.lis:
                    lis.append(
                        (title,url)
                    )
                    self.lis.append(url)
            yield lis
        else:
            self.now = False
        yield None

if __name__ == '__main__':
    y = yunpz('爬虫分布式')
    # print(unquote('0%20%e5%9b%bd%e5%ae%b6%3cb%3e%e8%a7%84%e8%8c%83%3c%2fb%3e%2f05%20%3cb%3e%e7%94%b5%3c%2fb%3e%e6%b0%94%3cb%3e%e8%a7%84%e8%8c%83%3c%2fb%3e%2f%3cb%3eGBT%3c%2fb%3e%20%3cb%3e33982%3c%2fb%3e-%3cb%3e2017%3c%2fb%3e%20%3cb%3e%e5%88%86%e5%b8%83%e5%bc%8f%3c%2fb%3e%3cb%3e%e7%94%b5%e6%ba%90%3c%2fb%3e%3cb%3e%e5%b9%b6%e7%bd%91%3c%2fb%3e%3cb%3e%e7%bb%a7%3c%2fb%3e%3cb%3e%e7%94%b5%3c%2fb%3e%3cb%3e%e4%bf%9d%e6%8a%a4%3c%2fb%3e%3cb%3e%e6%8a%80%e6%9c%af%e8%a7%84%e8%8c%83%3c%2fb%3e.%3cb%3epdf%3c%2fb%3e'))
    while 1:
        input('>>')
        for i in next(y):
            print(i)