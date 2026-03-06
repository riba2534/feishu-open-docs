---
title: "查询单个公司"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/get"
updateTime: "1770621214000"
---

# 查询单个公司

根据 ID 查询单个公司。


> **Warning**: 延迟说明：
> - **数据库主从延迟2s以内，即：直接创建公司后2s内调用此接口可能查询不到数据**
> - **响应体registered_office_address_info （注册地址）、office_address_info （办公地址）下的full_address_local_script（完整地址，本地文字）、full_address_western_script（完整地址，西方文字）字段为计算字段，延迟5s以内，堆积时会延长**


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/companies/:company_id |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:company:read` 获取公司信息 `corehr:corehr:readonly` 获取核心人事信息 `corehr:corehr` 更新核心人事信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `company_id` | `string` | 需要查询的公司ID。ID获取方式： - 调用[【创建公司】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/create)[【批量查询公司】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)等接口可以返回部门ID<br>**示例值**："151515" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `company` | `company` | 公司信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 公司 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `hiberarchy_common` | `hiberarchy_common` | 公司基本信息，该结构维护了公司的名称、编码、启用状态、上级公司等基础信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `parent_id` | `string` | 上级 ID - 若查询的是一级公司，则该字段不展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `enum` | 组织类型，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)组织类型（organization_type）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 是否启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 当前版本生效日期 - 返回格式：YYYY-MM-DD 00:00:00（最小单位到日） - 日期范围:1900-01-01 00:00:00～9999-12-31 23:59:59 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 当前失效日期 - 返回格式：YYYY-MM-DD 00:00:00（最小单位到日） - 日期范围:1900-01-01 00:00:00～9999-12-31 23:59:59 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 公司编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段（该字段暂不支持） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(如123, 123.23, "true", [\"id1\",\"id2\"], "2006-01-02 15:04:05") |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `enum` | 公司性质，通过[获取字段详情](https://open.larkoffice.com/document/server-docs/corehr-v1/basic-infomation/custom_field/get_by_param)查询获取。请求参数：object_api_name=company；custom_api_name=type。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `industry_list` | `enum\[\]` | 所在行业，通过[获取字段详情](https://open.larkoffice.com/document/server-docs/corehr-v1/basic-infomation/custom_field/get_by_param)查询获取。请求参数：object_api_name=company；custom_api_name=industry。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `legal_representative` | `i18n\[\]` | 法定代表人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `post_code` | `string` | 邮编 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tax_payer_id` | `string` | 纳税人识别号 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `confidential` | `boolean` | 是否保密 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sub_type_list` | `enum\[\]` | 主体类型，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)主体类型（company_sub_type）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `branch_company` | `boolean` | 是否为分公司 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `primary_manager` | `i18n\[\]` | 主要负责人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段（该字段暂不支持） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(如123, 123.23, "true", [\"id1\",\"id2\"], "2006-01-02 15:04:05") |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `currency` | `currency` | 默认币种 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 货币 ID。 - 调用[【查询货币信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-currency/search)接口返回货币详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `currency_name` | `i18n\[\]` | 货币名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `numeric_code` | `int` | 数字代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `currency_alpha_3_code` | `string` | 法定货币对应代码，如CNY、USD等，通过[查询货币信息v2](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-currency/search)查询获取。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id_list` | `string\[\]` | 货币所属国家/地区 ID 列表，详细信息可通过[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `phone` | `phone_number_and_area_code` | 电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `area_code` | `enum` | 区号对应的数字，可通过 [获取字段详情](https://open.larkoffice.com/document/server-docs/corehr-v1/basic-infomation/custom_field/get_by_param)查询获取。请求参数：object_api_name=phone；custom_api_name=international_area_code |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `fax` | `phone_number_and_area_code` | 传真 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `area_code` | `enum` | 区号对应的数字，可通过 [获取字段详情](https://open.larkoffice.com/document/server-docs/corehr-v1/basic-infomation/custom_field/get_by_param)查询获取。请求参数：object_api_name=phone；custom_api_name=international_area_code |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `registered_office_address` | `i18n\[\]` | 完整注册地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `office_address` | `i18n\[\]` | 完整办公地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `registered_office_address_info` | `address` | 注册地址详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_local_script` | `string` | 完整地址（本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_western_script` | `string` | 完整地址（西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 地址ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区id。各国家/地区填写字段可参考[地址填写规则](https://bytedance.larkoffice.com/wiki/GoL4wAKAXis3OWku72YcEjTxnKe?sheet=0sMjoP)查询。 国家/地区id可通过[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)查询获取。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_id` | `string` | 主要行政区id。 可通过 [查询省份/主要行政区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)查询获取。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_id` | `string` | 城市id，可通过 [查询城市信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-city/search)查询获取。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `distinct_id` | `string` | 区/县id，可通过 [查询区/县信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-district/search)查询获取。 |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_type_list` | `enum\[\]` | 地址类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `office_address_info` | `address` | 办公地址详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_local_script` | `string` | 完整地址（本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_western_script` | `string` | 完整地址（西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 地址ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区id。各国家/地区填写字段可参考[地址填写规则](https://bytedance.larkoffice.com/wiki/GoL4wAKAXis3OWku72YcEjTxnKe?sheet=0sMjoP)查询。 国家/地区id可通过[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)查询获取。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_id` | `string` | 主要行政区id。 可通过 [查询省份/主要行政区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)查询获取。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_id` | `string` | 城市id，可通过 [查询城市信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-city/search)查询获取。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `distinct_id` | `string` | 区/县id，可通过 [查询区/县信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-district/search)查询获取。 |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_type_list` | `enum\[\]` | 地址类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开地址 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "company": {
            "id": "4692472714243080020",
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
                "custom_fields": [
                    {
                        "field_name": "name",
                        "value": "\"Sandy\""
                    }
                ]
            },
            "type": {
                "enum_name": "type_1",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ]
            },
            "industry_list": [
                {
                    "enum_name": "type_1",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "张三"
                        }
                    ]
                }
            ],
            "legal_representative": [
                {
                    "lang": "zh-CN",
                    "value": "张三"
                }
            ],
            "post_code": "邮编",
            "tax_payer_id": "123456840",
            "confidential": true,
            "sub_type_list": [
                {
                    "enum_name": "type_1",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "张三"
                        }
                    ]
                }
            ],
            "branch_company": true,
            "primary_manager": [
                {
                    "lang": "zh-CN",
                    "value": "张三"
                }
            ],
            "custom_fields": [
                {
                    "field_name": "name",
                    "value": "\"Sandy\""
                }
            ],
            "currency": {
                "id": "1",
                "currency_name": [
                    {
                        "lang": "zh-CN",
                        "value": "刘梓新"
                    }
                ],
                "numeric_code": 12,
                "currency_alpha_3_code": "12",
                "country_region_id_list": [
                    "6862995757234914824"
                ]
            },
            "phone": {
                "area_code": {
                    "enum_name": "phone_type",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "刘梓新"
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
                            "value": "刘梓新"
                        }
                    ]
                },
                "phone_number": "213213"
            },
            "registered_office_address": [
                {
                    "lang": "zh-CN",
                    "value": "刘梓新"
                }
            ],
            "office_address": [
                {
                    "lang": "zh-CN",
                    "value": "刘梓新"
                }
            ],
            "registered_office_address_info": {
                "full_address_local_script": "中国北京北京",
                "full_address_western_script": "Beijing, Beijing, China,",
                "id": "6989822217869624863",
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
                                "value": "刘梓新"
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
                "id": "6989822217869624863",
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
                                "value": "刘梓新"
                            }
                        ]
                    }
                ],
                "is_primary": true,
                "is_public": true
            }
        }
    }
}
```


