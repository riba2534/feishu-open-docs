---
title: "查询指定生效日期的部门基本信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/query_timeline"
updateTime: "1779277899000"
---

# 查询指定日期的部门基本信息

查询指定生效的部门基本信息，含部门名称、部门类型、上级、编码、负责人、是否启用、描述等信息


> **Warning**: 延迟说明：数据库主从延迟 2s 以内，即：直接创建部门后2s内调用此接口可能查询不到数据。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/departments/query_timeline |
| HTTP Method | POST |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:department:read` 获取部门信息 `corehr:department:write` 读写部门信息 |
| 字段权限要求 | &gt; **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `corehr:department.cost_center_id:read` 获取部门成本中心字段信息 `corehr:department.custom_fields:read` 获取部门自定义字段 `corehr:department.manager:read` 获取部门负责人信息 `corehr:department.organize:read` 获取部门组织架构信息 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：people_corehr_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`people_corehr_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 此次调用中使用的部门 ID 类型<br>**示例值**：people_corehr_department_id<br>**可选值有**：<br>- `open_department_id`: 【飞书】用来在具体某个应用中标识一个部门，同一个department_id 在不同应用中的 open_department_id 相同。 - `department_id`: 【飞书】用来标识租户内一个唯一的部门。 - `people_corehr_department_id`: 【飞书人事】用来标识「飞书人事」中的部门。<br>**默认值**：`people_corehr_department_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `department_ids` | `string\[\]` | 是 | 部门 ID 列表 - 可通过[批量查询部门V2](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get) 或者[搜索部门信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/search) 获取详情<br>**示例值**：["7094136522860922111"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| `effective_date` | `string` | 是 | 版本生效日期 - 填写格式：YYYY-MM-DD - 系统默认为填写日期当天的 00:00:00 生效  - 该接口只支持到最小单位为日 - 日期范围要求:1900-01-01～9999-12-31<br>**示例值**："2020-01-01"<br>**数据校验规则**：<br>- 长度范围：`10` ～ `10` 字符 - 正则校验：`^((([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29))$` |
| `fields` | `string\[\]` | 否 | 需要返回的字段列表，字段可填写的列表如下： - department_name：部门名称 - sub_type：部门子类型 - tree_order：树形排序 - list_order：列表排序 - is_root：是否根部门 - is_confidential：是否保密 - staffing_model：岗职务模式 - cost_center_id：部门默认成本中心 - code：部门编码 - active：是否启用 - parent_department_id：上级部门ID - manager：负责人 - description：部门描述 - effective_date：当前版本生效日期 - expiration_date：当前版本失效日期 - custom_fields(自定义字段需传入具体的"custom_api_name"详细见[获取自定义字段列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query) ,比如:"shifouleixing_7795__c)<br>**示例值**：["department_name"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |


### 请求体示例

```json
{
    "department_ids": [
        "7094136522860922111"
    ],
    "effective_date": "2020-01-01",
    "fields": [
        "department_name"
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
| &nbsp;&nbsp;└ `items` | `department_timeline\[\]` | 部门信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 部门 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `version_id` | `string` | 部门版本 ID(默认返回) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `names` | `i18n\[\]` | 部门名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言，中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sub_type` | `enum` | 部门类型 - 通过[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)查询获取。请求参数：object_api_name=department；custom_api_name=subtype。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `parent_department_id` | `string` | 上级部门 ID  - 可通过[批量查询部门V2](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get) 或者[搜索部门信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/search) 获取详情 - 若查询的是一级部门，则该字段不展示<br>**字段权限要求**： `corehr:department.organize:read` 获取部门组织架构信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `manager` | `string` | 部门负责人，填写员工的雇佣ID - 详细信息可通过[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search) 或 [【批量查询员工】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get) 接口获取<br>**字段权限要求**： `corehr:department.manager:read` 获取部门负责人信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_date` | `string` | 当前版本生效日期 - 返回格式：YYYY-MM-DD（最小单位到日） - 日期范围:1900-01-01～9999-12-31 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 是否启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `descriptions` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言，中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段类型，详细见[获取自定义字段列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query) <br>**字段权限要求**： `corehr:department.custom_fields:read` 获取部门自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型，详细见[获取自定义字段列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_date` | `string` | 当前版本失效日期 - 返回格式：YYYY-MM-DD（最小单位到日） - 日期范围：1900-01-01 ～9999-12-31 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tree_order` | `string` | 树形排序，代表同层级的部门排序序号 - 数据类型为字符串，实际按数值大小排序，数值越小，同层级部门展示越靠前；仅对同一父部门下的直接子部门生效 - 数值生成规则：   -  编号长度由同层级部门数量动态决定：同层级部门≤10 个为 6 位编号，10~20 个为 7 位编号，超过 100 个统一为 16 位编号，以此类推   - 新建部门时系统自动赋值：同层级下一个新部门编号，会在上一个部门编号基础上按固定数值自动累加；例如 6 位编号每次固定加 1000，7 位编号每次固定加 10000   - 重排触发：当同层级部门数量超出当前编号长度可容纳范围，或多次拖拽排序无法正常插入位置时，会触发同层级编号全局重新编排；所有部门编号会按新的长度和累加规则重新生成，数值可能出现明显变大   - 当同一父部门下的子部门数量超过 1000 个时，系统在维护排序编号时可能出现异常问题。 - 更新时机：   - 创建部门场景tree_order不会实时生成，10分钟内更新完毕   - 在页面拖动部门排序时tree_order可以实时生成   - 变更部门上级时，会清空tree_order，并触发重算list_order和tree_order，10分钟内更新完毕（list_order由部门上级路径的所有tree_order用“-”拼接生成） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `list_order` | `string` | 列表排序，代表所有部门的混排序号，为该部门上级路径上所有tree_order用“-”拼接。 - 该字段在新建/更新场景非立即更新，10分钟后会延迟更新 - 由于list_order变更会导致[部门变更接口](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/events/updated)产生大量事件，因此事件接口不会针对该字段同步变更事件，如果有需求订阅请联系[Oncall](https://applink.feishu.cn/TLJpeNdW)单独开启。 - 同层部门（相同上级）数量超过1000时，该字段不再更新 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_root` | `boolean` | 是否根部门(默认返回) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_confidential` | `boolean` | 是否保密（该功能暂不支持，可以忽略） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `staffing_model` | `enum` | 岗职管理模式 - 详细枚举类型请查看[枚举场景](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)中关于staffing_model定义 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_id` | `string` | 成本中心id<br>**字段权限要求**： `corehr:department.cost_center_id:read` 获取部门成本中心字段信息 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "id": "4719456877659520852",
                "version_id": "7238516215202170412",
                "names": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ],
                "sub_type": {
                    "enum_name": "phone_type",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "parent_department_id": "4719456877659520111",
                "manager": "6893013238632416777",
                "code": "D00000456",
                "effective_date": "2020-05-01",
                "active": true,
                "descriptions": [
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
                ],
                "expiration_date": "2020-05-02",
                "tree_order": "001000",
                "list_order": "001000-001000",
                "is_root": false,
                "is_confidential": false,
                "staffing_model": {
                    "enum_name": "phone_type",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "cost_center_id": "7142384817131652652"
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 503 | 1161204 | Requset timeout | 接口超时，详情可联系飞书人事 [Oncall](https://applink.feishu.cn/TLJpeNdW) |
| 429 | 1161604 | QPS over limit | 接口请求次数超过接口频率限制，可尝试降低请求频率 |


