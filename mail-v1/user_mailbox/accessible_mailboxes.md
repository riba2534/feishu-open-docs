---
title: "列出可访问的邮箱"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/user_mailbox/accessible_mailboxes"
updateTime: "1776073357000"
---

# 列出可访问的邮箱

列出可访问的邮箱，包括拥有读信和发信权限的主账号、公共邮箱


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/user_mailboxes/:user_mailbox_id/accessible_mailboxes |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `mail:user_mailbox` 查询、创建、修改和删除用户的企业邮箱 `mail:user_mailbox:readonly` 查询用户的企业邮箱 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `user_mailbox_id` | `string` | 用户邮箱地址，用户身份下可以填写me。注意不可以使用公共邮箱访问此接口。<br>**示例值**："abc@abc.com" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `accessible_mailboxes` | `email_info\[\]` | 用户可访问的所有邮箱信息，包含主邮箱和公共邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `email_address` | `string` | 邮箱地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `email_type` | `string` | 邮箱地址类型<br>**可选值有**：<br>- `MAIL_GROUP`: 邮件组 - `PUBLIC_MAILBOX`: 公共邮箱 - `USER_PRIMARY`: 用户主地址 - `USER_ALIAS`: 用户别名 - `PUBLIC_MAILBOX_ALIAS`: 公共邮箱别名 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "accessible_mailboxes": [
            {
                "email_address": "abc@abc.com",
                "email_type": "USER_PRIMARY"
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1230001 | param is invalid, check user_mailbox_id | 参数错误，请检查user_mailbox_id参数是否正确 |
| 403 | 1230004 | permission denied: mailbox not found, unsupported mailbox type, or no access to this mailbox | 权限不足：邮箱不存在、邮箱类型不支持，或无权访问该邮箱，请检查user_mailbox_id参数和权限申请状态 |
| 500 | 1230003 | internal server error, please retry later | 服务器内部错误，请稍后重试 |
| 400 | 1230005 | tenant access token not support me | tenant_access_token身份下访问不可以使用"me"作为user_mailbox_id参数 |


