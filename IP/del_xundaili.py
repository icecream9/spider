# -*- coding: utf-8 -*-
# IP池管理相关
import pymysql
import time
import multiprocessing
from multiprocessing import Pool
import telnetlib
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def main():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='xxxx',
                           password='xxxx', db='zhiyuan', charset='utf8')
    cursor = conn.cursor()
    sql_1 = "SELECT * FROM IPproxy2 "
    cursor.execute(sql_1)
    rows = cursor.fetchall()
    if rows.__len__() < 90:
        print "ip ...xxx...warning..."
        time.sleep(30)
    sql_0 = "DELETE FROM IPproxy2 where grade < 1"
    cursor.execute(sql_0)
    conn.commit()
    sql = "UPDATE IPproxy2 SET grade = grade - 1"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.cursor()
    print "delete "
    print time.time()

if __name__ == "__main__":
    while True:
        main()
        time.sleep(60)
