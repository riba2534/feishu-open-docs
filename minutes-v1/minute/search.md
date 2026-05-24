---
title: "搜索妙记"
fullPath: "/uAjLw4CM/ukTMukTMukTM/minutes-v1/minute/search"
updateTime: "1778814032000"
---

# 搜索妙记

根据关键词、时间范围等条件搜索妙记，返回符合条件的妙记列表，包含妙记 token（用于标识妙记的唯一身份）、标题、开始时间等信息。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/minutes/v1/minutes/search |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `minutes:minutes.search:read` 搜索妙记 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 分页大小，默认15，最大单页不超过30<br>**示例值**：10 |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0= |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `query` | `string` | 否 | 搜索关键词<br>**示例值**："周会"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `50` 字符 |
| `filter` | `minutes_filter` | 否 | 妙记搜索的过滤条件 |
| &nbsp;&nbsp;└ `owner_ids` | `string\[\]` | 否 | 按妙记创建者过滤，传入用户 open_id 列表，可通过用户查询接口获取。默认值为空数组，不设置时不过滤该条件。<br>**示例值**：["ou-7890123456abcdef"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;└ `participant_ids` | `string\[\]` | 否 | 按妙记参与者过滤，传入用户 open_id 列表，可通过用户查询接口获取。默认值为空数组，不设置时不过滤该条件。<br>**示例值**：["ou-7890123456abcdef"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;└ `create_time` | `time_range` | 否 | 按妙记创建时间过滤，传入时间范围对象。其中 start_time 必须小于等于 end_time |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 否 | 起始时间，需符合 ISO 8601 标准并携带时区信息（create_time 的子参数<br>**示例值**："2026-03-21T16:15:30+08:00" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 否 | 结束时间，需符合 ISO 8601 标准并携带时区信息（create_time 的子参数<br>**示例值**："2026-03-21T16:15:30+08:00" |


### 请求体示例

```json
{
    "query": "周会",
    "filter": {
        "owner_ids": [
            "ou-7890123456abcdef"
        ],
        "participant_ids": [
            "ou-7890123456abcdef"
        ],
        "create_time": {
            "start_time": "2026-03-21T16:15:30+08:00",
            "end_time": "2026-03-21T16:15:30+08:00"
        }
    }
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `minutes_search_item\[\]` | 妙记列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 妙记 Token（标识妙记唯一身份的凭证） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `display_info` | `string` | 包含妙记基本信息的卡片，用户搜索关键词命中的文本片段，使用标签包裹标注 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `meta_data` | `minutes_meta` | 妙记元信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `app_link` | `string` | 妙记跳转链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar` | `string` | 妙记封面图片 URL |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 妙记描述 |
| &nbsp;&nbsp;└ `total` | `int` | 总数 |
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
                "token": "obbcwkkdw885tetaf82pu184",
                "display_info": "2026-03-28 产品周会纪要",
                "meta_data": {
                    "app_link": "https://example.feishu.cn/minutes/xxxxxx",
                    "avatar": "https://p3-lark-file.byteimg.com/img/xxxx.jpg",
                    "description": "产品周会纪要"
                }
            }
        ],
        "has_more": true,
        "page_token": "fcefd50bc6e8026a="
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2094001 | invalid request parameter | 请求参数不合法，请检查各参数是否符合类型/取值范围要求后重试 |
| 400 | 2094002 | query is too long | 搜索关键词过长，请缩短 query 长度后重试 |
| 400 | 2094003 | invalid filter | 过滤条件无效，请检查 minutes_filter 各字段取值（如 ID 格式、时间范围）是否合法 |
| 400 | 2094004 | invalid sorter | 排序条件无效，请核对后重试 |
| 400 | 2094005 | page_token is invalid or expired, please start a new search | 翻页 token 无效或已过期，请重新发起新的搜索请求 |
| 400 | 2094006 | page_size exceeds maximum allowed value | 每页条数超过上限，请调小 page_size 后重试 |
| 400 | 2094007 | pagination limit reached, please refine your query with more specific keywords or filters | 翻页已达最大偏移，请使用更精确的 query 或 minutes_filter 缩小结果集后重试 |
| 401 | 2094011 | user identity not found, please check your access token | 无法识别用户身份，请确保使用 user_access_token 调用并检查其有效性 |
| 401 | 2094012 | failed to initialize request context, please check your access token | 请求上下文初始化失败，通常为 access_token 失效或缺失必要字段，请检查鉴权信息 |
| 500 | 2095001 | search service error | 搜索下游服务异常，请稍后重试 |
| 500 | 2095002 | failed to process search result | 搜索结果处理失败，通常为下游数据格式异常，请稍后重试 |
| 400 | 2094101 | failed to build minutes filter | 妙记过滤条件构建失败，请检查参数是否合法 |
| 400 | 2094102 | minutes time format is invalid, expected ISO 8601 | 妙记时间格式不正确，create_time.start_time / end_time 必须使用 ISO 8601（例如 2024-01-01T00:00:00Z） |
| 500 | 2095101 | failed to convert minutes search result | 妙记搜索结果转换失败，通常为下游 Meta 数据缺失或格式异常，请稍后重试 |


