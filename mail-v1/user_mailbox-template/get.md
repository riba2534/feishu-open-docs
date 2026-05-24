---
title: "获取邮件模板"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/user_mailbox-template/get"
updateTime: "1778067830000"
---

# 获取个人邮件模板详情

获取指定邮件模板的完整详情，包括模板名称、主题、正文（HTML 或纯文本）、收件人/抄送/密送地址、附件信息等所有字段。常用于编辑模板前回填表单，或在发送邮件场景下读取模板内容做二次填充。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/user_mailboxes/:user_mailbox_id/templates/:template_id |
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
| `template_id` | `string` | 邮件模板 ID。可通过列出个人邮件模板接口或创建个人邮件模板接口的返回值获取。<br>**示例值**："7281187859195772947" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `template` | `template` | 模板详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `template_id` | `string` | 模板 id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 模板名称，不超过 100 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `subject` | `string` | 邮件主题，不超过 1000 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `template_content` | `string` | 模板正文（HTML 或纯文本）。单模板正文大小上限 3 MB（3 \* 1024 \* 1024 字节），超过将返回错误码 1230006 template content size limit exceeded。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_plain_text_mode` | `boolean` | 是否为纯文本模式。`true` 表示模板正文按纯文本渲染，`false` 表示按 HTML 渲染。默认 `false`（HTML 模式）。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tos` | `mail_address\[\]` | 默认收件人地址列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mail_address` | `string` | 邮件地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ccs` | `mail_address\[\]` | 默认抄送地址列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mail_address` | `string` | 邮件地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `bccs` | `mail_address\[\]` | 默认密送地址列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mail_address` | `string` | 邮件地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `attachments` | `template_attachment\[\]` | 模板附件与内嵌图片列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `filename` | `string` | 附件文件名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 附件 id（Drive file_key，用于引用 Drive medias 上传接口返回的 file_key） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `attachment_type` | `int` | 附件类型<br>**可选值有**：<br>- `1`: 普通附件 - `2`: 超大附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_inline` | `boolean` | 是否为内联图片，true 表示是内联图片 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cid` | `string` | 内容 ID，HTML 中通过 cid: 协议引用该图片 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 模板创建时间（毫秒级时间戳字符串，避免 JS 弱类型侧 i64 精度丢失） |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "template": {
            "template_id": "7281187859195772947",
            "name": "销售跟进模板",
            "subject": "关于本周订单跟进",
            "template_content": "Hi ${name},",
            "is_plain_text_mode": false,
            "tos": [
                {
                    "mail_address": "mike@outlook.com",
                    "name": "Mike"
                }
            ],
            "ccs": [
                {
                    "mail_address": "mike@outlook.com",
                    "name": "Mike"
                }
            ],
            "bccs": [
                {
                    "mail_address": "mike@outlook.com",
                    "name": "Mike"
                }
            ],
            "attachments": [
                {
                    "filename": "plan.xlsx",
                    "id": "boxcnrHpsg1QDqXPrJXWPwbqsKh",
                    "attachment_type": 1,
                    "is_inline": false,
                    "cid": "image1@example.com"
                }
            ],
            "create_time": "1716279320000"
        }
    }
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


