---
title: "批量获取评论"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment/batch_query"
updateTime: "1744103612000"
---

# 批量获取评论

该接口用于根据评论 ID 列表批量获取云文档评论信息，包括评论和回复 ID、回复的内容、评论人和回复人的用户 ID 等。支持返回全局评论以及局部评论（可通过 is_whole 字段区分）。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/drive/v1/files/:file_token/comments/batch_query |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `docs:document.comment:read` 获取云文档中的评论 `drive:drive` 查看、评论、编辑和管理云空间中所有文件 `drive:drive:readonly` 查看、评论和下载云空间中所有文件 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `file_token` | `string` | 文档 Token<br>**示例值**："doxbcdl03Vsxhm7Qmnj110abcef" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `file_type` | `string` | 是 | 云文档类型<br>**示例值**：docx<br>**可选值有**：<br>- `doc`: 旧版文档类型，已不推荐使用 - `docx`: 新版文档类型 - `sheet`: 电子表格类型 - `file`: 文件类型 - `slides`: 幻灯片 |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `comment_ids` | `string\[\]` | 是 | 需要获取数据的评论 ID ，可通过调用获取云文档所有评论接口获取 comment_id<br>**示例值**：["1654857036541812356"] |


### 请求体示例

```json
{
    "comment_ids": [
        "1654857036541812356"
    ]
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `file.comment\[\]` | 评论的相关信息、回复的信息、回复分页的信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `comment_id` | `string` | 评论 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `int` | 创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `update_time` | `int` | 更新时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_solved` | `boolean` | 是否已解决 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `solved_time` | `int` | 解决评论时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `solver_user_id` | `string` | 解决评论者的用户 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `has_more` | `boolean` | 是否有更多回复 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `page_token` | `string` | 回复分页标记 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole` | `boolean` | 是否是全文评论 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `quote` | `string` | 局部评论的引用字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `reply_list` | `reply_list` | 评论里的回复列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `replies` | `file.comment.reply\[\]` | 回复列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `reply_content` | 回复内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `reply_element\[\]` | 回复的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 回复的内容元素<br>**可选值有**：<br>- `text_run`: 普通文本 - `docs_link`: at 云文档链接 - `person`: at 联系人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text` | `string` | 回复 普通文本 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `docs_link` | `docs_link` | 添加云文档链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 回复 at 云文档 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `person` | `person` | 添加用户的 user_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 添加用户的 user_id 以@用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reply_id` | `string` | 回复 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `int` | 创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `update_time` | `int` | 更新时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `extra` | `reply_extra` | 回复的其他内容，图片 Token 等 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `image_list` | `string\[\]` | 评论中的图片 Token list |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "comment_id": "6916106822734512356",
                "user_id": "ou_cc19b2bfb93f8a44db4b4d6eababcef",
                "create_time": 1610281603,
                "update_time": 1610281603,
                "is_solved": false,
                "solved_time": 1610281603,
                "solver_user_id": "null",
                "has_more": false,
                "page_token": "6916106822734512356",
                "is_whole": true,
                "quote": "划词评论引用内容",
                "reply_list": {
                    "replies": [
                        {
                            "content": {
                                "elements": [
                                    {
                                        "type": "text_run",
                                        "text_run": {
                                            "text": "comment text"
                                        },
                                        "docs_link": {
                                            "url": "https://example.feishu.cn/docs/doccnHh7U87HOFpii5u5Gabcef"
                                        },
                                        "person": {
                                            "user_id": "ou_cc19b2bfb93f8a44db4b4d6eababcef"
                                        }
                                    }
                                ]
                            },
                            "reply_id": "6916106822734512356",
                            "user_id": "ou_cc19b2bfb93f8a44db4b4d6eab2abcef",
                            "create_time": 1610281603,
                            "update_time": 1610281603,
                            "extra": {
                                "image_list": [
                                    "xfsfseewewabcef"
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1069301 | fail | 重试，若稳定失败请联系相关业务方oncall人员 |
| 400 | 1069302 | param error | 检查参数有效性 |
| 403 | 1069303 | forbidden | 检查是否有待评论云文档的评论权限 |
| 400 | 1069304 | docs had been deleted | 检查待评论云文档是否已被删除 |
| 400 | 1069305 | docs not exist | 检查待评论云文档是否能正常访问 |
| 400 | 1069306 | content review not pass | 排查评论内容是否存在不合法内容 |
| 404 | 1069307 | not exist | 检查待评论云文档是否能正常访问、检查评论内容at人或云文档是否存在 |
| 400 | 1069308 | exceeded limit | 评论数据超过上限限制，详情请咨询客服 |
| 400 | 1069399 | internal error | 重试，若稳定失败请联系相关业务方oncall人员 |
| 400 | 1064230 | locked for data migration | 数据迁移中，暂时无法上传。 |


