---
title: "查询人才操作记录"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/talent_operation_log/search"
updateTime: "1724383049000"
---

# 查询人才操作记录

根据操作人和操作类型查询人才的操作记录。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/talent_operation_logs/search |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:talent:readonly` 获取人才信息 `hire:talent` 更新人才信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：eyJvZmZzZXQiOjEwLCJ0aW1lc3RhbXAiOjE2Mjc1NTUyMjM2NzIsImlkIjpudWxsfQ== |
| `page_size` | `int` | 否 | 分页大小<br>**示例值**：10<br>**默认值**：`10`<br>**数据校验规则**：<br>- 最大值：`100` |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `job_id_list` | `string\[\]` | 否 | 职位 ID 列表，可通过[获取职位列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/list)接口获取<br>**示例值**：["6949805467799537965"] |
| `operator_id_list` | `string\[\]` | 是 | 操作人 ID 列表，与入参 `user_id_type` 类型一致<br>**示例值**：["ou_b29276c7c3e2ff4bd3fcfb567ce690e3"] |
| `operation_list` | `int\[\]` | 是 | 操作类型 ID 列表，操作类型枚举可查看[枚举常量介绍](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/enum) 中 `操作类型枚举定义`<br>**示例值**：[1] |


### 请求体示例

```json
{
    "job_id_list": [
        "6949805467799537965"
    ],
    "operator_id_list": [
        "ou_b29276c7c3e2ff4bd3fcfb567ce690e3"
    ],
    "operation_list": [
        1
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
| &nbsp;&nbsp;└ `items` | `talent_operation_log\[\]` | 操作记录列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `application_id` | `string` | 投递 ID，详情可查看：[获取投递信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `talent_id` | `string` | 人才 ID，详情可参考：[获取人才信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/hire-v2/talent/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operator` | `id_name_object` | 操作人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 操作人 ID，与入参 `user_id_type` 类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 操作人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 操作人中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 操作人英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operation_type` | `int` | 操作类型，操作类型枚举可查看[枚举常量介绍](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/enum) 中 `操作类型枚举定义` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operation_time` | `string` | 操作时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operator_type` | `int` | 操作人类型<br>**注意**：当前只会返回类型为 `1`：员工 的操作记录<br>**可选值有**：<br>- `1`: 员工 |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |


### 响应体示例

```json
{
    "code": 0,
    "msg": "ok",
    "data": {
        "items": [
            {
                "application_id": "6949805467799537964",
                "talent_id": "6843547872837273223",
                "operator": {
                    "id": "ou_016632190e242d8c9eed0a542b00756c",
                    "name": {
                        "zh_cn": "张三",
                        "en_us": "Tom"
                    }
                },
                "operation_type": "3001",
                "operation_time": "1618500278663",
                "operator_type": 1
            }
        ],
        "has_more": true,
        "page_token": "eyJvZmZzZXQiOjEwLCJ0aW1lc3RhbXAiOjE2Mjc1NTUyMjM2NzIsImlkIjpudWxsfQ=="
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |


更多错误码信息，参见[通用错误码](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)。


