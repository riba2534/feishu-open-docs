---
title: "获取 Aily 消息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/aily-v1/aily_session-aily_message/get"
updateTime: "1752154940000"
---

# 获取 Aily 消息

该 API 用于获取某个飞书 Aily 应用的消息（Message）的详细信息；包括消息的内容、发送人等。


> **Tip**: 更多信息及示例代码，可参考 [Aily OpenAPI 接入与接口说明](https://bytedance.larkoffice.com/wiki/UTU6wVTVGigefykjO1acAOOvnNc)。


## 实体概念说明

- **会话**（Session）：管理用户与 Aily 助手之间的交互会话；每次会话记录了用户发送给 Aily 助手的消息以及 Aily 助手的响应。
- **消息**（Message）：消息可以包含文本、表格、图片等多种类型的内容。
- **运行**（Run）：Aily 助手基于会话内消息进行意图判定、调用匹配的技能，并返回技能执行后的结果消息。

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/aily/v1/sessions/:aily_session_id/messages/:aily_message_id |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `aily:message:read` 获取消息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `aily_session_id` | `string` | 会话 ID；参考 [创建会话](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/aily-v1/aily_session/create) 接口<br>**示例值**："session_4dfunz7sp1g8m"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `32` 字符 - 正则校验：`session_[0-9a-hjkmnp-z]{1,24}` |
| `aily_message_id` | `string` | 消息 ID<br>**示例值**："message_4df45f2xknvcc"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `32` 字符 - 正则校验：`message_[0-9a-hjkmnp-z]{1,24}` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `message` | `aily_message` | 消息信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 消息 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `session_id` | `string` | 会话 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `run_id` | `string` | 运行 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 消息内容类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 消息内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `files` | `aily_message_file\[\]` | 消息中包含的文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 文件 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mime_type` | `string` | 文件类型，参见[MIME 类型（IANA 媒体类型）](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Basics_of_HTTP/MIME_types) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 文件名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `metadata` | `string` | 其他透传信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `string` | 文件的创建时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `preview_url` | `aily_message_file_preview` | 文件预览链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 文件的 URL |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expired_at` | `string` | url 过期时间，秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `quote_message_id` | `string` | 引用的消息 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sender` | `aily_sender` | 发送者 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `entity_id` | `string` | 实体 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `identity_provider` | `string` | 身份提供者 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sender_type` | `string` | 发送人类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `aily_id` | `string` | 飞书智能伙伴创建平台账号体系下的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `mentions` | `aily_mention\[\]` | 被@的实体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `entity_id` | `string` | 实体 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `identity_provider` | `string` | 身份提供者 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 被@实体在消息体中的占位符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 被@实体的名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `aily_id` | `string` | 飞书智能伙伴创建平台账号体系下的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `plain_text` | `string` | 消息体的纯文本表达 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `string` | 消息的创建时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `string` | 状态 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "message": {
            "id": "message_4df45f2xknvcc",
            "session_id": "session_4dfunz7sp1g8m",
            "run_id": "run_4dfrxvctjqzzj",
            "content_type": "MDX",
            "content": "你好",
            "files": [
                {
                    "id": "file_4d9nu1ev3a2rq",
                    "mime_type": "image/png",
                    "file_name": "发票.png",
                    "metadata": "{}",
                    "created_at": "1711975665710",
                    "preview_url": {
                        "url": "http://path_to_file",
                        "expired_at": "1719413169"
                    }
                }
            ],
            "quote_message_id": "message_4de9bpg70qskh",
            "sender": {
                "entity_id": "ou_5ad573a6411d72b8305fda3a9c15c70e",
                "identity_provider": "FEISHU",
                "sender_type": "USER",
                "aily_id": "1794840334557292"
            },
            "mentions": [
                {
                    "entity_id": "ou_5ad573a6411d72b8305fda3a9c15c70e",
                    "identity_provider": "FEISHU",
                    "key": "@_user_1",
                    "name": "张三",
                    "aily_id": "1794840334557292"
                }
            ],
            "plain_text": "你好",
            "created_at": "1711975665710",
            "status": "COMPLETED"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2700001 | param is invalid | 参数错误 |


