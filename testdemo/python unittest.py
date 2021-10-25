import unittest

# 测试类demo
class demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    # setUp用来为测试准备环境
    def setUp(self):
        print("setUp")


    # tearDown用来清理环境
    def tearDown(self):
        print("tearDown")


    def test_case01(self):
        print("testCase01")
        # 判断是否相等
        self.assertEqual(2, 2, "判断相等")

    @unittest.skip("跳过这条用例")
    def test_case02(self):
        print("testCase02")
        # 判断是否相等
        self.assertEqual(2, 2, "判断相等")

    def test_case03(self):
        print("testCase03")
        # 判断是否相等
        self.assertEqual(2, 2, "判断相等")

# 测试类demo1
class demo1(unittest.TestCase):
    def test_demo1_case0(self):
        print("test_demo1_case0")

    def test_demo1_case1(self):
        print("test_demo1_case1")

# 测试类demo2
class demo2(unittest.TestCase):
    def test_demo2_case0(self):
        print("test_demo2_case0")

    def test_demo2_case1(self):
        print("test_demo2_case1")

# 测试用例执行
if __name__ == '__main__':
    # 执行方法一
    # unittest.main()

    # 执行方法2：加入容器中执行
    # suite = unittest.TestSuite()
    # suite.addTest(demo("test_case01"))
    # suite.addTest(demo1("test_demo1_case0"))
    # unittest.TextTestRunner().run(suite)

    # 执行方法3
    # suite=unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite1=unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suiteall=unittest.TestSuite([suite,suite1])
    # unittest.TextTestRunner().run(suiteall)

    # 执行方法4
    test_dir = "./testdemo"
    # 执行某个路径下的 符合规则的py文件
    discover =unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
    unittest.TextTestRunner().run(discover)