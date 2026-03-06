---
title: "批量更新块的内容"
fullPath: "/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/document-block/batch_update"
updateTime: "1758100532000"
---

# 批量更新块的内容

批量更新块的富文本内容。


> **Tip**: **应用频率限制**：单个应用调用频率上限为每秒 3 次，超过该频率限制，接口将返回 HTTP 状态码 400 及错误码 99991400；
> 
> **文档频率限制**：单篇文档并发编辑上限为每秒 3 次，超过该频率限制，接口将返回 HTTP 状态码 429，编辑操作包括：
> - 创建块
> - 创建嵌套块
> - 删除块
> - 更新块
> - 批量更新块
> 
> 当请求被限频，应用需要处理限频状态码，并使用指数退避算法或其它一些频控策略降低对 API 的调用速率。


## 前提条件

调用此接口前，请确保当前调用身份（tenant_access_token 或 user_access_token）已有云文档的阅读、编辑等文档权限，否则接口将返回 HTTP 403 或 400 状态码。了解更多，参考[如何为应用或用户开通文档权限](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a)。

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/docx/v1/documents/:document_id/blocks/batch_update |
| HTTP Method | PATCH |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `docx:document` 创建及编辑新版文档 `docx:document:write_only` 编辑新版文档 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `document_id` | `string` | 文档的唯一标识。点击[这里](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-overview)了解如何获取文档的 `document_id`<br>**示例值**："doxcnePuYufKa49ISjhD8Iabcef" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `document_revision_id` | `int` | 否 | 要操作的文档版本。-1 表示文档最新版本。文档创建后，版本为 1。你需确保你已拥有文档的编辑权限。你可通过调用[获取文档基本信息](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/document/get)获取文档的最新 revision_id<br>**示例值**：-1<br>**默认值**：`-1`<br>**数据校验规则**：<br>- 最小值：`-1` |
| `client_token` | `string` | 否 | 操作的唯一标识，与接口返回值的 client_token 相对应，用于幂等的进行更新操作。此值为空表示将发起一次新的请求，此值非空表示幂等的进行更新操作<br>**示例值**："0e2633a3-aa1a-4171-af9e-0768ff863566" |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**："open_id"<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `requests` | `update_block_request\[\]` | 是 | 批量更新块。不支持在一次批量更新中，对同一个块进行多次更新。即请求体中的 Block ID 不能重复<br>**数据校验规则**：<br>- 最大长度：`200` |
| &nbsp;&nbsp;└ `update_text_elements` | `update_text_elements_request` | 否 | 更新文本元素请求 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 是 | 更新后的文本元素列表，单次更新中：<br>- reminder 元素上限 30 个<br>- mention_doc 元素上限 50 个<br>- mention_user 元素上限 100 个<br>**数据校验规则**：<br>- 最小长度：`1` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 否 | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 是 | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符`<br>**示例值**："文本" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 否 | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 否 | 加粗<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 否 | 斜体<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 否 | 删除线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 否 | 下划线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | 否 | inline 代码<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 否 | 背景色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 否 | 字体颜色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 否 | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 是 | 超链接指向的 url (需要 url_encode)<br>**示例值**："https%3A%2F%2Fopen.feishu.cn%2F" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 否 | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。<br>**示例值**：["1660030311959965796"] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | 否 | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 是 | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。<br>**示例值**："ou_3bbe8a09c20e89cce9bff989ed840674" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 否 | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 否 | 加粗<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 否 | 斜体<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 否 | 删除线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 否 | 下划线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | 否 | inline 代码<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 否 | 背景色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 否 | 字体颜色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 否 | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 是 | 超链接指向的 url (需要 url_encode)<br>**示例值**："https%3A%2F%2Fopen.feishu.cn%2F" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 否 | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。<br>**示例值**：["1660030311959965796"] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | 否 | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 是 | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6)<br>**示例值**："doxbc873Y7cXD153gXqb76G1Y9b" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 是 | 云文档类型<br>**示例值**：22<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 否 | 云文档链接（需要 url_encode)<br>**示例值**："https%3A%2F%2Fbytedance.feishu-boe.cn%2Fdocx%2Fdoxbc873Y7cXD153gXqb76G1Y9b" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 否 | 文档标题，只读属性<br>**示例值**："undefined"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `800` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 否 | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 否 | 加粗<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 否 | 斜体<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 否 | 删除线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 否 | 下划线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | 否 | inline 代码<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 否 | 背景色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 否 | 字体颜色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 否 | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 是 | 超链接指向的 url (需要 url_encode)<br>**示例值**："https%3A%2F%2Fopen.feishu.cn%2F" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 否 | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。<br>**示例值**：["1660030311959965796"] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 否 | 无云文档阅读权限或云文档已删除时的降级方式<br>**示例值**："FallbackToLink"<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 否 | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 是 | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。<br>**示例值**："ou_84aad35d084aa403a838cf73eeabcef" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 否 | 是否通知<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 否 | 是日期还是整点小时<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 是 | 事件发生的时间（毫秒级时间戳）<br>**示例值**："1641967200000" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 是 | 触发通知的时间（毫秒级时间戳）<br>**示例值**："1643166000000" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 否 | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 否 | 加粗<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 否 | 斜体<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 否 | 删除线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 否 | 下划线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | 否 | inline 代码<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 否 | 背景色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 否 | 字体颜色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 否 | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 是 | 超链接指向的 url (需要 url_encode)<br>**示例值**："https%3A%2F%2Fopen.feishu.cn%2F" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 否 | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。<br>**示例值**：["1660030311959965796"] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 否 | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 否 | 附件 token<br>**示例值**："boxcnOj88GDkmWGm2zsTyCabcef" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 否 | 当前文档中该文件所处的 block 的 ID<br>**示例值**："doxcnM46kSWSkgUMW04ldKabcef" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 否 | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 否 | 加粗<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 否 | 斜体<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 否 | 删除线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 否 | 下划线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | 否 | inline 代码<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 否 | 背景色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 否 | 字体颜色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 否 | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 是 | 超链接指向的 url (需要 url_encode)<br>**示例值**："https%3A%2F%2Fopen.feishu.cn%2F" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 否 | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。<br>**示例值**：["1660030311959965796"] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 否 | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 否 | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 是 | 关联的内联状态的 block 的 block_id<br>**示例值**："doxcnPFi0R56ctbvh2Mjkkabcef" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 否 | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 否 | 加粗<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 否 | 斜体<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 否 | 删除线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 否 | 下划线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | 否 | inline 代码<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 否 | 背景色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 否 | 字体颜色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 否 | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 是 | 超链接指向的 url (需要 url_encode)<br>**示例值**："https%3A%2F%2Fopen.feishu.cn%2F" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 否 | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。<br>**示例值**：["1660030311959965796"] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 否 | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 是 | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符<br>**示例值**："E=mc^2\n" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 否 | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 否 | 加粗<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 否 | 斜体<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 否 | 删除线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 否 | 下划线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | 否 | inline 代码<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 否 | 背景色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 否 | 字体颜色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 否 | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 是 | 超链接指向的 url (需要 url_encode)<br>**示例值**："https%3A%2F%2Fopen.feishu.cn%2F" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 否 | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。<br>**示例值**：["1660030311959965796"] |
| &nbsp;&nbsp;└ `update_text_style` | `update_text_style_request` | 否 | 更新文本样式请求 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 是 | 文本样式。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo、Task 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 否 | 对齐方式<br>**示例值**：1<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版<br>**默认值**：`1` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | 否 | todo 的完成状态。支持对 Todo 块进行修改<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 否 | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 否 | 代码块的语言类型。仅支持对 Code 块进行修改<br>**示例值**：1<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 否 | 代码块是否自动换行。支持对 Code 块进行修改<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 否 | 块的背景色<br>**示例值**："LightGrayBackground"<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 否 | 首行缩进级别。仅支持对 Text 块进行修改。<br>**示例值**："NoIndent"<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 否 | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段<br>**示例值**：""auto"" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `fields` | `int\[\]` | 是 | 应更新的字段，必须至少指定一个字段。例如，要调整 Block 对齐方式，请设置 fields 为 [1]。<br>**示例值**：修改的文字样式属性<br>**可选值有**：<br>- `1`: 修改 Block 的对齐方式 - `2`: Todo 的完成状态。支持对 Todo 和 Task 块进行修改 - `3`: 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet、Todo 和 Task 块进行修改 - `4`: 代码块语言类型。仅支持对 Code 块进行修改 - `5`: 代码块是否自动换行。支持对 Code 块进行修改 - `6`: 块背景色 - `7`: 首行缩进级别。仅支持对 Text 块进行修改。 |
| &nbsp;&nbsp;└ `update_table_property` | `update_table_property_request` | 否 | 更新表格属性请求。仅支持对 Table 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `column_width` | `int` | 否 | 表格列宽，单位像素（px）<br>**示例值**：100<br>**数据校验规则**：<br>- 最小值：`50` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `column_index` | `int` | 否 | 需要修改列宽的表格列的索引<br>**示例值**：0<br>**数据校验规则**：<br>- 最小值：`0` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `header_row` | `boolean` | 否 | 设置首行为标题行<br>**示例值**：false |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `header_column` | `boolean` | 否 | 设置首列为标题列<br>**示例值**：false |
| &nbsp;&nbsp;└ `insert_table_row` | `insert_table_row_request` | 否 | 表格插入新行请求。仅支持对 Table 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `row_index` | `int` | 是 | 插入的行在表格中的索引。（-1表示在表格末尾插入一行）<br>**示例值**：-1<br>**数据校验规则**：<br>- 最小值：`-1` |
| &nbsp;&nbsp;└ `insert_table_column` | `insert_table_column_request` | 否 | 表格插入新列请求。仅支持对 Table 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `column_index` | `int` | 是 | 插入的列在表格中的索引。（-1表示在表格末尾插入一列）<br>**示例值**：-1<br>**数据校验规则**：<br>- 最小值：`-1` |
| &nbsp;&nbsp;└ `delete_table_rows` | `delete_table_rows_request` | 否 | 表格批量删除行请求。仅支持对 Table 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `row_start_index` | `int` | 是 | 行开始索引（区间左闭右开）<br>**示例值**：0<br>**数据校验规则**：<br>- 最小值：`0` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `row_end_index` | `int` | 是 | 行结束索引（区间左闭右开）<br>**示例值**：1<br>**数据校验规则**：<br>- 最小值：`1` |
| &nbsp;&nbsp;└ `delete_table_columns` | `delete_table_columns_request` | 否 | 表格批量删除列请求。仅支持对 Table 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `column_start_index` | `int` | 是 | 列开始索引（区间左闭右开）<br>**示例值**：0<br>**数据校验规则**：<br>- 最小值：`0` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `column_end_index` | `int` | 是 | 列结束索引（区间左闭右开）<br>**示例值**：1<br>**数据校验规则**：<br>- 最小值：`1` |
| &nbsp;&nbsp;└ `merge_table_cells` | `merge_table_cells_request` | 否 | 表格合并单元格请求。仅支持对 Table 块进行修改。表格单元格需要满足以下任一条件：<br>- 完全包含在之前合并的区域内<br>- 完全不在之前合并的区域内 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `row_start_index` | `int` | 是 | 行起始索引（区间左闭右开）<br>**示例值**：0<br>**数据校验规则**：<br>- 最小值：`0` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `row_end_index` | `int` | 是 | 行结束索引（区间左闭右开）<br>**示例值**：1<br>**数据校验规则**：<br>- 最小值：`1` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `column_start_index` | `int` | 是 | 列起始索引（区间左闭右开）<br>**示例值**：0<br>**数据校验规则**：<br>- 最小值：`0` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `column_end_index` | `int` | 是 | 列结束索引（区间左闭右开）<br>**示例值**：1<br>**数据校验规则**：<br>- 最小值：`1` |
| &nbsp;&nbsp;└ `unmerge_table_cells` | `unmerge_table_cells_request` | 否 | 表格取消单元格合并状态请求。仅支持对 Table 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `row_index` | `int` | 是 | table 行索引<br>**示例值**：0<br>**数据校验规则**：<br>- 最小值：`0` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `column_index` | `int` | 是 | table 列索引<br>**示例值**：0<br>**数据校验规则**：<br>- 最小值：`0` |
| &nbsp;&nbsp;└ `insert_grid_column` | `insert_grid_column_request` | 否 | 分栏插入新的分栏列请求。仅支持对 Grid 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `column_index` | `int` | 是 | 插入列索引，从 1 开始，如 1 表示在第一列后插入，注意不允许传 0（-1表示在最后一列后插入）<br>**示例值**：1<br>**数据校验规则**：<br>- 最小值：`-1` |
| &nbsp;&nbsp;└ `delete_grid_column` | `delete_grid_column_request` | 否 | 分栏删除列请求。仅支持对 Grid 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `column_index` | `int` | 是 | 删除列索引，从 0 开始，如 0 表示删除第一列（-1表示删除最后一列）<br>**示例值**：0<br>**数据校验规则**：<br>- 最小值：`-1` |
| &nbsp;&nbsp;└ `update_grid_column_width_ratio` | `update_grid_column_width_ratio_request` | 否 | 更新分栏列宽比例请求。仅支持对 Grid 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `width_ratios` | `int\[\]` | 是 | 更新列宽比例时，需要传入所有列宽占比，单位 %<br>**示例值**：50<br>**数据校验规则**：<br>- 长度范围：`1` ～ `99` |
| &nbsp;&nbsp;└ `replace_image` | `replace_image_request` | 否 | 替换图片请求。调用此请求前，你需确保已经上传过素材 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 是 | 图片 Token。可参考[如何插入图片-第二步：上传图片素材](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/faq#1908ddf0)上传图片得到图片 Token。<br>**示例值**："boxbckbfvfcqEg22hAzN8Dabcef" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `width` | `int` | 否 | 图片宽度，单位像素（px） 1. 优先使用本次请求传入的 width 值； 2. 若本次请求未传 width，且为首次更新（待更新的图片块 token 为空），服务端将检测并使用请求传入的图片的实际 width；检测失败将兜底为 100 px。 3. 若本次请求未传 width，且非首次更新，width 字段将保持原值不变。<br>**示例值**：100 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `height` | `int` | 否 | 图片高度，单位像素（px） 1. 优先使用本次请求传入的 height 值； 2. 若本次请求未传 height，且为首次更新（待更新的图片块 token 为空），服务端将检测并使用请求传入的图片的实际 height；检测失败将兜底为 100 px。 3. 若本次请求未传 height，且非首次更新，height 字段将保持原值不变。<br>**示例值**：100 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 否 | 对齐方式<br>**示例值**：2<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `caption` | `caption` | 否 | 图片描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 否 | 描述的文本内容<br>**示例值**："caption" |
| &nbsp;&nbsp;└ `replace_file` | `replace_file_request` | 否 | 替换附件请求。调用此请求前，你需确保已经上传过素材 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 是 | 附件 token<br>**示例值**："boxbckbfvfcqEg22hAzN8Dabcef" |
| &nbsp;&nbsp;└ `block_id` | `string` | 否 | Block 唯一标识。你可调用[获取文档所有块](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/document-block/list)获取文档中块的 `block_id`<br>**示例值**："doxcnSS4ouQkQEouGSUkTg9NJPe" |
| &nbsp;&nbsp;└ `update_text` | `update_text_request` | 否 | 更新文本元素及样式请求 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 是 | 更新的文本元素列表。单次更新中：<br>- reminder 上限 30 个<br>- mention_doc 上限 50 个<br>- mention_user 上限 100 个<br>**数据校验规则**：<br>- 最小长度：`1` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 否 | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 是 | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符`<br>**示例值**："文本" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 否 | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 否 | 加粗<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 否 | 斜体<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 否 | 删除线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 否 | 下划线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | 否 | inline 代码<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 否 | 背景色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 否 | 字体颜色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 否 | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 是 | 超链接指向的 url (需要 url_encode)<br>**示例值**："https%3A%2F%2Fopen.feishu.cn%2F" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 否 | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。<br>**示例值**：["1660030311959965796"] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | 否 | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 是 | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。<br>**示例值**："ou_3bbe8a09c20e89cce9bff989ed840674" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 否 | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 否 | 加粗<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 否 | 斜体<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 否 | 删除线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 否 | 下划线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | 否 | inline 代码<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 否 | 背景色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 否 | 字体颜色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 否 | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 是 | 超链接指向的 url (需要 url_encode)<br>**示例值**："https%3A%2F%2Fopen.feishu.cn%2F" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 否 | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。<br>**示例值**：["1660030311959965796"] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | 否 | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 是 | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6)<br>**示例值**："doxbc873Y7cXD153gXqb76G1Y9b" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 是 | 云文档类型<br>**示例值**：22<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 否 | 云文档链接（需要 url_encode)<br>**示例值**："https%3A%2F%2Fbytedance.feishu-boe.cn%2Fdocx%2Fdoxbc873Y7cXD153gXqb76G1Y9b" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 否 | 文档标题，只读属性<br>**示例值**："undefined"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `800` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 否 | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 否 | 加粗<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 否 | 斜体<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 否 | 删除线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 否 | 下划线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | 否 | inline 代码<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 否 | 背景色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 否 | 字体颜色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 否 | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 是 | 超链接指向的 url (需要 url_encode)<br>**示例值**："https%3A%2F%2Fopen.feishu.cn%2F" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 否 | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。<br>**示例值**：["1660030311959965796"] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 否 | 无云文档阅读权限或云文档已删除时的降级方式<br>**示例值**："FallbackToLink"<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 否 | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 是 | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。<br>**示例值**："ou_84aad35d084aa403a838cf73eeabcef" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 否 | 是否通知<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 否 | 是日期还是整点小时<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 是 | 事件发生的时间（毫秒级时间戳）<br>**示例值**："1641967200000" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 是 | 触发通知的时间（毫秒级时间戳）<br>**示例值**："1643166000000" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 否 | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 否 | 加粗<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 否 | 斜体<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 否 | 删除线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 否 | 下划线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | 否 | inline 代码<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 否 | 背景色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 否 | 字体颜色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 否 | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 是 | 超链接指向的 url (需要 url_encode)<br>**示例值**："https%3A%2F%2Fopen.feishu.cn%2F" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 否 | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。<br>**示例值**：["1660030311959965796"] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 否 | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 否 | 附件 token<br>**示例值**："boxcnOj88GDkmWGm2zsTyCabcef" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 否 | 当前文档中该文件所处的 block 的 ID<br>**示例值**："doxcnM46kSWSkgUMW04ldKabcef" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 否 | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 否 | 加粗<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 否 | 斜体<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 否 | 删除线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 否 | 下划线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | 否 | inline 代码<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 否 | 背景色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 否 | 字体颜色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 否 | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 是 | 超链接指向的 url (需要 url_encode)<br>**示例值**："https%3A%2F%2Fopen.feishu.cn%2F" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 否 | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。<br>**示例值**：["1660030311959965796"] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 否 | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 否 | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 是 | 关联的内联状态的 block 的 block_id<br>**示例值**："doxcnPFi0R56ctbvh2Mjkkabcef" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 否 | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 否 | 加粗<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 否 | 斜体<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 否 | 删除线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 否 | 下划线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | 否 | inline 代码<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 否 | 背景色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 否 | 字体颜色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 否 | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 是 | 超链接指向的 url (需要 url_encode)<br>**示例值**："https%3A%2F%2Fopen.feishu.cn%2F" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 否 | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。<br>**示例值**：["1660030311959965796"] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 否 | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 是 | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符<br>**示例值**："E=mc^2\n" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 否 | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 否 | 加粗<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 否 | 斜体<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 否 | 删除线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 否 | 下划线<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | 否 | inline 代码<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 否 | 背景色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 否 | 字体颜色<br>**示例值**：1<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 否 | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 是 | 超链接指向的 url (需要 url_encode)<br>**示例值**："https%3A%2F%2Fopen.feishu.cn%2F" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 否 | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。<br>**示例值**：["1660030311959965796"] |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 是 | 更新的文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 否 | 对齐方式<br>**示例值**：1<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版<br>**默认值**：`1` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | 否 | todo 的完成状态。支持对 Todo 块进行修改<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 否 | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 否 | 代码块的语言类型。仅支持对 Code 块进行修改<br>**示例值**：1<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 否 | 代码块是否自动换行。支持对 Code 块进行修改<br>**示例值**：true<br>**默认值**：`false` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 否 | 块的背景色<br>**示例值**："LightGrayBackground"<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 否 | 首行缩进级别。仅支持对 Text 块进行修改。<br>**示例值**："NoIndent"<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 否 | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段<br>**示例值**：""auto"" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `fields` | `int\[\]` | 是 | 文本样式中要更新的字段，必须至少指定一个字段。例如，要调整 Block 对齐方式，请设置 fields 为 [1]<br>**示例值**：[1]<br>**可选值有**：<br>- `1`: 修改 Block 的对齐方式 - `2`: 修改 todo 的完成状态。支持对 Todo 和 Task 块进行修改 - `3`: 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet、Todo 和 Task 块进行修改 - `4`: 代码块的语言类型。仅支持对 Code 块进行修改 - `5`: 代码块是否自动换行。支持对 Code 块进行修改 - `6`: 块背景色 - `7`: 首行缩进级别。仅支持对 Text 块进行修改。 |
| &nbsp;&nbsp;└ `update_task` | `update_task_request` | 否 | 更新任务 Block 请求 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `task_id` | `string` | 否 | 任务 ID。该字段仅在首次更新 Task Block 时生效，更新成功后，后续请求中将忽略该字段。<br>**示例值**："ba5040f4-8116-4042-ab3c-254e5cfe3ce7" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 否 | 折叠状态，字段为空时不更新折叠状态<br>**示例值**：false |


### 请求示例
```bash
curl --location --request PATCH 'https://open.feishu.cn/open-apis/docx/v1/documents/doxcnAJ9VRRJqVMYZ1MyKnavXWe/blocks/batch_update' \
--header 'Authorization: Bearer u-xxx'
--header 'Content-Type: application/json' \
--data-raw '{
    "requests": [
        {
            "block_id": "doxcnk0i44OMOaouw8AdXuXrp6b",
            "merge_table_cells": {
                "column_end_index": 2,
                "column_start_index": 0,
                "row_end_index": 1,
                "row_start_index": 0
            }
        },
        {
            "block_id": "doxcn0K8iGSMW4Mqgs9qlyTP50d",
            "update_text_elements": {
                "elements": [
                    {
                        "text_run": {
                            "content": "Hello",
                            "text_element_style": {
                                "background_color": 2,
                                "bold": true,
                                "italic": true,
                                "strikethrough": true,
                                "text_color": 2,
                                "underline": true                            }
                        }
                    },
                    {
                        "text_run": {
                            "content": "World ",
                            "text_element_style": {
                                "italic": true
                            }
                        }
                    },
                    {
                        "mention_doc": {
                            "obj_type": 22,
                            "token": "doxcnAJ9VRRJqVMYZ1MyKnayXWe",
                            "url": "https://test.feishu.cn/docx/doxcnAJ9VRRJqVMYZ1MyKnayXWe"
                        }
                    }
                ]
            }
        }
    ]
}'
# 调用前请替换 'Authorization: Bearer u-xxx' 中的 'u-xxx' 为真实的访问令牌
```

### 请求体示例

```json
{
    "requests": [
        {
            "block_id": "doxcnk0i44OMOaouw8AdXuXrp6b",
            "merge_table_cells": {
                "column_end_index": 2,
                "column_start_index": 0,
                "row_end_index": 1,
                "row_start_index": 0
            }
        },
        {
            "block_id": "doxcn0K8iGSMW4Mqgs9qlyTP50d",
            "update_text_elements": {
                "elements": [
                    {
                        "text_run": {
                            "content": "Hello",
                            "text_element_style": {
                                "background_color": 2,
                                "bold": true,
                                "italic": true,
                                "strikethrough": true,
                                "text_color": 2,
                                "underline": true
                            }
                        }
                    },
                    {
                        "text_run": {
                            "content": "World ",
                            "text_element_style": {
                                "italic": true
                            }
                        }
                    },
                    {
                        "mention_doc": {
                            "obj_type": 22,
                            "token": "doxcnAJ9VRRJqVMYZ1MyKnayXWe",
                            "url": "https%3A%2F%2Ftest.feishu.cn%2Fdocx%2FdoxcnAJ9VRRJqVMYZ1MyKnayXWe"
                        }
                    }
                ]
            }
        }
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
| &nbsp;&nbsp;└ `blocks` | `block\[\]` | 批量更新的 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 子块的唯一标识。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `parent_id` | `string` | 子块的父块 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `children` | `string\[\]` | 子块的子块 ID 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `block_type` | `int` | Block 类型<br>**可选值有**：<br>- `1`: 页面 Block - `2`: 文本 Block - `3`: 标题 1 Block - `4`: 标题 2 Block - `5`: 标题 3 Block - `6`: 标题 4 Block - `7`: 标题 5 Block - `8`: 标题 6 Block - `9`: 标题 7 Block - `10`: 标题 8 Block - `11`: 标题 9 Block - `12`: 无序列表 Block - `13`: 有序列表 Block - `14`: 代码块 Block - `15`: 引用 Block - `17`: 待办事项 Block - `18`: 多维表格 Block - `19`: 高亮块 Block - `20`: 会话卡片 Block - `21`: 流程图 & UML Block - `22`: 分割线 Block。为空结构体，需传入 `{}` 创建分割线 Block。 - `23`: 文件 Block - `24`: 分栏 Block - `25`: 分栏列 Block - `26`: 内嵌网页 Block - `27`: 图片 Block - `28`: 开放平台小组件 Block - `29`: 思维笔记 Block - `30`: 电子表格 Block - `31`: 表格 Block。了解如何在文档中插入表格，参考[文档常见问题-如何插入表格并往单元格填充内容](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/faq)。 - `32`: 表格单元格 Block - `33`: 视图 Block - `34`: 引用容器 Block。为空结构体，需传入 `{}` 创建引用容器 Block。 - `35`: 任务 Block - `36`: OKR Block - `37`: OKR Objective Block - `38`: OKR Key Result Block - `39`: OKR 进展 Block - `40`: 文档小组件 Block - `41`: Jira 问题 Block - `42`: Wiki 子目录 Block - `43`: 画板 Block - `44`: 议程 Block - `45`: 议程项 Block - `46`: 议程项标题 Block - `47`: 议程项内容 Block - `48`: 链接预览 Block - `49`: 源同步块，仅支持查询 - `50`: 引用同步块，仅支持查询。获取引用同步块内容详见：[如何获取引用同步块的内容](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/faq#19b71234) - `51`: Wiki 新版子目录 - `52`: AI 模板 Block，仅支持查询 - `999`: 未支持 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `page` | `text` | 文档的根 Block，也称页面 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `text` | `text` | 文本 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `heading1` | `text` | 一级标题 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `heading2` | `text` | 二级标题 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `heading3` | `text` | 三级标题 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `heading4` | `text` | 四级标题 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `heading5` | `text` | 五级标题 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `heading6` | `text` | 六级标题 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `heading7` | `text` | 七级标题 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `heading8` | `text` | 八级标题 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `heading9` | `text` | 九级标题 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `bullet` | `text` | 无序列表 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ordered` | `text` | 有序列表 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `text` | 代码块 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `quote` | `text` | 引用 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `text` | 公式 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `todo` | `text` | 待办事项 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `bitable` | `bitable` | 多维表格 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 多维表格文档 Token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `view_type` | `int` | 类型<br>**可选值有**：<br>- `1`: 数据表 - `2`: 看板 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `callout` | `callout` | 高亮块 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 高亮块背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 中红色 - `9`: 中橙色 - `10`: 中黄色 - `11`: 中绿色 - `12`: 中蓝色 - `13`: 中紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `border_color` | `int` | 边框色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 文字颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `emoji_id` | `string` | 高亮块图标 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `chat_card` | `chat_card` | 群聊卡片 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `chat_id` | `string` | 群聊天会话 ID。获取方式参考[群 ID 说明](ssl:ttdoc//uAjLw4CM/ukTMukTMukTM/reference/im-v1/chat-id-description) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `diagram` | `diagram` | 流程图/UML Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `diagram_type` | `int` | 绘图类型<br>**可选值有**：<br>- `1`: 流程图 - `2`: UML 图 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `divider` | `divider` | 分割线 Block。为空结构体，需传入 `{}` 创建分割线 Block。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `file` | 文件 Block。了解如何在文档中插入文件，参考[文档常见问题-如何插入文件/附件](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/faq)。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 附件 Token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 文件名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `view_type` | `int` | 视图类型，卡片视图（默认）或预览视图<br>**可选值有**：<br>- `1`: 卡片视图 - `2`: 预览视图 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `grid` | `grid` | 分栏 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `column_size` | `int` | 分栏列数量 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `grid_column` | `grid_column` | 分栏列 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `width_ratio` | `int` | 当前分栏列占整个分栏的比例，单位 % |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `iframe` | `iframe` | 内嵌 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `component` | `iframe_component` | iframe 的组成元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `iframe_type` | `int` | iframe 类型<br>**可选值有**：<br>- `1`: 哔哩哔哩 - `2`: 西瓜视频 - `3`: 优酷 - `4`: Airtable - `5`: 百度地图 - `6`: 高德地图 - `7`: Undefined - `8`: Figma - `9`: 墨刀 - `10`: Canva - `11`: CodePen - `12`: 飞书问卷 - `13`: 金数据 - `14`: Undefined - `15`: Undefined - `99`: Other |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | iframe 目标 url（需要进行 url_encode） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `image` | `image` | 图片 Block。了解如何在文档中插入图片，参考[文档常见问题-如何插入图片](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/faq)。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `width` | `int` | 宽度单位 px |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `height` | `int` | 高度单位 px |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 图片 Token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `caption` | `caption` | 图片描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 描述的文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `isv` | `isv` | 三方 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `component_id` | `string` | 团队互动应用唯一ID。该 ID 可通过调用[创建 BlockEntity](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/block-v2/entity/create) 接口，并从响应体中的 block_id 中获取，创建时使用的 `block_type_id` 需要与 `component_type_id` 一致。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `component_type_id` | `string` | 团队互动应用类型，比如信息收集"blk_5f992038c64240015d280958"。该 ID 可在 [开发者后台](https://open.feishu.cn/app) > **应用详情页** > **应用能力** > **云文档小组件** > **BlockTypeID** 获取。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `add_ons` | `add_ons` | Add-ons |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `component_id` | `string` | 文档小组件 ID。该 ID 可通过调用[创建 BlockEntity](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/block-v2/entity/create) 接口，并从响应体中的 block_id 中获取，创建时使用的 `block_type_id` 需要与 `component_type_id` 一致。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `component_type_id` | `string` | 文档小组件类型，比如问答互动"blk_636a0a6657db8001c8df5488"。该 ID 可在 [开发者后台](https://open.feishu.cn/app) > **应用详情页** > **应用能力** > **云文档小组件** > **BlockTypeID** 获取。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `record` | `string` | 文档小组件内容数据，JSON 字符串 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `mindnote` | `mindnote` | 思维笔记 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 思维导图 token |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sheet` | `sheet` | 电子表格 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 电子表格 block 的 token 和工作表的 ID 的组合 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `row_size` | `int` | 电子表格行数量 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `column_size` | `int` | 电子表格列数量 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `table` | `table` | 表格 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cells` | `string\[\]` | 单元格数组，数组元素为 Table Cell Block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `property` | `table_property` | 表格属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `row_size` | `int` | 行数 - **创建块**接口中，该字段最大值为 9  - **创建嵌套块**接口中，在单个表格单元格不超过上限 2000 情况下，该字段无固定最大值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `column_size` | `int` | 列数 - **创建块**接口中，该字段最大值为 9  - **创建嵌套块**接口中，该字段最大值为 100 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `column_width` | `int\[\]` | 列宽，单位像素（px） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `merge_info` | `table_merge_info\[\]` | 单元格合并信息。创建 Table 时，此属性只读，将由系统自动生成。如果需要合并单元格，可以通过更新块接口的子请求 `merge_table_cells` 实现 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `row_span` | `int` | 从当前行索引起被合并的连续行数 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `col_span` | `int` | 从当前列索引起被合并的连续列数 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `header_row` | `boolean` | 设置首行为标题行 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `header_column` | `boolean` | 设置首列为标题列 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `table_cell` | `table_cell` | 单元格 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `view` | `view` | 视图 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `view_type` | `int` | 视图类型<br>**可选值有**：<br>- `1`: 卡片视图 - `2`: 预览视图 - `3`: 内联视图 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined` | 未支持 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `quote_container` | `quote_container` | 引用容器 Block。为空结构体，需传入 `{}` 创建引用容器 Block。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `task` | `task` | 任务 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `task_id` | `string` | 任务 ID，查询具体任务详情见 [获取任务详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/task/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 折叠状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `okr` | `okr` | OKR Block，仅可在使用 `user_access_token` 时创建 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `okr_id` | `string` | OKR ID，获取需要插入的 OKR ID 可见[获取用户的 OKR 列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/user-okr/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `objectives` | `objective_id_with_kr_id\[\]` | OKR Block 中的 Objective ID 和 Key Result ID，此值为空时插入 OKR 下所有的 Objective 和 Key Result |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `objective_id` | `string` | OKR 中 Objective 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `kr_ids` | `string\[\]` | Key Result 的 ID 列表，此值为空时插入当前 Objective 下的所有 Key Result |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `period_display_status` | `string` | 周期的状态<br>**可选值有**：<br>- `default`: 默认 - `normal`: 正常 - `invalid`: 失效 - `hidden`: 隐藏 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `period_name_zh` | `string` | 周期名 - 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `period_name_en` | `string` | 周期名 - 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | OKR 所属的用户 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `visible_setting` | `okr_visible_setting` | 可见性设置 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `progress_fill_area_visible` | `boolean` | 进展编辑区域是否可见 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `progress_status_visible` | `boolean` | 进展状态是否可见 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `score_visible` | `boolean` | 分数是否可见 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `okr_objective` | `okr_objective` | OKR Objective Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `objective_id` | `string` | Objective ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `confidential` | `boolean` | 是否在 OKR 平台设置了私密权限 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `position` | `int` | Objective 的位置编号，对应 Block 中 O1、O2 的 1、2 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `score` | `int` | 打分信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `visible` | `boolean` | OKR Block 中是否展示该 Objective |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `weight` | `float` | Objective 的权重 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `progress_rate` | `okr_progress_rate` | 进展信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mode` | `string` | 状态模式<br>**可选值有**：<br>- `simple`: 简单模式 - `advanced`: 高级模式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `current` | `float` | 当前进度，单位 %，advanced 模式使用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `percent` | `float` | 当前进度百分比，simple 模式使用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `progress_status` | `string` | 进展状态<br>**可选值有**：<br>- `unset`: 未设置 - `normal`: 正常 - `risk`: 有风险 - `extended`: 已延期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start` | `float` | 进度起始值，单位 %，advanced 模式使用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `status_type` | `string` | 状态计算类型<br>**可选值有**：<br>- `default`: 以风险最高的 Key Result 状态展示 - `custom`: 自定义 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `target` | `float` | 进度目标值，单位 %，advanced 模式使用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `text` | Objective 的文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `okr_key_result` | `okr_key_result` | OKR Key Result |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `kr_id` | `string` | Key Result 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `confidential` | `boolean` | 是否在 OKR 平台设置了私密权限 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `position` | `int` | Key Result 的位置编号，对应 Block 中 KR1、KR2 的 1、2。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `score` | `int` | 打分信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `visible` | `boolean` | OKR Block 中此 Key Result 是否可见 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `weight` | `float` | Key Result 的权重 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `progress_rate` | `okr_progress_rate` | 进展信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mode` | `string` | 状态模式<br>**可选值有**：<br>- `simple`: 简单模式 - `advanced`: 高级模式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `current` | `float` | 当前进度，单位 %，advanced 模式使用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `percent` | `float` | 当前进度百分比，simple 模式使用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `progress_status` | `string` | 进展状态<br>**可选值有**：<br>- `unset`: 未设置 - `normal`: 正常 - `risk`: 有风险 - `extended`: 已延期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start` | `float` | 进度起始值，单位 %，advanced 模式使用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `status_type` | `string` | 状态计算类型<br>**可选值有**：<br>- `default`: 以风险最高的 Key Result 状态展示 - `custom`: 自定义 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `target` | `float` | 进度目标值，单位 %，advanced 模式使用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `text` | Key Result 的文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `text_style` | 文本样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `done` | `boolean` | todo 的完成状态。支持对 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `folded` | `boolean` | 文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 代码块的语言类型。仅支持对 Code 块进行修改<br>**可选值有**：<br>- `1`: PlainText - `2`: ABAP - `3`: Ada - `4`: Apache - `5`: Apex - `6`: Assembly Language - `7`: Bash - `8`: CSharp - `9`: C++ - `10`: C - `11`: COBOL - `12`: CSS - `13`: CoffeeScript - `14`: D - `15`: Dart - `16`: Delphi - `17`: Django - `18`: Dockerfile - `19`: Erlang - `20`: Fortran - `21`: FoxPro - `22`: Go - `23`: Groovy - `24`: HTML - `25`: HTMLBars - `26`: HTTP - `27`: Haskell - `28`: JSON - `29`: Java - `30`: JavaScript - `31`: Julia - `32`: Kotlin - `33`: LateX - `34`: Lisp - `35`: Logo - `36`: Lua - `37`: MATLAB - `38`: Makefile - `39`: Markdown - `40`: Nginx - `41`: Objective-C - `42`: OpenEdgeABL - `43`: PHP - `44`: Perl - `45`: PostScript - `46`: Power Shell - `47`: Prolog - `48`: ProtoBuf - `49`: Python - `50`: R - `51`: RPG - `52`: Ruby - `53`: Rust - `54`: SAS - `55`: SCSS - `56`: SQL - `57`: Scala - `58`: Scheme - `59`: Scratch - `60`: Shell - `61`: Swift - `62`: Thrift - `63`: TypeScript - `64`: VBScript - `65`: Visual Basic - `66`: XML - `67`: YAML - `68`: CMake - `69`: Diff - `70`: Gherkin - `71`: GraphQL - `72`: OpenGL Shading Language - `73`: Properties - `74`: Solidity - `75`: TOML |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wrap` | `boolean` | 代码块是否自动换行。支持对 Code 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 块的背景色<br>**可选值有**：<br>- `LightGrayBackground`: 浅灰色 - `LightRedBackground`: 浅红色 - `LightOrangeBackground`: 浅橙色 - `LightYellowBackground`: 浅黄色 - `LightGreenBackground`: 浅绿色 - `LightBlueBackground`: 浅蓝色 - `LightPurpleBackground`: 浅紫色 - `PaleGrayBackground`: 中灰色 - `DarkGrayBackground`: 灰色 - `DarkRedBackground`: 中红色 - `DarkOrangeBackground`: 中橙色 - `DarkYellowBackground`: 中黄色 - `DarkGreenBackground`: 中绿色 - `DarkBlueBackground`: 中蓝色 - `DarkPurpleBackground`: 中紫色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentation_level` | `string` | 首行缩进级别。仅支持对 Text 块进行修改。<br>**可选值有**：<br>- `NoIndent`: 无缩进 - `OneLevelIndent`: 一级缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sequence` | `string` | 用于确定有序列表项编号，为具体数值或'auto' - 开始新列表时，有序列表编号从 1 开始，sequence='1' - 手动修改为非连续编号时，有序列表编号为设定的具体数值，如 sequence='3' - 继续编号时，有序列表编号自动连续，sequence='auto' - 部分历史数据和通过 OpenAPI 创建的有序列表不返回此字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `okr_progress` | `okr_progress` | OKR 进展信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 id 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `jira_issue` | `jira_issue` | Jira 问题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | Jira 问题 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | Jira 问题 key |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `wiki_catalog` | `wiki_catalog` | Wiki 子目录 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wiki_token` | `string` | 知识库 token |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `board` | `board` | 画板 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 画板 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `width` | `int` | 宽度，单位 px；不填时自动适应文档宽度；值超出文档最大宽度时，页面渲染为文档最大宽度 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `height` | `int` | 高度，单位 px；不填时自动根据画板内容计算；值超出屏幕两倍高度时，页面渲染为屏幕两倍高度 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agenda` | `agenda` | 议程 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agenda_item` | `agenda_item` | 议程项 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agenda_item_title` | `agenda_item_title` | 议程项标题 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `agenda_title_element\[\]` | 文本元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联 block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agenda_item_content` | `agenda_item_content` | 议程项内容 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `link_preview` | `link_preview` | 链接预览 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url_type` | `string` | 链接类型<br>**可选值有**：<br>- `MessageLink`: 消息链接 - `Undefined`: 未定义的链接类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `source_synced` | `source_synced` | 源同步块，仅支持查询 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `text_element\[\]` | 同步块独立页标题，由文本元素组成 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_run` | `text_run` | 文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容。要实现文本内容的换行，你可以： - 在传入的文本内容中添加 `\n` 实现软换行（Soft Break，与在文档中通过操作 `Shift + Enter` 的效果一致） - 创建一个新的文本 Block，实现两个文本 Block 之间的硬换行（Hard Break，与在文档中通过操作 `Enter` 的效果一致）<br>**注意**：软换行在渲染时可能会被忽略，具体取决于渲染器如何处理；硬换行在渲染时始终会显示为一个新行。<br>**数据校验规则**： * 一个文本 Block 中 content 总长度最大值：`100,000 个 UTF-16 编码的字符` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_user` | `mention_user` | @用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 OpenID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mention_doc` | `mention_doc` | @文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 云文档 token。获取方式参考[如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `int` | 云文档类型<br>**可选值有**：<br>- `1`: Doc - `3`: Sheet - `8`: Bitable - `11`: MindNote - `12`: File - `15`: Slide - `16`: Wiki - `22`: Docx |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 云文档链接（需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题，只读属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fallback_type` | `string` | 无云文档阅读权限或云文档已删除时的降级方式<br>**可选值有**：<br>- `FallbackToLink`: 降级为超链接形式写入，超链接的文本内容为当前传入的文档标题，链接为当前传入的云文档链接（需要 url_encode） - `FallbackToText`: 降级为文本形式写入，文本内容为当前传入的云文档链接进行 URL 解码后的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reminder` | `reminder` | 日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建者用户 ID，ID 类型与查询参数 `user_id_type` 的取值一致。获取方式参考 `user_id_type` 参数说明。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_notify` | `boolean` | 是否通知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_whole_day` | `boolean` | 是日期还是整点小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `string` | 事件发生的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notify_time` | `string` | 触发通知的时间（毫秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file` | `inline_file` | 内联文件。仅支持删除或移动位置，不支持创建新的内联文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件 token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 当前文档中该文件所处的 block 的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `undefined` | `undefined_element` | 未支持的 TextElement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_block` | `inline_block` | 内联块。仅支持删除或移动位置，不支持创建新的内联块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_id` | `string` | 关联的内联状态的 block 的 block_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `equation` | `equation` | 公式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html<br>**数据校验规则**： * 长度范围：`1`~`10,000`字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_element_style` | `text_element_style` | 文本局部样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `boolean` | 斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikethrough` | `boolean` | 删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `underline` | `boolean` | 下划线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inline_code` | `boolean` | inline 代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `int` | 背景色<br>**可选值有**：<br>- `1`: 浅红色 - `2`: 浅橙色 - `3`: 浅黄色 - `4`: 浅绿色 - `5`: 浅蓝色 - `6`: 浅紫色 - `7`: 中灰色 - `8`: 红色 - `9`: 橙色 - `10`: 黄色 - `11`: 绿色 - `12`: 蓝色 - `13`: 紫色 - `14`: 灰色 - `15`: 浅灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_color` | `int` | 字体颜色<br>**可选值有**：<br>- `1`: 红色 - `2`: 橙色 - `3`: 黄色 - `4`: 绿色 - `5`: 蓝色 - `6`: 紫色 - `7`: 灰色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `link` | 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 超链接指向的 url (需要 url_encode) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `comment_ids` | `string\[\]` | 评论 ID 列表。在创建 Block 时，不支持传入评论 ID；在更新文本 Block 的 Element 时，允许将对应版本已存在的评论 ID 移动到同一个 Block 内的任意 Element 中，但不支持传入新的评论 ID。如需查询评论内容请阅览「[获取回复](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-comment-reply/list)」 API。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `align` | `int` | 对齐方式<br>**可选值有**：<br>- `1`: 居左排版 - `2`: 居中排版 - `3`: 居右排版 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `reference_synced` | `reference_synced` | 引用同步块，仅支持查询。获取引用同步块内容详见：[如何获取引用同步块的内容](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/faq#19b71234) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_document_id` | `string` | 源文档的文档 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_block_id` | `string` | 源同步块的 Block ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sub_page_list` | `sub_page_list` | Wiki 新版子目录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wiki_token` | `string` | 知识库节点 token，仅支持知识库文档创建子页面列表，且需传入当前页面的 wiki token |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ai_template` | `ai_template` | AI 模板 Block，仅支持查询 |
| &nbsp;&nbsp;└ `document_revision_id` | `int` | 当前更新成功后文档的版本号 |
| &nbsp;&nbsp;└ `client_token` | `string` | 操作的唯一标识，更新请求中使用此值表示幂等的进行此次更新 |


### 响应体示例

```json
{
    "code": 0,
    "data": {
        "blocks": [
            {
                "block_id": "doxcn0K8iGSMW4Mqgs9qlyTP50d",
                "block_type": 2,
                "parent_id": "doxcnAJ9VRRJqVMYZ1MyKnayXWe",
                "text": {
                    "elements": [
                        {
                            "text_run": {
                                "content": "Hello",
                                "text_element_style": {
                                    "background_color": 2,
                                    "bold": true,
                                    "inline_code": false,
                                    "italic": true,
                                    "strikethrough": true,
                                    "text_color": 2,
                                    "underline": true
                                }
                            }
                        },
                        {
                            "text_run": {
                                "content": "World ",
                                "text_element_style": {
                                    "bold": false,
                                    "inline_code": false,
                                    "italic": true,
                                    "strikethrough": false,
                                    "underline": false
                                }
                            }
                        },
                        {
                            "mention_doc": {
                                "obj_type": 22,
                                "title": "Demo",
                                "token": "doxcnAJ9VRRJqVMYZ1MyKnayXWe",
                                "url": "https%3A%2F%2Ftest.feishu.cn%2Fdocx%2FdoxcnAJ9VRRJqVMYZ1MyKnayXWe"
                            }
                        }
                    ],
                    "style": {
                        "done": false,
                        "folded": false,
                        "wrap": false
                    }
                }
            },
            {
                "block_id": "doxcnk0i44OMOaouw8AdXuXrp6b",
                "block_type": 31,
                "children": [
                    "doxcnO2UeYco4mu80sr6oRCiRpf",
                    "doxcnaAGMYMk6kcGeYXNfc1Rluc",
                    "doxcnCKuqMQOM0gAOYfysUgZD2d",
                    "doxcnMKg8Uk8wiAMIW8omQ06uoc"
                ],
                "parent_id": "doxcnAJ9VRRJqVMYZ1MyKnayXWe",
                "table": {
                    "cells": [
                        "doxcnO2UeYco4mu80sr6oRCiRpf",
                        "doxcnaAGMYMk6kcGeYXNfc1Rluc",
                        "doxcnCKuqMQOM0gAOYfysUgZD2d",
                        "doxcnMKg8Uk8wiAMIW8omQ06uoc"
                    ],
                    "property": {
                        "column_size": 2,
                        "column_width": [
                            100,
                            100
                        ],
                        "merge_info": [
                            {
                                "col_span": 2,
                                "row_span": 1
                            },
                            {
                                "col_span": 1,
                                "row_span": 1
                            },
                            {
                                "col_span": 1,
                                "row_span": 1
                            },
                            {
                                "col_span": 1,
                                "row_span": 1
                            }
                        ],
                        "row_size": 2
                    }
                }
            }
        ],
        "client_token": "e472907a-9ddc-4453-af28-22a6530b76b9",
        "document_revision_id": 387
    },
    "msg": ""
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1770001 | invalid param | 确认传入的参数是否合法 |
| 404 | 1770002 | not found | **文档场景中**： 文档的 `document_id` 不存在。请确认文档是否已被删除或 `document_id` 是否填写正确。参考[文档概述](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-overview)了解如何获取文档的 `document_id`。 **群公告场景中**： 群 ID `chat_id` 不存在。请确认群是否被解散或 `chat_id` 是否填写正确。 |
| 400 | 1770003 | resource deleted | 确认资源是否已被删除 |
| 400 | 1770004 | too many blocks in document | 确认文档 Block 数量是否超上限 |
| 400 | 1770005 | too deep level in document | 确认文档 Block 层级是否超上限 |
| 400 | 1770006 | schema mismatch | 确认文档结构是否合法 |
| 400 | 1770007 | too many children in block | 确认指定 Block 的 Children 数量是否超上限 |
| 400 | 1770008 | too big file size | 确认上传的文件尺寸是否超上限 |
| 400 | 1770010 | too many table column | 确认表格列数是否超上限 |
| 400 | 1770011 | too many table cell | 确认表格单元格数量是否超上限 |
| 400 | 1770012 | too many grid column | 确认 Grid 列数量是否超上限 |
| 400 | 1770013 | relation mismatch | 图片、文件等资源的关联关系不正确。请确保在创建图片、文件块时，同时上传了相关图片或文件素材至对应的文档块中。详情参考文档[常见问题 3 和 4](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/faq#1908ddf0) |
| 400 | 1770014 | parent children relation mismatch | 确认 Block 父子关系是否正确 |
| 400 | 1770015 | single edit with multi document | 确认 Block 所属文档与指定的 Document 是否相同 |
| 400 | 1770019 | repeated blockID in document | 确认 Document 中的 BlockID 是否有重复 |
| 400 | 1770020 | operation denied on copying document | 确认 Document 是否正在创建副本中 |
| 400 | 1770021 | too old document | 确认指定的 Document 版本（Revision_id）是否过旧。指定的版本号与文档最新版本号差值不能超过 1000 |
| 400 | 1770022 | invalid page token | 确认查询参数中的 page_token 是否合法 |
| 400 | 1770024 | invalid operation | 确认操作是否合法: - 除了 text_run，其他 text_element 不允许设置 link 属性 - 编辑请求中 text_element 中不允许设置 undefined 元素  - 分栏的列数范围在 [2, 10] 之间，不允许减少或者增加分栏列数超过约定范围 - 表格只有一行或者一列时，不允许通过减少表格行列的请求操作表格 |
| 400 | 1770025 | operation and block not match | 确认指定 Block 应用对应操作是否合法 |
| 400 | 1770026 | row operation over range | 确认行操作下标是否越界 |
| 400 | 1770027 | column operation over range | 确认列操作下标是否越界 |
| 400 | 1770028 | block not support create children | 确认指定 Block 添加 Children 是否合法 |
| 400 | 1770029 | block not support to create | 确认指定 Block 是否支持创建 |
| 400 | 1770030 | invalid parent children relation | 确认指定操作其父子关系是否合法 |
| 400 | 1770031 | block not support to delete children | 确认指定 Block 是否支持删除 Children |
| 400 | 1770033 | content size exceed limit | 纯文本内容大小超过 10485760  字符限制，请减少内容后重试。 |
| 400 | 1770034 | operation count exceed limited | 当前请求中涉及单元格个数过多，请拆分成多次请求 |
| 400 | 1770035 | resource count exceed limit | 当前请求中资源的数目超限，请拆分成多次请求。各类资源上限为：ChatCard 200 张，File 200 个，MentionDoc 200 个，MentionUser 200 个，Image 20 张，ISV 20 个，Sheet 5 篇，Bitable 5 篇。 |
| 400 | 1770038 | resource not found | 未查询到插入的资源或资源无权限插入，请检查资源标识是否正确。 |
| 403 | 1770032 | forbidden | **文档场景中**： 确认当前调用身份是否有文档阅读（获取相关接口）或编辑（更新、删除、创建相关接口）权限。请参考以下方式解决：    - 如果你使用的是 `tenant_access_token`，意味着当前应用没有文档权限。你需通过云文档网页页面右上方 **「...」** -> **「...更多」** ->**「添加文档应用」** 入口为应用添加文档权限。        **说明**：在 **添加文档应用** 前，你需确保目标应用至少开通了一个云文档或多维表格的 [API 权限](https://open.larkoffice.com/document/ukTMukTMukTM/uYTM5UjL2ETO14iNxkTN/scope-list)。否则你将无法在文档应用窗口搜索到目标应用。     ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/22c027f63c540592d3ca8f41d48bb107_CSas7OYJBR.png?height=1994&maxWidth=550&width=3278)     - 如果你使用的是 `user_access_token`，意味着当前用户没有文档权限。你需通过云文档网页页面右上方 **分享** 入口为当前用户添加文档权限。    ![image.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/3e052d3bac56f9441296ae22e2969d63_a2DEYrJup8.png?height=278&maxWidth=550&width=1383)    了解具体操作步骤或其它添加权限方式，参考[云文档常见问题 3](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a)。 对于创建和更新相关接口，你还需要确认： - 当前调用身份是否有 MentionDoc 即 @文档 中文档的阅读权限 - MentionUser 即 @用户 中的用户是否在职且与当前调用身份互为联系人 - 当前调用身份是否具有群卡片的查看和分享权限 - 当前调用身份是否具有访问指定 Wiki 即知识库子目录的权限 - 当前调用身份是否具有 OKR、ISV、Add-Ons 等文档块的查看权限 **群公告场景中**： 当前的操作者没有群公告的编辑权限。解决方案： - 方案一：调用[指定群管理员](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/chat-managers/add_managers)接口，将当前操作者置为群管理员，然后重试。 - 方案二：在 **飞书客户端 > 群组 > 设置 > 群管理** 中，将 **谁可以编辑群信息** 设置为 **所有群成员**，然后重试。 对于创建和更新相关接口，你还需要确认： - 当前调用身份是否有 MentionDoc 即 @文档 中文档的阅读权限 - MentionUser 即 @用户 中的用户是否在职且与当前调用身份互为联系人 - 当前调用身份是否具有群卡片的查看和分享权限 - 当前调用身份是否具有访问指定 Wiki 即知识库子目录的权限 - 当前调用身份是否具有 OKR、ISV、Add-Ons 等文档块的查看权限 |
| 500 | 1771001 | server internal error | 服务器内部错误。请重试，若仍无法解决请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。 |
| 500 | 1771006 | mount folder failed | 挂载文档到云空间文件夹失败。请检查是否错误地传入了 wiki_token 并重试。若仍无法解决请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。 |
| 500 | 1771002 | gateway server internal error | 网关服务内部错误。请重试，若仍无法解决请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。 |
| 500 | 1771003 | gateway marshal error | 网关服务解析错误。请重试，若仍无法解决请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。 |
| 500 | 1771004 | gateway unmarshal error | 网关服务反解析错误。请重试，若仍无法解决请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。 |
| 503 | 1771005 | system under maintenance | 系统服务正在维护中，请重试，若仍无法解决请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |


