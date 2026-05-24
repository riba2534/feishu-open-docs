---
title: "批量修改邮件会话"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/user_mailbox-thread/batch_modify"
updateTime: "1776073190000"
---

# 批量修改邮件会话

批量修改邮件会话的标签、所属文件夹和已读未读状态，支持为邮件会话添加旗标、归档、移入垃圾邮件文件夹。注意，接口不支持将邮件会话移入已删除文件夹，如需，请使用批量删除邮件会话接口。


> **Tip**: 注意，接口不支持将邮件会话移入已删除文件夹，如需，请使用批量删除邮件会话接口。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/user_mailboxes/:user_mailbox_id/threads/batch_modify |
| HTTP Method | POST |
| 接口频率限制 | [20 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `mail:user_mailbox.message:modify` 修改邮件 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `user_mailbox_id` | `string` | 用户邮箱地址。当使用用户身份访问时，可以输入"me"代表当前调用接口用户<br>**示例值**："me" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `add_label_ids` | `string\[\]` | 否 | 待添加的标签。可选值包括：UNREAD、IMPORTANT、OTHER、FLAGGED，以及自定义标签 ID。<br>**示例值**：["UNREAD"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `20` |
| `remove_label_ids` | `string\[\]` | 否 | 待移除的标签。可选值包括：UNREAD、IMPORTANT、OTHER、FLAGGED，以及自定义标签 ID。<br>**示例值**：["UNREAD"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `20` |
| `add_folder` | `string` | 否 | 需要移入的文件夹。支持INBOX、SENT、SPAM、ARCHIVED以及自定义文件夹ID<br>**示例值**："INBOX" |
| `thread_ids` | `string\[\]` | 否 | 需要操作的邮件会话ID，可通过列出邮件会话获取<br>**示例值**：["dXNCbmZydHpBOWNBOXNmTFU0NDdkYjlSRzlZPQ=="]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `20` |


### 请求体示例

```json
{
    "add_label_ids": [
        "UNREAD"
    ],
    "remove_label_ids": [
        "UNREAD"
    ],
    "add_folder": "INBOX",
    "thread_ids": [
        "dXNCbmZydHpBOWNBOXNmTFU0NDdkYjlSRzlZPQ=="
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
| 400 | 1230001 | param is invalid | 参数错误，请参考此文档修改参数 |
| 500 | 1230002 | Internal error | 服务器内部错误，请稍后重试 |
| 429 | 1236006 | Concurrent write conflict. Please retry later | 无法并发修改邮件，请稍后重试 |
| 400 | 1238008 | label or folder or thread not exist | 指定标签、文件夹或邮件会话不存在，请检查参数后重试 |
| 403 | 1230009 | permission denied | 无权限访问，请检查权限申请状态 |


