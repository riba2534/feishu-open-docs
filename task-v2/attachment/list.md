---
title: "列取附件"
fullPath: "/uAjLw4CM/ukTMukTMukTM/task-v2/attachment/list"
updateTime: "1699248308000"
---

# 列取附件

列取一个资源的所有附件。返回的附件列表支持分页，按照附件上传时间排序。

每个附件会返回一个可供下载的临时url，有效期为3分钟，最多可以支持3次下载。如果超过使用限制，需要通过本接口获取新的临时url。


> **Tip**: 获取任务的附件列表，需要该任务的读取权限。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/task/v2/attachments |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `task:attachment:read` 查看任务附件 `task:attachment:write` 查看、创建、删除任务附件 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 分页大小<br>**示例值**：50<br>**默认值**：`50`<br>**数据校验规则**：<br>- 取值范围：`1` ～ `100` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：aWQ9NzEwMjMzMjMxMDE= |
| `resource_type` | `string` | 否 | 附件归属的资源类型。目前只支持"task"。<br>**示例值**：task<br>**默认值**：`task` |
| `resource_id` | `string` | 是 | 附件归属资源的id，配合resource_type使用。例如希望获取任务的附件，需要设置 resource_type为task， resource_id为任务GUID。任务GUID的获取方式可以参考[任务功能概述](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/task/overview)。<br>**示例值**：9842501a-9f47-4ff5-a622-d319eeecb97f |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**默认值**：`open_id` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `attachment\[\]` | 附件列表 |
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
| &nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 附件的临时下载url，有效时间3分钟，且只允许调用3次进行附件下载。 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
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
        ],
        "page_token": "aWQ9NzEwMjMzMjMxMDE=",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1470400 | 请求参数有误 | 查看返回的请求体中的`msg`确定具体原因。 |
| 404 | 1470404 | 要查询附件的资源不存在或已删除。 | 确认要查询资源是否还存在。 |
| 500 | 1470500 | 服务器错误。 | 使用同样请求重试调用接口。如果持续返回错误，可以联系技术支持排查问题。 |
| 403 | 1470403 | 缺少列取附件的权限。 | 确认调用身份拥有列取附件列表的权限。 |


