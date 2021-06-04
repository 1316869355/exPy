# -*- coding: utf-8 -*-
import socket
from urllib import request, parse, error
import os
import sys
import time

class Downloader(object):
    def file_parse(self, path, url_prefix):   # 源码解析，提取需要的数据
        img_urls = []
        if path is None:
            return
        # 读取文件
        file = open(path, "r")
        imgs = []
        try:
            while True:
                text_line = file.readline()
                if text_line:
                     imgs.append(text_line)
                else:
                    break
        finally:
            file.close()
            
        for img in imgs:
            new_url = img  # 获取所有的链接
            new_full_url = (url_prefix + new_url)  # 让new_url按照page_url的格式拼接成一个完整的url
            # print(new_full_url)
            new_full_url = new_full_url.strip()
            img_urls.append(new_full_url)
            
        self.img_download(img_urls)

    def img_download(self, img_urls):    # 文件下载保存
        if img_urls is None or len(img_urls) == 0:
            print('no img can download')
            return
        
        cur_path = os.path.abspath(os.curdir)   # 获取当前绝对路径
        goal_path = cur_path + '\\' + 'imgs'+ '\\'   # 想将文件保存的路径

        if not os.path.exists(goal_path):      # os.path.isfile('test.txt') 判断文件夹/文件是否存在
            os.mkdir(goal_path)      # 创建文件夹

        name =''   # 用于给图片命名
        for img in img_urls:
            # print(img)
            name=img.rpartition('/')[-1]
            # for part in name:
            #    print(part, end='\n')
                
            
            print(img)
            
            try:
                response = request.urlopen(img)
                filename = goal_path + name
                
                if (response.getcode() == 200):
                    with open(filename, "wb") as f:
                        f.write(response.read()) # 将内容写入图片
            except OSError as err:
                print("OS error: {0}".format(err))
                print("error-", name)
            except:
                print("error-", name)
                print("Unexpected error:", sys.exc_info()[0])
                raise
            time.sleep(2)

if __name__ == '__main__':
    root_url = 'http://123.57.159.204/spider/'   # 页面地址
    file_path = 'C:/Users/yy-chanpin/Desktop/lost-img.txt' #
    downloader = Downloader()
    downloader.file_parse(file_path,root_url)
