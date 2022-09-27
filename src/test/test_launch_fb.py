import unittest
import sys
from main import config

sys.path.append("../../")


class test_fb(unittest.TestCase):
    fb = "https://www.facebook.com"
    username = "pavan.ramisetty123@gmail.com"
    password = "Dream@143"

    def test_login(self):
        assert config.login(self.fb, self.username, self.password)


if __name__ == "__main__":
    unittest.main()
