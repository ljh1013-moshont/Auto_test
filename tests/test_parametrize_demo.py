#使用pytest完成参数化测试
from unittest import expectedFailure

import pytest
#单参数
@pytest.mark.parametrize("number",[1,2,3,4,5,6,7])
def test_demo1(number):
    assert number<3
#多参数
@pytest.mark.parametrize("username,password","expected",[
    ("admin","123456","True"),
    ("122222","1111111","False"),],ids=["管理员正确密码","管理员错误密码"])
def test_demo2(username,password,expected):
    #简单写一下,实际应该为具体的登录方法的参数
    result =(username,password)
    assert result ==expected
#笛卡尔积参数化(多装饰器叠加)
@pytest.mark.parametrize("brower",["chromium","firefox","webkit"])
@pytest.mark.parametrize("viewport",[{"width":1920,"height":1080},
                                     {"width":375,"height":667}])
def test_demo3(brower,viewport):
    print(f"测试：{brower},浏览器视口大小:{viewport}")
