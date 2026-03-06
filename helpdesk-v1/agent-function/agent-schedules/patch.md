---
title: "更新客服工作日程"
fullPath: "/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/agent-schedules/patch"
updateTime: "1709724838000"
---

# 更新客服工作日程

该接口用于更新客服的日程。


> **Tip**: 注意事项：
> 	user_access_token 访问，需要操作者是当前服务台的管理员或所有者


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/helpdesk/v1/agents/:agent_id/schedules |
| HTTP Method | PATCH |
| 接口频率限制 | [特殊频控](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `helpdesk:all` 更新服务台资源详情 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


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
| `agent_id` | `string` | 客服 id<br>**示例值**："123456" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `agent_schedule` | `agent_schedule_update_info` | 否 | 工作日程列表 |
| &nbsp;&nbsp;└ `schedule` | `weekday_schedule\[\]` | 否 | 工作日程列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 否 | 开始时间, format 00:00 - 23:59<br>**示例值**："00:00" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 否 | 结束时间, format 00:00 - 23:59<br>**示例值**："24:00" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `weekday` | `int` | 否 | 星期几, 1 - Monday, 2 - Tuesday, 3 - Wednesday, 4 - Thursday, 5 - Friday, 6 - Saturday, 7 - Sunday, 9 - Everday, 10 - Weekday, 11 - Weekend<br>**示例值**：9 |
| &nbsp;&nbsp;└ `agent_skill_ids` | `string\[\]` | 否 | 客服技能 ids<br>**示例值**：["test-skill-id"] |


### 请求体示例

```json
{
    "agent_schedule": {
        "schedule": [
            {
                "start_time": "00:00",
                "end_time": "24:00",
                "weekday": 9
            }
        ],
        "agent_skill_ids": [
            "test-skill-id"
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
| `data` | `\-` | \- |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {}
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 154000 | Bad request, please check your request body | 请求不合法，请检查参数 |
| 403 | 154003 | Please check you have the correct access | 检查是否申请正确权限 |
| 500 | 155000 | Internal error | 内部错误，请联系我们 |


