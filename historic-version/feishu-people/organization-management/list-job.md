---
title: "批量查询职务"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job/list"
updateTime: "1707186600000"
---

# 批量查询职务

批量查询职务。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/jobs |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:corehr:readonly` 获取核心人事信息 `corehr:job:read` 获取职务信息 `corehr:corehr` 更新核心人事信息 `corehr:job:write` 读写职务信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：1231231987 |
| `page_size` | `string` | 是 | 分页大小<br>**示例值**：100 |
| `name` | `string` | 否 | 名称<br>**示例值**：keyword |
| `query_language` | `string` | 否 | 语言<br>**示例值**：zh |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `job\[\]` | 查询的职务信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职务 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 是否启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_title` | `i18n\[\]` | 职务头衔 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id_list` | `string\[\]` | 职务序列 ID 列表，枚举值及详细信息可通过【批量查询职务序列】接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_level_id_list` | `string\[\]` | 职务级别 ID 列表，枚举值及详细信息可通过【批量查询职务级别】接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `working_hours_type_id` | `string` | 工时制度 ID，枚举值及详细信息可通过【批量查询工时制度】接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 生效时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 失效时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(如123, 123.23, "true", [\"id1\",\"id2\"], "2006-01-02 15:04:05") |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "id": "4698040628992333549",
                "code": "JP422119",
                "name": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ],
                "description": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ],
                "active": true,
                "job_title": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ],
                "job_family_id_list": [
                    "4719519211875096301"
                ],
                "job_level_id_list": [
                    "4719519212005299950"
                ],
                "working_hours_type_id": "6890452208593372679",
                "effective_time": "2020-01-01 00:00:00",
                "expiration_time": "2021-01-01 00:00:00",
                "custom_fields": [
                    {
                        "field_name": "name",
                        "value": "\"Sandy\""
                    }
                ]
            }
        ],
        "has_more": true,
        "page_token": "1234452132"
    }
}
```


