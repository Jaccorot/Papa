import re
import urllib

def getHtml(url):
    page =urllib.urlopen(url)
    html=page.read()
    return html

def getImg(html):
    reg=r'<img class="BDE_Image" src="(.*?\.jpg)" pic_ext'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    x=0
    for imgurl in  imglist:
        urllib.urlretrieve(imgurl,'%s.jpg'%x )
        x+=1

html=getHtml("http://tieba.baidu.com/p/2818994217?fr_bdps_bottom_login=1")
getImg(html)
