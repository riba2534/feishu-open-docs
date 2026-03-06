---
title: "获取背调信息列表"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/background_check_order/list"
updateTime: "1755849123000"
---

# 获取背调信息列表

根据投递 ID 或背调更新时间批量获取背调订单信息。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/background_check_orders |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:background_check_order` 更新招聘背调信息 `hire:background_check_order:readonly` 获取招聘背调信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：eyJvZmZzZXQiOjEsInRpbWVzdGFtcCI6MTY0MDc2NTYzMjA4OCwiaWQiOm51bGx9 |
| `page_size` | `int` | 否 | 分页大小<br>**示例值**：100<br>**默认值**：`10`<br>**数据校验规则**：<br>- 最大值：`100` |
| `application_id` | `string` | 否 | 投递 ID。可通过[获取投递列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/list)接口获取<br>**示例值**：6985833807195212076 |
| `update_start_time` | `string` | 否 | 最早更新时间，毫秒时间戳。需小于等于update_end_time<br>**示例值**：1638848468868 |
| `update_end_time` | `string` | 否 | 最晚更新时间，毫秒时间戳。需大于等于update_start_time<br>**示例值**：1638848468869 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `items` | `background_check_order\[\]` | 背调订单列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `order_id` | `string` | 背调订单 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `application_id` | `string` | 投递 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `order_status` | `int` | 背调状态<br>**可选值有**：<br>- `2`: 已安排 - `3`: 已完成 - `4`: 已终止 - `5`: 审批中 - `6`: 审批已撤回 - `8`: 审批通过 - `9`: 审批未通过 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `account_third_type` | `int` | 供应商类型<br>**可选值有**：<br>- `1`: 八方锦程 - `2`: i背调 - `3`: 轩渡 - `127`: 自定义供应商 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `package` | `string` | 背调套餐名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 背调名称（仅用户手动录入的背调结果支持返回该字段） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `feedback_info_list` | `background_check_order_feedback_info\[\]` | 背调报告列表，按照报告创建时间降序排列。可通过[更新背调订单进度](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/eco_background_check/update_progress)更新报告 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 背调报告 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `attachment_url` | `string` | 背调信息附件下载链接（大部分供应商均支持该字段；该字段与「report_preview_url」同一供应商只能支持 1 种），有效期1小时 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `report_preview_url` | `string` | 背调预览链接（该字段与「attachment_url」同一供应商只能支持 1 种），有效期由供应商控制 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `result` | `string` | 背调结果。招聘系统预置的背调结果有 红灯、黄灯、蓝灯、绿灯，也可以是更新背调进度时推送的状态。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `report_type` | `int` | 报告类型<br>**可选值有**：<br>- `1`: 阶段性报告 - `2`: 终版报告 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `report_name` | `string` | 报告名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `process_info_list` | `background_check_order_process_info\[\]` | 背调进度列表，按照更新时间降序排列。可通过[更新背调订单进度](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/eco_background_check/update_progress)更新进度 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `process` | `string` | 背调进度 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `update_time` | `string` | 进度更新时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_process` | `string` | 英文背调进度 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `upload_time` | `string` | 录入时间毫秒时间戳（仅用户手动录入的背调结果支持返回该字段） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `candidate_info` | `user_contact_info` | 候选人信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile` | `string` | 手机号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `first_name` | `string` | 名字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `last_name` | `string` | 姓氏 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `creator_info` | `background_check_order_creator` | 背调发起人信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 发起人 ID，与入参 user_id_type 类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contactor_info` | `user_contact_info` | 背调联系人信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile` | `string` | 手机号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `begin_time` | `string` | 背调发起时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 背调结束时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `conclusion` | `string` | 背调结论。为最后一次背调报告的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `provider_info` | `provider_id_name_object` | 供应商信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `provider_id` | `string` | 供应商ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `provider_name` | `i18n` | 供应商名称信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_field_list` | `eco_background_check_custom_field_data\[\]` | 自定义字段模板。数据来源于[创建背调自定义字段](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/eco_background_check_custom_field/create) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 自定义字段类型<br>**可选值有**：<br>- `text`: 单行文本，最多100个汉字 - `textarea`: 多行文本，最多200个汉字 - `number`: 数字 - `boolean`: 布尔 - `select`: 单选 - `multiselect`: 多选 - `date`: 日期 - `file`: 附件 - `resume`: 候选人简历 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 自定义字段的标识，在同一账号内唯一 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 自定义字段的名称，用户在安排背调表单看到的控件标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_required` | `boolean` | 是否必填 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 自定义字段的描述，如果是输入控件，为用户在安排背调表单看到的 placeholder 或 提示文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `options` | `eco_background_check_custom_field_data_option\[\]` | type 为 select 或 multiselect 时必填，单选或多选的选项 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项的 key |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项的名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_data_list` | `background_check_custom_field_data_value\[\]` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 对应前文 *自定义字段模板* 的 key |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 用户填入的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ext_item_info_list` | `background_check_item_info\[\]` | 背调调查附加项列表。数据来源于[创建背调套餐和附加调查项](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/eco_background_check_package/create) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 附加项的ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 附加项的名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `update_time` | `string` | 订单更新时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `geo` | `string` | 属地<br>**可选值有**：<br>- `cn`: 中国大陆 - `sg`: 新加坡 - `us`: 美东 - `jp`: 日本 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `location_code` | `string` | 预计入职地点的编码，详见[查询地点列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `remark` | `string` | 备注 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "has_more": true,
        "page_token": "eyJvZmZzZXQiOjEsInRpbWVzdGFtcCI6MTY0MDc2NTYzMjA4OCwiaWQiOm51bGx9",
        "items": [
            {
                "order_id": "7037986982531778860",
                "application_id": "6985833807195212076",
                "order_status": 2,
                "account_third_type": 1,
                "package": "基础版",
                "name": "录入的背调",
                "feedback_info_list": [
                    {
                        "id": "6930815272790114324",
                        "attachment_url": "https://feishucdn.com/staource/v1/2de04c10-5cda-4c50~?image_size=np&cutpe=&quity=&mat=g&stmat=.wp",
                        "report_preview_url": "https://feishucdn.com/preview/file/6930815272790114324/",
                        "result": "红灯",
                        "report_type": 1,
                        "create_time": "1686645425868",
                        "report_name": "张三的背调报告"
                    }
                ],
                "process_info_list": [
                    {
                        "process": "待安排",
                        "update_time": "1638359554952",
                        "en_process": "arranged"
                    }
                ],
                "upload_time": "1662476247755",
                "candidate_info": {
                    "name": "王二",
                    "mobile": "176xxxx1234",
                    "email": "xxx@abc.vom",
                    "first_name": "Ming",
                    "last_name": "Lee"
                },
                "creator_info": {
                    "user_id": "6930815272790114324"
                },
                "contactor_info": {
                    "name": "王二",
                    "mobile": "176xxxx1234",
                    "email": "xxx@abc.vom"
                },
                "begin_time": "1686297649024",
                "end_time": "1686297649024",
                "conclusion": "绿灯",
                "provider_info": {
                    "provider_id": "6930815272790114324",
                    "provider_name": {
                        "zh_cn": "测试供应商",
                        "en_us": "test provider"
                    }
                },
                "custom_field_list": [
                    {
                        "type": "text",
                        "key": "candidate_resume",
                        "name": {
                            "zh_cn": "其他备注",
                            "en_us": "Other remark"
                        },
                        "is_required": true,
                        "description": {
                            "zh_cn": "其他备注描述",
                            "en_us": "Other remarks description"
                        },
                        "options": [
                            {
                                "key": "A",
                                "name": {
                                    "zh_cn": "选项A",
                                    "en_us": "A"
                                }
                            }
                        ]
                    }
                ],
                "custom_data_list": [
                    {
                        "key": "1",
                        "value": "user input value"
                    }
                ],
                "ext_item_info_list": [
                    {
                        "id": "6930815272790114324",
                        "name": "户籍查询"
                    }
                ],
                "update_time": "1686809576215",
                "geo": "cn",
                "location_code": "CN_1",
                "remark": "候选人很优秀"
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | System exception | 请根据实际报错信息定位问题或联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | Parameter error | 检查参数是否正确，例如类型，大小 |


