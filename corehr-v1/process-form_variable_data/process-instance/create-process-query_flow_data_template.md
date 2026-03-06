---
title: "查询流程数据参数模板"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/process-query_flow_data_template/create"
updateTime: "1769669700000"
---

# 查询流程数据参数模板

通过传入流程定义 ID 和变量的 ApiName，获取 process_form_variable_v2[] 类型参数模板。


> **Tip**: 该接口用于帮助开发人员理解 process_form_variable_v2[] 的数据结构，**业务生产环境不建议使用**。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/query_flow_data_template |
| HTTP Method | POST |
| 接口频率限制 | [20 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:process.instance:write` 通过或拒绝审批任务 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `flow_definition_id` | `string` | 是 | 流程定义ID。 获取方式：管理员在设置侧配置的流程，浏览器 URL 为  `https://{域名}/people/approvals/flow-builder/people_7023711013443944467_7554571297192562476`，其中 `people_7023711013443944467_7554571297192562476` 为当前流程的流程定义 ID。<br>**示例值**："people_7023711013443944467_7437160904904494892" |
| `variable_api_names` | `string\[\]` | 是 | 需要传入的变量的ApiName。如果是多级下钻变量用"."分割。 字段的ApiName查询方式： 1. 进入飞书人事 -> 设置 -> 流程设置 -> 流程管理。 2. 点击flow_definition_id对应的流程的"编辑"按钮，点击右上角"下一步"，进入"2. 流程设计"页面 3. 点击左侧的“变量”，找到你需要查询的变量，点击变量右侧的“API”按钮，复制变量的ApiName。<br>多级下钻变量举例，例如“批量异动.新部门”，分别按上面的步骤找到"批量异动"的ApiName为"batch_job_change"，新部门的ApiName为"target_department"，并用"."分割，则传参为"batch_job_change.target_department"。<br>**示例值**：["custome3adb7eb040.custom_field_2__c"]<br>**数据校验规则**：<br>- 长度范围：`1` ～ `1000` |


### 请求体示例

```json
{
    "flow_definition_id": "people_7023711013443944467_7437160904904494892",
    "variable_api_names": [
        "custome3adb7eb040.custom_field_2__c"
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
| &nbsp;&nbsp;└ `field_values` | `process_form_variable_v2\[\]` | 流程参数模板 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `variable_api_name` | `string` | 变量唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `variable_value` | `field_variable_value_to_for_review` | 变量值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_value` | `string` | 文本值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bool_value` | `boolean` | 布尔值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number_value` | `string` | 数字值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_value` | `string` | 枚举值，这里是枚举的id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date_value` | `string` | 从 1970 开始的天数 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date_time_value` | `string` | 时间戳，毫秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_value` | `field_variable_value_i18n` | 多语字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_value` | `field_variable_value_to_object` | 对象值，包括对象id和对象类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_id` | `string` | wukong的对象唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_api_name` | `string` | wukong的元数据唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_value` | `string` | 部门id，根据入参选择对应的部门id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employment_value` | `string` | 员工类型字段值，为用户id，根据入参选择返回的用户id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `list_values` | `string\[\]` | 数组类型值，里面包含多个值，每个元素都对应subValues中的key |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_value` | `field_variable_value_to_file_for_write` | 文件类型字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `open_file_id` | `string` | 主数据的文件id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 文件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `length` | `int` | 文件大小，单位：Byte |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `record_values` | `field_variable_value_to_record\[\]` | record类型字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `variable_api_name` | `string` | 变量唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sub_value_key` | `string` | 变量值，对应subValues中的key |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `record_id` | `string` | 记录唯一ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sub_values` | `field_variable_sub_vlaue_for_review\[\]` | 在list_values和record_values中引用的变量 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 用于关联list和record类型变量值中的key |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `field_variable_value_to_for_review` | 变量值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_value` | `string` | 文本值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bool_value` | `boolean` | 布尔值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number_value` | `string` | 数字值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_value` | `string` | 枚举值，这里是枚举的id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date_value` | `string` | 从 1970 开始的天数 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date_time_value` | `string` | 时间戳，毫秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_value` | `field_variable_value_i18n` | 多语字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_value` | `field_variable_value_to_object` | 对象值，包括对象id和对象类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_id` | `string` | wukong的对象唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_api_name` | `string` | wukong的元数据唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_value` | `string` | 部门id，根据入参选择对应的部门id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employment_value` | `string` | 员工类型字段值，为用户id，根据入参选择返回的用户id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `list_values` | `string\[\]` | 数组类型值，里面包含多个值，每个元素都对应subValues中的key |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_value` | `field_variable_value_to_file_for_write` | 文件类型字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `open_file_id` | `string` | 主数据的文件id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 文件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `length` | `int` | 文件大小，单位：Byte |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `record_values` | `field_variable_value_to_record\[\]` | record类型字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `variable_api_name` | `string` | 变量唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sub_value_key` | `string` | 变量值，对应subValues中的key |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `record_id` | `string` | 记录唯一ID |
| &nbsp;&nbsp;└ `error_info` | `string` | 错误信息。说明如下： 1. "variableAPIName [custome3adb7eb040] is invalid, record type cannot assign value, must assign record's drill down apiName"，表示custome3adb7eb040 这个 Record 类型变量未传下钻变量值 2. "variableAPIName [custome3adb7eb040.custom_field_3__c] is invalid, not found drill down apiName [custom_field_3__c]", 表示 custom_field_3__c 这个下钻变量未找到。请检查 ApiName 是否正确，或重新发布流程后重试 3. "variableAPIName [customc17e5b301ef] is invalid, not found root apiName [customc17e5b301ef]"，表示 customc17e5b301ef 这个变量未找到。请检查 ApiName 是否正确，或重新发布流程后重试 4. "variableAPIName [customc17e5b301ea.custom1dddafc864a] is invalid, [customc17e5b301ea] cannot drill down"，表示 customc17e5b301ea 不是Record 类型变量，不可下钻 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "field_values": [
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
                        "file_name": "file_name",
                        "length": 65535
                    },
                    "record_values": [
                        {
                            "variable_api_name": "city_v2",
                            "sub_value_key": "key1",
                            "record_id": "6863326263210149383"
                        }
                    ]
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
                                "file_name": "file_name",
                                "length": 65535
                            },
                            "record_values": [
                                {
                                    "variable_api_name": "city_v2",
                                    "sub_value_key": "key1",
                                    "record_id": "6863326263210149383"
                                }
                            ]
                        }
                    }
                ]
            }
        ],
        "error_info": "variableAPIName [new_emergency_contact.phone.xf] is invalid, not found drill down apiName [xf]"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1161002 | invalid param | 参数错误，请参考接口字段说明自查参数的正确性 |


