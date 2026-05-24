---
title: "列出邮件模板"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/user_mailbox-template/list"
updateTime: "1778067811000"
---

# 列出个人邮件模板

列出指定用户邮箱下的全部个人邮件模板基本信息（一次性返回，不分页），常用于在编辑或发送邮件场景下展示可选模板列表。如需获取模板正文与附件等完整字段，请通过获取个人邮件模板详情接口按 `template_id` 查询。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/user_mailboxes/:user_mailbox_id/templates |
| HTTP Method | GET |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `mail:user_mailbox.message:modify` 修改邮件 `mail:user_mailbox.message:readonly` 查询用户邮件 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `user_mailbox_id` | `string` | 用户邮箱地址，作为用户邮箱身份标识。使用 user_access_token 调用时，可使用占位符 `me` 表示当前授权用户的主邮箱。<br>**示例值**："user@example.com" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `\-\[\]` | 个人邮件模板列表。每个模板对象仅填充以下字段；如需获取完整模板内容，请通过获取个人邮件模板详情接口按 `template_id` 查询。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `template_id` | `string` | 模板 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 模板名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 模板创建时间（毫秒级时间戳字符串） |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "template_id": "7281187859195772947",
                "name": "销售跟进模板",
                "create_time": "1716279320000"
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1230001 | param invalid | 请根据错误信息「param invalid」核查请求参数后重试。 |
| 500 | 1230003 | internal server error | 服务端异常（1230003 internal server error）。可稍后重试，或携带 request id 联系接口负责人。 |
| 403 | 1230002 | permission deny | 权限不足（1230002 permission deny）。请确认 access_token 已开通该接口所需的 scope。 |


