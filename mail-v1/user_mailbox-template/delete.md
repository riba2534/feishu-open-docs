---
title: "删除邮件模板"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/user_mailbox-template/delete"
updateTime: "1778067869000"
---

# 删除邮件模板

永久删除指定用户邮箱下的某个个人邮件模板。删除操作不可恢复，删除后该模板将无法在「列出邮件模板」「获取邮件模板」等接口中再返回，常用于清理已废弃或不再使用的模板。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/user_mailboxes/:user_mailbox_id/templates/:template_id |
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
| `user_mailbox_id` | `string` | 用户邮箱地址，作为用户邮箱身份标识。使用 user_access_token 调用时，可使用占位符 `me` 表示当前授权用户的主邮箱。<br>**示例值**："user@example.com" |
| `template_id` | `string` | 邮件模板 ID。可通过列出个人邮件模板接口或创建个人邮件模板接口的返回值获取。<br>**示例值**："7281187859195772947" |


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
| 400 | 1230001 | param invalid | 请根据错误信息「param invalid」核查请求参数后重试。 |
| 500 | 1230003 | internal server error | 服务端异常（1230003 internal server error）。可稍后重试，或携带 request id 联系接口负责人。 |
| 403 | 1230002 | permission deny | 权限不足（1230002 permission deny）。请确认 access_token 已开通该接口所需的 scope。 |
| 404 | 1230007 | template not found | 资源不存在（1230007 template not found）。请核对路径参数是否指向真实存在的资源。 |
| 400 | 1230009 | invalid template param | 请根据错误信息「invalid template param」核查请求参数后重试。 |


