#-*- coding: utf-8 -*-

# 导入re模块，正则表达式
import re
# 获取网页内容
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.*?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%d.jpg' % x)
        x += 1

if __name__ == "__main__":
    print "Please input the url:"
    theurl = raw_input("> ")
    html = getHtml(theurl)
    # html = getHtml("http://tieba.baidu.com/p/2513960706")
    getImg(html)