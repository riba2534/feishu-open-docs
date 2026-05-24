---
title: "搜索会议记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/search"
updateTime: "1774684469000"
---

# 搜索会议记录

根据关键词、时间范围等条件搜索会议记录，返回符合条件的会议列表，包含会议 ID、主题、开始时间及参与者等信息。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/vc/v1/meetings/search |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `vc:meeting.search:read` 搜索视频会议 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0= |
| `page_size` | `int` | 否 | 分页大小，**默认15**，最大单页**不超过30**<br>**注意：** 最多返回**150条**记录<br>**示例值**：10 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `query` | `string` | 否 | 搜索关键词<br>**数据校验规则：** 长度范围：1 字符 ～ 50 字符<br>**示例值**："周会" |
| `meeting_filter` | `meeting_filter` | 否 | 会议搜索的过滤条件 |
| &nbsp;&nbsp;└ `organizer_ids` | `string\[\]` | 否 | 按会议组织者过滤，传入用户 open_id 列表，可通过用户查询接口获取。默认值为空数组，不设置时不过滤该条件。<br>**示例值**：["ou_789012"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `128` |
| &nbsp;&nbsp;└ `participant_ids` | `string\[\]` | 否 | 按参会人过滤，传入用户 open_id 列表，可通过用户查询接口获取。默认值为空数组，不设置时不过滤该条件。长度范围：0～128。<br>**示例值**：["ou_789012"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `128` |
| &nbsp;&nbsp;└ `open_room_ids` | `string\[\]` | 否 | 按会议室过滤，传入会议室 open_id 列表，可通过会议室查询接口获取。默认值为空数组，不设置时不过滤该条件。长度范围：0～128。<br>**示例值**：["omm_4de32cf10a4358788ff4e09e37ebbf9b"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `128` |
| &nbsp;&nbsp;└ `start_time` | `time_range` | 否 | 按会议开始时间过滤，传入时间范围对象。其中 start_time 必须小于等于 end_time（即 meeting_filter.start_time.end_time）。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 否 | 时间范围的起始时间，需符合 ISO 8601 标准并携带时区信息。<br>**示例值**："2026-03-21T16:15:30+08:00" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 否 | 时间范围的结束时间，需符合 ISO 8601 标准并携带时区信息。<br>**示例值**："2026-03-21T16:15:30+08:00" |


### 请求体示例

```json
{
    "query": "周会",
    "meeting_filter": {
        "organizer_ids": [
            "ou_789012"
        ],
        "participant_ids": [
            "ou_789012"
        ],
        "open_room_ids": [
            "omm_4de32cf10a4358788ff4e09e37ebbf9b"
        ],
        "start_time": {
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
| &nbsp;&nbsp;└ `total` | `int` | 匹配结果总数（辅助分页参考） |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `items` | `meeting_search_item\[\]` | 返回结果列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 会议ID（视频会议的唯一标识，视频会议开始后才会产生） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `display_info` | `string` | 包含基本信息的卡片，用户搜索关键词命中的文本片段，使用标签包裹标注 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `meta_data` | `meeting_meta` | 会议元信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `app_link` | `string` | 跳转链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar` | `string` | 图标url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 描述，包含会议时间、组织者和会议ID |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "total": 10,
        "has_more": true,
        "items": [
            {
                "id": "6911188411932033028",
                "display_info": "会议名 \n 片段1＜h>搜索词/h>片段2\n 会议时间 | 组织者：组织者姓名 | ID: 会议ID",
                "meta_data": {
                    "app_link": "https://applink.larkoffice.com/*",
                    "avatar": "https://lf-packag*",
                    "description": "会议时间 | 组织者：组织者姓名 | ID：123456789"
                }
            }
        ],
        "page_token": "eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0="
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 121001 | invalid param | 参数错误，请检查以下参数的取值范围是否符合要求：1. 搜索关键词（query）：长度范围 1～50 字符；2. 分页大小（page_size）：最大不超过 200；3. 组织者 OpenID（organizer_ids）、参与者 OpenID（participant_ids）、会议室 ID（open_room_ids）：长度范围 0～128。具体要求可参考接口文档中的「请求体参数」部分 |
| 500 | 121002 | network error | 服务器内部错误，如果重试无效可联系[技术支持](https://applink.larkoffice.com/TLJpeNdW) |
| 500 | 121011 | query is too long | 参数错误，请检查 query 字段长度是否超出限制 |
| 500 | 121012 | invalid filter | 参数错误，请检查视频会议过滤参数（meeting_filter）的格式是否符合接口要求（如是否为对象类型），以及其取值范围是否符合文档描述。 |
| 500 | 121020 | page_token is invalid or expired | page_token 无效或已过期，请重新从第一页开始请求 |
| 500 | 121021 | page_size exceeds maximum allowed value | 参数错误，page_size 超出最大限制，请减小后重试 |
| 500 | 121022 | pagination limit reached | 已达到分页深度上限，建议缩小时间范围后重新查询 |
| 500 | 121030 | user identity not found | 用户身份不存在，检查 token 是否有效且未过期 |
| 500 | 121031 | failed to initialize request context | 请求上下文初始化失败，检查 token 类型是否与接口要求一致 |
| 500 | 121040 | search service error | 服务器内部错误，如果重试无效可联系[技术支持](https://applink.larkoffice.com/TLJpeNdW) |
| 500 | 121041 | failed to process search result | 服务器内部错误，如果重试无效可联系[技术支持](https://applink.larkoffice.com/TLJpeNdW) |
| 500 | 122601 | meeting time format is invalid | 参数错误，请检查时间字段（如 start_time）的格式是否符合 ISO 8601 标准（示例：2026-03-21T16:15:30+08:00） |
| 500 | 122602 | failed to build meeting filter | 参数错误，请检查 meeting_filter 参数的筛选条件是否符合接口文档中的要求 |
| 500 | 122603 | failed to convert meeting search result | 服务器内部错误，如果重试无效可联系[技术支持](https://applink.larkoffice.com/TLJpeNdW) |
| 500 | 122604 | invalid meeting room ID format | 参数错误，请检查会议室 ID（open_room_ids）的格式是否与示例值一致（如 omm_4de32cf10a4358788ff4e09e37ebbf9b） |


