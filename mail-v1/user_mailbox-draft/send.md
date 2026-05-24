---
title: "发送草稿"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/user_mailbox-draft/send"
updateTime: "1776073305000"
---

# 发送草稿

将指定的草稿发送出去


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/user_mailboxes/:user_mailbox_id/drafts/:draft_id/send |
| HTTP Method | POST |
| 接口频率限制 | [20 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `mail:user_mailbox.message:send` 发送用户邮件 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `user_mailbox_id` | `string` | 用户邮箱地址。当使用用户身份访问时，可以输入"me"代表当前调用接口用户<br>**示例值**："aba@aac.com" |
| `draft_id` | `string` | 草稿ID，可通过创建草稿、更新草稿或列出草稿列表接口获得<br>**示例值**："268dce11-85f7-427d-8756-6be3abc850fd" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `message_id` | `string` | 发送后生成的已发送邮件ID |
| &nbsp;&nbsp;└ `thread_id` | `string` | 邮件所属会话ID |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "message_id": "xxxx",
        "thread_id": "xxxx"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1234008 | request parameter error | 参数错误，请检查请求参数的类型、格式或值是否与接口要求一致，具体可参考接口文档中的参数说明 |
| 400 | 1236003 | the number of recipients exceeds the limit | 收件人数量超过限制，请减少收件人后重试 |
| 400 | 1236004 | the number of attachments exceeds the limit | 附件数量超过限制，请减少附件数量后重试 |
| 400 | 1236014 | content risk | 草稿存在风险内容，请检查草稿中的内容是否包含违规信息（如敏感词、违法内容等），修改后重新提交 |
| 400 | 1236017 | sender check fail | 邮件发件人检查失败，请检查发件人信息和状态 |
| 400 | 1236018 | receiver check fail | 邮件收件人检查失败，请检查收件人信息 |
| 403 | 1234017 | permission deny | 无权限访问，请确认应用是否具备访问该资源的权限。如使用用户身份访问，请确认具备此用户的访问权限；如使用租户身份访问，请确认已申请对应的数据范围权限。 |
| 404 | 1234050 | draft not found | 指定草稿不存在，请核对草稿ID，或重新创建草稿 |
| 404 | 1234013 | user mailbox not found or user mailbox not active | 用户邮箱地址不存在，请检查输入的用户邮箱地址是否正确，或确认用户的邮箱处于正常状态 |
| 409 | 1236005 | send mail repeatedly | 邮件已发送成功，请勿重复发送邮件 |
| 429 | 1236006 | Concurrent write conflict. Please retry later | 同用户请勿并发请求 |
| 429 | 1236007 | the daily number of emails sent by the user exceeds the limit | 触达用户每日发信数量上限，请联系管理员提升限额后重试 |
| 429 | 1236008 | the number of external recipients the user sends messages to each day exceeds the limit | 用户每天发送邮件的外部收件人数量超过限制，请联系管理员提升限额后重试 |
| 429 | 1236009 | the number of external recipients the tenant sends messages to each day exceeds the limit | 企业每天发送邮件的外部收件人数量超过限制，请联系管理员提升限额后重试 |
| 429 | 1236010 | mail quota limit | 用户的发信请求被系统限流，请重试 |
| 429 | 1236013 | tenant storage limit | 租户存储空间已满，无法发送更多邮件，联系管理员提升空间后重试 |
| 500 | 1236019 | internal server error | 内部服务错误，请重试 |


