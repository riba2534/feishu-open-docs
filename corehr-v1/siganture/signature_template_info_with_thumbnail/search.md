---
title: "获取电子签模板内容"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/signature_template/search"
updateTime: "1764324063000"
---

# 获取电子签模板内容

根据多个模板ID获取电子签模板基本信息和内容列表。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/signature_templates/search |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:signature_template:read` 获取电子签模板信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `template_ids` | `string` | 否 | 电子签模板ids，用英文逗号分隔；如果不传 则返回所有电子签模版信息<br>**示例值**：7223256427270260268,7182520625066475540 |
| `select_custom_field` | `boolean` | 否 | 是否需要模板自定义字段，如果不需要，则默认只返回模板的系统字段。<br>**示例值**：true |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `signature_templates` | `signature_template\[\]` | 返回的电子签模板列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 电子签模板id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `brief_info` | `signature_template_brief_info` | 模板基本信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 电子签模板id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `label` | `i18n\[\]` | 模板名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 模板名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `category` | `enum` | 电子签模板分类，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)电子签模板类型（signature_template_category）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 模板类别名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 模板类别对应的多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `usage` | `enum` | 电子签模板用途，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)电子签模板用途（signature_template_usage）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 模板用途名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 模板用途的多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 人事合同 / 协议 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `signatory_labels` | `signature_signatory_label\[\]` | 模版签署对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `template_signatory_type` | `enum` | 电子签模板签署对象类型，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)电子签模板签署对象类型（signature_template_signatory_type）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 模板签署对象类型对应的枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `label` | `i18n\[\]` | 字段多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `apiname` | `string` | 模板签署类型名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 是否激活 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_by` | `string` | 创建人的雇佣ID，详细信息可通过[【查询员工信息接口】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `modify_by` | `string` | 修改人的雇佣ID，详细信息可通过[【查询员工信息接口】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `applicability` | `enum` | 电子签模板适用范围，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)电子签模板适用范围（signature_template_applicability）枚举定义部分 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 模板适用范围枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `creation_method` | `string` | 模板创建方式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `version` | `string` | 版本 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `update_time` | `string` | 更新时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `template_setting` | `signature_template_setting` | 模板设置 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `page_seal_types` | `string\[\]` | 骑缝章类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `template_region_info` | `signature_template_region_info` | 模板适用区域 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_global_scope` | `string` | 是否全球适用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `meta_infos` | `signature_meta_info\[\]` | 适用区域名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `api_name` | `string` | 区域名称apiName |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_id` | `string` | 区域对应的唯一ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `label` | `i18n\[\]` | 多语描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `template_code` | `string` | 模板编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `template_desc` | `i18n\[\]` | 模板描述 支持多语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `content_info` | `signature_template_content_info` | 模板内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contents` | `signature_template_content_item\[\]` | 【已废弃，无需关注】 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `enum` | 电子签模版内容的类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `filter_apiname` | `string` | 显示规则左值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 模版内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `label` | `i18n\[\]` | 中英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_desc` | `string` | 内容描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `signature_template_custom_field\[\]` | 自定义字段列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `label` | `i18n\[\]` | 中英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `apiname` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_field_type` | `enum` | 用户自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `used` | `boolean` | 是否使用到 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_required` | `boolean` | 是否需要 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_desc` | `string` | 自定义描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `common_info` | `signature_template_common_field_info` | 电子签模版公共字段信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source` | `enum` | 模板字段源类型；枚举值填到enum_name中，如："System" "MainData" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `apiname` | `string` | 主数据apiname |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `filter_fields` | `signature_template_filter\[\]` | 【已废弃，无需关注】 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `label` | `i18n\[\]` | 双语描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `apiname` | `string` | 主数据apiname |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `filters` | `signature_template_filter_item\[\]` | 过滤条件列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `left` | `string` | 左值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rights` | `string\[\]` | 右值列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `op` | `enum` | 操作符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `logic` | `enum` | 多个生效条件的logic |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_checked` | `boolean` | 是否被校验 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `filter_desc` | `string` | 过滤条件描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `criterion_list` | `string` | 过滤条件列表，使用string类型描述list的原因是为了避免循环引用问题，因为该list的item类型就是这个数据类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `using_fields` | `signature_template_common_field_info\[\]` | 【已废弃，无需关注】 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source` | `enum` | 模板字段源类型；枚举值填到enum_name中，如："System" "MainData" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `apiname` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `system_setting_fields` | `signature_template_field\[\]` | 系统字段列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_type` | `enum` | 模板字段值类型枚举 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `label` | `i18n\[\]` | 双语描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `common_info` | `signature_template_common_field_info` | 【无需关注】通用字段信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source` | `enum` | 模板字段源类型 - System - MainData |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `apiname` | `string` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `combination_info` | `signature_template_combination_field_info` | 【无需关注】组合字段信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `total_apiname` | `string` | 【无需关注】组合字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `apiname` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `i18n\[\]` | 中英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contents` | `signature_template_combination_sub_field_info\[\]\[\]` | 适用区域名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source` | `enum` | 【无需关注】电子签模板字段源类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `children` | `string` | 【无需关注】子模板配置信息列表对应的string，避免循环引用问题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `combination_info_v2` | `signature_template_combination_field_info_v2` | 弃用，无需关注 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `total_apiname` | `string` | 弃用，无需关注 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `apiname` | `string` | 弃用，无需关注 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source` | `enum` | 弃用，无需关注 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "signature_templates": [
            {
                "id": "7246307700768902956",
                "brief_info": {
                    "id": "1",
                    "label": [
                        {
                            "lang": "zh-CN",
                            "value": "合同续约模板"
                        }
                    ],
                    "category": {
                        "enum_name": "contract_agreement",
                        "display": [
                            {
                                "lang": "zh-CN",
                                "value": "人事合同 / 协议"
                            }
                        ]
                    },
                    "usage": {
                        "enum_name": "offboarding",
                        "display": [
                            {
                                "lang": "zh-CN",
                                "value": "离职"
                            }
                        ]
                    },
                    "signatory_labels": [
                        {
                            "template_signatory_type": {
                                "enum_name": "Person",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "label": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ],
                            "apiname": "status"
                        }
                    ],
                    "active": true,
                    "create_by": "123123123123123123",
                    "modify_by": "7287500478366090796",
                    "applicability": {
                        "enum_name": "signature",
                        "display": [
                            {
                                "lang": "zh-CN",
                                "value": "电子签"
                            }
                        ]
                    },
                    "creation_method": "online_edit",
                    "version": "v1",
                    "update_time": "31231232123",
                    "create_time": "3123123211",
                    "template_setting": {
                        "page_seal_types": [
                            "page_seal"
                        ]
                    },
                    "template_region_info": {
                        "is_global_scope": "global",
                        "meta_infos": [
                            {
                                "api_name": "7246307700768902956",
                                "wk_id": "7246307700768902956",
                                "label": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            }
                        ]
                    },
                    "template_code": "7246307700768902956",
                    "template_desc": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "content_info": {
                    "contents": [
                        {
                            "content_type": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "filter_apiname": "111",
                            "content": "111",
                            "label": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ],
                            "content_desc": "111"
                        }
                    ],
                    "custom_fields": [
                        {
                            "label": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ],
                            "apiname": "status",
                            "custom_field_type": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "used": true,
                            "is_required": true,
                            "custom_desc": "desc",
                            "common_info": {
                                "source": {
                                    "enum_name": "phone_type",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                },
                                "apiname": "status"
                            }
                        }
                    ],
                    "filter_fields": [
                        {
                            "label": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ],
                            "apiname": "status",
                            "filters": [
                                {
                                    "left": "aa",
                                    "rights": [
                                        "1"
                                    ],
                                    "op": {
                                        "enum_name": "phone_type",
                                        "display": [
                                            {
                                                "lang": "zh-CN",
                                                "value": "中文示例"
                                            }
                                        ]
                                    }
                                }
                            ],
                            "logic": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "is_checked": true,
                            "filter_desc": "desc",
                            "criterion_list": "[]"
                        }
                    ],
                    "using_fields": [
                        {
                            "source": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "apiname": "status"
                        }
                    ],
                    "system_setting_fields": [
                        {
                            "field_type": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "label": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ],
                            "common_info": {
                                "source": {
                                    "enum_name": "System",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                },
                                "apiname": "status"
                            },
                            "combination_info": {
                                "total_apiname": "status",
                                "apiname": "status",
                                "title": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ],
                                "contents": [
                                    [
                                        {
                                            "field_type": {
                                                "enum_name": "phone_type",
                                                "display": [
                                                    {
                                                        "lang": "zh-CN",
                                                        "value": "中文示例"
                                                    }
                                                ]
                                            },
                                            "info": {
                                                "source": {
                                                    "enum_name": "System",
                                                    "display": [
                                                        {
                                                            "lang": "zh-CN",
                                                            "value": "中文示例"
                                                        }
                                                    ]
                                                },
                                                "apiname": "status"
                                            },
                                            "label": [
                                                {
                                                    "lang": "zh-CN",
                                                    "value": "中文示例"
                                                }
                                            ]
                                        }
                                    ]
                                ],
                                "source": {
                                    "enum_name": "phone_type",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                }
                            },
                            "children": "无需关注",
                            "combination_info_v2": {
                                "total_apiname": "弃用，无需关注",
                                "apiname": "弃用，无需关注",
                                "source": {
                                    "enum_name": "phone_type",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1160001 | param is invalid | 请检查请求参数的类型、格式是否与接口要求一致（如template_ids需用英文逗号分隔，select_custom_field为boolean类型），或参考文档确认参数的必填项及示例值 |


