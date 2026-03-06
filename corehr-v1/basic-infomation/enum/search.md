---
title: "查询枚举信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/enum/search"
updateTime: "1736481355000"
---

# 查询枚举信息

根据枚举的APIName查询枚举详细信息，用于BPM等场景获取枚举选项。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/enums/search |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:common_data.meta_data:read` 获取元数据信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `enum_apiname_lists` | `string\[\]` | 否 | 枚举apiname列表（不传值查询结果为空）<br>**示例值**：["overtime_date_type"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `500` |


### 请求体示例

```json
{
    "enum_apiname_lists": [
        "overtime_date_type"
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
| &nbsp;&nbsp;└ `enums` | `enums\[\]` | 查询的枚举信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `enum_apiname` | `string` | 枚举名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `enum_items` | `enum_field\[\]` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `api_name` | `string` | ApiName |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 枚举值名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 枚举值描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_api_name` | `string` | 所属枚举常量ApiName |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `order` | `int` | 顺序 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 状态<br>**可选值有**：<br>- `1`: 生效 - `0`: 失效 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "enums": [
            {
                "enum_apiname": "overtime_date_type",
                "enum_items": [
                    {
                        "api_name": "special_day",
                        "name": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ],
                        "description": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ],
                        "enum_api_name": "overtime_date_type",
                        "order": 1,
                        "status": 1
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
| 500 | 1160998 | Internal Server Error | 服务内部错误，请稍后重试。如有问题请[联系技术支持]((https://applink.feishu.cn/TLJpeNdW)) |


