---
title: "新建职级"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/create"
updateTime: "1765434827000"
---

# 新建单个职级

该接口通过传入职级名称、职级数值等参数，创建单个职级对象
适用场景：
- 适用于HR系统中新增职级的场景


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/job_levels |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:corehr` 更新核心人事信息 `corehr:job_level:write` 读写职级信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `client_token` | `string` | 否 | 根据client_token是否一致来判断是否为同一请求<br>**示例值**：12454646 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `level_order` | `int` | 是 | 职级数值，单位：级。该字段主要用来在职级大小，职级的数值越大，代表职级越高 - 最小值0，最大值99999999<br>**示例值**：9999 |
| `code` | `string` | 否 | 职级编码。非必填字段，如果非空值会校验全局唯一性，如果传空值则不参与全局校验。<br>**示例值**："VQzo/BSonp8l6PmcZ+VlDhkd2595LMkhyBAGX6HAlCY=" |
| `name` | `i18n\[\]` | 是 | 职级名称，注意事项： - 目前name最大元素个数为2，仅支持中、英文 - 包含lang（语言）和value（职级名称）两个子参数，新建时需同时提供 |
| &nbsp;&nbsp;└ `lang` | `string` | 是 | 名称信息的语言，中文用zh-CN，英文用en-US。<br>**示例值**："zh-CN" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 名称信息的内容。注意事项： - 职级中英文名称会有全局唯一校验 - 名称不能包含「/」「；」「;」「\」「'」字符 - 最少1个字符，最多200个字符<br>**示例值**："P5" |
| `description` | `i18n\[\]` | 否 | 描述 - 包含lang（语言）和value（职级描述）两个子参数，更新时需同时提供 |
| &nbsp;&nbsp;└ `lang` | `string` | 是 | 名称信息的语言，中文用zh-CN，英文用en-US<br>**示例值**："zh-CN" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 名称信息的内容 - 最小1字符，最大200字符<br>**示例值**："普通职级" |
| `active` | `boolean` | 是 | 是否启用，true为启用，false为停用<br>**示例值**：true |
| `custom_fields` | `object_field_data\[\]` | 否 | 自定义字段（目前职级暂不支持该功能） - 包含field_name （字段名）和value（字段值）两个子参数，新建时需同时提供 |
| &nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名 - 最小1字符，最大200字符<br>**示例值**："name" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 字段值，为 JSON 转义后的字符串。 - 最小1字符，最大200字符<br>**注意：具体传值方式参见**[获取自定义字段的元数据](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**示例值**："\"Sandy\"" |
| `job_grade` | `string\[\]` | 否 | 职等 ID 列表<br>**示例值**：["4692446793125560154"] |
| `pathway_ids` | `string\[\]` | 否 | 通道ID，详情可以参考[【获取通道信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/pathway/batch_get)<br>**示例值**：["4719519211875096301"] |


### 请求体示例

```json
{
    "level_order": 9999,
    "code": "VQzo/BSonp8l6PmcZ+VlDhkd2595LMkhyBAGX6HAlCY=",
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
| &nbsp;&nbsp;└ `job_level` | `job_level` | 创建成功的职级信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职级 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `level_order` | `int` | 职级数值，单位：级。该字段主要用来在职级大小排序，职级的数值越大，代表职级越高 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 是否启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段(该功能暂不支持，可忽略) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同。如：```("\"123\"", "\"123.23\"", "\"true\"", [\"id1\",\"id2\"], \"2006-01-02 15:04:05\")``` |
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
            "level_order": 9999,
            "code": "VQzo/BSonp8l6PmcZ+VlDhkd2595LMkhyBAGX6HAlCY=",
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
    }
}
```


