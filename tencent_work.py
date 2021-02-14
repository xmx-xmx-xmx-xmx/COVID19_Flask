# tencent_work.py
# 腾讯数据爬取用程序 定时执行

import pymysql
import time
import json
import traceback # 追踪异常
import requests

def tencent_data_work():
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    url_hist = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other" # 历史数据
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36 Edg/88.0.705.63"
    }
    r = requests.get(url, headers)
    res = json.loads(r.text)
    data_all = json.loads(res["data"])

    r_his = requests.get(url_hist, headers)
    res_his = json.loads(r_his.text) # json字符串转字典
    data_his = json.loads(res_his["data"])

    history = {} # 历史数据
    for i in data_his["chinaDayList"]:
        ds = i["y"] + "." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)  # 改变时间格式,不然插入数据库会报错，数据库是date类型
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        history[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead}
    for i in data_his["chinaDayAddList"]:
        ds = i["y"] + "." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        history[ds].update({"confirm_add": confirm, "suspect_add": suspect, "heal_add": heal, "dead_add": dead})
    print("1" , type(history))

    detail = []
    update_time = data_all["lastUpdateTime"]
    data_country = data_all["areaTree"] # list countries
    data_province = data_country[0]["children"] # province
    for prov_infos in data_province:
        province = prov_infos["name"] # name
        for city_infos in prov_infos["children"]:
            city = city_infos["name"]
            confirm = city_infos["total"]["confirm"]
            confirm_add = city_infos["today"]["confirm"]
            heal = city_infos["total"]["heal"]
            dead = city_infos["total"]["dead"]
            detail.append([update_time, province, city, confirm, confirm_add, heal, dead])
    print("2" , type(detail))
    return history, detail

# tencent_data_work()

# # create connection
# conn = pymysql.connect(host = "localhost", user = "root", password = "Glgjssy@71hfbqz", db = "tencent_data", charset = "utf8")

# #create cursor
# cursor = conn.cursor() # 创建游标，默认是元组型

# sql = "select * from history"
# cursor.execute(sql) # 执行
# # conn.commit() # 增删改操作需要提交事务
# res = cursor.fetchall() # 获取执行结果
# print(res)

# # close conn
# cursor.close()
# conn.close()

def get_conn():
    """
    :return: 连接，游标
    """
    # 创建连接
    conn = pymysql.connect(host="127.0.0.1",user="root",password="Glgjssy@71hfbqz",db="tencent_data",charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor

def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def update_detail():
    """
    更新 details 表
    :return:
    """
    cursor = None
    conn = None
    try:
        li = tencent_data_work()[1]
        conn, cursor = get_conn()
        sql = "insert into detail(update_time,province,city,confirm,confirm_add,heal,dead) value(%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select %s=(select update_time from detail order by id desc limit 1)"
        cursor.execute(sql_query, li[0][0]) # 第一条的第一列（更新时间）
        if not cursor.fetchone()[0]: # fetchone() 获取单条数据
            print(f"{time.asctime()}开始更新最新数据")
            for item in li:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()}更新最新数据完毕")
        else:
            print(f"{time.asctime()}已经是最新数据")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)

def insert_history():
    """
    插入历史数据
    :return:
    """
    cursor = None
    conn = None
    try:
        dic = tencent_data_work()[0]  # 0 是历史数据字典,1 最新详细数据列表
        print(f"{time.asctime()}开始插入历史数据")
        conn, cursor = get_conn()
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for k, v in dic.items():
            # item 格式 {'2020-01-13': {'confirm': 41, 'suspect': 0, 'heal': 0, 'dead': 1}
            cursor.execute(sql, [k, v.get("confirm"), v.get("confirm_add"), v.get("suspect"),v.get("suspect_add"), v.get("heal"), v.get("heal_add"),v.get("dead"), v.get("dead_add")])
        conn.commit()  # 提交事务 update delete insert操作
        print(f"{time.asctime()}插入历史数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)    

def update_history():
    """
    更新 history 表
    :return:
    """
    cursor = None
    conn = None
    try:
        dic = tencent_data_work()[0]  # 0 是历史数据字典,1 最新详细数据列表
        print(f"{time.asctime()}开始更新历史数据")
        conn, cursor = get_conn()
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select confirm from history where ds=%s"
        print(type(dic))
        for k, v in dic.items():
            # item 格式 {'2020-01-13': {'confirm': 41, 'suspect': 0, 'heal': 0, 'dead': 1}
            if not cursor.execute(sql_query, k):
                cursor.execute(sql, [k, v.get("confirm"), v.get("confirm_add"), v.get("suspect"),v.get("suspect_add"), v.get("heal"), v.get("heal_add"),v.get("dead"), v.get("dead_add")])
        conn.commit()  # 提交事务 update delete insert操作
        print(f"{time.asctime()}历史数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)        

update_detail()
insert_history() 
update_history()