import unittest
import requests
from ddt import file_data, ddt
import warnings
import sys, os
# from pyunittest.test_excutes import case_listener
path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
import case_listener


test = case_listener.caseListener()

@ddt
class test_case_suite(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
        self.session = requests.session()
        self.session.keep_alive = False  # 关闭多余连接
        # 登陆用户类型的账号，目前写死，后面再做成可配置
        self.mobile1 = {"mobile": 13728888888}
        url_sms = 'https://t-api-app.apeiwan.com/sms/verify'
        self.r1 = self.session.post(url_sms, data=self.mobile1)
        login_info1 = {"code": 2222, "mobile": 13728888888}
        url_login = 'https://t-api-app.apeiwan.com/login'
        self.r1 = self.session.post(url_login, data=login_info1)
        self.login_json1 = self.r1.json()['data']['token']
        #登陆房主陪玩类型的账号
        self.mobile2 = {"mobile": 13729999999}
        self.r2 = self.session.post(url_sms, data=self.mobile2)
        login_info2 = {"code": 2222, "mobile": 13729999999}
        self.r2 = self.session.post(url_login, data=login_info2)
        self.login_json2 = self.r2.json()['data']['token']
    #测试参数和测试验证的字典
    @file_data("./test_app_dict.json")
    @test.method_automation(dict(classname="testapp"))
    def testapp(self,**kwargs):
        for i in range(len(kwargs["api"])):
            token_choose = kwargs["token_choose"][i]
            if token_choose == 1:
                token = self.login_json1
            elif token_choose == 2:
                token = self.login_json2
            api = kwargs["api"][i]
            url = 'https://t-api-app.apeiwan.com' + api
            headinfo = {
                "token": token
            }
            self.r = self.session.post(url, data=kwargs["key"][i], headers=headinfo)

            # response = requests.get(self.url,params=kwargs["key"])
            print(self.r.json())
            self.assertEqual(self.r.status_code, kwargs["status_code"][i])
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