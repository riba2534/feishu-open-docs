---
title: "查询语言信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-language/search"
updateTime: "1728546532000"
---

# 查询语言信息

根据语言 ID、状态，批量查询语言信息


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/basic_info/languages/search |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:common_data.basic_data:read` 获取基础数据信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 是 | 分页大小，最大 100<br>**示例值**：100<br>**数据校验规则**：<br>- 取值范围：`1` ～ `100` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：6862995772275688974 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `language_id_list` | `string\[\]` | 否 | 语言 ID 列表，如果为空，返回所有数据<br>**示例值**：["6863323445740963342"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| `status_list` | `int\[\]` | 否 | 状态列表<br>**示例值**：[1]<br>**可选值有**：<br>- `1`: 生效 - `0`: 失效<br>**默认值**：`[1]`<br>**数据校验规则**：<br>- 长度范围：`0` ～ `2` |


### 请求体示例

```json
{
    "language_id_list": [
        "6863323445740963342"
    ],
    "status_list": [
        1
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
| &nbsp;&nbsp;└ `items` | `language\[\]` | 查询到的语言列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `language_id` | `string` | 语言 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 语言名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ietf_language_tag` | `string` | IETF 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 状态<br>**可选值有**：<br>- `1`: 生效 - `0`: 失效 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "language_id": "6863323445740963342",
                "name": [
                    {
                        "lang": "zh-CN",
                        "value": "英文（英国）"
                    }
                ],
                "ietf_language_tag": "en-UK",
                "status": 1
            }
        ],
        "page_token": "6863323445740963342",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1160998 | Internal Server Error | 系统错误，请稍后重试。如有问题请联系技术支持 |


