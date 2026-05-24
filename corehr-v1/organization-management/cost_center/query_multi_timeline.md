---
title: "批量查询成本中心版本信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/query_multi_timeline"
updateTime: "1778206853000"
---

# 批量查询成本中心版本信息

根据成本中心 ID 列表，批量查询开始结束时间内的所有成本中心版本信息，含成本中心名称、编码、上级成本中心、负责人、版本生效日期、版本失效日期、是否启用、描述等信息。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/cost_centers/query_multi_timeline |
| HTTP Method | POST |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:cost_center:read` 查看成本中心信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

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
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：people_corehr_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`people_corehr_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `cost_center_ids` | `string\[\]` | 是 | 成本中心 ID 列表，详细信息可通过[【搜索成本中心信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口查询获得<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 长度范围：`1` ～ `10` |
| `effective_date_start` | `string` | 否 | 生效日期开始(包含)<br>- 若不传入 effective_date_start 和 effective_date_end，默认返回当前生效版本。 - 支持单独传入：仅传 effective_date_start 时，返回该日期及之后生效的版本。 - 与 effective_date_end 同时传入时，返回两者交集范围内生效的版本<br>**示例值**："2024-01-01"<br>**数据校验规则**：<br>- 长度范围：`10` ～ `10` 字符 - 正则校验：`^((([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29))$` |
| `effective_date_end` | `string` | 否 | 生效日期结束(包含)<br>- 若不传入 effective_date_start 和 effective_date_end，默认返回当前生效版本。 - 支持单独传入：仅传 effective_date_end 时，返回该日期及之前生效的版本。 - 与 effective_date_start 同时传入时，返回两者交集范围内生效的版本。<br>**示例值**："2024-12-31"<br>**数据校验规则**：<br>- 长度范围：`10` ～ `10` 字符 - 正则校验：`^((([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29))$` |
| `fields` | `string\[\]` | 否 | 返回数据的字段列表，可选 - name：成本中心名称 - code：编码 - active：当前实体是否启用 - parent_cost_center_id： 上级成本中心ID - managers：成本中心负责人ID 列表 - description：成本中心描述 - effective_date：版本生效日期 - expiration_date：版本失效日期<br>**示例值**：["name"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |


### 请求体示例

```json
{
    "cost_center_ids": [
        "7140964208476371111"
    ],
    "effective_date_start": "2024-01-01",
    "effective_date_end": "2024-12-31",
    "fields": [
        "name"
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
| &nbsp;&nbsp;└ `items` | `cost_center_timeline\[\]` | 成本中心信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_id` | `string` | 成本中心ID，详细信息可通过[【搜索成本中心信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `version_id` | `string` | 成本中心版本ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 成本中心名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言，支持中文和英文。中文用zh-CN；英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `parent_cost_center_id` | `string` | 上级成本中心ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `managers` | `string\[\]` | 成本中心负责人ID 列表，详细信息可通过[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 成本中心描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_date` | `string` | 版本生效日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_date` | `string` | 版本失效日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 当前实体是否启用 |
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
                "cost_center_id": "6969828847121885087",
                "version_id": "6969828847121885087",
                "name": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ],
                "code": "MDPD00000023",
                "parent_cost_center_id": "6862995757234914824",
                "managers": [
                    "6862995757234914824"
                ],
                "description": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ],
                "effective_date": "2020-01-01",
                "expiration_date": "2020-01-01",
                "active": true
            }
        ],
        "page_token": "6969828847121885087",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1160001 | param is invalid | 请检查参数是否合法 |
| 503 | 1161204 | Request timeout | 联系飞书人事 Oncall |
| 429 | 1161604 | QPS over limit | 联系飞书人事 Oncall |


