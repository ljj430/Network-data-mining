import requests
import urllib.request
from bs4 import BeautifulSoup
import os,re

def get_html(url):
    response = requests.get(url)
    html = response.text
    return html
def parseHTML(html,times):
    # pattern = re.compile(, re.S)
    soup = BeautifulSoup(html, 'html.parser')
    picUrls = soup.find_all('img',class_='BDE_Image')
    for picUrl in picUrls:
        times += 1
        print('第', times, '张图片:',picUrl['src'])
        savePic(picUrl['src'], times)
    return picUrls,times

def savePic(picUrl,name):
    if not os.path.exists('pic'):
        os.mkdir('pic')
    html = requests.get(picUrl)
    print(html)
    with open('pic/picture'+str(name)+'.jpg', 'wb') as file:
        file.write(html.content)
def find_nextpage(html_text,urlset):
    soup = BeautifulSoup(html_text, 'html.parser')
    v=soup.find_all(name='a', attrs={"href":re.compile("^/p/.*pn=.*")})
    for i in range(len(v)):
        if v[i]['href'] not in urlset :
            urlset.append(v[i]['href'])
    return urlset



url='https://tieba.baidu.com/p/5597745647'
url2='https://tieba.baidu.com'
urlset=['/p/5597745647?pn=1']

html_text=urllib.request.urlopen(url).read()

    #print(urllib.request.urlopen(url2+i['href']).read().decode('utf-8'))
urlset=find_nextpage(html_text,urlset)
print(urlset)
times=0

for urlid in urlset:

    html_text=urllib.request.urlopen(url2+urlid).read()
    picUrls,times=parseHTML(html_text,times)
    urlset=find_nextpage(html_text,urlset)
    print(find_nextpage(html_text,urlset))





