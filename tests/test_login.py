#登录测试

import pytest
from pages.login_page import LoginPage

class TestLogin:
    def test_login_success(self,page):
        login_page =LoginPage(page)
        login_page.navigate()
        login_page.login_success("admin","123456")
        welcome=login_page.welcome_text()
        assert welcome.is_visible()
    def test_login_wrong_password(self,page):
        login_page =LoginPage(page)
        login_page.navigate()
        login_page.login("admin","123123")
        error_message =login_page.get_error_message()
        assert "密码错误" in error_message

    @pytest.mark.parametrize("username,password,expected_error",[
        ("","123456","用户名不能为空"),
        ("admin","","密码不能为空"),
        ("nonexistent","123456","用户名不存在"),
    ])
    def test_login_invalid_inputs(self,page,username,password,expected_error):
        login_page =LoginPage(page)
        login_page.navigate()
        login_page.login(username,password)
        error_message =login_page.get_error_message()
        assert expected_error in error_message
