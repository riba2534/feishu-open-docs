---
title: "查询职等"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query"
updateTime: "1728972617000"
---

# 查询职等信息

查询职等的详细信息。


> **Tip**: - 每次最多传 100 个职等 ID 和 Code，如果不传则默认无筛选条件，返回全部列表


> **Warning**: - 延迟说明：数据库主从延迟 2s 以内，即：直接创建职等后2s内调用此接口可能查询不到数据。
> - 所有筛选项可一起使用，之间为 AND 关系


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/job_grades/query |
| HTTP Method | POST |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:corehr:readonly` 获取核心人事信息 `corehr:job_grade:read` 查看职等信息 `corehr:job_grade:write` 查看、创建、更新、删除职等信息 `corehr:corehr` 更新核心人事信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 是 | 分页大小，最大 100<br>**示例值**：100<br>**数据校验规则**：<br>- 取值范围：`1` ～ `100` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：6891251722631890445 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `ids` | `string\[\]` | 否 | 职等 ID 列表，不填写则返回全部列表<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| `codes` | `string\[\]` | 否 | 职等 code 列表，不填写则返回全部列表<br>**示例值**：["A1234"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| `active` | `boolean` | 否 | 是否启用，不填写则不作为过滤条件<br>**示例值**：true |


### 请求体示例

```json
{
    "ids": [
        "7140964208476371111"
    ],
    "codes": [
        "A1234"
    ],
    "active": true
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `job_grade\[\]` | 职等信息列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_grade_id` | `string` | 职等 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `grade_order` | `int` | 职等数值，数字越大代表职等越高 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `names` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言，支持中文和英文。中文用 zh-CN；英文用 en-US。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `descriptions` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言，支持中文和英文。中文用 zh-CN；英文用 en-US。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 是否启用 |
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
                "job_grade_id": "4692446793125560154",
                "grade_order": 9999,
                "code": "A01234",
                "names": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ],
                "descriptions": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ],
                "active": true
            }
        ],
        "page_token": "4692446793125560154",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 503 | 1161204 | Request timeout | 网络超时，请减少批量查询数量重试 |
| 429 | 1161604 | QPS over limit | 查询频率过高，请降低频率重试 |


