---
title: "查询岗位信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/position/query"
updateTime: "1770621346000"
---

# 查询岗位信息

支持通过岗位 ID、部门 ID 查询岗位的详细信息，例如岗位关联的职务、职级、序列，以及岗位描述，是否关键岗位等


> **Tip**: #### 前提条件:
> - 本接口会按照「岗位资源」权限范围返回数据，请确定在「开发者后台 - 权限管理 - 数据权限」中已申请此数据权限


> **Warning**: #### 限制说明:
> - 在筛选 ID 和 查询字段对象个数过多时，可能出现超时现象，请减少筛选项和字段对象个数。阻塞性问题请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)
> - 所有筛选项可一起使用，之间为 AND 关系
> - 请求体入参不填写默认为空，不参与筛选


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/positions/query |
| HTTP Method | POST |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:position:read` 获取岗位信息 `corehr:position:write` 读写岗位信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `department_id_type` | `string` | 否 | 此次调用中使用的部门 ID 类型，三种类型的 ID 都可通过飞书人事的[批量查询部门（ V2）](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get) 来获取<br>**示例值**：people_corehr_department_id<br>**可选值有**：<br>- `open_department_id`: 以 open_department_id 来标识部门 - `department_id`: 以 department_id 来标识部门 - `people_corehr_department_id`: 以 people_corehr_department_id 来标识部门<br>**默认值**：`people_corehr_department_id` |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：people_corehr_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`people_corehr_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `page_size` | `int` | 是 | 分页大小，最大 100<br>**示例值**：100<br>**数据校验规则**：<br>- 取值范围：`1` ～ `100` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：6891251722631897745 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `department_ids` | `string\[\]` | 否 | 部门 ID 列表 - department_ids参数的ID类型需与department_id_type参数取值一致 - 可通过飞书人事的[批量查询部门（ V2）](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get) 来获取<br>**示例值**：["7094136522860922111"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| `effective_time` | `string` | 否 | 生效日期，格式是 YYYY-MM-DD<br>**示例值**："2020-01-01"<br>**数据校验规则**：<br>- 长度范围：`10` ～ `10` 字符 - 正则校验：`^((([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29))$` |
| `active` | `boolean` | 否 | 启停用状态：true 为启用，false 为停用，不传则默认都返回<br>**示例值**：true |
| `fields` | `string\[\]` | 否 | 需要查询的字段列表，为空时仅返回 wk_id。可选以下预置字段及自定义字段： - "wk_id"：岗位 ID - "name"：名称 - "code"：编码 - "active"：状态 - "department"：所属部门 - "cost_center"：岗位默认成本中心 - "job"：职务 - "job_family"：序列 - "job_level"：职级 - "job_grade"：职等 - "work_location"：工作地点 - "employee_type"：人员类型 - "working_hours_type"：工时制度 - "direct_leader"：直属上级 - "dotted_line_leader"：虚线上级 - "is_key_position"：是否关键岗位 - "description"：描述 - "effective_time"：版本生效日期 - "expiration_time"：版本过期时间 - "created_by"：创建人 - "custom_fields"：自定义字段(需传入具体的"custom_api_name")详细见[获取自定义字段列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query) ,比如:"shifouleixing_7795__c"<br>**示例值**：["name"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| `position_ids` | `string\[\]` | 否 | 岗位 ID 列表<br>**示例值**：["7094136582860923111"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `200` |
| `position_codes` | `string\[\]` | 否 | 岗位 Code 列表<br>**示例值**：["42232132221241561"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `200` |


### 请求体示例

```json
{
    "department_ids": [
        "7094136522860922111"
    ],
    "effective_time": "2020-01-01",
    "active": true,
    "fields": [
        "name"
    ],
    "position_ids": [
        "7094136582860923111"
    ],
    "position_codes": [
        "42232132221241561"
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
| &nbsp;&nbsp;└ `items` | `position\[\]` | 岗位信息列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `position_id` | `string` | 岗位 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `names` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `descriptions` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 状态，true表示启用，false表示停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id_list` | `string\[\]` | 序列 ID 列表，详细信息可通过[查询单个序列](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/get)接口获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_id` | `string` | 成本中心 ID，可以通过[搜索成本中心信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获取对应的成本中心信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_id` | `string` | 职务，可通过[【查询单个职务】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_level_id_list` | `string\[\]` | 职级 ID 列表，可通过[【查询单个职级】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type_id_list` | `string\[\]` | 人员类型 ID 列表，可通过文档[查询人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/get)获得详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_grade_id_list` | `string\[\]` | 职等 ID 列表，可通过 [【查询职等】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_location_id_list` | `string\[\]` | 工作地点 ID 列表，详细信息可通过[查询单个地点](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/get)接口获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `working_hours_type_id` | `string` | 工时制度 ID 列表，可通过[【查询单个工时制度】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/get)查询详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 部门 ID，详细信息可通过[查询单个部门](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)接口获得 - 类型与 department_id_type 一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `direct_leader_id` | `string` | 直属上级岗位 ID，可通过本接口查询详细信息 - 若查询的是一级岗位，则该字段不展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dotted_line_leader_id` | `string` | 虚线上级岗位 ID，可通过本接口查询详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_key_position` | `boolean` | 是否关键岗位 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 生效日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 失效日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型，详细见[获取自定义字段列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_by` | `string` | 创建人 |
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
                "position_id": "4692446793125560154",
                "code": "A01234",
                "names": [
                    {
                        "lang": "zh-CN",
                        "value": "高级产品经理"
                    }
                ],
                "descriptions": [
                    {
                        "lang": "zh-CN",
                        "value": "岗位的描述"
                    }
                ],
                "active": true,
                "job_family_id_list": [
                    "4719519211875096301"
                ],
                "cost_center_id": "4719519211875096301",
                "job_id": "4719519211875096302",
                "job_level_id_list": [
                    "4719519211875096301"
                ],
                "employee_type_id_list": [
                    "4719519211875096301"
                ],
                "job_grade_id_list": [
                    "4719519211875096301"
                ],
                "work_location_id_list": [
                    "4719519211875096301"
                ],
                "working_hours_type_id": "4719519211875096301",
                "department_id": "4719519211875096301",
                "direct_leader_id": "4719519211875096301",
                "dotted_line_leader_id": "4719519211875096301",
                "is_key_position": true,
                "effective_time": "2020-05-01",
                "expiration_time": "2020-05-01",
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
                ],
                "created_by": "4719519211875096301"
            }
        ],
        "page_token": "eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0=",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 503 | 1161204 | Requset timeout | 接口超时，请减少批量查询数量后重试，调整查询参数“page_size”至更小值（最大值100）。必要时请联系 [技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 429 | 1161604 | QPS over limit | QPS 超出限制，请降低查询频率重试，必要时请联系 [技术支持](https://applink.feishu.cn/TLJpeNdW) |


