---
title: "更新工时制度"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/patch"
updateTime: "1735280526000"
---

# 更新工时制度

更新工时制度。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/working_hours_types/:working_hours_type_id |
| HTTP Method | PATCH |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:common_data.preset_data:write` 更新预置数据信息 `corehr:corehr` 更新核心人事信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `working_hours_type_id` | `string` | 工时制度ID - 可通过[批量查询工时制度](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/list)获取<br>**示例值**："1616161616" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `client_token` | `string` | 否 | 根据client_token是否一致来判断是否为同一请求<br>**示例值**：12454646 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `code` | `string` | 否 | 编码<br>**示例值**："1" |
| `name` | `i18n\[\]` | 否 | 名称 |
| &nbsp;&nbsp;└ `lang` | `string` | 是 | 名称信息的语言<br>**示例值**："zh-CN" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 名称信息的内容<br>**示例值**："张三" |
| `country_region_id_list` | `string\[\]` | 否 | 国家/地区 ID 列表 - 可通过[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取<br>**示例值**：["6890452208593356295"] |
| `default_for_job` | `boolean` | 否 | 职务默认值<br>**示例值**：true |
| `active` | `boolean` | 否 | 是否启用<br>**示例值**：true |
| `custom_fields` | `object_field_data\[\]` | 否 | 自定义字段 - 具体支持的对象请参考[自定义字段说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："name" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(如123, 123.23, "true", [\"id1\",\"id2\"], "2006-01-02 15:04:05")<br>**示例值**："\"Sandy\"" |


### 请求体示例

```json
{
    "code": "1",
    "name": [
        {
            "lang": "zh-CN",
            "value": "张三"
        }
    ],
    "country_region_id_list": [
        "6890452208593356295"
    ],
    "default_for_job": true,
    "active": true,
    "custom_fields": [
        {
            "field_name": "name",
            "value": "\"Sandy\""
        }
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
| &nbsp;&nbsp;└ `working_hours_type` | `working_hours_type` | 工时制度 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 工时制度 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id_list` | `string\[\]` | 国家/地区 ID 列表 - 可通过[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `default_for_job` | `boolean` | 职务默认值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 是否启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段 - 具体支持的对象请参考[自定义字段说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(如123, 123.23, "true", [\"id1\",\"id2\"], "2006-01-02 15:04:05") |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "working_hours_type": {
            "id": "6890452208593372679",
            "code": "1",
            "name": [
                {
                    "lang": "zh-CN",
                    "value": "张三"
                }
            ],
            "country_region_id_list": [
                "6890452208593356295"
            ],
            "default_for_job": true,
            "active": true,
            "custom_fields": [
                {
                    "field_name": "name",
                    "value": "\"Sandy\""
                }
            ]
        }
    }
}
```


