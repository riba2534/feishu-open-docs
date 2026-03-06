---
title: "发起转正"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/probation/submit"
updateTime: "1740729735000"
---

# 发起转正

通过本接口可以为员工发起转正


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/probation/submit |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:probation:write` 读写试用期信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `corehr:probation.assessment:read` 获取试用期考核信息 `corehr:probation.assessment:write` 读写试用期考核信息 `corehr:probation.custom_field:read` 获取试用期自定义字段信息 `corehr:probation.custom_field:write` 读写试用期自定义字段信息 `corehr:probation.notes:read` 读取试用期备注信息 `corehr:probation.notes:write` 读写试用期备注信息 `corehr:probation.self_review:read` 读取员工自评信息 `corehr:probation.self_review:write` 读写员工自评信息 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `client_token` | `string` | 否 | 根据 client_token 是否一致来判断是否为同一请求<br>**示例值**：6822122262122064111 |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `employment_id` | `string` | 是 | 试用期人员的雇佣 ID，可通过[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取<br>**示例值**："7140964208476371111" |
| `conversion_mode` | `int` | 是 | 转正方式<br>**示例值**：1<br>**可选值有**：<br>- `1`: 直接转正 - `2`: 发起转正 |
| `actual_probation_end_date` | `string` | 否 | 实际结束日期，如果为空则默认填入试用期预计结束日期，填入日期需满足：试用期开始时间 <= 实际结束日期 <= 试用期预计结束日期，格式："YYYY-MM-DD"<br>**示例值**："2022-05-20" |
| `submission_type` | `string` | 是 | 发起方<br>**示例值**："system"<br>**可选值有**：<br>- `self_submission`: 员工 - `system`: 系统 - `hr_submission`: HR |
| `initiator_id` | `string` | 否 | 发起人 ID，当发起方为 HR 时填写，为其他发起方时该字段会自动计算，可通过[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取<br>**示例值**："7140964208476371111" |
| `notes` | `string` | 否 | 备注，当为直接转正时必填<br>**示例值**："符合预期" |
| `self_review` | `string` | 否 | 员工自评<br>**示例值**："符合预期" |
| `custom_fields` | `custom_field_data\[\]` | 否 | 自定义字段（试用期中如果有附件自定义字段，当前不支持使用「上传文件」接口写入） |
| &nbsp;&nbsp;└ `custom_api_name` | `string` | 是 | 自定义字段 apiname，即自定义字段的唯一标识<br>**示例值**："name" |
| &nbsp;&nbsp;└ `name` | `custom_name` | 否 | 自定义字段名称（无需填写） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 否 | 中文<br>**示例值**："自定义姓名" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 否 | 英文<br>**示例值**："Custom Name" |
| &nbsp;&nbsp;└ `type` | `int` | 否 | 自定义字段类型（无需填写）<br>**示例值**：1 |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同，不同类型字段传值格式如下 - 文本，示例："你好" - 超链接，示例："https://www.baidu.com/" - 数字，示例："123" - 布尔，示例："true" - 单选，示例："option1" - 多选，示例："[\"option1\", \"option2\"]" - 人员（单选），示例："7140964208476371111" - 人员（多选），示例："[\"7140964208476371111\", \"7140964208476371112\"]" - 日期，示例："2025-01-01"<br>**示例值**："231" |


### 请求体示例

```json
{
    "employment_id": "7140964208476371111",
    "conversion_mode": 1,
    "actual_probation_end_date": "2022-05-20",
    "submission_type": "system",
    "initiator_id": "7140964208476371111",
    "notes": "符合预期",
    "self_review": "符合预期",
    "custom_fields": [
        {
            "custom_api_name": "name",
            "name": {
                "zh_cn": "自定义姓名",
                "en_us": "Custom Name"
            },
            "type": 1,
            "value": "231"
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
| &nbsp;&nbsp;└ `probation_info` | `probation_info_for_submit` | 试用期信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id` | `string` | 雇佣 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `probation_id` | `string` | 试用期信息 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `probation_start_date` | `string` | 试用期开始日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `probation_expected_end_date` | `string` | 试用期预计结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `actual_probation_end_date` | `string` | 试用期实际结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `initiating_time` | `string` | 转正发起日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `submission_type` | `enum` | 发起方 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `initiator_id` | `string` | 转正发起人的雇佣 ID，当系统发起转正时该字段为空 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `probation_status` | `enum` | 试用期状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `self_review` | `string` | 员工自评<br>**字段权限要求（满足任一）**： `corehr:probation.self_review:read` 读取员工自评信息 `corehr:probation.self_review:write` 读写员工自评信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `notes` | `string` | 备注<br>**字段权限要求（满足任一）**： `corehr:probation.notes:read` 读取试用期备注信息 `corehr:probation.notes:write` 读写试用期备注信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `process_id` | `string` | 流程实例 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `converted_via_bpm` | `boolean` | 是否通过 BPM 转正 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段<br>**字段权限要求（满足任一）**： `corehr:probation.custom_field:read` 获取试用期自定义字段信息 `corehr:probation.custom_field:write` 读写试用期自定义字段信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同，不同类型字段传值格式如下 - 文本，示例："你好" - 超链接，示例："https://www.baidu.com/" - 数字，示例："123" - 布尔，示例："true" - 单选，示例："option1" - 多选，示例："[\"option1\", \"option2\"]" - 人员（单选），示例："7140964208476371111" - 人员（多选），示例："[\"7140964208476371111\", \"7140964208476371112\"]" - 日期，示例："2025-01-01" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `final_assessment_status` | `enum` | 试用期考核最终状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `final_assessment_result` | `enum` | 试用期考核最终结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `final_assessment_score` | `number(float)` | 试用期考核最终得分<br>**字段权限要求（满足任一）**： `corehr:probation.assessment:read` 获取试用期考核信息 `corehr:probation.assessment:write` 读写试用期考核信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `final_assessment_grade` | `enum` | 试用期考核最终等级<br>**字段权限要求（满足任一）**： `corehr:probation.assessment:read` 获取试用期考核信息 `corehr:probation.assessment:write` 读写试用期考核信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `final_assessment_comment` | `string` | 试用期考核最终评语<br>**字段权限要求（满足任一）**： `corehr:probation.assessment:read` 获取试用期考核信息 `corehr:probation.assessment:write` 读写试用期考核信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `final_assessment_detail` | `string` | 最终考核结果页面超链接<br>**字段权限要求（满足任一）**： `corehr:probation.assessment:read` 获取试用期考核信息 `corehr:probation.assessment:write` 读写试用期考核信息 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "probation_info": {
            "employment_id": "6893014062142064135",
            "probation_id": "6893014062142064132",
            "probation_start_date": "2022-05-20",
            "probation_expected_end_date": "2022-05-28",
            "actual_probation_end_date": "2022-06-28",
            "initiating_time": "2022-07-28",
            "submission_type": {
                "enum_name": "phone_type",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ]
            },
            "initiator_id": "6893014062142061135",
            "probation_status": {
                "enum_name": "phone_type",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ]
            },
            "self_review": "符合预期",
            "notes": "高潜",
            "process_id": "6893014062142164135",
            "converted_via_bpm": false,
            "custom_fields": [
                {
                    "custom_api_name": "name",
                    "name": {
                        "zh_cn": "自定义姓名",
                        "en_us": "Custom Name"
                    },
                    "type": 1,
                    "value": "231"
                }
            ],
            "final_assessment_status": {
                "enum_name": "phone_type",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ]
            },
            "final_assessment_result": {
                "enum_name": "phone_type",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ]
            },
            "final_assessment_score": 99.9,
            "final_assessment_grade": {
                "enum_name": "phone_type",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ]
            },
            "final_assessment_comment": "超出预期",
            "final_assessment_detail": "暂无示例"
        }
    }
}
```


