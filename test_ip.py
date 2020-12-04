import time

import requests
import urllib3
from bs4 import BeautifulSoup
import spider_tools
def gaoni():
    targetUrl = "http://icanhazip.com/";
    proxy = spider_tools.get_proxy()
    '''head 信息'''
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Connection': 'keep-alive'}
    '''http://icanhazip.com会返回当前的IP地址'''
    urllib3.disable_warnings();
    html = requests.get(url=targetUrl, proxies={"http": 'http://' + proxy, "https": 'https://' + proxy},verify=False, timeout=15).content.decode()

    print(html)
def test():
    url = 'https://liuzhou.58.com/ershoufang/43850070965509x.shtml?utm_source=&spm=&cityListName=liuzhou&curListName=liuzhou&lg=https%3A%2F%2Flegoclick.58.com%2Fjump%3Ftarget%3Dszq_pgRlpAqdsWN3shPfUiq-0MPCULRhmyOMs1E1rjNknj0krHmdPHTOXaO1pZwVUT7bsymYnAEdPWb3syELrjTVPjNdnadBuHnOsyDvPhnOmyu6PvNdPkDzrHckrjmQPHcdPWN3PEDKnHmOnj0vP1nOrHcLrHm1n9DkTHDknTDQsjD1TH0Qn1nKnHmkPWbLPj9YPWb3nTDdrTDdraLb8C1hBmfhBstVOev8lpAvsRKjOl8fOmBgl2AClpAdTHDKnEDKsHDKTHD1n1nOPHm3Pjn3nWcvPHnYPjTKP9DKnE76PyEznAELnidBrjE3sHEvPHEVmHnYnBYdnjNdmWTk%27:%20No%20schema%20supplied.%20Perhaps%20you%20meant%20http:////liuzhou.58.com/ershoufang/43850070965509x.shtml?utm_source=&spm=&cityListName=liuzhou&curListName=liuzhou&lg=https%3A%2F%2Flegoclick.58.com%2Fjump%3Ftarget%3Dszq_pgRlpAqdsWN3shPfUiq-0MPCULRhmyOMs1E1rjNknj0krHmdPHTOXaO1pZwVUT7bsymYnAEdPWb3syELrjTVPjNdnadBuHnOsyDvPhnOmyu6PvNdPkDzrHckrjmQPHcdPWN3PEDKnHmOnj0vP1nOrHcLrHm1n9DkTHDknTDQsjD1TH0Qn1nKnHmkPWbLPj9YPWb3nTDdrTDdraLb8C1hBmfhBstVOev8lpAvsRKjOl8fOmBgl2AClpAdTHDKnEDKsHDKTHD1n1nOPHm3Pjn3nWcvPHnYPjTKP9DKnE76PyEznAELnidBrjE3sHEvPHEVmHnYnBYdnjNdmWTk?'
    proxy = spider_tools.get_proxy()
    urllib3.disable_warnings()
    html = requests.get(url=url, proxies={"http": 'http://' + proxy, "https": 'https://' + proxy}, verify=False,
                        timeout=15)
    return BeautifulSoup(html.content, 'lxml')
if __name__ == '__main__':
    ip=spider_tools.taiyang_ip()
    print(ip)