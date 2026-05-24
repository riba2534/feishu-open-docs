---
title: "列出邮件会话"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/user_mailbox-thread/list"
updateTime: "1776073232000"
---

# 列出邮件会话

列出用户指定文件夹或标签下的邮件会话，按时间倒序分页获取


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/user_mailboxes/:user_mailbox_id/threads |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `mail:user_mailbox.message:readonly` 查询用户邮件 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `user_mailbox_id` | `string` | 用户邮箱地址。当使用用户身份访问时，可以输入"me"代表当前调用接口用户<br>**示例值**："user@xxx.xx 或 me" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 是 | 分页大小<br>**示例值**：1<br>**数据校验规则**：<br>- 取值范围：`1` ～ `20` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：xxx |
| `folder_id` | `string` | 否 | 文件夹 id，支持INBOX、SENT、SPAM、ARCHIVED、SCHEDULED、TRASH、DRAFT以及自定义文件夹ID<br>**示例值**：INBOX 或者用户文件夹 id |
| `only_unread` | `boolean` | 否 | 是否只查询未读会话<br>**示例值**：true |
| `label_id` | `string` | 否 | 标签id，支持IMPORTANT、OTHER、FLAGGED以及自定义标签ID<br>**示例值**：FLAGGED |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `thread\[\]` | 会话列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 会话ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `body_preview` | `string` | 会话内的最新的一封邮件摘要，用于快速预览邮件核心内容 |
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
                "id": "xx",
                "body_preview": "hello world"
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
| 404 | 1234013 | user mailbox not found or user mailbox not active | 指定邮箱地址不存在或邮箱地址状态不正确，请检查输入的邮箱地址 |
| 400 | 1234040 | not support user type | 不支持输入的邮件地址类型，请更换邮箱地址 |
| 403 | 1234017 | permission deny | 无权限访问，请检查权限申请状态 |
| 400 | 1234037 | invalid page token | 分页参数错误，请检查分页参数 |
| 400 | 1234038 | invalid folder id | 不合法的folder_id，请检查folder_id参数 |
| 404 | 1234035 | folder not found | 指定folder不存在，请检查输入的folder参数 |
| 404 | 1234036 | label not found | 指定label不存在，请检查输入的label参数 |
| 400 | 1234039 | provide exactly one of folder_id or label_id | 必须且仅能指定 folder_id 或 label_id 中的一个，请检查参数 |
| 500 | 1234008 | internal server error | 服务器内部错误，请稍后重试 |
| 500 | 1235000 | unknown error | 服务器内部错误，请稍后重试 |


