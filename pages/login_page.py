#登录页

from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):

    URL = "https://example.com/login"

    def __init__(self,page:Page):
        super().__init__(page)
        #元素定位器，集中定位便于维护
        self.username_input =page.get_by_role("textbox",name="用户名")
        self.password_input =page.get_by_role("textbox",name="密码")
        self.login_button =page.get_by_role("button",name="登录")
        self.error_message =page.locator(".error-message")
        self.welcome_text =page.locator(".welcome-text")
    def navigate(self):
        self.open(self.URL)

    def login(self,username:str,password:str):
        self.fill(self.username_input,username,"用户名输入框")
        self.fill(self.password_input,password,"密码输入框")
        self.click(self.login_button,"登录按钮")

    def login_success(self,username:str,password:str):
        self.login(username,password)
        self.assert_visible(self.welcome_text)

    def get_error_message(self) -> str| None:
        return self.get_text(self.error_message)
