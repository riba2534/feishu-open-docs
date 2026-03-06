---
title: "批量获取面试评价详细信息（新版）"
fullPath: "/uAjLw4CM/ukTMukTMukTM/hire-v2/interview_record/list"
updateTime: "1765445666000"
---

# 批量获取面试评价详细信息（新版）

批量获取面试评价详细信息，如面试结论、面试得分和面试官等信息（含模块评价）。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v2/interview_records |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:interview:readonly` 获取面试信息 `hire:interview` 更新面试信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `ids` | `string\[\]` | 否 | 面试评价 ID 列表，可通过[获取面试信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview/list)接口获取，使用该筛选项时不会分页<br>**示例值**：7171693733661327361<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| `page_size` | `int` | 否 | 分页大小<br>**注意**：若不传该参数，则默认根据 `ids` 参数获取数据<br>**示例值**：10<br>**数据校验规则**：<br>- 取值范围：`0` ～ `100` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0= |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `interview_record\[\]` | 面试评价详细信息列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 面试评价 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `feedback_form_id` | `string` | 面试评价表 ID，详情可查看：[获取面试评价表列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_feedback_form/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `commit_status` | `int` | 提交状态<br>**可选值有**：<br>- `1`: 已提交 - `2`: 未提交 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `submit_time` | `string` | 面试评价提交时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `record_score` | `record_score` | 面试评价分数 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `score` | `number(float)` | 面试评价得分，精确到小数点后两位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `total_score` | `number(float)` | 面试评价总分，精确到小数点后两位 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `interviewer` | `id_name_object` | 面试官信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 面试官 ID，与入参 `user_id_type` 类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 面试官姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 面试官中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 面试官英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `attachments` | `attachment\[\]` | 面试评价附件列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 附件创建时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `module_assessments` | `module_assessment\[\]` | 模块评价列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `interview_feedback_form_module_id` | `string` | 面试评价表模块 ID，详情可查看：[获取面试评价表列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_feedback_form/list)返回结果中 `data.items.modules` 字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `module_name` | `i18n` | 模块名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 模块中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 模块英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `module_type` | `int` | 模块类型<br>**可选值有**：<br>- `1`: 系统预置「面试结论」模块 - `2`: 自定义模块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `module_weight` | `number(float)` | 模块权重，精确到小数点后两位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `module_score` | `number(float)` | 模块打分，精确到小数点后两位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dimension_assessments` | `dimension_assessment\[\]` | 模块评价 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `interview_feedback_form_dimension_id` | `string` | 维度 ID，详情可查看：[获取面试评价表列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_feedback_form/list)返回结果中 `data.items.modules.dimensions` 字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dimension_name` | `i18n` | 维度名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 维度中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 维度英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dimension_type` | `int` | 维度评价方式<br>**可选值有**：<br>- `1`: 单选题 - `2`: 多选题 - `3`: 描述题 - `5`: 职级建议 - `6`: 打分题(单选) - `7`: 打分题(填空) - `10`: 系统预置-结论 - `11`: 系统预置-得分 - `12`: 系统预置-记录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `weight` | `number(float)` | 维度权重，精确到小数点后两位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dimension_content` | `string` | 当维度评价方式为 `描述题` 时，从此取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dimension_option` | `dimension_option` | 当维度评价方式为 `单选题` 时，从此取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 选项 ID，详情可查看：[获取面试评价表列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_feedback_form/list)返回结果中 `data.items.modules.dimensions.option_items` 字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `score_val` | `int` | 选项分数<br>**数据范围**： - `0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dimension_options` | `dimension_option\[\]` | 当维度评价方式为 `多选题` 时，从此取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 选项 ID，详情可查看：[获取面试评价表列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_feedback_form/list)返回结果中 `data.items.modules.dimensions.option_items` 字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `score_val` | `int` | 选项分数<br>**数据范围**： - `0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dimension_score` | `int` | 当维度评价方式为 `打分题(填空)` 时，从此取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `recommended_job_level` | `recommended_job_level` | 当维度评价方式为 `职级建议` 时，从此取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lower_limit_job_level_name` | `i18n` | 最低职级建议 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 最低职级建议中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 最低职级建议英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `higher_limit_job_level_name` | `i18n` | 最高职级建议 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 最高职级建议中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 最高职级建议英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `question_assessments` | `question_assessment\[\]` | 面试题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `question_type` | `int` | 面试题类型<br>**可选值有**：<br>- `1`: 普通面试题目 - `2`: 在线编程题目 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `i18n` | 面试题名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 面试题中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 面试题英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 面试题描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 面试题中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 面试题英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 面试者作答内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `abilities` | `ability\[\]` | 能力项列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 能力项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 能力项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 能力项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 能力项描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 能力项中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 能力项英文描述 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "SUCCESS",
    "data": {
        "items": [
            {
                "id": "7171693733661327361",
                "feedback_form_id": "71716937336613273612",
                "commit_status": 1,
                "submit_time": "1710405457390",
                "record_score": {
                    "score": 100.00,
                    "total_score": 100.00
                },
                "interviewer": {
                    "id": "7171693733661327364",
                    "name": {
                        "zh_cn": "小明",
                        "en_us": "xiaoming"
                    }
                },
                "attachments": [
                    {
                        "file_id": "7140517838785481004",
                        "file_name": "1.13测试1的面试记录.pdf",
                        "content_type": "application/pdf",
                        "file_size": 16615,
                        "create_time": "1710399930151"
                    }
                ],
                "module_assessments": [
                    {
                        "interview_feedback_form_module_id": "7171693733661327361",
                        "module_name": {
                            "zh_cn": "面试结论",
                            "en_us": "Interview Result"
                        },
                        "module_type": 1,
                        "module_weight": 10.00,
                        "module_score": 10.00,
                        "dimension_assessments": [
                            {
                                "interview_feedback_form_dimension_id": "7171693733661327361",
                                "dimension_name": {
                                    "zh_cn": "行业知识储备水平",
                                    "en_us": "Industry knowledge reserve level"
                                },
                                "dimension_type": 1,
                                "weight": 1.00,
                                "dimension_content": "描述题作答",
                                "dimension_option": {
                                    "id": "7171693733661327361",
                                    "name": {
                                        "zh_cn": "选项一",
                                        "en_us": "Option 1"
                                    },
                                    "score_val": 10
                                },
                                "dimension_options": [
                                    {
                                        "id": "7171693733661327361",
                                        "name": {
                                            "zh_cn": "选项一",
                                            "en_us": "Option 1"
                                        },
                                        "score_val": 10
                                    }
                                ],
                                "dimension_score": 10,
                                "recommended_job_level": {
                                    "lower_limit_job_level_name": {
                                        "zh_cn": "2-2",
                                        "en_us": "2-2"
                                    },
                                    "higher_limit_job_level_name": {
                                        "zh_cn": "3-2",
                                        "en_us": "3-2"
                                    }
                                },
                                "question_assessments": [
                                    {
                                        "question_type": 1,
                                        "title": {
                                            "zh_cn": "操作系统进程调度",
                                            "en_us": "Operating system process scheduling"
                                        },
                                        "description": {
                                            "zh_cn": "操作系统中如何进行进程调度？",
                                            "en_us": "How is process scheduling performed in an operating system?"
                                        },
                                        "content": "操作系统的进程调度是通过...",
                                        "abilities": [
                                            {
                                                "name": {
                                                    "zh_cn": "算法",
                                                    "en_us": "Algorithm"
                                                },
                                                "description": {
                                                    "zh_cn": "候选人算法能力如何？",
                                                    "en_us": "What are the candidate’s algorithmic abilities?"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
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
| 500 | 1002001 | System error | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002003 | Parameter error | 检查参数是否正确，例如类型，大小 |


更多错误码信息，参见[通用错误码](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)。


