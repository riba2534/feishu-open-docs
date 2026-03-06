---
title: "查询指定工单详情"
fullPath: "/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/ticket/get"
updateTime: "1741783326000"
---

# 查询指定工单详情

该接口用于获取单个服务台工单详情。仅支持自建应用。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/helpdesk/v1/tickets/:ticket_id |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `helpdesk:all:readonly` 获取服务台资源详情 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


> **Tip**: 服务台请求Header中还需添加“服务台token”参数：
>   
>   Key: X-Lark-Helpdesk-Authorization
>   
>   Value: base64(helpdesk_id:helpdesk_token)，通过base64加密将helpdesk_id和helpdesk_token用':'连接而成的字符串。
>   
>   [了解更多：获取与使用服务台token](https://open.larkoffice.com/document/ukTMukTMukTM/ugDOyYjL4gjM24CO4IjN)


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `ticket_id` | `string` | 工单 ID。可通过[查询全部工单详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/ticket/list)获取<br>**示例值**："123456" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `ticket` | `ticket_v2` | 工单详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ticket_id` | `string` | 工单ID<br>[可以从工单列表里面取](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/ticket/list)<br>[也可以订阅工单创建事件获取](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/ticket/events/created) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `helpdesk_id` | `string` | 服务台ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `guest` | `ticket_user` | 工单创建用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_url` | `string` | 用户头像url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 用户邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `string` | 所在部门名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city` | `string` | 城市 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country` | `string` | 国家代号(CountryCode)，参考：http://www.mamicode.com/info-detail-2186501.html |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `comments` | `comments` | 备注 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 备注 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `int` | 备注时间，单位毫秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `int` | 备注ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_avatar_url` | `string` | 备注人头像 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_name` | `string` | 备注人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `int` | 备注人ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ticket_type` | `int` | 工单阶段：1. 机器人 2. 人工 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 工单状态，1：已创建 2: 处理中 3: 排队中 4：待定 5：待用户响应 50: 被机器人关闭 51: 被客服关闭 52: 用户自己关闭 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `score` | `int` | 工单评分，1：不满意，2:一般，3:满意 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `int` | 工单创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_at` | `int` | 工单更新时间，没有值时为-1 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `closed_at` | `int` | 工单结束时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dissatisfaction_reason` | `i18n` | 不满意原因 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 日文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agents` | `ticket_user\[\]` | 工单客服 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_url` | `string` | 用户头像url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 用户邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `string` | 所在部门名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city` | `string` | 城市 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country` | `string` | 国家代号(CountryCode)，参考：http://www.mamicode.com/info-detail-2186501.html |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `channel` | `int` | 工单渠道，描述： 9：Open API 2：二维码 14：分享 13：搜索 其他数字：其他渠道 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `solve` | `int` | 工单是否解决 1:没解决 2:已解决 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `closed_by` | `ticket_user` | 关单用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_url` | `string` | 用户头像url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 用户邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `string` | 所在部门名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city` | `string` | 城市 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country` | `string` | 国家代号(CountryCode)，参考：http://www.mamicode.com/info-detail-2186501.html |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `collaborators` | `ticket_user\[\]` | 工单协作者 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_url` | `string` | 用户头像url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 用户邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `string` | 所在部门名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city` | `string` | 城市 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country` | `string` | 国家代号(CountryCode)，参考：http://www.mamicode.com/info-detail-2186501.html |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `customized_fields` | `customized_field_display_item\[\]` | 自定义字段列表，没有值时不设置   下拉菜单的value对应工单字段里面的children.display_name [获取全部工单自定义字段](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/ticket_customized_field/list-ticket-customized-fields) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 自定义字段ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key_name` | `string` | 键名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_name` | `string` | 展示名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `position` | `int` | 展示位置 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `required` | `boolean` | 是否必填 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `editable` | `boolean` | 是否可修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agent_service_duration` | `number(float)` | 客服服务时长，客服最后一次回复时间距离客服进入时间间隔，单位分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agent_first_response_duration` | `int` | 客服首次回复时间距离客服进入时间的间隔(秒) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `bot_service_duration` | `int` | 机器人服务时间：客服进入时间距离工单创建时间的间隔，单位秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agent_resolution_time` | `int` | 客服解决时长，从首位客服接入服务到工单关闭的用时，单位秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `actual_processing_time` | `int` | 工单实际处理时长，处理时长=解决时长-工单待定时长（将工单状态修改为待定后的时间），单位秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agent_entry_time` | `int` | 客服进入时间，单位毫秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agent_first_response_time` | `int` | 客服首次回复时间，单位毫秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agent_last_response_time` | `int` | 客服最后回复时间，单位毫秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agent_owner` | `ticket_user` | 主责客服 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_url` | `string` | 用户头像url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 用户邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `string` | 所在部门名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city` | `string` | 城市 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country` | `string` | 国家代号(CountryCode)，参考：http://www.mamicode.com/info-detail-2186501.html |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tags` | `ticket_tag\[\]` | 工单标签（仅工单含有工单标签会返回） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 标签 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 标签 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "ticket": {
            "ticket_id": "6626871355780366331",
            "helpdesk_id": "6626871355780366330",
            "guest": {
                "id": "ou_37019b7c830210acd88fdce886e25c71",
                "avatar_url": "https://xxxx",
                "name": "abc",
                "email": "xxxx@abc.com",
                "department": "用户部门名称(有权限才展示)",
                "city": "城市",
                "country": "国家"
            },
            "comments": {
                "content": "备注内容",
                "created_at": 1690970837624,
                "id": 12,
                "user_avatar_url": "备注人头像",
                "user_name": "备注人姓名",
                "user_id": 7262656095919128578
            },
            "ticket_type": 1,
            "status": 50,
            "score": 1,
            "created_at": 1616920429000,
            "updated_at": 1616920429000,
            "closed_at": 1616920429000,
            "dissatisfaction_reason": {
                "zh_cn": "答案看不懂",
                "en_us": "I don't understand",
                "ja_jp": "回答が複雑すぎる"
            },
            "agents": [
                {
                    "id": "ou_37019b7c830210acd88fdce886e25c71",
                    "avatar_url": "https://xxxx",
                    "name": "abc",
                    "email": "xxxx@abc.com",
                    "department": "用户部门名称(有权限才展示)",
                    "city": "城市",
                    "country": "国家"
                }
            ],
            "channel": 0,
            "solve": 1,
            "closed_by": {
                "id": "ou_37019b7c830210acd88fdce886e25c71",
                "avatar_url": "https://xxxx",
                "name": "abc",
                "email": "xxxx@abc.com",
                "department": "用户部门名称(有权限才展示)",
                "city": "城市",
                "country": "国家"
            },
            "collaborators": [
                {
                    "id": "ou_37019b7c830210acd88fdce886e25c71",
                    "avatar_url": "https://xxxx",
                    "name": "abc",
                    "email": "xxxx@abc.com",
                    "department": "用户部门名称(有权限才展示)",
                    "city": "城市",
                    "country": "国家"
                }
            ],
            "customized_fields": [
                {
                    "id": "123",
                    "value": "value",
                    "key_name": "key",
                    "display_name": "display name",
                    "position": 1,
                    "required": true,
                    "editable": true
                }
            ],
            "agent_service_duration": 42624.95,
            "agent_first_response_duration": 123869,
            "bot_service_duration": 1,
            "agent_resolution_time": 66,
            "actual_processing_time": 68,
            "agent_entry_time": 1636444596000,
            "agent_first_response_time": 1636444696000,
            "agent_last_response_time": 1636444796000,
            "agent_owner": {
                "id": "ou_37019b7c830210acd88fdce886e25c71",
                "avatar_url": "https://xxxx",
                "name": "abc",
                "email": "xxxx@abc.com",
                "department": "用户部门名称(有权限才展示)",
                "city": "城市",
                "country": "国家"
            },
            "tags": [
               {
                   "id": "7474857595946745884",
                   "name": "标签名称"
               }
           ]
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 154000 | Bad request, please check your request body | 请求不合法，请检查路径参数 `ticket_id` 填写是否正确 |
| 500 | 155000 | Internal error | 内部错误，请联系我们 |
| 404 | 154004 | Resource not found | 资源不存在，请检查ID值 |
| 401 | 154001 | Unauthorized, please check you have the correct access | 检查Authorization 和 X-Lark-Helpdesk-Authorization 是否正确，应用和服务台属于同一租户 |


