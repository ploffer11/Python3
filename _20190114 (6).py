from urllib.request import urlopen
import time 

class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
        self._content = urlopen(self.url).read()
        return self._content

# with interactive mode
webpage = WebPage("http://www.naver.com")
now = time.time() 
content1 = webpage.content
time.time() - now 
now = time.time()
content2 = webpage.content
time.time() - now 
content2 == content1 

class AverageList(list):
    @property
    def average(self):
        return sum(self) / len(self)
a = AverageList([1,2,3,4])
a.average