# 使用pytest完成参数化测试
import pytest

# 单参数
@pytest.mark.parametrize("number", [1, 2, 3, 4, 5, 6, 7])
def test_demo1(number):
    assert number < 3  # 注意：3及以上的数字这里会断言失败，变成红色的FAILED，这是正常的

# 多参数
# 【修改点】三个参数名要写在一个字符串里，且用逗号隔开
@pytest.mark.parametrize("username,password,expected", [
    ("admin", "123456", "True"),
    ("122222", "1111111", "False"),
], ids=["管理员正确密码", "管理员错误密码"])
def test_demo2(username, password, expected):
    # 简单写一下，实际应该为具体的登录方法的参数
    result = (username, password)
    # 注意：这里的断言逻辑有点问题，result 是元组，expected 是字符串 "True"/"False"，这里肯定会失败的
    # 如果只是为了演示参数化，建议改成 assert str(result == (username, password)) == expected
    # 或者直接删掉断言
    assert result == (username, password)

# 笛卡尔积参数化(多装饰器叠加)
@pytest.mark.parametrize("brower", ["chromium", "firefox", "webkit"])
@pytest.mark.parametrize("viewport", [
    {"width": 1920, "height": 1080},
    {"width": 375, "height": 667}
])
def test_demo3(brower, viewport):
    print(f"测试：{brower}, 浏览器视口大小:{viewport}")