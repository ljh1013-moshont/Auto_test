#校验响应体的结构与字段

import pytest
import jsonschema

#定义响应 schema
user_schema ={
    "type":"object",
    "properties":{
        "id":{"type":"integer"},
        "username":{"type":"string"},
        "email":{"type":"string","format":"email"},
        "role":{"type":"string","enum":["admin","user","guest"]},
        "created_at":{"type":"string"}
    },
    "required":["id","username","email","role"]
}

#使用jsonschema校验结构
def test_user_api_schema(api_session,base_url):
    resp =api_session.get(f"{base_url}/get")
    assert resp.status_code==200

    #模拟用户数据
    mock_user ={
        "id":1,
        "username":"admin",
        "email":"admin@example.com",
        "role":"admin",
        "created_at":"2025-01-01t00:00:z"
    }

    try:
        #instance是数据，schema 是规则，validate 判断数据是否满足规则。
        jsonschema.validate(instance=mock_user,schema=user_schema)
        print("schema校验通过")
    except jsonschema.ValidationError as e:
        pytest.fail(f"schema校验失败:{e.message}")