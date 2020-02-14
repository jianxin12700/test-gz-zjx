import unittest

from api.api_employee import ApiEmployee
from tools.assert_common import assert_common
import api


class TestEmployee(unittest.TestCase):


    # 类级别初始化
    @classmethod
    def setUpClass(cls):
        cls.employee = ApiEmployee()


    # 新增员工
    def test01_post(self):
        # 调用新增接口
        response = self.employee.api_post_employee(
            "gz-day-v012", "13575400100", "14159627")
        # 断言
        assert_common(self, response)
        # 提取id值 追加到api公共变量
        api.user_id = response.json().get("data").get("id")

    # 更新员工
    def test02_put(self):
        # 调用更新接口
        response = self.employee.api_put_employee("gz6q-v02-r12")
        # 断言
        assert_common(self, response)

    # 查询员工
    def test03_get(self):
        # 调用查询接口
        response = self.employee.api_get_employee()
        # 断言
        assert_common(self, response)

    # 删除员工
    def test04_del(self):
        # 调用删除接口
        response = self.employee.api_del_employee()
        # 断言
        assert_common(self, response)
