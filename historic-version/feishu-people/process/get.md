---
title: "获取流程表单数据"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/process-form_variable_data/get"
updateTime: "1714122838000"
---

# 获取流程表单数据

根据流程实例 id（process_id）获取流程表单字段数据，包括表单里的业务字段和自定义字段。仅支持飞书人事、假勤相关业务流程。


> **Tip**: 建议使用新版本 API 文档。详情参见[获取流程表单数据](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/process-form_variable_data/get)。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/processes/:process_id/form_variable_data |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:corehr:readonly` 获取核心人事信息 `corehr:process:read` 获取流程数据 `corehr:corehr` 更新核心人事信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `process_id` | `string` | 流程实例 ID<br>**示例值**："123456987" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `field_variable_values` | `form_field_variable\[\]` | 流程变量 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `variable_api_name` | `string` | 变量api名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `variable_name` | `bpm_dataengine_i18n` | 变量名称的i18n描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | （基于系统兼容性，该参数名称在文档中展示为zh_cn，但在实际返回的 JSON Key 中展示为 zh-CN）i18n类型字段，中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | （基于系统兼容性，该参数名称在文档中展示为en_us，但在实际返回的 JSON Key 中展示为 en-US）i18n类型字段，英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `variable_value` | `form_variable_value_info` | 变量值的对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_value` | `form_field_variable_text_value` | 文本变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本类型变量的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number_value` | `form_field_variable_number_value` | 数值变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 数值类型变量的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date_value` | `form_field_variable_date_value` | 日期变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `int` | 日期变量的值，从1970起的天数 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employment_value` | `form_field_variable_employment_value` | 员工变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | employmentID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 员工ID 如3158117 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date_time_value` | `form_field_variable_datetime_value` | 日期时间变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `int` | 毫秒的时间戳。注：此字段数据类型为 int64 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zone` | `string` | 时区，+08:00 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_value` | `form_field_variable_enum_value` | 枚举变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `bpm_dataengine_i18n` | 枚举的名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | （基于系统兼容性，该参数名称在文档中展示为zh_cn，但在实际返回的 JSON Key 中展示为 zh-CN）i18n类型字段，中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | （基于系统兼容性，该参数名称在文档中展示为en_us，但在实际返回的 JSON Key 中展示为 en-US）i18n类型字段，英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `desc` | `bpm_dataengine_i18n` | 枚举的描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | （基于系统兼容性，该参数名称在文档中展示为zh_cn，但在实际返回的 JSON Key 中展示为 zh-CN）i18n类型字段，中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | （基于系统兼容性，该参数名称在文档中展示为en_us，但在实际返回的 JSON Key 中展示为 en-US）i18n类型字段，英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `null_value` | `form_field_variable_null_value` | 空变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bool_value` | `form_field_variable_bool_value` | 布尔变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `boolean` | 布尔变量的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_value` | `form_field_variable_department_value` | 部门变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 部门ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_value` | `form_field_variable_file_value` | 文件变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_type` | `int` | 文件源类型（1BPM; 2主数据） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 文件id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 文件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `length` | `int` | 文件长度 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mime_type` | `string` | 扩展类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_value` | `form_field_variable_i18n_value` | i18n变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `bpm_dataengine_i18n` | i18n值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | （基于系统兼容性，该参数名称在文档中展示为zh_cn，但在实际返回的 JSON Key 中展示为 zh-CN）i18n类型字段，中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | （基于系统兼容性，该参数名称在文档中展示为en_us，但在实际返回的 JSON Key 中展示为 en-US）i18n类型字段，英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_value` | `form_field_variable_object_value` | 对象变量 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 对象ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_api_name` | `string` | 主数据apiName |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `list_value` | `form_field_variable_list_value` | 列表对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `values` | `form_field_variable_list_object\[\]` | 列表值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_value` | `form_field_variable_text_value` | 文本变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本类型变量的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number_value` | `form_field_variable_number_value` | 数值变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 数值类型变量的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date_value` | `form_field_variable_date_value` | 日期变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `int` | 日期变量的值，从1970起的天数 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employment_value` | `form_field_variable_employment_value` | 员工变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | employmentID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 员工ID 如3158117 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date_time_value` | `form_field_variable_datetime_value` | 日期时间变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `int` | 毫秒的时间戳。注：此字段数据类型为 int64 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zone` | `string` | 时区，+08:00 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_value` | `form_field_variable_enum_value` | 枚举变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `bpm_dataengine_i18n` | 枚举的名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | （基于系统兼容性，该参数名称在文档中展示为zh_cn，但在实际返回的 JSON Key 中展示为 zh-CN）i18n类型字段，中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | （基于系统兼容性，该参数名称在文档中展示为en_us，但在实际返回的 JSON Key 中展示为 en-US）i18n类型字段，英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `desc` | `bpm_dataengine_i18n` | 枚举的描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | （基于系统兼容性，该参数名称在文档中展示为zh_cn，但在实际返回的 JSON Key 中展示为 zh-CN）i18n类型字段，中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | （基于系统兼容性，该参数名称在文档中展示为en_us，但在实际返回的 JSON Key 中展示为 en-US）i18n类型字段，英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `null_value` | `form_field_variable_null_value` | 空变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bool_value` | `form_field_variable_bool_value` | 布尔变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `boolean` | 布尔变量的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_value` | `form_field_variable_department_value` | 部门变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 部门ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_value` | `form_field_variable_file_value` | 文件变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `source_type` | `int` | 文件源类型（1BPM; 2主数据） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 文件id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 文件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `length` | `int` | 文件长度 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mime_type` | `string` | 扩展类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_value` | `form_field_variable_i18n_value` | i18n变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `bpm_dataengine_i18n` | i18n值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | （基于系统兼容性，该参数名称在文档中展示为zh_cn，但在实际返回的 JSON Key 中展示为 zh-CN）i18n类型字段，中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | （基于系统兼容性，该参数名称在文档中展示为en_us，但在实际返回的 JSON Key 中展示为 en-US）i18n类型字段，英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_value` | `form_field_variable_object_value` | 对象变量 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 对象ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_api_name` | `string` | 主数据apiName |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `record_value` | `form_field_variable_record_value` | 记录对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `values` | `form_field_variable_record_value_example` | 注：该参数实际为 Map 数据类型，Key 是变量唯一标识，Value 是变量值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region` | `form_variable_value_info_example` | 这个属性名称是map的key的示例，属性值是map的value的示例，值和外层的variable_value是的一样的结构。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_value` | `form_field_variable_object_value` | 文本变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 对象ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_api_name` | `string` | 主数据apiName |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `record_value` | `form_field_variable_record_value` | 记录对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `values` | `form_field_variable_record_value_example` | 注：该参数实际为 Map 数据类型，Key 是变量唯一标识，Value 是变量值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region` | `form_variable_value_info_example` | 这个属性名称是map的key的示例，属性值是map的value的示例，值和外层的variable_value是的一样的结构。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_value` | `form_field_variable_object_value` | 文本变量对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 对象ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_api_name` | `string` | 主数据apiName |


### 响应体示例

```json
{
    "code": 0,
    "data":
    {
        "field_variable_values":
        [
            {
                "variable_api_name": "reason",
                "variable_name":
                {
                    "en-US": "Reason",
                    "zh-CN": "离职原因"
                },
                "variable_value":
                {
                    "enum_value":
                    {
                        "desc": null,
                        "enum_source_id": 123,
                        "enum_source_type": 2,
                        "name":
                        {
                            "en-US": "",
                            "zh-CN": "测试"
                        },
                        "value": "reason_for_offboarding_option96",
                        "wk_api_name": "reason_for_offboarding"
                    }
                }
            },
            {
                "variable_api_name": "offboarding_date",
                "variable_name":
                {
                    "en-US": "Offboarding date",
                    "zh-CN": "离职日期"
                },
                "variable_value":
                {
                    "date_value":
                    {
                        "value": 19265
                    }
                }
            },
            {
                "variable_api_name": "employment",
                "variable_name":
                {
                    "en-US": "Employment",
                    "zh-CN": "员工"
                },
                "variable_value":
                {
                    "employment_value":
                    {
                        "user_id": "123321",
                        "value": "123321"
                    }
                }
            }
        ],
        "process_id": "123321"
    },
    "msg": "",
    "success": true
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1160100 | 审批流程不存在 | 确认审批流程ID是否正确 |
| 500 | 1160500 | 服务端内部错误 | 内部错误，建议联系飞书开发平台技术支持 |


