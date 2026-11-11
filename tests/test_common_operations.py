from playwright.sync_api import Page,expect

def test_common_operations(page: Page):

    #导航操作
    page.goto("https://example.com")  #访问url

    page.go_back()     #后退

    page.go_forward()  #前进

    page.reload()      #刷新

    print(page.url)
    print(page.title())

    #元素交互操作

    page.locator("#username").fill("admin")

    page.locator("#password").fill("1234516")


    #check() 和 click() 的区别：check() 是幂等的——目标已是选中状态就什么都不做；click() 每次都切换，可能把已选中的点掉。操作复选框/单选框优先用 check()


    page.locator("#login-btn").click()

    page.locator("#checkbox").check() #勾选复选框

    page.locator("#radio").check()     #选中单选框

    page.locator("#select").select_option("value") #下拉选择

    page.locator("#input").press("Enter")   #模拟按键

    page.locator("#input").type("hello",delay=100)   #逐字符输入，模拟真实打字

    #元素信息获取

    text = page.locator(".welcome").text_content()   #获取文本内容
    attr = page.locator("#link").get_attribute("href")   #获取属性值
    is_visible =page.locator("#modal").is_visible()     #是否可见
    is_enabled =page.locator(".item").is_enabled()     #是否可用
    count =page.locator(".item").count()

    #等待操作
    #能断言就用 expect()（自动重试）→ 需要等元素用 wait_for() → 实在没办法才用 wait_for_timeout()。sleep 式等待会让测试变慢且不稳定。
    page.wait_for_load_state("networkidle")  #等待网络空闲
    page.locator("#result").wait_for()      #等待元素出现
    page.wait_for_timeout(2000)             #固定等待2秒

    #截图与录制
    page.screenshot(path="screenshot.png",full_page=True)  #整页截图
    page.locator("#chart").screenshot(path="chart.png")    #元素截图

    #断言(自动重试，默认超时5秒）
    #默认 5 秒内反复重试，直到条件满足或超时
    expect(page.locator("#welcome")).to_have_text("欢迎,admin")
    expect(page.locator("#status")).to_contain_text("成功")
    expect(page.locator("#count")).to_have_text("10")
    expect(page).to_have_url("https://example.com")
    expect(page).to_have_title("首页")
    expect(page.locator("#modal")).to_be_hidden()






