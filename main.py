import unittest
from po.config import HTTPConfig

if __name__ == '__main__':
    S = HTTPConfig.S
    loader = unittest.TestLoader().discover("./insper/page", pattern="Test*.py")
    unittest.TextTestRunner().run(loader)
