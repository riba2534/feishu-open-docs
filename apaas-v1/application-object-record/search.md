---
title: "搜索记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/apaas-v1/application-object/search"
updateTime: "1727087317000"
---

# 搜索记录

在应用内搜索记录


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/apaas/v1/applications/:namespace/objects/search |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `app_engine:object.record:read` 查看对象记录数据 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `namespace` | `string` | 应用命名空间<br>**示例值**："package_test__c"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `256` 字符 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `q` | `string` | 否 | 搜索词<br>**示例值**："搜索关键字" |
| `search_objects` | `search_object_param\[\]` | 否 | 搜索对象范围<br>**数据校验规则**：<br>- 长度范围：`0` ～ `256` |
| &nbsp;&nbsp;└ `api_name` | `string` | 否 | 对象 APIName<br>**示例值**："_user"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `256` 字符 |
| &nbsp;&nbsp;└ `search_fields` | `string\[\]` | 否 | 搜索字段 SearchFields 列表<br>**示例值**：["_id"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `500` |
| &nbsp;&nbsp;└ `select` | `string\[\]` | 否 | 召回字段 APIID/APIName 列表<br>**示例值**：["_id"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` |
| &nbsp;&nbsp;└ `filter` | `criterion` | 否 | 过滤条件，序列化的结果{"filter": "「标准Criterion」"} |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `conditions` | `condition\[\]` | 否 | 查询条件<br>**数据校验规则**：<br>- 长度范围：`0` ～ `10` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `index` | `string` | 否 | 序号<br>**示例值**："1" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `left` | `condition_value` | 否 | 左值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 否 | 左值类型，只支持 "metadataVariable"，表示字段<br>**示例值**："metadataVariable" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `settings` | `string` | 否 | 字段具体值，以 JSONString 表示，格式：{"fieldPath":[{"fieldApiName": "字段名","objectApiName": "对象名"}]}<br>**示例值**："{\"fieldPath\":[{\"fieldApiName\": \"_id\",\"objectApiName\": \"_user\"}]}" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `right` | `condition_value` | 否 | 右值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 否 | 右值类型，只支持 "constant"，表示常量<br>**示例值**："constant" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `settings` | `string` | 否 | 常量具体值，以 JSONString 表示，格式：{"data":"常量具体值"}<br>**示例值**："{\"fieldPath\":[{\"fieldApiName\": \"_id\",\"objectApiName\": \"_user\"}]}" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `operator` | `string` | 否 | 操作符<br>**示例值**："equal" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `logic_expression` | `string` | 否 | 逻辑关系<br>**示例值**："1 and 2" |
| &nbsp;&nbsp;└ `order_by` | `order_condition` | 否 | 排序条件 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `field` | `string` | 否 | 字段名<br>**示例值**："_id"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `256` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `order_type` | `string` | 否 | 排序方式<br>**示例值**："asc"<br>**可选值有**：<br>- `asc`: 升序 - `desc`: 降序<br>**数据校验规则**：<br>- 长度范围：`0` ～ `256` 字符 |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**："eyJvYmplY3RzX3BhZ2VfdG9rZW4iOlt7Im9ial9pZCI6MTc2OTI4NzM5M" |
| `page_size` | `string` | 否 | 返回数量，默认为50，最大不超过2000<br>**示例值**："100" |
| `metadata` | `string` | 否 | 返回元数据枚举值<br>**示例值**："Label"<br>**可选值有**：<br>- `Label`: 只返回 Label - `SearchLayout`: 返回搜索布局信息 |


### 请求体示例

```json
{
    "q": "搜索关键字",
    "search_objects": [
        {
            "api_name": "_user",
            "search_fields": [
                "_id"
            ],
            "select": [
                "_id"
            ],
            "filter": {
                "conditions": [
                    {
                        "index": "1",
                        "left": {
                            "type": "metadataVariable",
                            "settings": "{\"fieldPath\":[{\"fieldApiName\": \"_id\",\"objectApiName\": \"_user\"}]}"
                        },
                        "right": {
                            "type": "constant",
                            "settings": "{\"fieldPath\":[{\"fieldApiName\": \"_id\",\"objectApiName\": \"_user\"}]}"
                        },
                        "operator": "equal"
                    }
                ],
                "logic_expression": "1 and 2"
            },
            "order_by": {
                "field": "_id",
                "order_type": "asc"
            }
        }
    ],
    "page_token": "eyJvYmplY3RzX3BhZ2VfdG9rZW4iOlt7Im9ial9pZCI6MTc2OTI4NzM5M",
    "page_size": "100",
    "metadata": "Label"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `records` | `string` | 搜索结果列表 |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `next_page_token` | `string` | 分页标记，当 HasMore 为 true 时，会同时返回新的 NextPageToken |
| &nbsp;&nbsp;└ `objects` | `object_meta\[\]` | 对象信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `object` | `object` | 对象信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `int` | 对象 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `api_name` | `string` | 对象 API 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `label` | `map<string, string>` | 对象名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `settings` | `object_settings` | 对象配置 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_name` | `string` | 展示名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `allow_search_fields` | `string\[\]` | 允许搜索字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `search_layout` | `object_search_layout` | 展示字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_fields` | `string\[\]` | 展示字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `fields` | `object_field\[\]` | 字段信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `int` | 字段 id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `api_name` | `string` | API 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `label` | `map<string, string>` | 字段名称 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "records": "[]",
        "has_more": true,
        "next_page_token": "eyJvYmplY3RzX3BhZ2VfdG9rZW4iOlt7Im9ial9pZCI6MTc2OTI4NzM5M",
        "objects": [
            {
                "object": {
                    "id": 1764024447556775,
                    "api_name": "user",
                    "label": {
                        "zh_cn": "text"
                    },
                    "settings": {
                        "display_name": "_id",
                        "allow_search_fields": [
                            "_id"
                        ],
                        "search_layout": {
                            "display_fields": [
                                "_id"
                            ]
                        }
                    }
                },
                "fields": [
                    {
                        "id": 1764024447525960,
                        "api_name": "user",
                        "type": "string",
                        "label": {
                            "zh_cn": "text"
                        }
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
| 400 | 2320001 | param is invalid | 请检查输入参数 |


