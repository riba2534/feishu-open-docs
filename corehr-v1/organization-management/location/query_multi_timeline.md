---
title: "查询指定时间范围地点版本"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/location/query_multi_timeline"
updateTime: "1770621176000"
---

# 查询指定时间范围地点版本

- 接口支持查询出对象生效时间段在指定的start_date和end_date之间的版本（即：会查询出生效时间段和查询时间段有交集的版本）
- 接口支持对象版本相关字段的查询和返回（默认返回id和version_id）


> **Tip**: 延迟说明：数据库主从延迟2s以内，即：直接创建对象后2s内调用此接口可能查询不到数据。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/locations/query_multi_timeline |
| HTTP Method | POST |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:locations:read` 获取地点信息 `corehr:locations:write` 更新地点信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `location_ids` | `string\[\]` | 是 | 地点ID。ID获取方式： - 调用[【创建地点】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/create)[【批量分页查询地点】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)等接口可以返回地点ID<br>**示例值**：["7094136522860922111"]<br>**数据校验规则**：<br>- 长度范围：`1` ～ `10` |
| `start_date` | `string` | 否 | 查询开始时间（包含）<br>**示例值**："2024-01-01"<br>**数据校验规则**：<br>- 长度范围：`10` ～ `10` 字符 - 正则校验：`^((([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29))$` |
| `end_date` | `string` | 否 | 查询结束时间(不包含)<br>**示例值**："2024-12-31"<br>**数据校验规则**：<br>- 长度范围：`10` ～ `10` 字符 - 正则校验：`^((([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29))$` |
| `fields` | `string\[\]` | 否 | 返回数据的字段列表，可选["location_name", "code", "active", "parent_location", "description", "effective_date", "expiration_date", "location_usage", "working_hours_type", "locale", "time_zone", "display_language", "address"]<br>**示例值**：["location_name"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |


### 请求体示例

```json
{
    "location_ids": [
        "7094136522860922111"
    ],
    "start_date": "2024-01-01",
    "end_date": "2024-12-31",
    "fields": [
        "location_name"
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
| &nbsp;&nbsp;└ `items` | `location_timeline\[\]` | 地点信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `location_version_data` | `location_version_data\[\]` | 地点版本信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `location_id` | `string` | 地点ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `location_version_id` | `string` | 地点版本ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `location_names` | `i18n\[\]` | 地点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 - 中文用zh-CN，英文用en-US。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `parent_location_id` | `string` | 上级地点ID - 若查询的是一级地点，则该字段不展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `effective_date` | `string` | 当前版本生效日期 - 返回格式：YYYY-MM-DD （最小单位到日） - 日期范围:1900-01-01 ～9999-12-31  - 详情可以参考[时间轴介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/about-timeline-version) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_date` | `string` | 当前版本失效日期 - 返回格式：YYYY-MM-DD （最小单位到日） - 日期范围:1900-01-01 ～9999-12-31  - 详情可以参考[时间轴介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/about-timeline-version) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 是否启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `descriptions` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 - 中文用zh-CN，英文用en-US。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `location_usages` | `enum\[\]` | 地点用途，枚举值及详细信息可通过[【批量查询地点用途】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询获得。 - 请求参数object_api_name=location；custom_api_name=location_usage |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 - 中文用zh-CN，英文用en-US。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `enum` | 区域设置ID  - 枚举值及详细信息可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询获得。 - 请求参数object_api_name=location；custom_api_name=locale |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 - 中文用zh-CN，英文用en-US。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_zone_id` | `string` | 时区 ID  - 详细信息可通过[【查询时区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-time_zone/search)接口查询获得。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_language_id` | `string` | 默认语言 ID  - 详细信息可通过[【查询语言信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-language/search)。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `working_hours_type_id` | `string` | 工时制度 ID - 详细信息可通过[【批量查询工时制度】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address` | `address\[\]` | 地址信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_local_script` | `string` | 完整地址（本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_western_script` | `string` | 完整地址（西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_id` | `string` | 地址 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区 ID。ID获取方式： - 可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)接口获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_id` | `string` | 主要行政区 ID。ID获取方式： - 可通过[【查询省份/行政区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)接口获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_id` | `string` | 城市ID。ID获取方式： - 调用[【查询城市信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-city/search)接口可以返回城市ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `distinct_id` | `string` | 区县ID。ID获取方式： - 调用[【查询区县信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-district/search)接口可以返回区县ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line1` | `string` | 地址行 1 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line2` | `string` | 地址行 2 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line3` | `string` | 地址行 3 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line4` | `string` | 地址行 4 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line5` | `string` | 地址行 5 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line6` | `string` | 地址行 6 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line7` | `string` | 地址行 7 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line8` | `string` | 地址行 8 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line9` | `string` | 地址行 9 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line1` | `string` | 地址行 1（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line2` | `string` | 地址行 2（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line3` | `string` | 地址行 3（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line4` | `string` | 地址行 4（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line5` | `string` | 地址行 5（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line6` | `string` | 地址行 6（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line7` | `string` | 地址行 7（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line8` | `string` | 地址行 8（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line9` | `string` | 地址行 9（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `postal_code` | `string` | 邮政编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_type_list` | `enum\[\]` | 地址类型  - 枚举值及详细信息可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询获得。 - 请求参数object_api_name=address；custom_api_name=address_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 - 中文用zh-CN，英文用en-US。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开地址 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "location_version_data": [
                    {
                        "location_id": "4719456877659520852",
                        "location_version_id": "7238516215202170412",
                        "location_names": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ],
                        "parent_location_id": "8961456877659520953",
                        "effective_date": "2020-05-01",
                        "expiration_date": "2020-05-02",
                        "active": true,
                        "descriptions": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ],
                        "code": "BD38591",
                        "location_usages": [
                            {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            }
                        ],
                        "locale": {
                            "enum_name": "phone_type",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        },
                        "time_zone_id": "4690238309151997779",
                        "display_language_id": "4690238309151997779",
                        "working_hours_type_id": "4690238309151997779"
                    }
                ],
                "address": [
                    {
                        "full_address_local_script": "中国北京北京",
                        "full_address_western_script": "Beijing, Beijing, China,",
                        "address_id": "6989822217869624863",
                        "country_region_id": "6862995757234914824",
                        "region_id": "6863326815667095047",
                        "city_id": "6863333254578046471",
                        "distinct_id": "6863333516579440141",
                        "address_line1": "丹佛测试地址-纽埃时区",
                        "address_line2": "PoewH",
                        "address_line3": "PoewH",
                        "address_line4": "jmwJc",
                        "address_line5": "jmwJc",
                        "address_line6": "jmwJc",
                        "address_line7": "jmwJc",
                        "address_line8": "rafSu",
                        "address_line9": "McPRG",
                        "local_address_line1": "丹佛测试地址-纽埃时区",
                        "local_address_line2": "PoewH",
                        "local_address_line3": "PoewH",
                        "local_address_line4": "jmwJc",
                        "local_address_line5": "jmwJc",
                        "local_address_line6": "jmwJc",
                        "local_address_line7": "jmwJc",
                        "local_address_line8": "rafSu",
                        "local_address_line9": "McPRG",
                        "postal_code": "611530",
                        "address_type_list": [
                            {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            }
                        ],
                        "is_primary": true,
                        "is_public": true
                    }
                ]
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 503 | 1161204 | Request timeout | 接口超时，可尝试重试。如果无法解决可以联系飞书人事 [技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 429 | 1161604 | QPS over limit | 接口请求次数超过接口频率限制，可尝试降低请求频率 |


