---
title: "查询指定时间范围公司版本"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/company/query_multi_timeline"
updateTime: "1770621233000"
---

# 查询指定时间范围公司版本

- 接口支持查询出对象生效时间段在指定的start_date和end_date之间的版本（即：会查询出生效时间段和查询时间段有交集的版本）
- 接口支持对象版本相关字段的查询和返回（默认返回id和version_id）


> **Tip**: 延迟说明：数据库主从延迟2s以内，即：直接创建对象后2s内调用此接口可能查询不到数据。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/companies/query_multi_timeline |
| HTTP Method | POST |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:company:read` 获取公司信息 `corehr:company:write` 查看、创建、更新、删除公司信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `company_ids` | `string\[\]` | 是 | 公司ID。ID获取方式： - 调用[【创建公司】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/create)[【批量查询公司】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)等接口可以返回公司ID<br>**示例值**：["7094136522860922111"]<br>**数据校验规则**：<br>- 长度范围：`1` ～ `10` |
| `start_date` | `string` | 否 | 查询开始时间（包含）<br>**示例值**："2024-01-01"<br>**数据校验规则**：<br>- 长度范围：`10` ～ `10` 字符 - 正则校验：`^((([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29))$` |
| `end_date` | `string` | 否 | 查询结束时间（不包含）<br>**示例值**："2024-12-31"<br>**数据校验规则**：<br>- 长度范围：`10` ～ `10` 字符 - 正则校验：`^((([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29))$` |
| `fields` | `string\[\]` | 否 | 返回数据的字段列表，可选["company_name", "code", "active", "parent_company","description", "effective_date", "expiration_date", "type", "industry_list", "legal_representative", "post_code", "tax_payer_id", "confidential", "sub_type_list", "branch_company", "primary_manager", "currency", "phone", "fax", "registered_office_address", "office_address", "registered_office_address_info", "office_address_info"]<br>**示例值**：["company_name"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |


### 请求体示例

```json
{
    "company_ids": [
        "7094136522860922111"
    ],
    "start_date": "2024-01-01",
    "end_date": "2024-12-31",
    "fields": [
        "company_name"
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
| &nbsp;&nbsp;└ `items` | `company_timeline\[\]` | 公司信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `company_version_data` | `company_version_data\[\]` | 公司版本信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `company_id` | `string` | 公司 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `company_version_id` | `string` | 公司版本 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `company_names` | `i18n\[\]` | 公司名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文：zh-CN，英文en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `parent_company_id` | `string` | 上级公司 ID - 若查询的是一级公司，则该字段不展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `effective_date` | `string` | 当前版本生效日期 - 返回格式：YYYY-MM-DD （最小单位到日） - 日期范围:1900-01-01 ～9999-12-31  - 详情可以参考[时间轴介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/about-timeline-version) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_date` | `string` | 当前版本失效日期 - 返回格式：YYYY-MM-DD （最小单位到日） - 日期范围:1900-01-01 ～9999-12-31  - 详情可以参考[时间轴介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/about-timeline-version) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 是否启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `descriptions` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文：zh-CN，英文：en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `enum` | 公司性质 - 可通过[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)查询获取。请求参数：object_api_name=company；custom_api_name=type。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文：zh-CN，英文en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `industry_list` | `enum\[\]` | 所在行业 - 可通过[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)查询获取。查询参数：object_api_name=company；custom_api_name=industry |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文：zh-CN，英文en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `legal_representative` | `i18n\[\]` | 法定代表人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文：zh-CN，英文en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `post_code` | `string` | 邮编 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tax_payer_id` | `string` | 纳税人识别号 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `confidential` | `boolean` | 是否保密 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sub_type_list` | `enum\[\]` | 公司主体类型 - 可通过[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)查询获取。查询参数：object_api_name=company；custom_api_name=subtype |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文：zh-CN，英文en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `branch_company` | `boolean` | 是否为分公司 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `primary_manager` | `i18n\[\]` | 主要负责人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文：zh-CN，英文en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `currency` | `currency` | 默认币种 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `currency_id` | `string` | 货币 ID - 调用[【查询货币信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-currency/search)接口返回货币详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id_list` | `string\[\]` | 货币所属国家/地区 ID 列表 - 详细信息可通过[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `currency_name` | `i18n\[\]` | 货币名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文：zh-CN，英文en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `numeric_code` | `int` | 数字代码（ISO 4217），对应币种的指代代码，通过系统内部查找，通过[查询货币信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-currency/search)查询获取。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `currency_alpha_3_code` | `string` | 法定货币对应代码，如CNY、USD等，通过[查询货币信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-currency/search)查询获取。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 状态<br>**可选值有**：<br>- `1`: 生效 - `0`: 失效 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `phone` | `phone_number_and_area_code` | 电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `area_code` | `enum` | 电话区号 - 通过[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)查询获取。请求参数：object_api_name=phone；custom_api_name=international_area_code。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文：zh-CN，英文en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `fax` | `phone_number_and_area_code` | 传真 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `area_code` | `enum` | 传真区号 - 通过[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)查询获取。请求参数：object_api_name=phone；custom_api_name=international_area_code。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文：zh-CN，英文en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `registered_office_address` | `i18n\[\]` | 完整注册地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文：zh-CN，英文en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `office_address` | `i18n\[\]` | 完整办公地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文：zh-CN，英文en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `registered_office_address_info` | `address` | 注册地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_local_script` | `string` | 完整地址（本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_western_script` | `string` | 完整地址（西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_id` | `string` | 地址 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区 ID - 各国家/地区填写字段可参考[地址填写规则](https://bytedance.larkoffice.com/wiki/GoL4wAKAXis3OWku72YcEjTxnKe?sheet=0sMjoP)查询。可通过 [查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)查询获取。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_id` | `string` | 主要行政区 ID - 可通过[查询省份/主要行政区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)查询获取。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_id` | `string` | 城市 ID - 调用[【查询城市信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-city/search)接口返回城市详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `distinct_id` | `string` | 区/县 ID - 调用[【查询区县信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-district/search)接口返回区县详细信息 |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_type_list` | `enum\[\]` | 地址类型 - 通过[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)查询获取。请求参数：object_api_name=address；custom_api_name= address_type。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 地址类型 - 通过[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)查询获取。请求参数：object_api_name=address；custom_api_name= address_type。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文：zh-CN，英文en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `office_address_info` | `address` | 办公地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_local_script` | `string` | 完整地址（本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_western_script` | `string` | 完整地址（西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_id` | `string` | 地址 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区 ID - 各国家/地区填写字段可参考[地址填写规则](https://bytedance.larkoffice.com/wiki/GoL4wAKAXis3OWku72YcEjTxnKe?sheet=0sMjoP)查询。可通过 [查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)查询获取。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_id` | `string` | 主要行政区 ID - 可通过[查询省份/主要行政区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)查询获取。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_id` | `string` | 城市 ID - 调用[【查询城市信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-city/search)接口返回城市详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `distinct_id` | `string` | 区/县 ID - 调用[【查询区县信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-district/search)接口返回区县详细信息 |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_type_list` | `enum\[\]` | 地址类型 - 通过[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)查询获取。请求参数：object_api_name=address；custom_api_name= address_type。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文：zh-CN，英文en-US |
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
                "company_version_data": [
                    {
                        "company_id": "4719456877659520852",
                        "company_version_id": "7238516215202170412",
                        "company_names": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ],
                        "parent_company_id": "4719456877659520852",
                        "effective_date": "2020-05-01",
                        "expiration_date": "2020-05-02",
                        "active": true,
                        "descriptions": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ],
                        "code": "FJK387"
                    }
                ],
                "type": {
                    "enum_name": "phone_type",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "industry_list": [
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
                "legal_representative": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ],
                "post_code": "645623412342",
                "tax_payer_id": "341244646234",
                "confidential": true,
                "sub_type_list": [
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
                "branch_company": true,
                "primary_manager": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ],
                "currency": {
                    "currency_id": "6863329932261459464",
                    "country_region_id_list": [
                        "6862995757234914824"
                    ],
                    "currency_name": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ],
                    "numeric_code": 156,
                    "currency_alpha_3_code": "CNY",
                    "status": 1
                },
                "phone": {
                    "area_code": {
                        "enum_name": "phone_type",
                        "display": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ]
                    },
                    "phone_number": "213213"
                },
                "fax": {
                    "area_code": {
                        "enum_name": "phone_type",
                        "display": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ]
                    },
                    "phone_number": "213213"
                },
                "registered_office_address": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ],
                "office_address": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ],
                "registered_office_address_info": {
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
                },
                "office_address_info": {
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


