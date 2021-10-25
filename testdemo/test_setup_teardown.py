import pytest

def setup_module():
    print("这是setup_module 方法")

def teardown_module():
    print("这是teardown_module 方法")


def setup_function():
    print("这是setup_function 方法")


def teardown_function():
    print("这是teardown_function 方法")

def test_login():
    print("这是一个外部的方法")

class testDemo():
    def setup_class(self):
        print("setup_class")

    def setup_method(self):
        print("setup_method")

    def setup(self):
        print("setup")

    def teardown_class(self):
        print("teardown_class")

    def teardown_method(self):
        print("teardown_method")

    def teardown(self):
        print("teardown")

    def test_one(self):
        print("开始执行 test_one_方法")
        x='this'
        assert 'h' in x

    def test_two(self):
        print("开始执行 test_two_方法")
        x='hello'
        assert 'e'in x

    def test_three(self):
        print("开始执行 test_three_方法")
        a = 'hello'
        b = 'hello world'
        assert a in b

if __name__ == '__main__':
    pytest.main()