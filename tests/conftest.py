#fixture夹具

import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    # 基础环境，url，默认使用测试环境
    import os
    return os.getenv("API_BASE_URL","https://httpbin.org")

@pytest.fixture(scope="session")
# api回话夹具，整个测试会话复用一个session
def api_session():
    session=requests.Session()
    session.headers.update({
        "User-Agent":"AutoTest/1.0",
        "Accept":"application/json"
    })
    yield session
    session.close()

@pytest.fixture(scope="function")
def auth_token(api_session,base_url):
    """"每个测试前获取认证token"""
    resp = api_session.post(
        f"{base_url}/post",
        json={"username":"test","password":"test123"}
    )
    token =resp.json().get("headers",{}).get("X-Token","mock-token")
    api_session.headers.update({"Authorization":f"Bearer{token}"})
    yield token

    #测试后清理
    api_session.headers.pop("Authorization",None)



