---
title: "回复用户在工单里的提问"
fullPath: "/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/ticket/answer_user_query"
updateTime: "1692084861000"
---

# 回复用户在工单里的提问

该接口用于回复用户提问结果至工单，需要工单仍处于进行中且未接入人工状态。仅支持自建应用。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/helpdesk/v1/tickets/:ticket_id/answer_user_query |
| HTTP Method | POST |
| 接口频率限制 | [特殊频控](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `helpdesk:all` 更新服务台资源详情 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


> **Tip**: 服务台请求Header中还需添加“服务台token”参数：
>   
>   Key: X-Lark-Helpdesk-Authorization
>   
>   Value: base64(helpdesk_id:helpdesk_token)，通过base64加密将helpdesk_id和helpdesk_token用':'连接而成的字符串。
>   
>   [了解更多：获取与使用服务台token](https://open.larkoffice.com/document/ukTMukTMukTM/ugDOyYjL4gjM24CO4IjN)


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `ticket_id` | `string` | 工单ID<br>**示例值**："6945345902185807891" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `event_id` | `string` | 是 | 事件ID,可从订阅事件中提取<br>**示例值**："abcd" |
| `faqs` | `user_query_faq_info\[\]` | 否 | faq结果列表 |
| &nbsp;&nbsp;└ `id` | `string` | 否 | faq服务台内唯一标识<br>**示例值**："12345" |
| &nbsp;&nbsp;└ `score` | `number(float)` | 否 | faq匹配得分<br>**示例值**：0.9 |


### 请求体示例

```json
{
    "event_id": "abcd",
    "faqs": [
        {
            "id": "12345",
            "score": 0.9
        }
    ]
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {}
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 154000 | Bad request, please check your request body | 请求不合法，请检查参数 |
| 403 | 154003 | Please check you have the correct access | 检查是否申请正确权限 |
| 500 | 155000 | Internal error | 内部错误，请联系我们 |
| 404 | 154004 | Resource not found | 资源不存在，请检查ID值 |


