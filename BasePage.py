import unittest
from po.config import HTTPConfig


class BasePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.S = HTTPConfig.S
        print("*" * 40 + "开始执行 " + cls.__name__ + " 测试用例" + "*" * 40)
