import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import parse_qs


def sc(email):
    url='https://www.google.com/search?q='+email+' site:linkedin.com&sxsrf=ALiCzsbddS-qteZWPLnOO3ohTf0tKpGptw:1659630633133&gbv=1&sei=KfTrYpbcB_So8QOY-63QAw'
    x = requests.get(url,headers = {
            "x-client-data": 'CJe2yQEIprbJAQipncoBCJCUywEIk6HLAQjb78sBCLi5zAEItrrMAQiJu8wBCPPAzAEIssHMAQjFwcwBCNbBzAEI38TMAQiDyMwBGKupygE=',
            "x-restli-protocol-version": "2.0.0",
        })


    soup=BeautifulSoup(x.text,"lxml")

    f = open("demofile2.txt", "w")
    f.write(x.text)
    f.close()
    
    a=soup.find_all('a')
    
    for i in a:
        url=i['href']
        if(url.find('https://www.linkedin.com/in/') > -1):
           
            url_b=urlparse(url)
            url_b=parse_qs(url_b.query)
            print(url_b['q'][0])
            if url_b['q'][0]:
                return url_b['q'][0]
    return 'n/a'

    

print(sc('alexis.l.wilson@bofa.com'))