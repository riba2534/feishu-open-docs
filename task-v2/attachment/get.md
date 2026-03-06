---
title: "获取附件"
fullPath: "/uAjLw4CM/ukTMukTMukTM/task-v2/attachment/get"
updateTime: "1699248329000"
---

# 获取附件

提供一个附件GUID，返回附件的详细信息，包括GUID，名称，大小，上传时间，临时可下载链接等。


> **Tip**: 获取附件需要附件归属资源的可读取权限。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/task/v2/attachments/:attachment_guid |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `task:attachment:read` 查看任务附件 `task:attachment:write` 查看、创建、删除任务附件 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `attachment_guid` | `string` | 获取详情的附件GUID。可以通过创建[上传附件](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/attachment/upload)接口创建, 或者通过[列取附件](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/attachment/list)接口查询得到。<br>**示例值**："b59aa7a3-e98c-4830-8273-cbb29f89b837" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**默认值**：`open_id` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `attachment` | `attachment` | 附件详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `guid` | `string` | 附件guid |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件在云文档系统中的token |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 附件名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `size` | `int` | 附件的字节大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `resource` | `resource` | 附件归属的资源 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 资源类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 资源ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `uploader` | `member` | 附件上传者 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 表示member的id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 成员的类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `role` | `string` | 成员角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_cover` | `boolean` | 是否是封面图 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `uploaded_at` | `string` | 上传时间戳(ms) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 附件的临时下载url，有效时间3分钟，且只允许调用3次进行附件下载。只有在获取附件时会动态生成。 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "attachment": {
            "guid": "f860de3e-6881-4ddd-9321-070f36d1af0b",
            "file_token": "boxcnTDqPaRA6JbYnzQsZ2doB2b",
            "name": "foo.jpg",
            "size": 62232,
            "resource": {
                "type": "task",
                "id": "e6e37dcc-f75a-5936-f589-12fb4b5c80c2"
            },
            "uploader": {
                "id": "ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f",
                "type": "user",
                "role": "editor"
            },
            "is_cover": false,
            "uploaded_at": "1675742789470",
            "url": "https://example.com/download/authcode/?code=OWMzNDlmMjJmZThkYzZkZGJlMjYwZTI0OTUxZTE2MDJfMDZmZmMwOWVj"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1470400 | 请求参数有误。 | 查看返回中的`msg`确定具体原因。 |
| 404 | 1470404 | 附件不存在或已删除。 | 确认附件是否还存在。 |
| 500 | 1470500 | 服务器错误。 | 使用同样请求重试调用接口。如果持续返回错误，可以联系技术支持排查问题。 |
| 403 | 1470403 | 缺少获取附件的权限。 | 确认调用身份拥有获取附件的权限。 |


