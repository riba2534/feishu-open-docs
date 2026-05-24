---
title: "获取模板附件下载链接"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/user_mailbox-template/download_url"
updateTime: "1778067772000"
---

# 获取模板附件下载链接

获取指定邮件模板下的附件下载链接。用于在已知模板 ID 与附件 ID 的场景下，二次获取附件的有效访问 URL，便于在用户端预览或下载邮件模板中的附件资源。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/user_mailboxes/:user_mailbox_id/templates/:template_id/attachments/download_url |
| HTTP Method | GET |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `mail:user_mailbox.message:readonly` 查询用户邮件 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `user_mailbox_id` | `string` | 用户邮箱地址，作为用户邮箱身份标识。使用 user_access_token 调用时，可使用占位符 `me` 表示当前授权用户的主邮箱。<br>**示例值**："user@example.com" |
| `template_id` | `string` | 邮件模板 ID。可通过列出个人邮件模板接口或创建个人邮件模板接口的返回值获取。<br>**示例值**："7281187859195772947" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `attachment_ids` | `string\[\]` | 是 | 待获取下载链接的附件 ID 列表。可通过获取个人邮件模板详情接口返回的 attachments 字段中的 id 获取。<br>**示例值**：YQqYbQHoQoDqXjxWKhJbo8Gicjf<br>**数据校验规则**：<br>- 长度范围：`1` ～ `20` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `download_urls` | `attachment_download_url_item\[\]` | 下载链接列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `attachment_id` | `string` | 附件 id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `download_url` | `string` | 下载链接 |
| &nbsp;&nbsp;└ `failed_reasons` | `attachment_download_failed_reason\[\]` | 附件下载链接获取失败原因列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `attachment_id` | `string` | 附件 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `reason` | `string` | 失败原因 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "download_urls": [
            {
                "attachment_id": "YQqYbQHoQoDqXjxWKhJbo8Gicjf",
                "download_url": "https://api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTZiZGViMDg3NzRjMzEwOWRkMGI1MTJlYmQxYTFmYTBfZTA5ZjZiOWU4NDYzMzkxMDUyOTIxMzBmNTVjMjAyZTFfSUQ6NzI4MTE4Nzg1OTE5NTc3Mjk0N18xNjk1ODg4NjQyOjE2OTU4ODg3MDJfVjM"
            }
        ],
        "failed_reasons": [
            {
                "attachment_id": "YQqYbQHoQoDqXjxWKhJbo8Gicjf",
                "reason": "attachment_not_found"
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
| 404 | 1230007 | template not found | 资源不存在（1230007 template not found）。请核对路径参数是否指向真实存在的资源。 |
| 404 | 1230010 | template attachment not found | 资源不存在（1230010 template attachment not found）。请核对路径参数是否指向真实存在的资源。 |
| 403 | 1230011 | template attachment forbidden | 权限不足（1230011 template attachment forbidden）。请确认 access_token 已开通该接口所需的 scope。 |


