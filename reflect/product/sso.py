# SSOLogin 类测试登录的功能
# 登录需要提供用户名和密码，用户名和密码通过yaml文件定义
# 登录成功后需要保存Cookie,用于后续测试
from ddt import ddt, file_data
import unittest
from po.config import ProductConfig
from po.BasePage import BasePage


@ddt
class SSOLogin(BasePage):

    # 测试案例从 Login.yaml 文件中读取
    @file_data("../case/Login.yaml")
    def test_login(self, username, password):
        # 登录时的请求参数
        payload = {"userName": username, "password": password}

        # 登陆时的请求 API, ProductConfig 的 url 属性保存了SSO的Http地址
        url = '%s/authentication/api/login' % ProductConfig.url

        # 发送登录请求，自动保存 Cookies
        response = self.S.post(url, json=payload)

        # 如果没有获取到 Cookies，说明本次登录失败
        self.assertTrue(response.cookies)


if __name__ == '__main__':
    unittest.main()
