---
title: "获取入职流程列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/pre_hire/onboarding-flow"
updateTime: "1720766086000"
---

# 获取入职流程列表

入职系统配置好流程后，通过此接口获取所有流程列表  


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/onboarding_flows |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:pre_hire:read` 获取待入职人员信息 `corehr:pre_hire:write` 读写待入职人员信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `flow_list` | `onboarding_flow\[\]` | 入职流程信息列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 流程id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n_v2` | 流程名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "flow_list": [
            {
                "id": "628caefb0eb4ac9c806982ee",
                "name": {
                    "zh_cn": "流程中文名",
                    "en_us": "flow english name"
                }
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1160001 | param is invalid | 参数无效 |


