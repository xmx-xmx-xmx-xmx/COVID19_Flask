# tencent_search.py
# 爬取api提供的热搜

from typing import Text
import requests
import json
import time
from bs4 import BeautifulSoup
from requests.api import head
import pymysql
import traceback

def get_news():
    url = "https://lab.isaaclin.cn/nCoV/api/news?page=1&num=10"
    headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36 Edg/88.0.705.63"
        }
    r = requests.get(url, headers)
    r.encoding = "utf-8"
    res = json.loads(r.text)
    print(type(res))
    print(res.keys())
    print("{:=^50s}".format("今日疫情速报"))
    news = {}
    for i in res["results"]:
        time1 = (i["pubDate"]) # 毫秒为单位的Unix时间戳
        realtime = time.strftime("%Y-%m-%d", time.localtime((int(time1) / 1000)))
        # print("发布时间：{}".format(realtime))
        # print(i["title"])
        # print(i["sourceUrl"])
        title = i["title"]
        sourceUrl = i["sourceUrl"]
        news[realtime] = {"title": title, "sourceUrl": sourceUrl}
    # _news = {}
    # for j in range(len(news)):
    #     _news[j] = news[j]
    # print(type(news))
    # print(type(_news))
    return news

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

def insert_news():
    cursor = None
    conn = None
    try:
        dic = get_news()
        print(f"{time.asctime()}开始插入新闻数据")
        conn, cursor = get_conn()
        sql = "insert into news_info values(%s,%s,%s)"
        print(type(dic))
        # _dic = {}
        # for j in range(len(dic)):
        #     _dic[j] = dic[j]
        # print(type(_dic))
        for k, v in dic.items():
            cursor.execute(sql, [k, v.get("title"), v.get("sourceUrl")])
        conn.commit()  # 提交事务 update delete insert操作
        print(f"{time.asctime()}插入新闻数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)    

insert_news()