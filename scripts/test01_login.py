# 导包
import unittest
import api
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.assert_common import assert_common
from tools.read_data import read_data


# 新建测试类 集成unittest.TestCase
class TestLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 获取apilogin对象
        self.login = ApiLogin()

    # 登录测试接口方法
    @parameterized.expand(read_data("login.json"))
    def test_login(self, mobile, password):
        # 调用登录接口
        result = self.login.api_login(mobile, password)
        print(result.json())
        # 断言
        assert_common(self,result)
        # 提取token值
        token = result.json().get("data")
        # 追加到api公共变量
        api.headers["Authorization"] = "Bearer " + token
        print(api.headers)
