---
title: "更新职位设置"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/update_config"
updateTime: "1735045934000"
---

# 更新职位设置

更新职位设置，包括面试评价表、Offer 申请表等。


## 注意事项

调用此接口前，需先打开「飞书招聘」-「设置」-「职位管理」-「职位设置」-「通过 API 同步职位开关」开关。

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/jobs/:job_id/update_config |
| HTTP Method | POST |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:job` 更新职位信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `job_id` | `string` | 职位 ID，可通过[获取职位列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/list)接口获取<br>**示例值**："6960663240925956660" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `offer_apply_schema_id` | `string` | 否 | Offer 申请表 ID，可通过[获取 Offer 申请表列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer_application_form/list)接口获取，当`update_option_list`包含`更新 Offer 申请表`时，该参数必填<br>**示例值**："6960663240925956573" |
| `offer_process_conf` | `string` | 否 | Offer 审批流程 ID，可通过[获取 Offer 审批流配置列表](https://open.larkoffice.com/document/server-docs/hire-v1/recruitment-related-configuration/offer-settings/offer_approval_template/list)接口获取<br>**示例值**："6960663240925956572" |
| `recommended_evaluator_id_list` | `string\[\]` | 否 | 建议评估人 ID 列表，需与入参`user_id_type`类型一致<br>**示例值**：["6966533137982392320"] |
| `update_option_list` | `int\[\]` | 是 | 更新选项，传入要更新的配置项 - 接口将按照所选择的「选项」进行设置参数校验和更新。若设置的必填字段更新时未填写内容，接口将报错无法完成更新。<br>**示例值**：[6]<br>**可选值有**：<br>- `1`: 更新面试评价表 - `2`: 更新 Offer 申请表 - `3`: 更新 Offer 审批流程 - `4`: 更新招聘需求 - `5`: 更新建议面试官 - `6`: 更新建议评估人 - `8`: 更新关联职位 - `9`: 更新面试官安排面试配置 - `10`: 更新面试登记表 - `11`: 更新入职登记表 - `12`: 更新官网申请表 |
| `assessment_template_biz_id` | `string` | 否 | 面试评价表 ID，可通过[获取面试评价表列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_feedback_form/list)接口获取，当同时满足以下两个条件时，该参数必填： - `update_option_list`包含`更新面试评价表` - 「飞书招聘」-「设置」-「面试轮次类型设置」-「启用面试轮次类型」开关关闭<br>**示例值**："6960663240925956571" |
| `interview_round_conf_list` | `job_config_interview_round_conf\[\]` | 否 | 建议面试官列表，当`update_option_list`包含`更新建议面试官`时，该参数必填 |
| &nbsp;&nbsp;└ `interviewer_id_list` | `string\[\]` | 否 | 建议面试官 ID 列表，需与入参`user_id_type`类型一致<br>**示例值**：["6960663240925956571"] |
| &nbsp;&nbsp;└ `round` | `int` | 否 | 面试轮次<br>**示例值**：1 |
| `jr_id_list` | `string\[\]` | 否 | 关联招聘需求，可通过[获取招聘需求信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_requirement/list_by_id)接口获取<br>**示例值**：["6966533137982392320"] |
| `interview_registration_schema_id` | `string` | 否 | 面试登记表 ID，可通过[获取面试登记表模板列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_registration_schema/list)接口获取。 注意： - 当在「飞书招聘」-「设置」 -「信息登记表使用设置」 - 「申请表和登记表使用设置」中选择「HR 按职位选择登记表」时，该字段为必填；否则该字段不生效 - 当`update_option_list`包含`更新面试登记表`时，该参数必填<br>**示例值**："6930815272790114324" |
| `onboard_registration_schema_id` | `string` | 否 | 入职登记表 ID，可通过[获取信息登记表模板列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/registration_schema/list)接口获取。 注意： - 当在飞书招聘「设置」 - 「信息登记表使用设置」 - 「入职登记表使用方式」中选择「HR 按职位选择登记表」时，该字段为必填；否则该字段不生效 - 当`update_option_list`包含`更新入职登记表`时，该参数必填<br>**示例值**："6930815272790114324" |
| `interview_round_type_conf_list` | `job_config_round_type\[\]` | 否 | 面试轮次类型 ID 列表，当同时满足以下两个条件时，该参数必填： - `update_option_list`包含`更新面试评价表` - 「飞书招聘」-「设置」-「面试轮次类型设置」-「启用面试轮次类型」开关打开 |
| &nbsp;&nbsp;└ `round_biz_id` | `string` | 否 | 面试轮次类型 ID，可通过接口[获取面试轮次类型列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_round_type/list)获取。<br>**示例值**："7012129842917837100" |
| &nbsp;&nbsp;└ `assessment_template_biz_id` | `string` | 否 | 面试评价表 ID，可通过[获取面试评价表列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_feedback_form/list)接口获取<br>**示例值**："6960663240925956632" |
| `related_job_id_list` | `string\[\]` | 否 | 关联职位列表，如职位为实体职位则关联虚拟职位 ID，如职位为虚拟职位则关联实体职位 ID，可通过[获取职位列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/list)接口获取<br>**示例值**：["6966533137982392320"] |
| `interview_appointment_config` | `interview_appointment_config` | 否 | 自助约面配置，当`update_option_list`包含`更新面试官安排面试配置`时，该参数必填 |
| &nbsp;&nbsp;└ `enable_interview_appointment_by_interviewer` | `boolean` | 否 | 是否开启面试官自助约面<br>**示例值**：true |
| &nbsp;&nbsp;└ `config` | `interview_appointment_config_content` | 否 | 配置详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `interview_type` | `int` | 否 | 面试类型<br>**示例值**：1<br>**可选值有**：<br>- `1`: 现场面试 - `2`: 电话面试 - `3`: 视频面试 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `talent_timezone_code` | `string` | 否 | 候选人时区<br>**示例值**："Asia/Shanghai" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contact_user_id` | `string` | 否 | 面试联系人 ID，需与入参`user_id_type`类型一致<br>**示例值**："ou_c99c5f35d542efc7ee492afe11af19ef" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contact_mobile` | `string` | 否 | 面试联系人电话<br>**示例值**："151********" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contact_email` | `string` | 否 | 面试联系人邮箱<br>**示例值**："test@email" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address_id` | `string` | 否 | 面试地点 ID，可通过[获取地址列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/list)接口获取<br>**示例值**："6960663240925956576" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `video_type` | `int` | 否 | 视频面试类型<br>**示例值**：1<br>**可选值有**：<br>- `1`: zoom - `2`: 牛客技术类型 - `3`: 牛客非技术类型 - `4`: 赛码 - `5`: 飞书 - `8`: Hackerrank - `9`: 飞书(含代码考核) - `100`: 不使用系统工具 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cc` | `string\[\]` | 否 | 抄送人 ID 列表，需与入参`user_id_type`类型一致<br>**示例值**：["6930815272790114324"] |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `remark` | `string` | 否 | 面试配置备注<br>**示例值**："仅仅用于视频面试" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `interview_notification_template_id` | `string` | 否 | 面试通知模板 ID<br>**示例值**："6960663240925956573" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `appointment_notification_template_id` | `string` | 否 | 预约通知模板 ID<br>**示例值**："6960663240925956573" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cancel_interview_notification_template_id` | `string` | 否 | 取消面试通知模版 ID<br>**示例值**："6960663240925956573" |
| `portal_website_apply_form_schema_id` | `string` | 否 | 官网申请表ID，可通过[获取招聘官网申请表模板列表 ](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/portal_apply_schema/list)接口获取<br>**示例值**："6930815272790114324" |


### 请求体示例

```json
{
    "offer_apply_schema_id": "6960663240925956573",
    "offer_process_conf": "6960663240925956572",
    "recommended_evaluator_id_list": [
        "6966533137982392320"
    ],
    "update_option_list": [
        6
    ],
    "assessment_template_biz_id": "6960663240925956571",
    "interview_round_conf_list": [
        {
            "interviewer_id_list": [
                "6960663240925956571"
            ],
            "round": 1
        }
    ],
    "jr_id_list": [
        "6966533137982392320"
    ],
    "interview_registration_schema_id": "6930815272790114324",
    "onboard_registration_schema_id": "6930815272790114324",
    "interview_round_type_conf_list": [
        {
            "round_biz_id": "7012129842917837100",
            "assessment_template_biz_id": "6960663240925956632"
        }
    ],
    "related_job_id_list": [
        "6966533137982392320"
    ],
    "interview_appointment_config": {
        "enable_interview_appointment_by_interviewer": true,
        "config": {
            "interview_type": 1,
            "talent_timezone_code": "Asia/Shanghai",
            "contact_user_id": "ou_c99c5f35d542efc7ee492afe11af19ef",
            "contact_mobile": "151********",
            "contact_email": "test@email",
            "address_id": "6960663240925956576",
            "video_type": 1,
            "cc": [
                "6930815272790114324"
            ],
            "remark": "仅仅用于视频面试",
            "interview_notification_template_id": "6960663240925956573",
            "appointment_notification_template_id": "6960663240925956573",
            "cancel_interview_notification_template_id": "6960663240925956573"
        }
    },
    "portal_website_apply_form_schema_id": "6930815272790114324"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `job_config` | `job_config_result` | 职位设置 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `offer_apply_schema` | `id_name_object` | Offer 申请表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | Offer 申请表 ID，详情可查看：[获取 Offer 申请表列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer_application_form/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | Offer 申请表名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | Offer 申请表中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | Offer 申请表英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `offer_process_conf` | `id_name_object` | Offer 审批流程 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | Offer 审批流程 ID，详情请查看：[获取 Offer 审批流配置列表](https://open.larkoffice.com/document/server-docs/hire-v1/recruitment-related-configuration/offer-settings/offer_approval_template/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | Offer 审批流程名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | Offer 审批流程中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | Offer 审批流程英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `recommended_evaluator_list` | `id_name_object\[\]` | 建议评估人列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 评估人 ID，与入参`user_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 评估人名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 评估人中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 评估人英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `assessment_template` | `id_name_object` | 面试评价表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 面试评价表 ID，详情请查看：[获取面试评价表列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_feedback_form/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 面试评价表名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 面试评价表中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 面试评价表英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职位 ID，详情请查看：[获取职位信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `interview_round_list` | `job_config_interview_round\[\]` | 建议面试官列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `interviewer_list` | `id_name_object\[\]` | 面试官列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 面试官 ID，与入参`user_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 面试官名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 面试官中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 面试官英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `round` | `int` | 面试轮次 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_requirement_list` | `id_name_object\[\]` | 招聘需求 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 招聘需求 ID，详情请查看：[获取招聘需求信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_requirement/list_by_id) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 招聘需求名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 招聘需求中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 招聘需求英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `interview_registration` | `registration_info` | 面试登记表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `schema_id` | `string` | 面试登记表 ID，详情可查看：[获取面试登记表模板列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_registration_schema/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 面试登记表名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `onboard_registration` | `registration_info` | 入职登记表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `schema_id` | `string` | 入职登记表 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 入职登记表名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `interview_round_type_list` | `job_config_round_type_result\[\]` | 面试轮次类型列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `assessment_round` | `id_name_object` | 面试轮次类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 面试轮次类型 ID，详情请查看：[获取面试轮次类型列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_round_type/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 面试轮次类型名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 面试轮次类型中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 面试轮次类型英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `assessment_template` | `id_name_object` | 面试评价表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 面试评价表 ID，详情请查看：[获取面试评价表列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_feedback_form/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 面试评价表名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 面试评价表中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 面试评价表英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `related_job_list` | `id_name_object\[\]` | 关联职位列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 关联职位 ID，详情请查看[获取职位信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 关联职位名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 关联职位中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 关联职位英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_attribute` | `int` | 职位属性 可选值： - 1：实体职位 - 2：虚拟职位 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `interview_appointment_config` | `interview_appointment_config` | 面试官安排面试配置 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enable_interview_appointment_by_interviewer` | `boolean` | 是否开启面试官安排面试 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `config` | `interview_appointment_config_content` | 配置详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `interview_type` | `int` | 面试类型<br>**可选值有**：<br>- `1`: 现场面试 - `2`: 电话面试 - `3`: 视频面试 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `talent_timezone_code` | `string` | 候选人时区 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contact_user_id` | `string` | 面试联系人 ID，与入参`user_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contact_mobile` | `string` | 面试联系人电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contact_email` | `string` | 面试联系人邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_id` | `string` | 面试地点 ID，详情请查看：[获取地址列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `video_type` | `int` | 视频面试类型<br>**可选值有**：<br>- `1`: zoom - `2`: 牛客技术类型 - `3`: 牛客非技术类型 - `4`: 赛码 - `5`: 飞书 - `8`: Hackerrank - `9`: 飞书(含代码考核) - `100`: 不使用系统工具 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cc` | `string\[\]` | 抄送人 ID 列表，需与入参`user_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `remark` | `string` | 面试配置备注 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `interview_notification_template_id` | `string` | 面试通知模板 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `appointment_notification_template_id` | `string` | 预约通知模板 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cancel_interview_notification_template_id` | `string` | 取消面试通知模版 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `portal_website_apply_form_schema_info` | `registration_info` | 官网申请表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `schema_id` | `string` | 官网申请表ID，可通过[获取招聘官网申请表模板列表 ](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/portal_apply_schema/list)获取申请表详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 官网申请表名称 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "ok",
    "data": {
        "job_config": {
            "offer_apply_schema": {
                "id": "7392444731470563625",
                "name": {
                    "zh_cn": "测试 Offer 申请表",
                    "en_us": "Test Offer 申请表"
                }
            },
            "offer_process_conf": {
                "id": "7392444731470563625",
                "name": {
                    "zh_cn": "审批流程1",
                    "en_us": "Test Process 1"
                }
            },
            "recommended_evaluator_list": [
                {
                    "id": "7392444731470563625",
                    "name": {
                        "zh_cn": "张三",
                        "en_us": "ZhangSan"
                    }
                }
            ],
            "assessment_template": {
                "id": "7392444731470563625",
                "name": {
                    "zh_cn": "评价表1",
                    "en_us": "assessment_template·1"
                }
            },
            "id": "6960663240925956574",
            "interview_round_list": [
                {
                    "interviewer_list": [
                        {
                            "id": "7392444731470563625",
                            "name": {
                                "zh_cn": "张三",
                                "en_us": "ZhangSan"
                            }
                        }
                    ],
                    "round": 1
                }
            ],
            "job_requirement_list": [
                {
                    "id": "6930815272790114324",
                    "name": {
                        "zh_cn": "校招需求",
                        "en_us": "campus jr"
                    }
                }
            ],
            "interview_registration": {
                "schema_id": "6930815272790114324",
                "name": "默认登记表"
            },
            "onboard_registration": {
                "schema_id": "6930815272790114324",
                "name": "默认登记表"
            },
            "interview_round_type_list": [
                {
                    "assessment_round": {
                        "id": "7392444731470563625",
                        "name": {
                            "zh_cn": "测试类型",
                            "en_us": "Test type"
                        }
                    },
                    "assessment_template": {
                        "id": "7392444731470563625",
                        "name": {
                            "zh_cn": "评价表1",
                            "en_us": "assessment_template·1"
                        }
                    }
                }
            ],
            "related_job_list": [
                {
                    "id": "6930815272790114324",
                    "name": {
                        "zh_cn": "测试职位",
                        "en_us": "test job"
                    }
                }
            ],
            "job_attribute": 1,
            "interview_appointment_config": {
                "enable_interview_appointment_by_interviewer": true,
                "config": {
                    "interview_type": 1,
                    "talent_timezone_code": "Asia/Shanghai",
                    "contact_user_id": "ou_c99c5f35d542efc7ee492afe11af19ef",
                    "contact_mobile": "177xxxx1773",
                    "contact_email": "test@open.com",
                    "address_id": "6960663240925956576",
                    "video_type": 1,
                    "cc": [
                        "ou_c99c5f35d542efc7ee492afe11af19ef"
                    ],
                    "remark": "这个职位最好选择现场牛客网面试",
                    "interview_notification_template_id": "6960663240925956573",
                    "appointment_notification_template_id": "6960663240925956573",
                    "cancel_interview_notification_template_id": "6960663240925956573"
                }
            },
            "portal_website_apply_form_schema_info": {
                "schema_id": "6930815272790114324",
                "name": "默认申请表"
            }
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |
| 400 | 1002613 | 「通过 API 同步职位」开关尚未打开，仅支持在招聘系统中新建、编辑或关闭职位 | 请确认「通过 API 同步职位」开关是否已开启；路径：「招聘系统」-「设置」-「职位管理」-「职位设置」-「通过 API 同步职位」 |
| 400 | 1002609 | 职位已关闭 | 职位已关闭，请通过[获取职位信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/get)接口查看职位关闭状态 |
| 400 | 1002611 | Offer 审批流程不适用于当前部门 | 可通过[获取 Offer 审批流配置列表](https://open.larkoffice.com/document/server-docs/hire-v1/recruitment-related-configuration/offer-settings/offer_approval_template/list)接口查看当前流程的适用部门是否包含当前 Offer 对应部门 |
| 400 | 1002620 | 不可关联同属性职位 | 不可关联同属性职位，如虚拟职位不能关联虚拟职位，请检查`related_job_id_list `参数是否正确 |
| 400 | 1002621 | 实体职位只可关联一个虚拟职位 | 实体职位只可关联一个虚拟职位，请检查`related_job_id_list `参数是否正确 |
| 400 | 1002703 | 招聘需求不存在 | 招聘需求不存在，请检查`jr_id_list `参数是否正确 |


