---
title: "获取评论列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/task-v2/comment/list"
updateTime: "1689560303000"
---

# 获取评论列表

给定一个资源，返回该资源的评论列表。

支持分页。评论可以按照创建时间的正序（asc, 从最老到最新），或者逆序（desc，从最老到最新），返回数据。


> **Tip**: 获取任务的评论列表需要任务的读取权限，详见[任务是如何鉴权的？](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/faq)


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/task/v2/comments |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `task:comment:read` 查看任务评论 `task:comment:write` 查看、创建、修改、删除任务评论 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 分页大小，默认为50。<br>**示例值**：50<br>**默认值**：`50`<br>**数据校验规则**：<br>- 取值范围：`1` ～ `100` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：aWQ9NzEwMjMzMjMxMDE=<br>**数据校验规则**：<br>- 最大长度：`100` 字符 |
| `resource_type` | `string` | 否 | 要获取评论列表的资源类型，目前只支持"task"，默认为"task"。<br>**示例值**：task<br>**默认值**：`task` |
| `resource_id` | `string` | 是 | 要获取评论的资源ID。例如要获取任务的评论列表，此处应该填写任务全局唯一ID<br>**示例值**：d300a75f-c56a-4be9-80d1-e47653028ceb |
| `direction` | `string` | 否 | 返回数据的排序方式。"asc"表示从最老到最新顺序返回；"desc"表示从最新到最老顺序返回。默认为"asc"。<br>**示例值**：asc<br>**可选值有**：<br>- `asc`: 评论发表时间升序 - `desc`: 评论发表时间降序<br>**默认值**：`asc` |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**默认值**：`open_id` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `comment\[\]` | 评论列表数据 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 评论id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 评论内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `creator` | `member` | 评论创建人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 表示member的id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 成员的类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `role` | `string` | 成员角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `reply_to_comment_id` | `string` | 被回复的评论的ID，如果不是回复评论，则为空。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `string` | 评论创建时间戳（ms) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_at` | `string` | 评论更新时间戳（ms） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `resource_type` | `string` | 任务关联的资源类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `resource_id` | `string` | 任务关联的资源ID |
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
                "id": "7197020628442939411",
                "content": "这是一条评论",
                "creator": {
                    "id": "ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f",
                    "type": "user",
                    "role": "creator"
                },
                "reply_to_comment_id": "7166825117308174356",
                "created_at": "1675742789470",
                "updated_at": "1675742789470",
                "resource_type": "task",
                "resource_id": "ccb55625-95d2-2e80-655f-0e40bf67953f"
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
| 400 | 1470400 | 请求参数错误，如传入了不支持的resource_type。 | 错误原因见返回的msg提示的信息。 |
| 404 | 1470404 | 要获取列表的资源不存在或已删除。 | 确认要获取列表的资源不存在或已删除。 |
| 500 | 1470500 | 服务器错误。 | 尝试重试调用。如持续失败，请联系支持人员进行反馈。 |
| 403 | 1470403 | 缺少获取评论列表的权限。 | 获取一个任务的评论列表需要该任务的读取权限，详见[任务是如何鉴权的？](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/faq) |


