# def func(x):
#     return x + 1
#
#
# def test_answer():
#     assert func(3) == 5

def test_one():
    print("开始执行 test_one 方法")
    x='this'
    assert 'h' in x

def test_two():
    print("开始执行 test_two方法")
    x='helo'
    assert 'e' in x

def test_three():
    print("开始执行 test_three 方法")
    a='hello'
    b='hello world'
    assert a in b