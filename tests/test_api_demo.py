import pytest

class TestHttpBinAPI:

    def test_get_request(self,api_session,base_url):
        resp =api_session.get(
            f"{base_url}/get",
            params={"name":"pytest","version":"8.3"}
        )
        assert resp.status_code == 200
        data =resp.json()
        assert data["args"]["name"] =="pytest"
        assert data["args"]["version"] =="8.3"
#测试post json请求
    def test_post_json(self,api_session,base_url):
        payload ={"username":"admin","role":"tester"}
        resp =api_session.post(f"{base_url}/post",json=payload)
        assert resp.status_code == 200
        assert resp.json()["json"] == payload

#测试不同状态码响应
    @pytest.mark.parametrize("code",[200,201,400,500])
    def test_status_code(self,api_session,base_url,code):
        resp =api_session.get(f"{base_url}/status/{code}")
        assert resp.status_code == code

#测试响应时间
    def test_response_time(self,api_session,base_url):
        resp =api_session.get(f"{base_url}/delay/1")
        assert resp.status_code == 200
        assert resp.elapsed.total_seconds()<3.0

#参数化测试延迟接口
    @pytest.mark.parametrize("delay",[1,2,3])
    def test_delay_api(self,api_session,base_url,delay):
        resp =api_session.get(f"{base_url}/delay/{delay}")
        assert resp.status_code ==200
