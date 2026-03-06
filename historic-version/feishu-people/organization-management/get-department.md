---
title: "查询单个部门"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get"
updateTime: "1725613225000"
---

# 查询单个部门

该接口支持通过部门id批量查询当天的部门详情信息，包括部门包含的名称、描述、启用状态等。


> **Error**: 本接口不再推荐使用（不支持更复杂的字段鉴权功能），请使用[批量查询部门V2](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)接口（支持对成本中心、部门负责人、自定义字段鉴权）。


> **Warning**: 延迟说明：数据库主从延迟 2s 以内，即：直接创建职级后2s内调用此接口可能查询不到数据。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/departments/:department_id |
| HTTP Method | GET |
| 接口频率限制 | [特殊频控](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:corehr:readonly` 获取核心人事信息 `corehr:corehr` 更新核心人事信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `department_id` | `string` | 部门ID。ID获取方式： - 调用[【创建部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/create)[【搜索部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/search)等接口可以返回部门ID - 也可以通过[【事件】创建部门](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/events/created)[【事件】更新部门](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/events/updated) 获取部门ID信息<br>**示例值**："45456564" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：people_corehr_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`people_corehr_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 此次调用中使用的部门 ID 类型<br>**示例值**：people_corehr_department_id<br>**可选值有**：<br>- `open_department_id`: 以 open_department_id 来标识部门 - `department_id`: 以 department_id 来标识部门 - `people_corehr_department_id`: 以 people_corehr_department_id 来标识部门<br>**默认值**：`people_corehr_department_id` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `department` | `department` | 部门信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 部门 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sub_type` | `enum` | 部门类型，通过[获取字段详情](https://open.larkoffice.com/document/server-docs/corehr-v1/basic-infomation/custom_field/get_by_param)查询获取。请求参数：object_api_name=department；custom_api_name=subtype。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 枚举值信息的语言，中文为zh-CN，英文为en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 枚举值信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `manager` | `string` | 部门负责人ID - 详细信息可通过[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search) 或 [【批量查询员工】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get) 接口获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_confidential` | `boolean` | 是否保密（该字段暂无功能支持，可忽略） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `hiberarchy_common` | `hiberarchy_common` | 组织实体公共字段，包括名称、描述、上级、启停用状态、生效日期、编码等基础信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `parent_id` | `string` | 上级部门 ID ，详细信息可通过[【查询单个部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)接口获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言，中文为zh-CN，英文为en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `enum` | 组织类型，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)组织类型（organization_type）枚举定义部分获得 - 该接口返回值为固定值：department |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 枚举值信息的语言，中文为zh-CN，英文为en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 枚举值信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 是否启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 当前版本生效日期（和data.effective_time内容一致） - 返回格式：YYYY-MM-DD 00:00:00（最小单位到日） - 日期范围:1900-01-01 00:00:00～9999-12-31 23:59:59 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 当前版本失效日期（和data.expiration_time内容一致） - 返回格式：YYYY-MM-DD 00:00:00（最小单位到日） - 日期范围:1900-01-01 00:00:00～9999-12-31 23:59:59 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 描述信息的语言，中文为zh-CN，英文为en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 描述信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tree_order` | `string` | 树形排序，代表同层级的部门排序序号 - 创建部门场景tree_order不会实时生成，10分钟内更新完毕 - 在页面拖动部门排序时tree_order可以实时生成 - 变更部门上级时，会清空tree_order，并触发重算list_order和tree_order，10分钟内更新完毕 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `list_order` | `string` | ListOrder 列表排序，代表所有部门的混排序号，为该部门上级路径上所有tree_order用“-”拼接。 - 该字段在新建/更新场景非立即更新，10分钟后会延迟更新 - 由于list_order变更会导致[部门变更接口](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/events/updated)产生大量事件，因此事件接口不会针对该字段同步变更事件，如果有需求订阅请联系Oncall单独开启。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段类型，详细见[获取自定义字段列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 自定义字段 API Name，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同。如：```("\"123\"", "\"123.23\"", "\"true\"", [\"id1\",\"id2\"], \"2006-01-02 15:04:05\")``` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 当前版本生效日期（和data. hiberarchy_common. effective_time内容一致） - 返回格式：YYYY-MM-DD 00:00:00（最小单位到日） - 日期范围:1900-01-01 00:00:00～9999-12-31 23:59:59 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 当前版本失效日期（和data. hiberarchy_common.expiration_time内容一致） - 返回格式：YYYY-MM-DD 00:00:00（最小单位到日） - 日期范围:1900-01-01 00:00:00～9999-12-31 23:59:59 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段类型，详细见[获取自定义字段列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 自定义字段 API Name，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(如123, 123.23, "true", [\"id1\",\"id2\"], "2006-01-02 15:04:05") |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_id` | `string` | 成本中心id，详细信息可通过[【搜索成本中心信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `staffing_model` | `enum` | 岗职管理模式 - 详细枚举类型请查看[枚举场景](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)中关于staffing_model定义 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言，中文为zh-CN，英文为en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "department": {
            "id": "6969828847121885087",
            "sub_type": {
                "enum_name": "type_1",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ]
            },
            "manager": "6893013238632416776",
            "is_confidential": true,
            "hiberarchy_common": {
                "parent_id": "4719168654814483759",
                "name": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ],
                "type": {
                    "enum_name": "type_1",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "张三"
                        }
                    ]
                },
                "active": true,
                "effective_time": "2020-05-01 00:00:00",
                "expiration_time": "2020-05-02 00:00:00",
                "code": "12456",
                "description": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ],
                "tree_order": "001000",
                "list_order": "001000-001000",
                "custom_fields": [
                    {
                        "field_name": "name",
                        "value": "\"Sandy\""
                    }
                ]
            },
            "effective_time": "2020-05-01 00:00:00",
            "expiration_time": "2020-05-02 00:00:00",
            "custom_fields": [
                {
                    "field_name": "name",
                    "value": "\"Sandy\""
                }
            ],
            "cost_center_id": "7142384817131652652",
            "staffing_model": {
                "enum_name": "position",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "刘梓新"
                    }
                ]
            }
        }
    }
}
```


