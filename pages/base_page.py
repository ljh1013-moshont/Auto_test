#页面基类
from playwright.sync_api import Page,expect,Locator
from utils.logger import logger

#页面基类，封装通用=
class BasePage:
    def __init__(self,page:Page):
        self.page =page

    def open(self,url:str):
        logger.info(f"打开页面,{url}")
        self.page.goto(url)

    def click(self,locator:Locator,description:str = ""):
        logger.info(f"点击元素,{description}")
        locator.click()

    def fill(self,locator:Locator,text:str,description:str =""):
        logger.info(f"填充输入框:{description},内容:{text}")
        locator.fill(text)

    def get_text(self,locator:Locator)->str |None:
        return locator.text_content()

    def is_visible(self,locator:Locator,timeout:int =5000)->bool:
        try:
            locator.wait_for(state="visible",timeout=timeout)
            return True
        except Exception:
            return False

    def wait_for_element(self,locator:Locator,timeout:int =5000):
        locator.wait_for(state="visible",timeout=timeout)

    def screenshot(self,path:str):
        self.page.screenshot(path=path)
        logger.info(f"截图已保存:{path}")

    def assert_text(self,locator:Locator,expected:str):
        expect(locator).to_have_text(expected)
        logger.info(f"断言成功，文本为:{expected}")

    def assert_visible(self,locator:Locator):
        expect(locator).to_be_visible()
        logger.info("断言成功，元素可见")
