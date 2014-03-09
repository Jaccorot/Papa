#coding=utf-8
#!/usr/bin/python

import re
import urllib
import os


def get_html(url):
    page = urllib.urlopen(url)
    return page.read()


def get_image(html_content, downaddress):
    imgre = re.compile(r'<img class="BDE_Image" src="(.*?\.jpg)" pic_ext')
    imglist = re.findall(imgre,html_content)
    if not os.path.exists(downaddress):
        os.makedirs(downaddress)

    for imgurl in  imglist:
        local = os.path.join(os.path.abspath(downaddress),'%s' % get_url_name(imgurl))
        urllib.urlretrieve(imgurl, local , download_callback_func)


def get_url_name(url):
    """
    从url里解析出原始图片的文件名
    """
    separator_index = url.rfind('/')
    if (separator_index > 0):
        return url[separator_index+1 :]


def download_callback_func(downloaded_size, block_size, omote_total_size):
    per = 100.0 * downloaded_size * block_size / romote_total_size
    if per > 100:
        per = 100
    print "%.2f%%" %per
    if 100.00 == per:
        print "*"*10+"FINISH"+"*"*10


if __name__ == "__main__":
    html_url=raw_input("Knock the web address like\nhttp://tieba.baidu.com/p/2818994217?fr_bdps_bottom_login=1\nhttp://")
    #这里需要对录入内容进行校验
    save_path=raw_input("Download target:(like F:\\pictures)\n")
    #对保存路径进行设置,可以考虑使用配置文件而不是用户输入,如果输入也需要验证
    #html=get_html("http://tieba.baidu.com/p/2818994217?fr_bdps_bottom_login=1")
    html_content=get_html("http://"+html_url)
    get_image(get_html,save_path)

