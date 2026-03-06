---
title: "获取清单列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/task-v2/tasklist/list"
updateTime: "1699520950000"
---

# 获取清单列表

获取调用身份所有可读取的清单列表。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/task/v2/tasklists |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `task:tasklist:read` 查看任务清单 `task:tasklist:write` 查看、创建、更新、删除任务清单 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 每页返回的清单数量<br>**示例值**：50<br>**默认值**：`50`<br>**数据校验规则**：<br>- 取值范围：`1` ～ `100` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：aWQ9NzEwMjMzMjMxMDE= |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**默认值**：`open_id` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `tasklist\[\]` | 清单数据列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `guid` | `string` | 清单的全局唯一ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 清单名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `creator` | `member` | 清单创建者 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 表示member的id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 成员类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `role` | `string` | 清单角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `owner` | `member` | 清单负责人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 表示member的id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 成员类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `role` | `string` | 成员角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `members` | `member\[\]` | 清单协作成员列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 表示member的id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 成员的类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `role` | `string` | 成员角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 该清单分享的applink |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `string` | 清单创建时间戳(ms) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_at` | `string` | 清单最后一次更新时间戳（ms) |
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
                "guid": "cc371766-6584-cf50-a222-c22cd9055004",
                "name": "年会总结工作任务清单",
                "creator": {
                    "id": "ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f",
                    "type": "user",
                    "role": "creator"
                },
                "owner": {
                    "id": "ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f",
                    "type": "user",
                    "role": "owner"
                },
                "members": [
                    {
                        "id": "ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f",
                        "type": "user",
                        "role": "editor"
                    }
                ],
                "url": "https://applink.feishu.cn/client/todo/task_list?guid=b45b360f-1961-4058-b338-7f50c96e1b52",
                "created_at": "1675742789470",
                "updated_at": "1675742789470"
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
| 400 | 1470400 | 请求参数错误，例如将page_size设为负数等。 | 错误原因见返回的msg提示的信息。 |
| 500 | 1470500 | 服务器错误。 | 尝试重试调用。如持续失败，请联系支持人员进行反馈。 |


