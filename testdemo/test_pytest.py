import pytest
class TestDemo():
    def test_one(self):
        print("开始执行 test_one 方法")
        x='this'
        # assert 'h' in x
        pytest.assume('h' not in x )
        pytest.assume(1==2)
        pytest.assume('x' in 'xxx')

    def test_two(self):
        print("开始执行 test_two方法")
        x='helo'
        assert 'b' in x

    def test_three(self):
        print("开始执行 test_three 方法")
        a='hello'
        b='hello world'
        assert a in b

class TestDemo1():
    def test_a(self):
        print("开始执行 test_a 方法")
        x='this'
        assert 'h' in x

    def test_b(self):
        print("开始执行 test_b方法")
        x='helo'
        assert 'e' in x

    def test_c(self):
        print("开始执行 test_c 方法")
        a='hello'
        b='hello world'
        assert a in b

if __name__ == '__main__':
    # 第一种方式
    pytest.main('-v TestDemo')
    # 第二种方式
    pytest.main(['-v','TestDemo'])
    # 执行所有的测试用例
    pytest.main()


