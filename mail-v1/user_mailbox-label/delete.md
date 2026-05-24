---
title: "删除标签"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/user_mailbox-label/delete"
updateTime: "1776073274000"
---

# 删除标签

删除用户指定的标签


> **Warning**: 注意，删除的标签无法恢复


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/user_mailboxes/:user_mailbox_id/labels/:label_id |
| HTTP Method | DELETE |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `mail:user_mailbox.message:modify` 修改邮件 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `user_mailbox_id` | `string` | 用户邮箱地址，当使用user_access_token访问时，可以填写me<br>**示例值**："user@xxx.xx 或 me" |
| `label_id` | `string` | 标签ID，创建标签成功后返回的标签ID，或可通过列出标签、获取邮件详情等接口获得<br>**示例值**："7620003644728938013" |


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
| 400 | 1234000 | invalid params | 不合法的参数，请根据本文档检查参数 |
| 500 | 1234017 | internal error | 服务器内部错误，请稍后重试 |
| 403 | 1234030 | permission deny | 无权限访问，请检查申请的权限状态 |
| 400 | 1234013 | user mailbox not found or user mailbox not active | 指定邮箱地址不存在或邮箱状态不正确，请检查输入的邮箱地址 |
| 400 | 1230100 | label not found | 指定的标签不存在，请检查输入的标签是否正确 |


