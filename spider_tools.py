# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:53:21 2020
@author: WYH
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import zipfile
import requests
import shutil
import time
from PIL import Image
from io import BytesIO
from multiprocessing.dummy import Pool
import re
import urllib3
def taiyang_ip():
    api='http://http.tiqu.qingjuhe.cn/getip?num=1&type=1&pack=59169&port=11&yys=100017&lb=6&sb=%3B&pb=45&regions='
    return requests.get(api).content.decode().replace(';','')
def web_taiyang(URL_HOME):
    while 1:
        proxy = taiyang_ip()
        try:
            urllib3.disable_warnings()
            html = requests.get(url=URL_HOME, proxies={"http": 'http://' + proxy, "https": 'https://' + proxy},
                            verify=False,
                            timeout=15)
            soup = BeautifulSoup(html.content, 'lxml')
            house_basic = soup.find("div", {"class": "house-basic-right fr"})
            jiage_t = house_basic.find("span", {"class": "price strongbox"})
            return soup
        except Exception:
            print("重试,并删除IP"+proxy)
            time.sleep(2)
def test():
    url = 'http://pv.sohu.com/cityjson?ie=utf-8'
    proxy = get_proxy1().get("proxy")
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy,
    }
    urllib3.disable_warnings()
    html=requests.get(url=url, proxies={"http" : 'http://' + proxy, "https" : 'https://' + proxy}, verify=False, timeout=15).content.decode()
    return html
def web_home(URL_HOME):
    while 1:
        proxy = get_proxy1().get("proxy")
        try:
            urllib3.disable_warnings()
            html = requests.get(url=URL_HOME, proxies={"http": 'http://' + proxy, "https": 'https://' + proxy},
                            verify=False,
                            timeout=15)
            soup = BeautifulSoup(html.content, 'lxml')
            house_basic = soup.find("div", {"class": "house-basic-right fr"})
            jiage_t = house_basic.find("span", {"class": "price strongbox"})
            return soup
        except Exception:
            print("重试,并删除IP"+proxy)
            delete_proxy(proxy)
def web(url):
    web_html = requests.get(url)
    return BeautifulSoup(web_html.content, 'lxml')
def driver_weh(URL_HOME):
    while 1:
        proxy = get_proxy()
        try:
            urllib3.disable_warnings()
            html = requests.get(url=URL_HOME, proxies={"http": 'http://' + proxy, "https": 'https://' + proxy}, verify=False,
                                timeout=15)
            soup = BeautifulSoup(html.content, 'lxml')
            return soup
        except Exception:
                print("重试")
            # 删除代理池中代理
    return None
def get_proxy1():
    return requests.get("http://home.wyh2019.club:5010/get/").json()
def delete_proxy(proxy):
    requests.get("http://home.wyh2019.club:5010/delete/?proxy={}".format(proxy))
def get_proxy():
    order = '08080904864a867c278bb8907beff18b'
    apiUrl = "http://dynamic.goubanjia.com/dynamic/get/" + order + ".html";
    res = requests.get(apiUrl).content.decode()
    ips = res.split('\n')[0];
    return ips
def get_name(url):
    return url.split('/')[-2]
def get_num(url):
    return (url.split('/')[-1])[7:9]
