import unittest
import requests
from ddt import file_data, ddt
import warnings
import json

#####本地调试时用这一段，部署到jenkins时，用下面一段，只能存在一个
from pyunittest.test_excutes import case_listener #本地执行路径

#####放到jenkin时，用这一段，上面的注释掉
# import sys, os
# path = os.path.abspath(__file__)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(BASE_DIR)
# import case_listener


test = case_listener.caseListener()

@ddt
class Servicepatrol_suite(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
        self.session = requests.session()
        self.session.keep_alive = False  # 关闭多余连接
    #测试参数和测试验证的字典
    # @file_data("./Test_Data/ServicePatrol_dict.json")
    @file_data("./Test_Data/Recovery_dict.json")
    @test.method_automation(dict(classname="test_Servicepatrol"))
    def test_Servicepatrol(self,**kwargs):
        for i in range(len(kwargs["api"])):
            apikey = kwargs["apikey"][i]
            api = kwargs["api"][i]
            env = kwargs["env"][i]
            url = "%s%s" % (env, api)
            # 环境参数，0位置控制接口调用方法如post，get，1位置控制参数类型，是body类型还是普通参数类型
            method = kwargs["method"][i]

            if method[1] == 1:
                headinfo = {
                    "apikey": apikey,
                    "Content-Type": "application/json"}
                payload = json.dumps(kwargs["key"][i])
            elif method[1] == 2:
                headinfo = {
                    "apikey": apikey}
                payload = kwargs["key"][i]

            if method[0] == 1:
                self.r = self.session.post(url, data=payload, headers=headinfo,verify=False)
            elif method[0] == 2:
                self.r = self.session.get(url, params=payload, headers=headinfo,verify=False)

            # response = requests.get(self.url,params=kwargs["key"])
            print(self.r.json())
            self.assertEqual(self.r.json()["code"], kwargs["status_code"][i])
        # api = kwargs["api"]
        # url = 'https://t-api-app.apeiwan.com' + api
        # headinfo = {
        #     "token": self.login_json
        # }
        # self.r = self.session.post(url, data=kwargs["key"], headers=headinfo)
        #
        # # response = requests.get(self.url,params=kwargs["key"])
        # print(self.r.json())
        # self.assertEqual(self.r.status_code, kwargs["status_code"])



if __name__=="__main__":
    unittest.main()