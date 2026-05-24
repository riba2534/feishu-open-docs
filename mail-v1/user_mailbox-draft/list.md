---
title: "列出草稿列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/user_mailbox-draft/list"
updateTime: "1776073315000"
---

# 列出草稿列表

列出用户草稿箱中的草稿，只会返回草稿ID信息，不会返回草稿内容


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/user_mailboxes/:user_mailbox_id/drafts |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `mail:user_mailbox.message:readonly` 查询用户邮件 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `user_mailbox_id` | `string` | 用户邮箱地址。当使用用户身份访问时，可以输入"me"代表当前调用接口用户<br>**示例值**："user@xxx.xx 或 me" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 分页大小<br>**示例值**：20<br>**默认值**：`20`<br>**数据校验规则**：<br>- 取值范围：`1` ～ `100` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：xxx |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `draft\[\]` | 草稿列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 草稿ID |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "id": "268dce11-85f7-427d-8756-6be3abc850fd"
            }
        ],
        "page_token": "xxx",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1234008 | request parameter error | 参数错误，请检查请求参数的类型、格式或值是否与接口要求一致，具体可参考接口文档中的参数说明 |
| 403 | 1234017 | permission deny | 无权限访问，请确认应用是否具备访问该资源的权限。如使用用户身份访问，请确认具备此用户的访问权限；如使用租户身份访问，请确认已申请对应的数据范围权限。 |
| 404 | 1234013 | user mailbox not found or user mailbox not active | 用户邮箱地址不存在，请检查输入的用户邮箱地址是否正确，或确认用户的邮箱处于正常状态 |
| 429 | 1236006 | too many request | 请求被限流，请勿并发调用接口 |
| 500 | 1236019 | internal server error | 内部服务错误，请重试 |


