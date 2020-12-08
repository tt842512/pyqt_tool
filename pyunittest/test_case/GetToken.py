#部分接口除了apikey以外还依赖tenant的token值，此处获取
import requests
import json
import warnings

class get_token():
    def __init__(self,env):
        warnings.simplefilter('ignore', ResourceWarning)
        requests.packages.urllib3.disable_warnings()
        requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
        self.session = requests.session()
        self.session.keep_alive = False  # 关闭多余连接
        self.ip = env


    def get_authcode(self):
        codeurl = "http://" + self.ip + "/tenant/api/v1/base/code/getcode"
        headinfo = {
                "Content-Type": "application/json"}
        payload = json.dumps({})
        r = self.session.get(codeurl, params=payload, headers=headinfo, verify=False)
        return r.json()['data']['authCode']

    def login(self):
        loginurl = "http://" + self.ip + "/tenant/api/v1/user/login"
        site = "https://" + self.ip + "//#/"
        headinfo = {
                "Content-Type": "application/json"}
        payload = json.dumps({"authCode": self.get_authcode(), "email": "admin",
         "passwd": "Admin@123", "return_insite": site})
        r = self.session.post(loginurl, data=payload, headers=headinfo, verify=False)
        return r.json()['data']['token']

    def getapikey(self):
        url = "http://" + self.ip + "/tenant/api/v1/user/details/view"
        headinfo = {
            "Content-Type": "application/json",
            "Cookie": "token=%s" % self.login()}
        payload = json.dumps({})
        r = self.session.get(url, params=payload, headers=headinfo, verify=False)
        return r.json()['data']['apiKeys'][0]['key']

    def dics(self):
        paradic = {'token': self.login(), 'apikey': self.getapikey()}
        return paradic


if __name__=="__main__":
    a = get_token('192.168.0.66').dics()
    print(a)
    print(a['apikey'])