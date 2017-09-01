# -*- coding: utf-8 -*
# eol 另一种方法的专业分数
import urllib2
import json
import sys
import time
import os

reload(sys)
sys.setdefaultencoding("utf-8")
num = 10000
num_t = 0
path_n = "E:\\school\\schoolprovince\\kkk"


def get_detail(name, id, province, wenli, p_c):
    time.sleep(0.2)
    url = "http://gkcx.eol.cn/schoolhtm/scores/provinceScores" + \
          id + "_" + province + "_"+wenli + "_"+p_c+".xml"
    request = urllib2.Request(url)
    response_code = "0"
    hd = ""
    try:
        print url
        response = urllib2.urlopen(request, timeout=3)
        hd = response.read()
        # print hd
    except:
        print url
        path_ex = "E:\\school\\schoolprovince\\exx\\ex"

        file3 = file(path_ex, "a+")
        file3.write(str(url))
        file3.write("\n")
        file3.close()
        return
    # response_code = str(response.getcode())
    # print response.read()

    if str(hd).startswith("<?xml version=\"1.0"):
        # print hd
        global num
        global num_t
        global path_n
        num_t += 1
        if num_t > num:
            num += 10000
            path_n = "E:\\school\\schoolprovince\\" + str(num_t)
            if os.path.exists(path_n):
                pass
            else:
                os.makedirs(path_n)
        # path_u = "E:\\school\\schoolprovince\\kkk"
        # print "hd", hd
        path = (str(path_n) + "\\" + str(name).replace("\n", "") +
                "_" + str(province) + "_"+str(wenli)+ "_"+str(p_c))
        print path
        ipath = unicode(path,"utf-8")
        file2 = file(ipath, "a+")
        file2.write(hd)
        file2.close()
        # print  response.getcode()


def get_xml(name, id):
    provinces = []
    # beijing
    provinces.append("10003")
    # 上海
    provinces.append("10000")
    # guangdong
    provinces.append("10011")
    # 天津
    provinces.append("10006")
    # 重庆
    provinces.append("10028")
    # 湖北
    provinces.append("10021")
    # 四川
    provinces.append("10005")
    # 河北
    provinces.append("10016")
    # 河南
    provinces.append("10017")
    # 山东
    provinces.append("10009")
    # 山西
    provinces.append("10010")
    # 江苏
    provinces.append("10014")
    # 陕西
    provinces.append("10029")
    # 浙江
    provinces.append("10018")
    # 江西
    provinces.append("10015")
    # 广西
    provinces.append("10012")
    # 湖南
    provinces.append("10022")
    # 辽宁
    provinces.append("10027")
    # 安徽
    provinces.append("10008")
    # 福建
    provinces.append("10024")
    # 贵州
    provinces.append("10026")
    # 甘肃
    provinces.append("10023")
    # 吉林
    provinces.append("10004")
    # 海南
    provinces.append("10019")
    # 云南
    provinces.append("10001")
    # 新疆
    provinces.append("10013")
    # 宁夏
    provinces.append("10007")
    # 西藏
    provinces.append("10025")
    # 青海
    provinces.append("10030")
    # 内蒙古
    provinces.append("10002")
    # 黑龙江
    provinces.append("10031")
    print provinces.__len__()
    # 10036: 一批, 10037: 二批, 10038: 三批
    pi_ci = ["10036", "10037", "10038"]
    for province in provinces:
        for p_c in pi_ci:
            # wen
            get_detail(name, id, province, "10034", p_c)
            # li
            get_detail(name, id, province, "10035", p_c)


def get_list(i):
    url = "http://data.api.gkcx.eol.cn/soudaxue/queryschool.html?messtype=jsonp&callback=jQuery18307305760356055457_1502290521022&province=&schooltype=&page="+str(i)+"&size=50&keyWord1=&schoolprop=&schoolflag=&schoolsort=&schoolid=&_=1502290521617"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    hd = response.read()
    hf=hd[41:-2]
    json_h=json.loads(hf)
    print json_h['totalRecord']['num']
    file1 = file("school_list",'a+')
    for school in json_h['school']:
        id = school['schoolid']
        name = school['schoolname']
        file1.write(str(id).replace("\n", ""))
        file1.write("*")
        file1.write(str(name).replace("\n", ""))
        file1.write("\n")
    file1.close()


if __name__ == "__main__":
    file1 = file("school_list")
    for line in file1:
        temp = line.split("*")
        name = temp[1]
        id = temp[0]
        get_xml(name, id)
