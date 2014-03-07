#coding=utf-8
#!/usr/bin/python

import re
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    return page.read()


def getImg(html):
    imgre = re.compile(r'<img class="BDE_Image" src="(.*?\.jpg)" pic_ext')
    imglist = re.findall(imgre,html)

    for imgurl in  imglist:
        urllib.urlretrieve(imgurl, '%s' % get_url_name(imgurl))


def get_url_name(url):
    """从url里解析出原始图片的文件名"""
    separator_index = url.rfind('/')
    if (separator_index > 0):
        return url[separator_index+1 :]

if __name__ == "__main__":
    html=getHtml("http://tieba.baidu.com/p/2818994217?fr_bdps_bottom_login=1")
    getImg(html)
