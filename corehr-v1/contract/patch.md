---
title: "更新合同"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/patch"
updateTime: "1739935999000"
---

# 更新合同

通过该接口可以更新员工合同相关信息，没有修改的参数会保留原值


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/contracts/:contract_id |
| HTTP Method | PATCH |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:corehr` 更新核心人事信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `contract_id` | `string` | 合同ID，该ID可以通过[【批量查询合同】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取<br>**示例值**："7091849027838838316" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `client_token` | `string` | 否 | 自定义值，根据client_token是否一致来判断是否为同一请求<br>**示例值**：227988d7-66da-4afb-9943-32e73d5cda8b |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `effective_time` | `string` | 否 | 合同开始日期<br>**示例值**："2050-01-01 00:00:00" |
| `expiration_time` | `string` | 否 | 合同实际结束日期，合同实际结束日期小于等于合同结束日期<br>**示例值**："9999-12-31 23:59:59" |
| `employment_id` | `string` | 否 | 该接口不能传递该参数，否则会更新失败。<br>**示例值**："空" |
| `contract_type` | `enum` | 否 | 合同类型，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)合同类型（contract_type）枚举定义部分获得 |
| &nbsp;&nbsp;└ `enum_name` | `string` | 是 | 枚举值<br>**示例值**："labor_contract" |
| `first_party_company_id` | `string` | 否 | 甲方, 引用Company的ID，详细信息可通过[【查询单个公司】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/get) 接口查询获得<br>**示例值**："6892686614112241165" |
| `person_id` | `string` | 否 | 该接口不能传递该参数，否则会更新失败。<br>**示例值**："空" |
| `custom_fields` | `object_field_data\[\]` | 否 | 自定义字段，预留，暂时不支持 |
| &nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："name" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(如123, 123.23, "true", [\"id1\",\"id2\"], "2006-01-02 15:04:05")<br>**示例值**："Sandy" |
| `duration_type` | `enum` | 否 | 期限类型，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)合同期限类型（duration_type）枚举定义部分获得<br>**示例值**：fixed_term |
| &nbsp;&nbsp;└ `enum_name` | `string` | 是 | 枚举值<br>**示例值**："open_ended" |
| `contract_end_date` | `string` | 否 | 合同预计的结束日期<br>**示例值**："2006-01-02" |
| `contract_number` | `string` | 否 | 合同编号<br>**示例值**："6919737965274990093" |
| `signing_type` | `enum` | 否 | 签订类型，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)签订类型（signing_type）枚举定义部分获得 |
| &nbsp;&nbsp;└ `enum_name` | `string` | 是 | 枚举值<br>**示例值**："new" |


### 请求体示例

```json
{
    "effective_time": "2050-01-01 00:00:00",
    "expiration_time": "9999-12-31 23:59:59",
    "employment_id": "空",
    "contract_type": {
        "enum_name": "labor_contract"
    },
    "first_party_company_id": "6892686614112241165",
    "person_id": "空",
    "custom_fields": [
        {
            "field_name": "name",
            "value": "Sandy"
        }
    ],
    "duration_type": {
        "enum_name": "open_ended"
    },
    "contract_end_date": "2006-01-02",
    "contract_number": "6919737965274990093",
    "signing_type": {
        "enum_name": "new"
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
| &nbsp;&nbsp;└ `contract` | `contract` | 合同 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 合同ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 合同开始日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 实际结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id` | `string` | 雇员 ID，详细信息可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get) 接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_type` | `enum` | 合同类型，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)合同类型（contract_type）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `first_party_company_id` | `string` | 合同主体,  详细信息可通过[【查询公司详情接口】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/get)接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `person_id` | `string` | Person ID，详细信息可通过接口文档[【查询个人信息接口】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/person/get)接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(如123, 123.23, "true", [\"id1\",\"id2\"], "2006-01-02 15:04:05") |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `duration_type` | `enum` | 期限类型，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)合同期限类型（duration_type）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_end_date` | `string` | 合同结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_number` | `string` | 合同编号 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `signing_type` | `enum` | 签订类型，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)签订类型（signing_type）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_status` | `enum` | 合同协议状态，枚举值可通过文档【飞书人事枚举常量】合同协议状态（contract_status）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `renewal_status` | `enum` | 续签状态，枚举值可通过文档【飞书人事枚举常量】续签状态（renewal_status）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `signing_times` | `int` | 第几次签署 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "contract": {
            "id": "6919737965274990093",
            "effective_time": "2050-01-01 00:00:00",
            "expiration_time": "9999-12-31 23:59:59",
            "employment_id": "6893013238632416776",
            "contract_type": {
                "enum_name": "labor_contract",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "劳动合同"
                    }
                ]
            },
            "first_party_company_id": "6892686614112241165",
            "person_id": "151515151",
            "custom_fields": [
                {
                    "field_name": "name",
                    "value": "Sandy"
                }
            ],
            "duration_type": {
                "enum_name": "fixed_term",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "固定期限类型合同"
                    }
                ]
            },
            "contract_end_date": "2006-01-02",
            "contract_number": "6919737965274990093",
            "signing_type": {
                "enum_name": "changed",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "变更"
                    }
                ]
            },
            "contract_status": {
                "enum_name": "phone_type",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "刘梓新"
                    }
                ]
            },
            "renewal_status": {
                "enum_name": "phone_type",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "刘梓新"
                    }
                ]
            },
            "signing_times": 1
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1160545 | effective time has been occupied | 该时间段已存在合同，请修改合同生效时间段 |
| 400 | 1160546 | Conflicting contracts existed | 该合同已经存在 |


