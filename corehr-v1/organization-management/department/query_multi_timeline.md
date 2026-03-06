---
title: "批量查询部门版本信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/query_multi_timeline"
updateTime: "1770621157000"
---

# 批量查询部门版本信息

根据部门ID列表，批量查询开始结束时间内的所有部门版本信息，含部门名称、部门类型、上级、编码、负责人、是否启用、描述等信息


> **Warning**: - 延迟说明：数据库主从延迟 2s 以内，即：直接创建部门后2s内调用此接口可能查询不到数据。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/departments/query_multi_timeline |
| HTTP Method | POST |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:department:read` 获取部门信息 `corehr:department:write` 读写部门信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `corehr:department.custom_fields:read` 获取部门自定义字段 `corehr:department.manager:read` 获取部门负责人信息 `corehr:department.organize:read` 获取部门组织架构信息 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 是 | 分页大小，最大 100<br>**示例值**：100<br>**数据校验规则**：<br>- 取值范围：`1` ～ `100` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：6891251722631890445 |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：people_corehr_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`people_corehr_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 此次调用中使用的部门 ID 类型<br>**示例值**：people_corehr_department_id<br>**可选值有**：<br>- `open_department_id`: 【飞书】用来在具体某个应用中标识一个部门，同一个department_id 在不同应用中的 open_department_id 相同。 - `department_id`: 【飞书】用来标识租户内一个唯一的部门。 - `people_corehr_department_id`: 【飞书人事】用来标识「飞书人事」中的部门。<br>**默认值**：`people_corehr_department_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `department_ids` | `string\[\]` | 是 | 部门 ID 列表，可请求[搜索部门信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/search)获取。<br>**示例值**：["7094136522860922111"]<br>**数据校验规则**：<br>- 长度范围：`1` ～ `10` |
| `effective_date_start` | `string` | 否 | 生效日期开始(包含)<br>**示例值**："2024-01-01"<br>**数据校验规则**：<br>- 长度范围：`10` ～ `10` 字符 - 正则校验：`^((([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29))$` |
| `effective_date_end` | `string` | 否 | 生效日期结束(包含)<br>**示例值**："2024-12-31"<br>**数据校验规则**：<br>- 长度范围：`10` ～ `10` 字符 - 正则校验：`^((([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29))$` |
| `fields` | `string\[\]` | 否 | 需要返回的字段列表，字段可填写的列表如下： - department_name - sub_type - code - active - parent_department_id - manager - description - effective_date - expiration_date - custom_fields(自定义字段需传入具体的"custom_api_name"详细见[获取自定义字段列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query) ,比如:"shifouleixing_7795__c)<br>**示例值**：["department_name"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |


### 请求体示例

```json
{
    "department_ids": [
        "7094136522860922111"
    ],
    "effective_date_start": "2024-01-01",
    "effective_date_end": "2024-12-31",
    "fields": [
        "department_name"
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
| &nbsp;&nbsp;└ `items` | `department_timeline\[\]` | 部门信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 部门 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `version_id` | `string` | 部门版本 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `names` | `i18n\[\]` | 部门名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言，中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sub_type` | `enum` | 部门类型 - 通过[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)查询获取。请求参数：object_api_name=department；custom_api_name=subtype。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `parent_department_id` | `string` | 上级部门 ID  - 详细信息可通过[【查询单个部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)接口获得 - 若查询的是一级部门，则该字段不展示<br>**字段权限要求**： `corehr:department.organize:read` 获取部门组织架构信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `manager` | `string` | 部门负责人雇佣 ID，枚举值及详细信息可通过[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口查询获得<br>**字段权限要求**： `corehr:department.manager:read` 获取部门负责人信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_date` | `string` | 生效日期 - 返回格式：YYYY-MM-DD（最小单位到日） - 日期范围:1900-01-01～9999-12-31 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 是否启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `descriptions` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言，支持中文和英文。中文用zh-CN；英文用en-US。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段类型，详细见[获取自定义字段列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query) <br>**字段权限要求**： `corehr:department.custom_fields:read` 获取部门自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型，详细见[获取自定义字段列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_date` | `string` | 失效日期 - 返回格式：YYYY-MM-DD （最小单位到日） - 日期范围:1900-01-01 ～9999-12-31 |
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
                "id": "4719456877659520852",
                "version_id": "7238516215202170412",
                "names": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ],
                "sub_type": {
                    "enum_name": "phone_type",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "parent_department_id": "4719456877659520111",
                "manager": "6893013238632416777",
                "code": "D00000456",
                "effective_date": "2020-05-01",
                "active": true,
                "descriptions": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ],
                "custom_fields": [
                    {
                        "custom_api_name": "name",
                        "name": {
                            "zh_cn": "自定义姓名",
                            "en_us": "Custom Name"
                        },
                        "type": 1,
                        "value": "\"231\""
                    }
                ],
                "expiration_date": "2020-05-02"
            }
        ],
        "page_token": "eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0=",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 503 | 1161204 | Request timeout | 联系飞书人事 Oncall |
| 429 | 1161604 | QPS over limit | 联系飞书人事 Oncall |


