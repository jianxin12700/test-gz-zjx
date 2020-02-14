def assert_common(self, response,
                  status_code=200,
                  success=True,
                  code=10000,
                  message="操作成功！"):
    """

    :param self: TestCase实例
    :param response: 响应对象
    :return: 无
    """
    response_json = response.json()
    # 断言
    # 断言状态码
    self.assertEqual(status_code, response.status_code)
    # 断言success
    self.assertEqual(success, response_json.get("success"))
    # 断言 code错误码
    self.assertEqual(code, response_json.get("code"))
    # 断言 message文本提示
    self.assertEqual(message, response_json.get("message"))
