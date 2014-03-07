#coding=utf-8
#!/usr/bin/python

import re
import urllib
import os


def getHtml(url):
    page = urllib.urlopen(url)
    return page.read()


def getImg(html,downaddress):
    imgre = re.compile(r'<img class="BDE_Image" src="(.*?\.jpg)" pic_ext')
    imglist = re.findall(imgre,html)
    if not os.path.exists(downaddress):
        os.makedirs(downaddress)

    for imgurl in  imglist:
        local = os.path.join(os.path.abspath(downaddress),'%s' % get_url_name(imgurl))
        urllib.urlretrieve(imgurl, local , callback_f)


def get_url_name(url):
    """从url里解析出原始图片的文件名"""
    separator_index = url.rfind('/')
    if (separator_index > 0):
        return url[separator_index+1 :]


def callback_f(downloaded_size,block_size,romote_total_size):
    per = 100.0 * downloaded_size * block_size / romote_total_size
    if per > 100:
        per = 100
    print "%.2f%%" %per
    if 100.00 == per:
        print "*"*10+"FINISH"+"*"*10


if __name__ == "__main__":
    HtmlAddress=raw_input("Knock the web address like\nhttp://tieba.baidu.com/p/2818994217?fr_bdps_bottom_login=1\nhttp://")
    DownloadAddress=raw_input("Download target:(like F:\\pictures)\n")
    #html=getHtml("http://tieba.baidu.com/p/2818994217?fr_bdps_bottom_login=1")
    html=getHtml("http://"+HtmlAddress)
    getImg(html,DownloadAddress)

