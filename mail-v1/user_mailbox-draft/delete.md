---
title: "删除草稿"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/user_mailbox-draft/delete"
updateTime: "1776073337000"
---

# 删除草稿

删除指定邮箱账户下的单份邮件草稿。


> **Tip**: 对于草稿状态的邮件，只能使用本接口删除，禁止使用删除邮件接口


> **Warning**: 被删除的草稿数据无法恢复，请谨慎使用


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/user_mailboxes/:user_mailbox_id/drafts/:draft_id |
| HTTP Method | DELETE |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `mail:user_mailbox.message:modify` 修改邮件 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `user_mailbox_id` | `string` | 用户邮箱地址不存在，请检查输入的用户邮箱地址是否正确，或确认用户的邮箱处于正常状态<br>**示例值**："aba@aac.com 或 me" |
| `draft_id` | `string` | 草稿ID，可通过列出草稿列表接口获得<br>**示例值**："268dce11-85f7-427d-8756-6be3abc850fd" |


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
| 403 | 1234017 | permission deny | 无权限访问，请确认应用是否具备访问该资源的权限。如使用用户身份访问，请确认具备此用户的访问权限；如使用租户身份访问，请确认已申请对应的数据范围权限。 |
| 404 | 1234050 | draft not found | 指定草稿不存在，请核对草稿ID，或草稿已经删除成功 |
| 404 | 1234013 | user mailbox not found or user mailbox not active | 用户邮箱地址不存在，请检查输入的用户邮箱地址是否正确，或确认用户的邮箱处于正常状态 |
| 429 | 1236006 | Concurrent write conflict. Please retry later | 请求被限流，请勿并发调用，请稍后重试 |
| 500 | 1236019 | internal server error | 内部服务错误，请稍后重试 |


