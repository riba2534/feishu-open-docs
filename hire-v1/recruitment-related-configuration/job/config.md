---
title: "获取职位设置"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/config"
updateTime: "1740109824000"
---

# 获取职位设置

获取职位设置，包含 Offer 申请表、Offer 审批流程、建议评估人列表、面试评价表、建议面试官列表、招聘需求、面试登记表、入职登记表、面试轮次类型列表、关联职位列表等设置。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/jobs/:job_id/config |
| HTTP Method | GET |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:job:readonly` 获取职位信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `job_id` | `string` | 职位 ID，可通过[获取职位列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/list)接口获取<br>**示例值**："6960663240925956660" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_admin_id`: 以people_admin_id来识别用户<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `job_config` | `job_config_result` | 职位设置 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `offer_apply_schema` | `id_name_object` | Offer 申请表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | Offer 申请表 ID，详情请查看：[获取 Offer 申请表信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer_application_form/get) |
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
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职位 ID，详情可查看：[获取职位信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/get) |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `schema_id` | `string` | 面试登记表模版 ID，详情可查看：[获取信息登记表模板列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/registration_schema/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 面试登记表名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `onboard_registration` | `registration_info` | 入职登记表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `schema_id` | `string` | 入职登记表 ID，详情请查看：[获取信息登记表模板列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/registration_schema/list) |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 关联职位 ID，详情可查看：[获取职位信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 关联职位名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 关联职位中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 关联职位英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_attribute` | `int` | 职位属性 可选值： - 1：实体职位 - 2：虚拟职位 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `interview_appointment_config` | `interview_appointment_config` | 面试官安排面试配置 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enable_interview_appointment_by_interviewer` | `boolean` | 是否允许面试官安排面试 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `config` | `interview_appointment_config_content` | 配置详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `interview_type` | `int` | 面试类型<br>**可选值有**：<br>- `1`: 现场面试 - `2`: 电话面试 - `3`: 视频面试 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `talent_timezone_code` | `string` | 候选人时区。基于IANA标准时区码，完整时区码列表请参考：[维基百科时区列表](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contact_user_id` | `string` | 面试联系人 ID，与入参`user_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contact_mobile` | `string` | 面试联系人电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contact_email` | `string` | 面试联系人邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_id` | `string` | 面试地点 ID，详情请查看：[获取地址列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `video_type` | `int` | 视频面试类型<br>**可选值有**：<br>- `1`: zoom - `2`: 牛客技术类型 - `3`: 牛客非技术类型 - `4`: 赛码 - `5`: 飞书 - `8`: Hackerrank - `9`: 飞书(含代码考核) - `100`: 不使用系统工具 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cc` | `string\[\]` | 抄送人 ID 列表，与入参`user_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `remark` | `string` | 面试配置备注 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `interview_notification_template_id` | `string` | 面试通知模板 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `appointment_notification_template_id` | `string` | 预约通知模板 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cancel_interview_notification_template_id` | `string` | 取消面试通知模版 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `portal_website_apply_form_schema_info` | `registration_info` | 官网申请表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `schema_id` | `string` | 官网申请表ID，可通过[获取招聘官网申请表模板列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/portal_apply_schema/list)获取申请表详情 |
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
                    "zh_cn": "申请表1",
                    "en_us": "Offer Apply 1"
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
                    "id": "6949805467799537964",
                    "name": {
                        "zh_cn": "华中大区部门",
                        "en_us": "JR Test"
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
                            "zh_cn": "测试评价表",
                            "en_us": "Test Name"
                        }
                    }
                }
            ],
            "related_job_list": [
                {
                    "id": "7392444731470563625",
                    "name": {
                        "zh_cn": "职位1",
                        "en_us": "job1"
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


