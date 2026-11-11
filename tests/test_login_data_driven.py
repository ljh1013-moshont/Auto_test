import pytest
import yaml
from pages.login_page import LoginPage

def load_test_data(file_path):
    #读取数据
    with open(file_path,"r",encoding="utf-8")as f:
        #解析文件
        data =yaml.safe_load(f)
    #返回yaml中数据
    return data["test_cases"]
#调用方法获取数据
test_data=load_test_data("data/login_data.yaml")

#把test_data中数据依次注入case中
@pytest.mark.parametrize("case",test_data,ids=[c["case_name"] for c in test_data])
def test_login_data_driven(page,case):
    login_page=LoginPage(page)
    login_page.navigate()
    login_page.login(case["username"],case["password"])

    if case["expected"] =="success":
        #playwright自动等待机制保证不会立即执行
        assert(login_page.welcome_text).to_be_visible()
    else:
        error_msg =login_page.get_error_message()
        assert case["error_message"] in error_msg

