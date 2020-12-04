import pymysql
import main
def insert_ershou_url(id,h):
    con = pymysql.Connect(
        host='server.wyh2019.club',
        port=3306,
        user='House',
        passwd='137815840',
        db='House',
        charset='utf8'
    )
    cursor = con.cursor()
    sql = """INSERT INTO ershou_url(id,url)
             VALUES ('{}','{}')""".format(id,h)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        con.commit()
    except:
        # Rollback in case there is any error
        con.rollback()
    cursor.close()
    con.close()
def insert_ershou_info(href,jiag,hux,louc,pingf,zhuangx,chaox,shij,xiaoq,diq_d,diq_x,diq_h):
    con = pymysql.Connect(
        host='server.wyh2019.club',
        port=3306,
        user='House',
        passwd='137815840',
        db='House',
        charset='utf8'
    )
    cursor = con.cursor()
    sql = """INSERT INTO ershou_info(url,jiage,huxing,louceng,pingfang,zhuangxiu,chaoxiang,shijian,xiaoqu,diqu_DA,diqu_Xiao,diqu_hao)
             VALUES ('{}',{},'{}','{}',{},'{}','{}','{}','{}','{}','{}','{}')""".format(href,jiag,hux,louc,pingf,zhuangx,chaox,shij,xiaoq,diq_d,diq_x,diq_h)
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        con.commit()
    except:
        # Rollback in case there is any error
        con.rollback()
    cursor.close()
    con.close()

def get_ershou_url():
    con = pymysql.Connect(
        host='server.wyh2019.club',
        port=3306,
        user='House',
        passwd='137815840',
        db='House',
        charset='utf8'
    )
    cur = con.cursor()
    sql='select url from ershou_url'
    cursor = cur.execute(sql)
    result = cur.fetchall()
    href=[]
    for h in result:
        href.append(h[0])
    cur.close()
    con.close()
    return href
def clear_done():
    con = pymysql.Connect(
        host='server.wyh2019.club',
        port=3306,
        user='House',
        passwd='137815840',
        db='House',
        charset='utf8'
    )
    cur = con.cursor()
    sql = 'select url from ershou_info'
    cursor = cur.execute(sql)
    result = cur.fetchall()
    href = []
    for h in result:
        key=main.B_href(h[0])
        delect(key[0])
    print('删除完成!')
def delect(key):
    con = pymysql.Connect(
        host='server.wyh2019.club',
        port=3306,
        user='House',
        passwd='137815840',
        db='House',
        charset='utf8'
    )
    cur = con.cursor()
    sql="DELETE FROM ershou_url WHERE id ='{}'".format (key)
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 提交修改
        con.commit()
        print("delete OK")
    except:
        # 发生错误时回滚
        con.rollback()
    # 关闭连接
    con.close()
if __name__ == '__main__':
    clear_done()