import allure

# 文本
def test_attach_text():
    allure.attach("这是一个文本",attachment_type=allure.attachment_type.TEXT)

# html
def test_attach_html():
    allure.attach("<body>这是一段htmlbody块</body>","html测试块",attachment_type=allure.attachment_type.HTML)

# 图片
def test_attach_photo():
    allure.attach.file("D:\PycharmProjects\PyTest\photo\photo.png",name="这是一个图片",attachment_type=allure.attachment_type.PNG)
