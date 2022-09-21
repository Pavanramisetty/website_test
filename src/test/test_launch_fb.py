import sys

sys.path.append("../../")
from main import config

fb = "https://fb.com"
base = config.BaseConfig


def test_login():
    assert base.login(fb), "FAiled blah blah, blah"
