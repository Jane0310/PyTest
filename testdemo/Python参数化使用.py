import pytest

class TestPatams:
    # 使用string
    @pytest.mark.parametrize("a,b",[(10,20),(10,30)])
    def test_param(self,a,b):
        print(a+b)  # 输出：30,40
        # print("-----string------")


    # 使用list
    @pytest.mark.parametrize(["a","b"],[(10,20),(10,30)])
    def test_listparam(self,a,b):
        print(a+b)  # 输出：30,40
        # print("-----list------")

    # 使用tuple
    @pytest.mark.parametrize(("a", "b"), [(10, 20), (10, 30)])
    def test_tupleparam(self, a, b):
        print(a + b)  # 输出：30,40
        # print("-----tuple------")

if __name__ == '__main__':
    pytest.main()