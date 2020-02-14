import api
import requests



class ApiLogin(object):
    # 组装登录URL
    url_login = api.host + "/api/sys/login"

    # # 初始化
    # def __init__(self):
    #     pass

    # 登录接口封装
    def api_login(self, mobile=None, password=None):
        # 定义测试数据
        data = {"mobile": mobile, "password": password}
        # 调用post方法
        return requests.post(url=self.url_login, json=data, headers=api.headers)
