---
title: "查询用户云文档事件订阅状态"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/user/subscription_status"
updateTime: "1775123703000"
---

# 查询用户云文档事件订阅状态

该接口用于查询用户云文档事件的订阅状态。仅当is_subscribe（订阅状态）为 true，应用才可收到 “用户云文档事件”下的各类通知事件。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/drive/v1/user/subscription_status |
| HTTP Method | GET |
| 接口频率限制 | [10 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `docs:event:subscribe` 订阅云文档事件 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `event_type` | `string` | 是 | 事件类型<br>路由到 云文档事件列表，当前仅支持一种事件<br>可选值：<br>  drive.notice.comment_add_v1：添加评论、回复通知事件<br>**示例值**：drive.notice.comment_add_v1 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `data` | `string` | 订阅状态 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "data": {
            "is_subscribe": true
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1069601 | fail | 重试，若稳定失败请联系[技术支持](https://applink.feishu.cn/client/helpdesk) |
| 400 | 1069602 | param error | 检查参数有效性 |


