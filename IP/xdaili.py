import urllib2
import json
import time
import pymysql


def main():
    # xundaili ip url
    url = ""
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    hd = response.read()
    # print hd
    json_h = json.loads(hd)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='xxxx',
                           password='xxxx', db='zhiyuan', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO IPproxy2(host,port,grade) VALUES(%s, %s, %s)"
    sql_1 = "INSERT INTO IPproxy3(host,port,grade) VALUES(%s, %s, %s)"
    for line in json_h['RESULT']:
        port = line['port']
        ip = line['ip']
        try:
            cursor.execute(sql, (ip, port, 5))
            cursor.execute(sql_1, (ip, port, 0))
            conn.commit()
        except:
            pass

    cursor.close()
    conn.close()


if __name__ == "__main__":
    i = 0
    while True:
        try:
            main()
        except:
            time.sleep(5)
            pass
        print i
        i += 1
        time.sleep(12)
