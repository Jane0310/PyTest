import pytest

# 公共方法封装
@pytest.fixture()
def login():
    print("这是个登录方法")