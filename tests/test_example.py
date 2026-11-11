from playwright.sync_api import Page
#常用定位方法
def test_example(page: Page):

    page.goto("https://example.com/login")
    #基于角色定位
    page.get_by_role("textbox",name="用户名").fill("admin")

    page.get_by_role("textbox",name="密码").fill("123456")

    page.get_by_role("button",name="登录").click()

    #基于label定位(标签文本)

    page.get_by_label("邮箱").fill("325760587@qq.com")

    #基于placeholder(占位符文本定位)

    page.get_by_placeholder("请输入手机号").fill("111111222222")

    #基于文本定位

    page.get_by_text("忘记密码").click()

    #基于test_id定位
    page.get_by_test_id("submit-button").click()

    #css选择器定位
    page.locator("nav >> .menu-item").first.click()
    page.locator("div.card:has-text('特价')").click()

    #xpath定位
    #contains(字符串1，字符串2)表示在，字符串1中寻找匹配字符串2的内容，text()表示，获取当前指定标签的所有文本子节点的第一个
    #contains(a, b) = “a 里有没有 b”，结果是布尔值。
    #text() = “当前节点的直接文本子节点集合”，不是“第一个文本”。
    #想匹配任意位置（含嵌套）的文本，用 contains(., '登录')，. 会把所有后代文本拼起来；text() 只适合纯文本、无嵌套的场景。
    page.locator("//div[@class='header']//a[contains(text(),'登录')]").click()