import api
import requests

from tools.get_log import GetLog

log = GetLog.get_logger()


class ApiEmployee(object):
    # 新增URL
    url1 = api.host + "/api/sys/user"
    # 修改、查询、删除URL
    url2 = api.host + "/api/sys/user/"
    log.info("新增员工url: {}".format(url1))
    log.info("删除、更新、查询公共url模板：{}".format(url2))

    # # 初始化
    # def __init__(self):
    #     pass

    # 新增员工
    def api_post_employee(self, username, mobile, workNumber):
        # 参数数据
        data = {"username": username,
                "mobile": mobile,
                "workNumber": workNumber}
        log.info("新增员工数据：{} 新增员工请求信息头：{}".format(data, api.headers))
        # 调用post方法 返回响应对象
        return requests.post(url=self.url1, json=data, headers=api.headers)

    # 修改员工
    def api_put_employee(self, username):
        # 参数数据
        data = {"username": username}
        log.info("修改员工url：{} 修改员工数据：{} 请求header:{}".format(self.url2 + api.user_id, data, api.headers))
        # 调用put方法 返回响应对象
        return requests.put(url=self.url2 + api.user_id, json=data, headers=api.headers)

    # 查询员工
    def api_get_employee(self):
        log.info("查询员工url:{} 请求头：{}".format(self.url2 + api.user_id, api.headers))

        # 调用get方法 返回响应对象
        return requests.get(url=self.url2 + api.user_id, headers=api.headers)

    # 删除员工
    def api_del_employee(self):
        log.info("删除员工url : {} 删除员工请求信息头：{}".format(self.url2 + api.user_id, api.headers))
        # 调用delete方法 返回响应对象
        return requests.delete(url=self.url2 + api.user_id, headers=api.headers)
