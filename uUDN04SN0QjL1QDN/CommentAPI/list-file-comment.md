---
title: "获取云文档所有评论"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment/list"
updateTime: "1744103612000"
---

# 获取云文档所有评论

该接口用于根据云文档 Token 分页获取文档所有评论信息，包括评论和回复 ID、回复的内容、评论人和回复人的用户 ID 等。该接口支持返回全局评论以及局部评论（可通过 is_whole 字段区分）。默认每页返回 50 个评论。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/drive/v1/files/:file_token/comments |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `docs:doc` 查看、评论、编辑和管理文档 `docs:doc:readonly` 查看、评论和导出文档 `docs:document.comment:read` 获取云文档中的评论 `drive:drive` 查看、评论、编辑和管理云空间中所有文件 `drive:drive:readonly` 查看、评论和下载云空间中所有文件 `sheets:spreadsheet` 查看、评论、编辑和管理电子表格 `sheets:spreadsheet:readonly` 查看、评论和导出电子表格 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `file_token` | `string` | 云文档的 token。获取方式参考 [如何获取云文档相关 token](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6)。<br>**示例值**："XIHSdYSI7oMEU1xrsnxc8fabcef" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `file_type` | `string` | 是 | 云文档类型<br>**示例值**：doc<br>**可选值有**：<br>- `doc`: 旧版文档类型，已不推荐使用 - `docx`: 新版文档类型 - `sheet`: 电子表格类型 - `file`: 文件类型 - `slides`: 幻灯片 |
| `is_whole` | `boolean` | 否 | 是否全文评论<br>**示例值**：false |
| `is_solved` | `boolean` | 否 | 是否已解决（可选）<br>**示例值**：false |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：7153511712153412356 |
| `page_size` | `int` | 否 | 分页大小，默认每页返回 50 个评论<br>**示例值**：10<br>**数据校验规则**：<br>- 最大值：`100` |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `items` | `file.comment\[\]` | 评论列表 |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 添加用户的 user_id 以@用户。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reply_id` | `string` | 回复 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `int` | 创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `update_time` | `int` | 更新时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `extra` | `reply_extra` | 回复的其他内容，图片 Token 等 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `image_list` | `string\[\]` | 评论中的图片 Token list。暂不支持通过接口下载图片。 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "has_more": true,
        "page_token": "6916106822734512356",
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
                            "reply_id": "6916106822734512356",
                            "user_id": "ou_cc19b2bfb93f8a44db4b4d6eab2abcef",
                            "create_time": 1610281603,
                            "update_time": 1610281603,
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
| 400 | 1069301 | fail | 重试，若稳定失败请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1069302 | param error | 检查参数有效性 |
| 403 | 1069303 | forbidden | 检查是否有待评论云文档的评论权限 |
| 400 | 1069308 | exceeded limit | 评论数据超过上限限制，详情请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1069304 | docs had been deleted | 检查待评论云文档是否已被删除 |
| 404 | 1069307 | not exist | 检查待评论云文档是否能正常访问、检查评论内容at人或云文档是否存在 |
| 400 | 1069399 | internal error | 重试，若稳定失败请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |


