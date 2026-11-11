import pytest
from playwright.sync_api import Page,expect

def test_baidu_search(page: Page):
    #进入百度页面
    page.set_viewport_size({"width":1920,"height":1080})
    page.goto("https://www.baidu.com")

    expect(page).to_have_title("百度一下，你就知道")

    print("标题:", page.title())
    print("URL:", page.url)

    search_box=page.locator("#kw")

    search_box.wait_for(state="visible",timeout=10000)

    search_box.click()

    search_box.fill("playwright自动化测试")

    page.locator("#su").wait_for(state="visible",timeout=10000)

    page.locator("#su").click()


    expect(page.locator("#content_left")).to_be_visible(timeout=10000)

    result_items =page.locator(".result.c-container")

    assert result_items.count() > 0
    page.screenshot(path="screenshots/baidu_serch_result.png")

#参数化测试
from playwright.sync_api import Page, expect
import pytest

def test_baidu_search_with_multiple_keywords(page: Page):
    keywords = ["python", "Pytest", "Playwright"]

    for keyword in keywords:
        page.goto("https://www.baidu.com", wait_until="networkidle")  # 等待网络基本空闲

        # 显式等待搜索框可见、可编辑，避免元素存在但尚未就绪
        search_input = page.locator('//*[@id="main-wrapper"]')  # .first 防止 strict mode 匹配到多个
        search_input.wait_for(state="visible", timeout=10000)

        search_input.fill(keyword)
        page.get_by_role("button", name="百度一下").click()

        # 修正断言写法：to_be_visible 会自动等待
        expect(page.locator("#content_left")).to_be_visible(timeout=15000)
        print(f"关键字:{keyword} 搜索成功")



