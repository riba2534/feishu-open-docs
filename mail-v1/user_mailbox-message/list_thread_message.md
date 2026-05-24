---
title: "查询会话下邮件信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/user_mailbox-message/list_thread_message"
updateTime: "1776073471000"
---

# 查询会话邮件信息

通过用户邮箱地址和邮件会话ID，获取该会话下的所有邮件关键信息列表。


> **Tip**: 使用应用身份访问时，需要申请邮件数据资源的数据权限。如需查询主题、正文、摘要、收发件人信息，请申请字段权限。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/user_mailboxes/:user_mailbox_id/threads/:thread_id/messages |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `mail:user_mailbox.message:readonly` 查询用户邮件 |
| 字段权限要求 | &gt; **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `mail:user_mailbox.message.address:read` 获取邮件内容中地址相关字段 `mail:user_mailbox.message.body:read` 获取邮件正文 `mail:user_mailbox.message.subject:read` 获取邮件主题 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `user_mailbox_id` | `string` | 用户邮箱地址。当使用用户身份访问时，可以输入"me"代表当前调用接口用户<br>**示例值**："user@xxx.xx 或 me" |
| `thread_id` | `string` | 邮件会话ID。可通过发送邮件、回复邮件的接口返回值或获取邮件详情接口查询获得。<br>**示例值**："xxxxxxxxxxxx" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `format` | `string` | 否 | 需要获取的邮件内容<br>**示例值**：full<br>**可选值有**：<br>- `full`: 全文，包括标签、文件夹、主题、收发件人、纯文本、HTML等信息 - `plain_text_full`: 全文，只返回纯文本正文内容，不返回HTML。返回内容包括标签、文件夹、主题、收发件人、纯文本等信息 - `metadata`: 邮件元数据信息，包括标签、文件夹、主题、收发件人、摘要等信息，不返回正文内容 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `message_meta\[\]` | 邮件元数据列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `message_id` | `string` | 邮件的唯一标识符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `thread_id` | `string` | 邮件所属会话的唯一标识符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `folder_id` | `string` | 邮件所属文件夹的ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `smtp_message_id` | `string` | SMTP协议中使用的邮件ID（符合RFC 2822标准） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `internal_date` | `string` | 创建/收/发信时间（毫秒） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `message_state` | `int` | 邮件状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `message` | `message` | 使用format参数后返回的邮件内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `raw` | `string` | MIME邮件数据，基于base64url编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `subject` | `string` | 主题<br>**字段权限要求**： `mail:user_mailbox.message.subject:read` 获取邮件主题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `to` | `mail_address\[\]` | 收件人<br>**字段权限要求**： `mail:user_mailbox.message.address:read` 获取邮件内容中地址相关字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mail_address` | `string` | 邮件地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cc` | `mail_address\[\]` | 抄送<br>**字段权限要求**： `mail:user_mailbox.message.address:read` 获取邮件内容中地址相关字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mail_address` | `string` | 邮件地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bcc` | `mail_address\[\]` | 密送<br>**字段权限要求**： `mail:user_mailbox.message.address:read` 获取邮件内容中地址相关字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mail_address` | `string` | 邮件地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `head_from` | `mail_address` | 发件人<br>**字段权限要求**： `mail:user_mailbox.message.address:read` 获取邮件内容中地址相关字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mail_address` | `string` | 邮件地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `body_html` | `string` | 正文(base64url)<br>**字段权限要求**： `mail:user_mailbox.message.body:read` 获取邮件正文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `internal_date` | `string` | 创建/收/发信时间（毫秒） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `message_state` | `int` | 邮件状态，1（收信）2（发信）3（草稿） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `smtp_message_id` | `string` | RFC协议id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `message_id` | `string` | 邮件id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `attachments` | `attachment\[\]` | 邮件附件列表<br>**字段权限要求**： `mail:user_mailbox.message.body:read` 获取邮件正文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `body` | `string` | 附件的正文，使用 base64url 编码（支持的文件最大 37MB） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `filename` | `string` | 附件文件名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 附件 id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `attachment_type` | `int` | 附件类型<br>**可选值有**：<br>- `1`: 普通附件 - `2`: 超大附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_inline` | `boolean` | 是否为内联图片，true 表示是内联图片 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cid` | `string` | 内容 ID，HTML 中通过 cid: 协议引用该图片 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `body_plain_text` | `string` | 正文纯文本(base64url)<br>**字段权限要求**： `mail:user_mailbox.message.body:read` 获取邮件正文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `thread_id` | `string` | 会话id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `body_preview` | `string` | 邮件正文纯文本内容的前100个字符，基于base64url编码，用于快速预览邮件核心内容，无需解码完整正文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `label_ids` | `string\[\]` | 标签ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folder_id` | `string` | 文件夹ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `in_reply_to` | `string` | In-Reply-To邮件头 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reply_to` | `string` | Reply-To邮件头 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `priority_type` | `string` | 邮件优先级<br>**可选值有**：<br>- `0`: 无优先级 - `1`: 高优先级 - `3`: 正常优先级 - `5`: 低优先级 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `security_level` | `security_level` | 安全信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_risk` | `boolean` | 是否风险邮件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `risk_banner_level` | `string` | 风险邮件等级<br>**可选值有**：<br>- `WARNING`: 警告 - `DANGER`: 危险 - `INFO`: 提示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `risk_banner_reason` | `string` | 风险邮件原因<br>**可选值有**：<br>- `NO_REASON`: 未知 - `IMPERSONATE_DOMAIN`: 相似域名仿冒 - `IMPERSONATE_KP_NAME`: KP姓名仿冒 - `UNAUTH_EXTERNAL`: 未认证外部域名 - `MALICIOUS_URL`: 恶意链接 - `MALICIOUS_ATTACHMENT`: 高危附件 - `PHISHING`: 钓鱼邮件 - `IMPERSONATE_PARTNER`: 仿冒合作伙伴 - `EXTERNAL_ENCRYPTION_ATTACHMENT`: 外部邮件携带加密附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_header_from_external` | `boolean` | 发件人是否外部邮件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `via_domain` | `string` | 代发或伪造邮件展示SPF或DKIM域名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `spam_banner_type` | `string` | 垃圾邮件原因<br>**可选值有**：<br>- `USER_REPORT`: 用户曾标记邮件是垃圾邮件 - `USER_BLOCK`: 用户曾将发件人的邮件标记为垃圾邮件 - `ANTI_SPAM`: 系统判为垃圾邮件 - `USER_RULE`: 命中收信规则进入垃圾邮件 - `BLOCK_DOMIN`: 用户已拦截来自该域名的邮件 - `BLOCK_ADDRESS`: 用户已拦截来自该邮件地址的邮件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `spam_user_rule_id` | `string` | 命中的收信规则ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `spam_banner_info` | `string` | 命中用户黑名单的地址或域名信息 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "message_id": "xxx",
                "thread_id": "xxx",
                "folder_id": "INBOX",
                "smtp_message_id": "123456@example.com",
                "internal_date": "1651234567890",
                "message_state": 1,
                "message": {
                    "raw": "Q29udGVudC1UeXBlOiB0ZXh0L3BsYWluOyBjaGFyc2V0PSJ1cy1hc2NpaSIKTUlNRS1WZXJzaW9uOiAxLjAKQ29udGVudC1UcmFuc2Zlci1FbmNvZGluZzogN2JpdAp0bzogInRvIiA8dG9AeHh4Lnh4Pgpmcm9tOiAiZnJvbSIgPGZyb21AeHh4Lnh4PgpzdWJqZWN0OiB0aGlzIGlzIGEgc3ViamVjdAoKdGhpcyBpcyB0aGUgbWVzc2FnZSBib2R5Lg",
                    "subject": "邮件标题",
                    "to": [
                        {
                            "mail_address": "mike@outlook.com",
                            "name": "Mike"
                        }
                    ],
                    "cc": [
                        {
                            "mail_address": "mike@outlook.com",
                            "name": "Mike"
                        }
                    ],
                    "bcc": [
                        {
                            "mail_address": "mike@outlook.com",
                            "name": "Mike"
                        }
                    ],
                    "head_from": {
                        "mail_address": "mike@outlook.com",
                        "name": "Mike"
                    },
                    "body_html": "xxxx",
                    "internal_date": "1682377086000",
                    "message_state": 1,
                    "smtp_message_id": "ay0azrJDvbs3FJAg@outlook.com",
                    "message_id": "tfuh9N4WnzU6jdDw=",
                    "attachments": [
                        {
                            "body": "aGVsbG8gd29ybGQK",
                            "filename": "helloworld.txt",
                            "id": "YQqYbQHoQoDqXjxWKhJbo8Gicjf",
                            "attachment_type": 1,
                            "is_inline": false,
                            "cid": "image1@example.com"
                        }
                    ],
                    "body_plain_text": "xxxxx",
                    "thread_id": "tfuh9N4WnzU6jdDw=",
                    "body_preview": "xxxxx",
                    "label_ids": [
                        "FLAGGED"
                    ],
                    "folder_id": "INBOX",
                    "in_reply_to": "06d20.dbf451a3.808a.475a.acc9.1363dfd20f36@larksuite.com",
                    "reply_to": "06d20.dbf451a3.808a.475a.acc9.1363dfd20f36@larksuite.com",
                    "priority_type": "0",
                    "security_level": {
                        "is_risk": false,
                        "risk_banner_level": "WARNING",
                        "risk_banner_reason": "IMPERSONATE_DOMAIN",
                        "is_header_from_external": false,
                        "via_domain": "larksuite.com",
                        "spam_banner_type": "USER_REPORT",
                        "spam_user_rule_id": "7618365627924925388",
                        "spam_banner_info": "larksuite.com"
                    }
                }
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 404 | 1234013 | user mailbox not found or user mailbox not active | 用户邮箱地址不存在，请检查输入的用户邮箱地址是否正确，或确认用户的邮箱处于正常状态 |
| 403 | 1234017 | permission deny | 无权限访问，请确认应用是否具备访问该资源的权限。如使用用户身份访问，请确认具备此用户的访问权限；如使用租户身份访问，请确认已申请对应的数据范围权限。 |
| 400 | 1234008 | request parameter error | 根据提示信息，检查请求参数是否正确 |
| 500 | 1236019 | internal server error | 服务器内部错误，请稍后重试 |
| 404 | 1236022 | mail thread not found | 检查会话ID是否正确 |


