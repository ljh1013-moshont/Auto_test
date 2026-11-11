import pytest

from pages.login_page import LoginPage
from utils.excel_reader import read_excel

test_data =read_excel("data/test_cases.xlsx","登录测试")
@pytest.mark.parametrize("data",test_data,ids=[d.get("用例名称",f"case_{i}") for i,d in enumerate(test_data)])
def test_login_from_excel(page,data):
    login_page=LoginPage(page)
    login_page.navigate()
    login_page.login(data["用户名"],data["密码"])

    if data["预期结果"] ==("成功"):
        assert login_page.welcome_text.is_visible()
    else:
        assert data["错误信息"] in login_page.get_error_message()