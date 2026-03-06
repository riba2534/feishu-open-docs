---
title: "根据条件批量获取序列信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_family/batch_get"
updateTime: "1770621309000"
---

# 根据条件批量查询序列信息

通过序列 ID 或序列 Code 批量查询当前生效版本序列的详情信息，包括序列名称、启用状态、上级序列等。


> **Tip**: - 如果你只需要单一序列查询场景，建议通过[【查询单个序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/get)获取序列信息。
> - 序列ID和序列Code可一起使用，之间为 AND 关系
> - 数据库主从延迟 2s 以内，即：直接创建序列后2s内调用此接口可能查询不到数据。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/job_families/batch_get |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:job_family:read` 获取序列信息 `corehr:job_family:write` 读写序列信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `job_family_ids` | `string\[\]` | 否 | 序列ID列表。 - 序列 ID 列表和序列 Code 列表至少有一项有值，否则接口将调用失败。 - 未设置时表示不筛选该条件 - ID获取方式：调用[【创建序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/create)[【批量查询序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/list)等接口可以返回序列ID<br>**示例值**：["1554548"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| `job_family_codes` | `string\[\]` | 否 | 序列 Code 列表。 - 序列 ID 列表和序列 Code 列表至少有一项有值，否则接口将调用失败。 - 未设置时表示不筛选该条件 - Code获取方式：调用[【创建序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/create)[【批量查询序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/list)等接口可以返回序列Code<br>**示例值**：["122348"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |


### 请求体示例

```json
{
   "job_family_ids": [
    "7485328827867711096",
    "7486375838641787444"
    ],
  "job_family_codes": [
    "code1110",
    "code1112",
    "code1114"
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
| &nbsp;&nbsp;└ `items` | `job_family\[\]` | 查询的序列信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id` | `string` | 序列 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 启用状态，启用为true，停用为false |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `selectable` | `boolean` | 是否可被使用，true为可被使用，false为不可被使用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `parent_id` | `string` | 上级序列 ID，详细信息可通过[【查询单个序列】](get.md)接口查询获得（若查询的是一级序列，则该字段不展示） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `pathway_ids` | `string\[\]` | 通道ID，详情可以参考[【获取通道信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/pathway/batch_get) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 生效时间，返回格式：YYYY-MM-DD 00:00:00（最小单位到日） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 失效时间，返回格式：YYYY-MM-DD 00:00:00（最小单位到日） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 (不能与其他记录的编码重复) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段（该字段暂时不支持） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 - 自定义字段详细见[【获取自定义字段列表】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "job_family_id": "4698019107896524633",
                "name": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ],
                "active": true,
                "selectable": true,
                "parent_id": "4698020757495316313",
                "pathway_ids": [
                    "4719519211875096301"
                ],
                "effective_time": "2020-05-01 00:00:00",
                "expiration_time": "2020-05-02 00:00:00",
                "code": "123456",
                "description": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ],
                "custom_fields": [
                    {
                        "custom_api_name": "name",
                        "name": {
                            "zh_cn": "自定义姓名",
                            "en_us": "Custom Name"
                        },
                        "type": 1,
                        "value": "\"231\""
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
| 400 | 1160001 | Param is invalid | 参数错误，请确认请求参数是否符合接口传参规范 |


