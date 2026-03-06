---
title: "查询单个合同"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/get"
updateTime: "1724639907000"
---

# 查询单个合同

该接口用于根据合同 ID 查询单个合同详细信息，包括合同开始日期、结束日期、公司主体等信息


> **Tip**: 如需要一次性查询多份合同，请检索[批量查询接口](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)，更适合分批查询合同列表的场景


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/contracts/:contract_id |
| HTTP Method | GET |
| 接口频率限制 | [特殊频控](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:corehr:readonly` 获取核心人事信息 `corehr:corehr` 更新核心人事信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `contract_id` | `string` | 合同ID，该ID可以通过[【批量查询合同】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取<br>**示例值**："7091849027838838316" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `contract` | `contract` | 合同信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 合同ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 合同开始日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 实际结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id` | `string` | 雇佣 ID，详细信息可通过[【查询员工信息接口】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_type` | `enum` | 合同类型，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)合同类型（contract_type）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `first_party_company_id` | `string` | 合同主体ID,  详细信息可通过[【查询公司详情接口】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/get)接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `person_id` | `string` | Person ID，详细信息可通过接口文档[【批量查询员工信息接口】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)接口查询获得 |
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
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_status` | `enum` | 合同协议状态，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)合同协议状态（contract_status）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `renewal_status` | `enum` | 续签状态，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)续签状态（renewal_status）枚举定义部分获得 |
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
                "enum_name": "internship_agreement",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "实习协议"
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
                "enum_name": "open_ended",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "无固定期限"
                    }
                ]
            },
            "contract_end_date": "2006-01-02",
            "contract_number": "6919737965274990093",
            "signing_type": {
                "enum_name": "renewed",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "续签"
                    }
                ]
            },
            "contract_status": {
                "enum_name": "contract_closed",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "已终止"
                    }
                ]
            },
            "renewal_status": {
                "enum_name": "not_started",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "未发起"
                    }
                ]
            },
            "signing_times": 1
        }
    }
}
```


