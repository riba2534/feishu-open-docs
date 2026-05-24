---
title: "获取标签信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/user_mailbox-label/get"
updateTime: "1776073264000"
---

# 获取标签信息

根据指定ID，获取邮件标签信息，包括名称、未读数据、颜色等信息


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/user_mailboxes/:user_mailbox_id/labels/:label_id |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `mail:user_mailbox.message:modify` 修改邮件 `mail:user_mailbox.message:readonly` 查询用户邮件 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `user_mailbox_id` | `string` | 用户邮箱地址。当使用用户身份访问时，可以输入"me"代表当前调用接口用户<br>**示例值**："user@xxx.xx 或 me" |
| `label_id` | `string` | 标签ID，创建标签成功后返回的标签ID，或可通过列出标签、获取邮件详情等接口获得<br>**示例值**："7620003644728938013" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `label` | `label` | 标签 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 标签ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 标签名称，最长 255 个字符。支持嵌套标签，嵌套层级之间以 / 分隔（如 a/b/c 表示三级嵌套标签）。创建或更新嵌套标签时，需要传入完整路径（如 a/b/c），不能只传最后一级名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 标签背景颜色，支持以下颜色值：blue、indigo、purple、violet、carmine、red、orange、yellow、lime、green、turquoise、wathet |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `messages_unread` | `int` | 带有该标签的未读邮件数量 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "label": {
            "id": "7620003644728938013",
            "name": "test",
            "background_color": "blue",
            "messages_unread": 0
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1234000 | invalid params | 不合法的参数，请参考本文档检查输入的参数 |
| 500 | 1234017 | internal error | 服务器内部错误，请重试 |
| 403 | 1234030 | permission deny | 无权限访问，请检查申请的权限 |
| 400 | 1234013 | user mailbox not found or user mailbox not active | 指定邮箱地址不存在或状态不正确，请检查输入的邮箱地址 |
| 400 | 1230100 | label not found | 指定的标签不存在，请检查输入的标签 |


