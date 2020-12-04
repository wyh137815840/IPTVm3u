# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import base64
import time
from fontTools.ttLib import TTFont, BytesIO
import spider_tools
import DBtools
import re
def get_list(i):
    Root_url='https://liuzhou.58.com/ershoufang/pn{}'
    url=Root_url.format(i)
    soup=spider_tools.web(url)
    ul=soup.find_all("ul", {"class": "house-list-wrap"})
    h2=ul[0].find_all('h2')
    for h in h2:
        href = h.find('a').get('href')
        rs=B_href(href)
        DBtools.insert_ershou_url(rs[0], rs[1])

def get_Maxpage(soup):
    pager=soup.find("div", {"class": "pager"})
    a=pager.find_all('a')
    p=a[len(a)-2].string
    return p
def get_info(url):
    href = 'https:' + url
    soup=spider_tools.web_taiyang(href)
    if(soup==None):
        print("无代理IP可用")
        return
    house_basic=soup.find("div", {"class": "house-basic-right fr"})
    jiage_t=house_basic.find("span", {"class": "price strongbox"})
    jiage_t=str(jiage_t).split('>')[1]
    jiage_t=jiage_t.split("<")[0]
    jiage = get_font(soup, jiage_t)
    room=house_basic.find("p", {"class": "room"})
    area = house_basic.find("p", {"class": "area"})
    toward = house_basic.find("p", {"class": "toward"})
    huxing=room.find("span", {"class": "main"}).string.strip()
    louceng=room.find("span", {"class": "sub"}).string.strip()
    pingfang=get_num(area.find("span", {"class": "main"}).string.strip())
    zhuangxiu=area.find("span", {"class": "sub"}).string.strip()
    chaoxiang=toward.find("span", {"class": "main"}).string.strip()
    shijian=get_num(toward.find("span", {"class": "sub"}).string)
    loca=house_basic.find_all("a", {"class": "c_000"})
    xiaoqu=loca[0].string.strip()
    diqu_DA=loca[1].string.strip()
    diqu_Xiao=loca[2].string.strip()
    diqu_hao=loca[3].string.strip().replace(" ","").replace("－","")
    DBtools.insert_ershou_info(url,jiage,huxing,louceng,pingfang,zhuangxiu,chaoxiang,shijian,xiaoqu,diqu_DA,diqu_Xiao,diqu_hao)
    DBtools.delect(get_ID(url))
def num_trans (soup,data):
    get_font(soup)
    newmap = parse_font()
    rs=parse_data(data,newmap)
    return rs
def get_font(data,getText):
    bs64Str = re.findall("charset=utf-8;base64,(.*?)'\)", data.text)[0]

    binData = base64.decodebytes(bs64Str.encode())
    with open('fangchan-secret.ttf','wb') as f:
        f.write(binData)
    font01 = TTFont(BytesIO(binData))

    uniList = font01['cmap'].tables[0].ttFont.getGlyphOrder()
    utfList = font01['cmap'].tables[0].ttFont.tables['cmap'].tables[0].cmap  # c = font.getBestCmap()
    retList = []
    for i in getText:
        # ord()以字符作为参数，返回对应的Unicode数值
        if ord(i) in utfList:
            text = int(utfList[ord(i)][-2:]) - 1
        else:
            text = i
        retList.append(text)
    crackText = ''.join([str(i) for i in retList])
    return crackText

def parse_font():
    font = TTFont('fangchan-secret.ttf')
    bestcmap = font['cmap'].getBestCmap()
    newmap = dict()
    for key in bestcmap.keys():
        value = int(re.search(r'(\d+)', bestcmap[key]).group(1)) - 1
        key = hex(key)
        newmap[key] = value
    return newmap
def parse_data(data,newmap):
    for key,value in newmap.items():
        key_ = key.replace('0x','&#x') + ';'
        if key_ in data:
            data = data.replace(key_,str(value))
    return data
def get_num(str):
    return re.sub("[^0-9.]","",str)
# Press the green button in the gutter to run the script.

def main():
    #DBtools.clear_done()
    url=DBtools.get_ershou_url()
    i=1
    t=0
    for u in url:
        start = time.time();
        print('第'+str(i))
        get_info(u)
        i=i+1
        end = time.time();
        D_time = end - start
        t=t+D_time
        print("用时:"+str(D_time)+'平均时间:'+str(t/i))
        time.sleep(2)
def get_ID(url):
    id_t = (url.split('?'))[0]
    id_t = id_t.split('/')[-1]
    id = id_t.split('.')[0]
    print(id)
def B_href(href):
    head=href.split('/')[0]
    if(head=='https:'):
        href=href.replace('https:','')
    id_t = (href.split('?'))[0]
    id_t = id_t.split('/')[-1]
    id = id_t.split('.')[0]
    rs=[]
    rs.append(id)
    rs.append(href)
    return rs
def list_get():
    for i in range(4,31):
        print(i)
        get_list(i)
        time.sleep(5)
if __name__ == '__main__':
    main()
    #list_get()
    #print('End')
