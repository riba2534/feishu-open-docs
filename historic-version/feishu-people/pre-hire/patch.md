---
title: "更新待入职信息（不推荐）"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/pre_hire/patch"
updateTime: "1720766086000"
---

# 更新待入职信息（不推荐）

更新待入职信息接口，本接口只是会更新待入职数据，不会校验数据规则，推荐使用新接口[【更新待入职信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/pre_hire/patch)。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/pre_hires/:pre_hire_id |
| HTTP Method | PATCH |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:corehr` 更新核心人事信息 `corehr:pre_hire:write` 读写待入职人员信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `pre_hire_id` | `string` | 待入职ID<br>**示例值**："1616161616" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `client_token` | `string` | 否 | 根据client_token是否一致来判断是否为同一请求<br>**示例值**：12454646 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `ats_application_id` | `string` | 否 | 招聘投递 ID ，详细信息可以通过招聘的【获取投递信息】接口查询获得（仅部分租户可用）<br>**示例值**："4719168654814483759" |
| `hire_date` | `string` | 否 | 入职日期<br>**示例值**："2020-01-01" |
| `employee_type` | `enum` | 否 | 雇佣类型 |
| &nbsp;&nbsp;└ `enum_name` | `string` | 是 | 枚举值<br>**示例值**："type_1" |
| `worker_id` | `string` | 否 | 人员编号<br>**示例值**："1245646" |
| `employee_type_id` | `string` | 否 | 雇佣类型<br>**示例值**："正式" |
| `person_id` | `string` | 否 | 引用Person ID<br>**示例值**："656464648662" |
| `custom_fields` | `object_field_data\[\]` | 否 | 自定义字段 |
| &nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："name" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(如123, 123.23, "true", [\"id1\",\"id2\"], "2006-01-02 15:04:05")<br>**示例值**："\"Sandy\"" |
| `cost_center_rate` | `support_cost_center_item\[\]` | 否 | 成本中心分摊信息 |
| &nbsp;&nbsp;└ `cost_center_id` | `string` | 否 | 支持的成本中心id<br>**示例值**："6950635856373745165" |
| &nbsp;&nbsp;└ `rate` | `int` | 否 | 分摊比例<br>**示例值**：100 |
| `onboarding_status` | `enum` | 是 | 入职状态<br>- 待入职(preboarding)<br>- 已删除(deleted)<br>- 准备就绪(day_one)<br>- 已撤销(withdrawn)<br>- 已完成(completed) |
| &nbsp;&nbsp;└ `enum_name` | `string` | 是 | 枚举值<br>**示例值**："type_1" |


### 请求体示例

```json
{
    "ats_application_id": "4719168654814483759",
    "hire_date": "2020-01-01",
    "employee_type": {
        "enum_name": "type_1"
    },
    "worker_id": "1245646",
    "employee_type_id": "正式",
    "person_id": "656464648662",
    "custom_fields": [
        {
            "field_name": "name",
            "value": "\"Sandy\""
        }
    ],
    "cost_center_rate": [
        {
            "cost_center_id": "6950635856373745165",
            "rate": 100
        }
    ],
    "onboarding_status": {
        "enum_name": "type_1"
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
| &nbsp;&nbsp;└ `pre_hire` | `pre_hire` | 待入职数据 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ats_application_id` | `string` | 招聘投递 ID ，详细信息可以通过招聘的【获取投递信息】接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 待入职ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `hire_date` | `string` | 入职日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type` | `enum` | 雇佣类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `worker_id` | `string` | 人员编号 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type_id` | `string` | 雇佣类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `person_id` | `string` | 引用Person ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(如123, 123.23, "true", [\"id1\",\"id2\"], "2006-01-02 15:04:05") |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_rate` | `support_cost_center_item\[\]` | 成本中心分摊信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_id` | `string` | 支持的成本中心id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rate` | `int` | 分摊比例 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `onboarding_status` | `enum` | 入职状态<br>- 待入职(preboarding)<br>- 已删除(deleted)<br>- 准备就绪(day_one)<br>- 已撤销(withdrawn)<br>- 已完成(completed) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "pre_hire": {
            "ats_application_id": "4719168654814483759",
            "id": "154545454",
            "hire_date": "2020-01-01",
            "employee_type": {
                "enum_name": "type_1",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "刘梓新"
                    }
                ]
            },
            "worker_id": "1245646",
            "employee_type_id": "正式",
            "person_id": "656464648662",
            "custom_fields": [
                {
                    "field_name": "name",
                    "value": "\"Sandy\""
                }
            ],
            "cost_center_rate": [
                {
                    "cost_center_id": "6950635856373745165",
                    "rate": 100
                }
            ],
            "onboarding_status": {
                "enum_name": "type_1",
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


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1161019 | Duplicate cost center | Please check cost_center_id in cost_center_rate |
| 400 | 1161020 | The number of allocation proportion must be an integer from 1 to 100 | Please check rate in cost_center_rate |
| 400 | 1161021 | Incomplete cost center data | Please check cost_center_rate |
| 400 | 1161022 | No cost centers found | Please check cost_center_id in cost_center_rate |
| 400 | 1161023 | The total allocation proportion of all cost centers must be 100% | Please check the sum of rate in cost_center_rate |
| 400 | 1161024 | Cost center is deactivated | Please check cost_center_id in cost_center_rate |
| 400 | 1161025 | Cost center  will be disabled | Please check cost_center_id in cost_center_rate |
| 500 | 1160025 | Please check description | Please check suggestion |


