import time
import pymysql
from pymysql.cursors import Cursor

def get_time(): # 这个函数是获取时间的
    time_str = time.strftime("{}%Y{}%m{}%d{}%X{}%A")
    return time_str.format("现在是北京时间：","年","月","日 "," ")

def get_conn(): # 连接数据库
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


def query(sql, *args): # 这个函数是获取中间四个数据的
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res

def get_center1_data():
    """
        释义：
        第一行 查找累计确诊
        第二行 
        第三行 
        第四行 
    """
    sql = "select (select confirm from history order by ds desc limit 1), (select suspect from history order by ds desc limit 1), sum(heal), sum(dead) from detail where update_time=(select update_time from detail order by update_time desc limit 1)"
    res = query(sql)
    return res[0]

def get_center2_data():
    """
        释义：获取最新的累计确诊显示在地图上
    """
    sql1 = "select province, sum(confirm) from detail where update_time=(select update_time from detail order by update_time desc limit 1) group by province"
    res = query(sql1)
    return res

def get_left1_data():
    """
        释义：获取左1
    """
    sql2 = "select ds,confirm,suspect,heal,dead from history"
    res = query(sql2)
    return res

def get_left2_data():
    """
        释义：获取左2
    """
    sql3 = "select ds,confirm_add,suspect_add from history"
    res = query(sql3)
    return res

# if __name__ == "__main__": # 测试
#     print(get_center1_data())