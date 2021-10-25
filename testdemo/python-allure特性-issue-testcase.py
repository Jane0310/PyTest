import allure

@allure.link("http://www.baidu.com",name="百度链接")
def test_with_link():
    print("这是一条加了链接的测试")
    pass

TEST_CASE_LINK='http://github.com/qameta/alure-integrations/issues'
@allure.testcase(TEST_CASE_LINK,'登录用例')
def test_with_testcase_link():
    print("这是一条测试用例的链接，链接到测试用例地址")
    pass