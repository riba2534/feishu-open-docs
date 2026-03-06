---
title: "查询省份/主要行政区信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search"
updateTime: "1719656470000"
---

# 查询省份/主要行政区信息

根据国家/地区 ID、省份/主要行政区 ID、状态，批量查询国家/地区下辖的一级行政区（如省份、直辖市、自治区、州等）数据


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/basic_info/country_region_subdivisions/search |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:common_data.basic_data:read` 获取基础数据信息 |

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


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `country_region_id_list` | `string\[\]` | 否 | 国家/地区 ID 列表，可通过[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)接口获取，不填写则返回全部<br>**示例值**：["6891251722631891995"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `country_region_subdivision_id_list` | `string\[\]` | 否 | 省份/主要行政区 ID 列表，不填写则返回全部<br>**示例值**：["6891251222631891995"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `status_list` | `int\[\]` | 否 | 状态列表，不填写则返回全部<br>**示例值**：[1]<br>**可选值有**：<br>- `1`: 生效 - `0`: 失效<br>**默认值**：`[1]`<br>**数据校验规则**：<br>- 最大长度：`2` |


### 请求体示例

```json
{
    "country_region_id_list": [
        "6891251722631891995"
    ],
    "country_region_subdivision_id_list": [
        "6891251222631891995"
    ],
    "status_list": [
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
| &nbsp;&nbsp;└ `items` | `country_region_subdivision\[\]` | 查询的省份/主要行政区信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_subdivision_id` | `string` | 省份/主要行政区 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 省份/主要行政区名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 所属国家/地区 ID，详细信息可通过[查询国家 / 地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `subdivision_type` | `enum` | 行政区类型，枚举值可通过[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant#402ea9a0)文档中行政区类型（subdivision_type）定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `iso_code` | `string` | 省份/主要行政区编码（ISO 3166-2） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 状态<br>**可选值有**：<br>- `1`: 生效 - `0`: 失效 |
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
                "country_region_subdivision_id": "6863326571462133262",
                "name": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ],
                "country_region_id": "6862995791674344967",
                "subdivision_type": {
                    "enum_name": "governorate",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "iso_code": "PSE-GZA",
                "status": 1
            }
        ],
        "page_token": "6891251722631890445",
        "has_more": true
    }
}
```


