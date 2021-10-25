import pytest

@pytest.fixture(params=[1,2,3,'linda'])
def test_data(request):
    return request.params

def test_one(test_data):
    print('\ntest data：%s' % test_data)


# 参数组合
@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[8,10,11])
def test_foo(x,y):
    print("测试数据组合x："+{str(x)}+",y："+{str(y)})

if __name__ == '__main__':
    pytest.main()