---
title: "订阅服务台事件"
fullPath: "/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/event/subscribe"
updateTime: "1692084864000"
---

# 订阅服务台事件

本接口用于订阅服务台事件。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/helpdesk/v1/events/subscribe |
| HTTP Method | POST |
| 接口频率限制 | [特殊频控](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `helpdesk:all:readonly` 获取服务台资源详情 |

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


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `events` | `event\[\]` | 是 | 可订阅的事件列表 |
| &nbsp;&nbsp;└ `type` | `string` | 是 | 事件类型<br>**示例值**："helpdesk.ticket_message" |
| &nbsp;&nbsp;└ `subtype` | `string` | 是 | 事件子类型<br>**示例值**："ticket_message.created_v1" |


### 请求体示例

```json
{
    "events": [
        {
            "type": "helpdesk.ticket_message",
            "subtype": "ticket_message.created_v1"
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


