---
title: "校验应用管理员"
fullPath: "/ukTMukTMukTM/uITN1EjLyUTNx4iM1UTM"
updateTime: "1647332683000"
---

# 获取某个用户是否有应用管理权限

该接口用于查询用户是否为应用管理员。
> 此处应用管理员是指可以进入企业管理后台对应用进行审核和管理的企业管理员，并不是应用的开发者。

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/application/v3/is_user_admin |
| HTTP Method | GET |
| 支持的应用类型 | custom,isv |
| 权限要求  调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `admin:app.admin:check` 校验用户是否为应用管理员 `admin:app.admin:readonly` 获取应用管理员 ID、管理范围等信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token`   **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560"             [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求参数
|参数|类型|必须|说明|
|--|-----|--|----|
|open_id|string|否|用户 open_id，open_id 和 employee_id 两个参数必须包含其一，若同时传入取 open_id|
|employee_id|string|否|用户 employee_id（同通讯录 v3 版本中的 user_id），open_id 和 employee_id 两个参数必须包含其一，若同时传入取 open_id|

## 响应

### 响应体
|参数|说明|
|--|--|
|code|返回码，非 0 表示失败|
|msg|返回码的描述|
|data|返回的业务信息|
|&emsp;∟is_app_admin|用户是否为管理员，true 为是，false 为否|

### 响应示例
```json
{ 
    "code": 0, 
    "msg": "ok", 
    "data": { 
        "is_app_admin": false
    } 
}
```
