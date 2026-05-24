---
title: "批量获取消息表情回复"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message-reaction/batch_query"
updateTime: "1777424652000"
---

# 批量获取消息表情回复

支持批量分页的获取消息上的表情详情、支持批量获取消息上表情的统计


## 前提条件

- 应用身份调用接口需要开启[机器人能力](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-enable-bot-ability)。
- 调用当前接口的机器人或者用户，需要在待查询的消息所属的会话内。

## 使用限制

已被撤回的消息、消息不可见等情况无法获取表情回复列表。

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/im/v1/messages/reactions/batch_query |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `im:message.reactions:read` 查看消息表情回复 `im:message:readonly` 获取单聊、群组消息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `queries` | `message_query\[\]` | 是 | 要查询的消息<br>**数据校验规则**：<br>- 长度范围：`1` ～ `20` |
| &nbsp;&nbsp;└ `message_id` | `string` | 否 | 消息ID<br>**示例值**："om_8964d1b4*********2b31383276113" |
| &nbsp;&nbsp;└ `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果。<br>**示例值**："YhljsPiGfUgnVAg9urvRFd-BvSqRL20" |
| `page_size_per_message` | `int` | 否 | 每个消息最多返回多少个表情 **默认值：**10<br>**示例值**：10<br>**数据校验规则**：<br>- 取值范围：`1` ～ `10` |
| `reaction_type` | `string` | 否 | 待查询的表情类型，支持的枚举值参考[表情文案说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message-reaction/emojis-introduce)中的 emoji_type 值。<br>**注意**：该参数为可选参数，不传入该参数时将查询消息内所有的表情回复。<br>**示例值**："LAUGH" |


### 请求体示例

```json
{
    "queries": [
        {
            "message_id": "om_8964d1b4*********2b31383276113",
            "page_token": "YhljsPiGfUgnVAg9urvRFd-BvSqRL20"
        }
    ],
    "page_size_per_message": 10,
    "reaction_type": "LAUGH"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `success_msg_reaction_details` | `success_msg_reaction_details\[\]` | 成功获取到的表情列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `message_id` | `string` | 消息id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `message_reaction_items` | `reaction\[\]` | 表情实体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reaction_id` | `string` | 表情ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `operator` | `operator` | 操作者信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `operator_id` | `string` | 操作人ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `operator_type` | `string` | 操作人身份，用户或应用<br>**可选值有**：<br>- `app`: 应用 - `user`: 用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `action_time` | `string` | 表情添加时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `emoji_type` | `string` | 表情类型 |
| &nbsp;&nbsp;└ `success_msg_reaction_counts` | `success_msg_reaction_count\[\]` | 每条消息上所有表情的数量统计 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `message_id` | `string` | 消息ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `reaction_count` | `reaction_count\[\]` | 消息上不同表情的数量 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reaction_type` | `string` | 表情类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `count` | `string` | 表情数量 |
| &nbsp;&nbsp;└ `fail_msg_reaction_details` | `fail_msg_reaction_details\[\]` | 未成功获取的消息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `message_id` | `string` | 消息id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `fail_reason` | `string` | 获取表情失败的原因<br>**可选值有**：<br>- `invalid`: 无效的消息ID - `invalid_page_token`: 该消息对应的page_token无效 - `no_permission`: 操作者对该消息无权限 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "success_msg_reaction_details": [
            {
                "message_id": "om_a8f2294b************a1a38afaac9d",
                "has_more": true,
                "page_token": "NzYxNDA2NjMyNzA3Mzg1Mjk0NDoy",
                "message_reaction_items": [
                    {
                        "reaction_id": "ZCaCIjUBVVWSrm5L-3ZTw****",
                        "operator": {
                            "operator_id": "ou_ff0b7ba35fb********67dfc8b885136",
                            "operator_type": "user"
                        },
                        "action_time": "1626086391570",
                        "emoji_type": "SMILE"
                    }
                ]
            }
        ],
        "success_msg_reaction_counts": [
            {
                "message_id": "om_8964d1b4*********2b31383276113",
                "reaction_count": [
                    {
                        "reaction_type": "LAUGH",
                        "count": "20"
                    }
                ]
            }
        ],
        "fail_msg_reaction_details": [
            {
                "message_id": "om_8964d1b4*********2b31383276113",
                "fail_reason": "invalid"
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 230001 | Your request contains an invalid request parameter. | 参数错误，可根据接口实际返回的错误信息，并参考接口文档内容，检查输入参数是否填写错误。 |
| 400 | 230006 | Bot ability is not activated. | 应用未启用机器人能力。启用方式参见[如何启用机器人能力](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-enable-bot-ability)。 |


