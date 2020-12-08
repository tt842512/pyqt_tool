import pymysql.cursors
import json


conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       passwd='root',
                       db='lend_mobile',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)

#创建游标
cursor = conn.cursor()

sql = 'select * from test order by id asc'

cursor.execute(sql)
results = cursor.fetchall()
temp = results
cursor.close()
conn.close()

jsonx = {}
for i in range(len(temp)):
    #创建用例基础格式
    jsonx[temp[i]['title']] = {"method": 1, "api": 1, "env": 1, "key": 1, "apikey": 1, "status_code": 1, "des": 1}
    #创建添加用例内容
    jsonx[temp[i]['title']]["method"] = [[temp[i]['method_moudel'], temp[i]['method_apiway']]]
    jsonx[temp[i]['title']]["api"] = [temp[i]['api']]
    jsonx[temp[i]['title']]["env"] = [temp[i]['env']]
    jsonx[temp[i]['title']]["key"] = [eval(temp[i]['params'])]
    jsonx[temp[i]['title']]["apikey"] = [temp[i]['apikey']]
    jsonx[temp[i]['title']]["status_code"] = [temp[i]['statuscode']]
    jsonx[temp[i]['title']]["des"] = temp[i]['des']

tyj = json.dumps(jsonx, ensure_ascii=False,indent=3)

print(tyj)
f = open('filename.json', 'w')
f.write(tyj)
f.close

