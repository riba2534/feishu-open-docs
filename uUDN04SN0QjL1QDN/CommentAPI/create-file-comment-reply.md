---
title: "添加回复"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/create"
updateTime: "1775548666000"
---

# 添加回复

使用该接口可对云文档中的某条评论进行回复，回复内容支持普通文本、云文档链接等。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/drive/v1/files/:file_token/comments/:comment_id/replies |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `docs:doc` 查看、评论、编辑和管理文档 `docs:doc:readonly` 查看、评论和导出文档 `docs:document.comment:create` 添加、回复云文档中的评论 `drive:drive` 查看、评论、编辑和管理云空间中所有文件 `drive:drive:readonly` 查看、评论和下载云空间中所有文件 `sheets:spreadsheet` 查看、评论、编辑和管理电子表格 `sheets:spreadsheet:readonly` 查看、评论和导出电子表格 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `file_token` | `string` | 文档token<br>可以通过浏览器该文档的 URL 栏上直接获取文档 Token 。<br>**示例值**："TLLKdcpDro9ijQxA33ycNMabcef" |
| `comment_id` | `string` | 评论ID<br>在 添加评论、获取评论 等接口中有返回。<br>**示例值**："69161068xxxxx512356" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `file_type` | `string` | 是 | 云文档类型<br>**示例值**：doc<br>**可选值有**：<br>- `doc`: 文档 - `sheet`: 表格 - `file`: 文件 - `docx`: 新版文档 |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `content` | `reply_content` | 是 | 回复内容 |
| &nbsp;&nbsp;└ `elements` | `reply_element\[\]` | 是 | 回复内容的元素列表。最大元素个数为100 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 是 | 回复内容的元素类型。同时传入多个子参数时，仅与 type 取值匹配的参数生效，其他忽略<br>**示例值**："docs_link"<br>**可选值有**：<br>- `text_run`: 普通文本 - `docs_link`: at 云文档链接 - `person`: at 联系人 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 否 | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text` | `string` | 是 | 回复 普通文本<br>type为“text_run”时，此项必填。最大长度 10000字符<br>**示例值**："reply text" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `docs_link` | `docs_link` | 否 | 云文档链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 是 | 回复 at 云文档<br>type为“docs_link”时，此项必填<br>**示例值**："https://example.feishu.cn/docs/doccnHh7U87HOFpii5u5Gabcef" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `person` | `person` | 否 | 联系人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 是 | 回复 at 联系人<br>type为“person”时，此项必填。类型需与查询参数 user_id_type 的取值一致<br>**示例值**："ou_cc19b2bfb93f8a44db4b4d6eababcef" |


### 请求体示例

```json
{
    "content": {
        "elements": [
            {
                "type": "docs_link",
                "text_run": {
                    "text": "reply text"
                },
                "docs_link": {
                    "url": "https://example.feishu.cn/docs/doccnHh7U87HOFpii5u5Gabcef"
                },
                "person": {
                    "user_id": "ou_cc19b2bfb93f8a44db4b4d6eababcef"
                }
            }
        ]
    }
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `file.comment.reply` | \- |
| &nbsp;&nbsp;└ `content` | `reply_content` | 回复内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `reply_element\[\]` | 回复内容的元素列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 回复内容的元素类型<br>**可选值有**：<br>- `text_run`: 普通文本 - `docs_link`: at 云文档链接 - `person`: at 联系人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text` | `string` | 回复 普通文本 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `docs_link` | `docs_link` | 云文档链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 回复 at 云文档 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `person` | `person` | 联系人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 回复 at 联系人 |
| &nbsp;&nbsp;└ `reply_id` | `string` | 回复 ID |
| &nbsp;&nbsp;└ `user_id` | `string` | 用户 ID |
| &nbsp;&nbsp;└ `create_time` | `int` | 创建时间（单位：秒） |
| &nbsp;&nbsp;└ `update_time` | `int` | 更新时间（单位：秒） |
| &nbsp;&nbsp;└ `extra` | `reply_extra` | 回复的其他内容，图片 Token 等 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `image_list` | `string\[\]` | 回复中的图片 Token list |
| &nbsp;&nbsp;└ `reactions` | `file_comment_v2_batch_query_reaction_data\[\]` | 评论回复卡片上对应的表情回复信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `reaction_key` | `string` | 表情回复的唯一标识，用于区分不同类型的评论表情（如点赞、鼓掌等）。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `count` | `int` | 该表情回复的累计使用次数，统计范围为当前评论下所有用户的有效回复记录。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ahead_users` | `string\[\]` | 用于在界面优先展示核心互动用户。用户ID可通过用户信息查询接口获取。 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "content": {
            "elements": [
                {
                    "type": "docs_link",
                    "text_run": {
                        "text": "reply text"
                    },
                    "docs_link": {
                        "url": "https://example.feishu.cn/docs/doccnHh7U87HOFpii5u5Gabcef"
                    },
                    "person": {
                        "user_id": "ou_cc19b2bfb93f8a44db4b4d6eab2abcef"
                    }
                }
            ]
        },
        "reply_id": "6916106xxxxx4512356",
        "user_id": "ou_cc19b2bfb93f8a44db4b4d6eab2abcef",
        "create_time": 1610281603,
        "update_time": 1610281603,
        "extra": {
            "image_list": [
                "xfsfseewewabcef"
            ]
        },
        "reactions": []
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1069301 | fail | 重试，若稳定失败请联系[技术支持](https://applink.feishu.cn/client/helpdesk) |
| 400 | 1069302 | param error | 检查参数有效性 |
| 403 | 1069303 | forbidden | 检查是否有待回复云文档的评论权限 |
| 400 | 1069304 | docs had been deleted | 检查待回复云文档是否已被删除 |
| 400 | 1069305 | docs not exist | 检查待回复云文档是否能正常访问 |
| 400 | 1069306 | content review not pass | 排查回复内容是否存在不合法内容 |
| 404 | 1069307 | not exist | 检查待回复云文档是否能正常访问、检查回复内容at人或云文档是否存在 |
| 400 | 1069308 | exceeded limit | 回复数据超过上限限制，请联系[技术支持](https://applink.feishu.cn/client/helpdesk) |
| 400 | 1069399 | internal error | 重试，若稳定失败请联系[技术支持](https://applink.feishu.cn/client/helpdesk) |


