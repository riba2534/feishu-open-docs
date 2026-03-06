---
title: "更新评论"
fullPath: "/uAjLw4CM/ukTMukTMukTM/task-v2/comment/patch"
updateTime: "1691401988000"
---

# 更新评论

更新一条评论。

更新时，将`update_fields`字段中填写所有要修改的评论的字段名，同时在`comment`字段中填写要修改的字段的新值即可。更新接口规范详情见[功能概述](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/overview)中的“ 关于资源的更新”章节。

目前只支持更新评论的"conent"字段。


> **Tip**: 更新评论需要评论归属任务的读取权限，并且只能更新自己创建的评论。详情见[任务功能概述](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/task/overview)中的“任务是如何鉴权的？”章节。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/task/v2/comments/:comment_id |
| HTTP Method | PATCH |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `task:comment:write` 查看、创建、更新、删除任务评论 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `comment_id` | `string` | 要更新的评论ID<br>**示例值**："7198104824246747156"<br>**数据校验规则**：<br>- 最大长度：`100` 字符 |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**默认值**：`open_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `comment` | `input_comment` | 是 | 要更新的评论数据。 |
| &nbsp;&nbsp;└ `content` | `string` | 否 | 要更新的评论内容。如果更新该字段，不允许设为空，最大支持3000个utf8字符。<br>**示例值**："举杯邀明月，对影成三人"<br>**数据校验规则**：<br>- 最大长度：`10000` 字符 |
| `update_fields` | `string\[\]` | 是 | 要更新的字段，支持<br>- `content`: 评论内容<br>**示例值**：["content"] |


### 请求体示例

```json
{
    "comment": {
        "content": "举杯邀明月，对影成三人"
    },
    "update_fields": [
        "content"
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
| &nbsp;&nbsp;└ `comment` | `comment` | 更新后的评论 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 评论id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 评论内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `creator` | `member` | 评论创建人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 表示member的id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 成员的类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `role` | `string` | 成员角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `reply_to_comment_id` | `string` | 被回复评论的id。如果不是回复评论，则为空。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `string` | 评论创建时间戳（ms) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_at` | `string` | 评论更新时间戳（ms） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `resource_type` | `string` | 任务关联的资源类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `resource_id` | `string` | 任务关联的资源ID |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "comment": {
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
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1470400 | 请求参数错误，比如update_fields中填写了不支持的字段名。 | 错误原因见返回的msg提示的信息。 |
| 404 | 1470404 | 要更新的评论不存在或已删除。 | 确认要更新的评论是否存在或已删除。 |
| 500 | 1470500 | 服务器错误。 | 尝试重试调用。如持续失败，请联系支持人员进行反馈。 |
| 403 | 1470403 | 缺少更新评论的权限。 | 更新评论需要评论归属任务的读取权限，并且只能更新自己发出的评论。详情见[任务功能概述](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/task/overview)中的“任务是如何鉴权的？”章节。 |


