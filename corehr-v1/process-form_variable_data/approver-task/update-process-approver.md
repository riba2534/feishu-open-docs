---
title: "通过/拒绝审批任务"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/process-approver/update"
updateTime: "1770039496000"
---

# 通过/拒绝审批任务

对于单个审批任务进行通过（提交）或拒绝操作。对于多人或签节点，一个审批任务通过则整个节点通过；对于多人会签节点，所有审批任务通过则节点通过。在通过（提交）时，若表单中有必填字段，支持写入表单字段。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/processes/:process_id/approvers/:approver_id |
| HTTP Method | PUT |
| 接口频率限制 | [50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:process.instance:write` 通过或拒绝审批任务 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `process_id` | `string` | 流程实例id，是一个流程的唯一标识。<br>可通过[查询流程实例列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/process/list)接口返回的 process_ids 字段获取<br>**示例值**："7328345170959681068" |
| `approver_id` | `string` | 标识流程中一个审批节点的一个审批人的审批任务。 同一个审批节点如果有多个审批人，不同审批人的 approver_id 不同。<br>可通过 [获取单个流程详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/process/get)接口获取流程中各审批任务的 approver_id。<br>**示例值**："7381468648050787884" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 此次调用中使用的部门 ID 类型<br>**示例值**：open_department_id<br>**可选值有**：<br>- `open_department_id`: 以 open_department_id 来标识部门 - `department_id`: 以 department_id 来标识部门 - `people_corehr_department_id`: 以 people_corehr_department_id 来标识部门<br>**默认值**：`open_department_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `status` | `int` | 是 | 将审批任务修改为同意/拒绝<br>**示例值**：2<br>**可选值有**：<br>- `2`: 拒绝 - `3`: 通过 |
| `user_id` | `string` | 否 | 用户id，按user_id_type类型传递。如果system_approval为false，则必填审批任务“approver_id”对应的原审批人的user_id；为true时非必填。<br>**示例值**："ou_91791271921729102012" |
| `system_approval` | `boolean` | 否 | 是否为系统身份审批。<br>true - 使用系统身份审批，若使用系统身份，将代替approver_id对应的原审批人进行审批，原审批人将失去审批任务的查看权限；false - 按照所传的人员身份审批<br>**示例值**：true<br>**默认值**：`false` |
| `reason` | `string` | 否 | 通过/拒绝原因，当拒绝时原因必填<br>**默认值**：""<br>**示例值**："原因自定义字符串"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| `field_values_v2` | `process_form_variable_v2\[\]` | 否 | 表单数据<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100000` |
| &nbsp;&nbsp;└ `variable_api_name` | `string` | 否 | 变量唯一标识，可通过[获取流程表单数据](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/process-form_variable_data/get)查询变量<br>**示例值**："custom123" |
| &nbsp;&nbsp;└ `variable_value` | `field_variable_value_to_for_review` | 否 | 变量值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `text_value` | `string` | 否 | 文本值<br>**示例值**："测试测试" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `bool_value` | `boolean` | 否 | 布尔值<br>**示例值**：true |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `number_value` | `string` | 否 | 数字值<br>**示例值**："100" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `enum_value` | `string` | 否 | 枚举值，这里是枚举的id<br>**示例值**："home_address" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `date_value` | `string` | 否 | 从 1970 开始的天数<br>**示例值**："19838" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `date_time_value` | `string` | 否 | 时间戳，毫秒<br>**示例值**："1714013877512" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_value` | `field_variable_value_i18n` | 否 | 多语字段值<br>**示例值**：ou_c57053dad6eea0aea4696c48433d8562 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 否 | 中文值<br>**示例值**："北京" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 否 | 英文值<br>**示例值**："Beijing" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `object_value` | `field_variable_value_to_object` | 否 | 对象值<br>**示例值**：od-a761814f6bc3f14bd3b00905ec1d7c6f |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_id` | `string` | 否 | 飞书人事主数据对象唯一标识。<br>例如：<br>wk_api_name为"job"时，wk_id代表职务ID。详请可参考[查询单个职务（V2）](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/get)<br>wk_api_name为"job_level"时，wk_id代表职级ID。详情可参考[查询单个职级](https://open.larkoffice.com/document/server-docs/corehr-v1/job-management/job_level/get)<br>**示例值**："6863326263210149383" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_api_name` | `string` | 否 | 飞书人事元数据对象的唯一标识。<br>例如：<br>职务的wk_api_name为"job"；职级的wk_api_name为"job_level"；<br>如需获取更多对象信息，可查询[获取飞书人事对象列表](https://open.larkoffice.com/document/server-docs/corehr-v1/basic-infomation/custom_field/list_object_api_name)接口<br>**示例值**："country_region_subdivision" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_value` | `string` | 否 | 部门id，根据查询参数department_id_type类型选择对应的部门id。<br>可通过[搜索部门信息](https://open.larkoffice.com/document/server-docs/corehr-v1/organization-management/department/search) 或 [批量查询部门（ V2）](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)接口查询详情。<br>**示例值**："od-a761814f6bc3f14bd3b00905ec1d7c6f" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_value` | `string` | 否 | 员工类型字段值，为用户id，根据入参选择的user_id_type类型返回的用户id。<br>可通过[搜索员工信息](https://open.larkoffice.com/document/server-docs/corehr-v1/employee/search) 或 [批量查询员工信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)接口查询详情。<br>**示例值**："ou_c57053dad6eea0aea4696c48433d8562" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `list_values` | `string\[\]` | 否 | 数组类型值，里面包含多个值，每个元素都对应sub_values中的key<br>**示例值**：["key1"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `10000` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `file_value` | `field_variable_value_to_file_for_write` | 否 | 文件类型字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `open_file_id` | `string` | 否 | 通过在[上传文件接口](https://open.larkoffice.com/document/server-docs/corehr-v1/employee/person/upload)上传文件后获得的ID<br>**示例值**："66867ed00740ddd4a0bad4a5_c99b5322dc744fe4b99b76426ffe5d53" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 否 | 文件名称（需带有文件后缀），如果填写，则会覆盖上传文件的名称，否则通过open_file_id获取原始名称<br>**示例值**："file_name.jpg" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `length` | `int` | 否 | 文件大小，单位：Byte，如果填写，则会覆盖上传文件的大小，否则通过open_file_id获取文件原始大小<br>**示例值**：65535<br>**数据校验规则**：<br>- 取值范围：`0` ～ `52428800` |
| &nbsp;&nbsp;└ `sub_values` | `field_variable_sub_vlaue_for_review\[\]` | 否 | 在list_values和record_values中引用的变量<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100000` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 否 | 用于关联list_values和record_values类型变量值中的key<br>**示例值**："key1" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `field_variable_value_to_for_review` | 否 | 变量值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_value` | `string` | 否 | 文本值<br>**示例值**："测试测试" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bool_value` | `boolean` | 否 | 布尔值<br>**示例值**：true |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number_value` | `string` | 否 | 数字值<br>**示例值**："100" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_value` | `string` | 否 | 枚举值，这里是枚举的id<br>**示例值**："home_address" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date_value` | `string` | 否 | 从 1970 开始的天数<br>**示例值**："19838" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date_time_value` | `string` | 否 | 时间戳，毫秒<br>**示例值**："1714013877512" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_value` | `field_variable_value_i18n` | 否 | 多语字段值<br>**示例值**：ou_c57053dad6eea0aea4696c48433d8562 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 否 | 中文值<br>**示例值**："北京" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 否 | 英文值<br>**示例值**："Beijing" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_value` | `field_variable_value_to_object` | 否 | 对象值，包括对象id和对象类型<br>**示例值**：od-a761814f6bc3f14bd3b00905ec1d7c6f |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_id` | `string` | 否 | 飞书人事主数据对象唯一标识。<br>例如：<br>wk_api_name为"job"时，wk_id代表职务ID。详请可参考[查询单个职务（V2）](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/get)<br>wk_api_name为"job_level"时，wk_id代表职级ID。详情可参考[查询单个职级](https://open.larkoffice.com/document/server-docs/corehr-v1/job-management/job_level/get)<br>**示例值**："6863326263210149383" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_api_name` | `string` | 否 | 飞书人事元数据对象的唯一标识。<br>例如：<br>职务的wk_api_name为"job"；职级的wk_api_name为"job_level"；<br>如需获取更多对象信息，可查询[获取飞书人事对象列表](https://open.larkoffice.com/document/server-docs/corehr-v1/basic-infomation/custom_field/list_object_api_name)接口<br>**示例值**："country_region_subdivision" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_value` | `string` | 否 | 部门id，根据查询参数department_id_type类型选择对应的部门id。<br>可通过[搜索部门信息](https://open.larkoffice.com/document/server-docs/corehr-v1/organization-management/department/search) 或 [批量查询部门（ V2）](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)接口查询详情。<br>**示例值**："od-a761814f6bc3f14bd3b00905ec1d7c6f" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employment_value` | `string` | 否 | 员工类型字段值，为用户id，根据入参选择的user_id_type类型返回的用户id。<br>可通过[搜索员工信息](https://open.larkoffice.com/document/server-docs/corehr-v1/employee/search) 或 [批量查询员工信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)接口查询详情。<br>**示例值**："ou_c57053dad6eea0aea4696c48433d8562" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `list_values` | `string\[\]` | 否 | 数组类型值，里面包含多个值，每个元素都对应sub_values中的key<br>**示例值**：["key1"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `10000` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_value` | `field_variable_value_to_file_for_write` | 否 | 文件类型字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `open_file_id` | `string` | 否 | 通过在[上传文件接口](https://open.larkoffice.com/document/server-docs/corehr-v1/employee/person/upload)上传文件后获得的ID<br>**示例值**："66867ed00740ddd4a0bad4a5_c99b5322dc744fe4b99b76426ffe5d53" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 否 | 文件名称（需带有文件后缀），如果填写，则会覆盖上传文件的名称，否则通过open_file_id获取原始名称<br>**示例值**："file_name.jpg" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `length` | `int` | 否 | 文件大小，单位：Byte，如果填写，则会覆盖上传文件的大小，否则通过open_file_id获取文件原始大小<br>**示例值**：65535<br>**数据校验规则**：<br>- 取值范围：`0` ～ `52428800` |


### 请求体示例

```json
{
    "status": 2,
    "user_id": "ou_91791271921729102012",
    "system_approval": true,
    "reason": "原因自定义字符串",
    "field_values_v2": [
        {
            "variable_api_name": "custom123",
            "variable_value": {
                "text_value": "测试测试",
                "bool_value": true,
                "number_value": "100",
                "enum_value": "home_address",
                "date_value": "19838",
                "date_time_value": "1714013877512",
                "i18n_value": {
                    "zh_cn": "北京",
                    "en_us": "Beijing"
                },
                "object_value": {
                    "wk_id": "6863326263210149383",
                    "wk_api_name": "country_region_subdivision"
                },
                "department_value": "od-a761814f6bc3f14bd3b00905ec1d7c6f",
                "employment_value": "ou_c57053dad6eea0aea4696c48433d8562",
                "list_values": [
                    "key1"
                ],
                "file_value": {
                    "open_file_id": "66867ed00740ddd4a0bad4a5_c99b5322dc744fe4b99b76426ffe5d53",
                    "file_name": "file_name.jpg",
                    "length": 65535
                }
            },
            "sub_values": [
                {
                    "key": "key1",
                    "value": {
                        "text_value": "测试测试",
                        "bool_value": true,
                        "number_value": "100",
                        "enum_value": "home_address",
                        "date_value": "19838",
                        "date_time_value": "1714013877512",
                        "i18n_value": {
                            "zh_cn": "北京",
                            "en_us": "Beijing"
                        },
                        "object_value": {
                            "wk_id": "6863326263210149383",
                            "wk_api_name": "country_region_subdivision"
                        },
                        "department_value": "od-a761814f6bc3f14bd3b00905ec1d7c6f",
                        "employment_value": "ou_c57053dad6eea0aea4696c48433d8562",
                        "list_values": [
                            "key1"
                        ],
                        "file_value": {
                            "open_file_id": "66867ed00740ddd4a0bad4a5_c99b5322dc744fe4b99b76426ffe5d53",
                            "file_name": "file_name.jpg",
                            "length": 65535
                        }
                    }
                }
            ]
        }
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
| &nbsp;&nbsp;└ `code` | `int` | 错误码，非 0 表示失败 |
| &nbsp;&nbsp;└ `msg` | `string` | 错误描述 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "code": 0,
        "msg": "错误原因"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1161001 | 审批已被处理 | 审批任务已被处理，无需再次审批 |
| 400 | 1161002 | 参数非法 | 参数错误，请操作接口字段说明自查 |
| 403 | 1161003 | 无权限 | 请确认是否已申请权限 |
| 400 | 1161004 | 自动提交表单失败 | 自动提交表单失败，请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)协助排查。 |
| 400 | 1161005 | 审批状态已更新 | 审批状态已更新，请刷新页面 |


