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


def delete_ip():
    conn = pymysql.connect(host='172.0.0.1', port=3306, user='xxx',
                           password='xxx', db='zhiyuan', charset='utf8')
    cursor = conn.cursor()
    sql_2 = "DELETE FROM IPproxy3 where grade < -2 "
    cursor.execute(sql_2)
    conn.commit()
    cursor.close()
    conn.cursor()


def to_DB_IPproxy2(list1):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='xxxx',
                           password='xxx', db='zhiyuan', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO IPproxy2(host,port,grade) VALUES(%s, %s, %s)"
    for lines in list1:
        i_1 = 5
        try:
            cursor.execute(sql, (str(lines).split(":")[0], str(lines).split(":")[1], i_1))
            conn.commit()
        except:
            pass
    cursor.close()
    conn.close()


def change_grade(grade):
    print " 更新数据库"
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='xxx',
                           password='xxx', db='zhiyuan', charset='utf8')
    cursor = conn.cursor()
    # print "genxin:", IP_grade
    try:
        sql = "UPDATE IPproxy3 SET grade = %s WHERE host = %s and port = %s"
        print sql
        for line_ip in grade:
            # print line_ip
            temp = int(grade[line_ip])

            if int(grade[line_ip]) > 5:
                temp = 5
            cursor.execute(sql, (temp, str(line_ip).split(":")[0], str(line_ip).split(":")[1]))
        conn.commit()
    except:
        print " IP 数据库更新失败 一次"
        pass
    cursor.close()
    conn.cursor()
    print "更新完成"


def te_ip(ip_m, ip_list_yes):
    try:
        telnetlib.Telnet(str(ip_m).split(":")[0],
                         port=str(ip_m).split(":")[1], timeout=2)
    except:
        print ip_m, 'connect failed'
        return -1
    else:
        print ip_m, 'success'
        ip_list_yes.append(str(ip_m))
        return 1


def main():
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                           user='xxx',
                           password='xxxx', db='zhiyuan',
                           charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM IPproxy3 "
    cursor.execute(sql)
    rows = cursor.fetchall()
    i = 0
    while i < rows.__len__():
        grade = {}
        sql_1 = "SELECT * FROM IPproxy3 LIMIT %s, %s"
        cursor.execute(sql_1, (i, 40))
        rows_1 = cursor.fetchall()
        mgr = multiprocessing.Manager()
        ip_list_yes = mgr.list()
        pool = Pool(processes=4)
        for row in rows_1:
            temp = row[0] + ":" + row[1]
            re = pool.apply_async(te_ip, args=(temp, ip_list_yes))
            grade[temp] = int(row[2]) + int(re.get())
        pool.close()
        pool.join()
        change_grade(grade)

        if ip_list_yes.__len__() > 0:
            to_DB_IPproxy2(ip_list_yes)
        i += 40
    cursor.close()
    conn.close()


if __name__ == "__main__":
    while True:
        main()
        delete_ip()
