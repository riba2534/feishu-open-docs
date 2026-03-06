---
title: "更新单个职级"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/patch"
updateTime: "1765434827000"
---

# 更新单个职级

该接口通过职级ID更新单个职级信息，包括职级数值、名称等信息。


> **Tip**: 所有非必填参数不传值时则不更新数据


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/job_levels/:job_level_id |
| HTTP Method | PATCH |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:corehr` 更新核心人事信息 `corehr:job_level:write` 读写职级信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `job_level_id` | `string` | 职级ID。ID获取方式： - 调用[【新建职级】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/create)[【查询租户的职级信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/list)等接口可以返回职级ID<br>**示例值**："1616161616" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `client_token` | `string` | 否 | 根据client_token是否一致来判断是否为同一请求<br>**示例值**：12454646 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `level_order` | `int` | 否 | 职级数值，单位：级。该字段主要用来在职级大小，职级的数值越大，代表职级越高 - 如果不填该字段则不更新<br>**示例值**：10 |
| `code` | `string` | 否 | 职级编码。非必填字段，如果非空值会校验全局唯一性，如果传空值则不参与全局校验。 - 不传值时默认不更新此字段，保持原值<br>**示例值**："J001" |
| `name` | `i18n\[\]` | 否 | 职级名称，注意事项： - 包含lang（语言）和value（职级名称）两个子参数，更新时需同时提供 - 不传值时默认不更新此字段，保持原值 |
| &nbsp;&nbsp;└ `lang` | `string` | 是 | 名称信息的语言，中文用zh-CN，英文用en-US - 最小1字符，最大200字符<br>**示例值**："zh-CN" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 名称信息的内容 - 最小1字符，最大200字符 - 名称不能包含「/」「；」「;」「\」「'」字符<br>**示例值**："P5" |
| `description` | `i18n\[\]` | 否 | 描述 - 不传值时默认不更新此字段，保持原值 |
| &nbsp;&nbsp;└ `lang` | `string` | 是 | 描述信息的语言 - 最小1字符，最大200字符<br>**示例值**："zh-CN" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 描述信息的内容 - 最小1字符，最大200字符<br>**示例值**："普通职级" |
| `active` | `boolean` | 否 | 是否启用，true为启用，false为停用 - 不传值时默认不更新此字段，保持原值<br>**示例值**：true |
| `custom_fields` | `object_field_data\[\]` | 否 | 自定义字段（该字段暂时不支持） - 不传值时默认不更新此字段，保持原值 - 包含filed_name（字段名）和value（字段值）两个子参数，更新时需同时提供 |
| &nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名 - 最小1字符，最大200字符<br>**示例值**："name" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 字段值，是json转义后的字符串，具体传值方式参见[获取自定义字段的元数据](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) - 最小1字符，最大200字符<br>**示例值**："\"Sandy\"" |
| `job_grade` | `string\[\]` | 否 | 职等 ID 列表 - 不传值时默认不更新此字段，保持原值。<br>**示例值**：["4692446793125560154"] |
| `pathway_ids` | `string\[\]` | 否 | 通道ID，详情可以参考[【获取通道信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/pathway/batch_get) - 不传值时默认不更新此字段，保持原值。<br>**示例值**：["4719519211875096301"] |


### 请求体示例

```json
{
    "level_order": 10,
    "code": "J001",
    "name": [
        {
            "lang": "zh-CN",
            "value": "P5"
        }
    ],
    "description": [
        {
            "lang": "zh-CN",
            "value": "普通职级"
        }
    ],
    "active": true,
    "custom_fields": [
        {
            "field_name": "name",
            "value": "\"Sandy\""
        }
    ],
    "job_grade": [
        "4692446793125560154"
    ],
    "pathway_ids": [
        "4719519211875096301"
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
| &nbsp;&nbsp;└ `job_level` | `job_level` | 职级 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职级 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `level_order` | `int` | 职级数值，单位：级 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 描述信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 描述信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 是否启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段(该功能暂不支持，可忽略) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 自定义字段 API Name，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_grade` | `string\[\]` | 职等 ID 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `pathway_ids` | `string\[\]` | 通道ID，详情可以参考[【获取通道信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/pathway/batch_get) |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "job_level": {
            "id": "4692446793125560154",
            "level_order": 10,
            "code": "J001",
            "name": [
                {
                    "lang": "zh-CN",
                    "value": "P5"
                }
            ],
            "description": [
                {
                    "lang": "zh-CN",
                    "value": "普通职级"
                }
            ],
            "active": true,
            "custom_fields": [
                {
                    "field_name": "name",
                    "value": "\"工程师\""
                }
            ],
            "job_grade": [
                "4692446793125560154"
            ],
            "pathway_ids": [
                "4719519211875096301"
            ]
        }
    }
}
```


