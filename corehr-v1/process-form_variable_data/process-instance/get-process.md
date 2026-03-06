---
title: "获取单个流程详情"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/process/get"
updateTime: "1769396383000"
---

# 获取单个流程详情

根据流程实例 id（process_id）获取单个流程详情（此功能不受数据权限范围控制）。比如流程状态、流程发起人、流程发起时间、流程摘要、流程里的所有待办、已办、抄送任务等。


> **Tip**: 休假类型流程的“撤销”的实例状态，以及是否属于“更正流程”需要去休假的[批量查询员工请假记录](https://open.larkoffice.com/document/server-docs/corehr-v1/leave/leave_request_history?appId=cli_a7b01a4272581013) 接口查询


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/processes/:process_id |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:process:read` 获取流程数据 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `process_id` | `string` | 流程实例ID。可通过[查询流程实例列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/process/list)接口获取<br>**示例值**："7278949005675988535" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `process_id` | `string` | 流程实例ID |
| &nbsp;&nbsp;└ `status` | `int` | 流程状态<br>**可选值有**：<br>- `1`: 进行中 - `2`: 拒绝 - `4`: 撤回 - `8`: 撤销 - `9`: 已完成 - `15`: 撤销中 |
| &nbsp;&nbsp;└ `flow_template_id` | `string` | 业务类型ID |
| &nbsp;&nbsp;└ `flow_template_name` | `dataengine_i18n` | 业务类型名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;└ `flow_definition_id` | `string` | 流程定义ID |
| &nbsp;&nbsp;└ `flow_definition_name` | `dataengine_i18n` | 流程定义名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;└ `initiator_id` | `string` | 流程发起人ID，当发起人为系统时，该字段返回为空 |
| &nbsp;&nbsp;└ `initiator_name` | `dataengine_i18n` | 流程发起人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;└ `create_time` | `string` | 流程发起时间，Unix毫秒时间戳 |
| &nbsp;&nbsp;└ `complete_time` | `string` | 流程结束时间，Unix毫秒时间戳 |
| &nbsp;&nbsp;└ `start_links` | `process_link` | 发起单据地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `web_link` | `string` | web端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `pc_link` | `string` | 飞书pc端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_link` | `string` | 飞书移动端单据详情页地址 |
| &nbsp;&nbsp;└ `abstracts` | `process_abstract_item\[\]` | 流程摘要，会随着流程流转发生变化 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `dataengine_i18n` | 摘要标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `dataengine_i18n` | 摘要值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;└ `todos` | `process_todo_item\[\]` | 待办列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `approver_id` | `string` | 单据ID,注意单据id和operator_id并不是一对一的 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 单据类型<br>**可选值有**：<br>- `1`: 审批单 - `5`: 表单 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `links` | `process_link` | 单据地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `web_link` | `string` | web端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_link` | `string` | 飞书pc端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_link` | `string` | 飞书移动端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operator_id` | `string` | 待办人ID，每个节点下待办人标识唯一 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operator_name` | `dataengine_i18n` | 操作人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `node_name` | `dataengine_i18n` | 节点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 创建时间，Unix毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `node_definition_id` | `string` | 节点定义ID（注：在回退场景，同一个节点会对应多个节点实例） |
| &nbsp;&nbsp;└ `cc_list` | `process_cc_item\[\]` | 抄送列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `approver_id` | `string` | 单据ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `links` | `process_link` | 单据地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `web_link` | `string` | web端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_link` | `string` | 飞书pc端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_link` | `string` | 飞书移动端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operator_id` | `string` | 抄送人ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operator_name` | `dataengine_i18n` | 抄送人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `node_name` | `dataengine_i18n` | 节点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 抄送时间，Unix毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `node_definition_id` | `string` | 节点定义ID（注：在回退场景，同一个节点会对应多个节点实例） |
| &nbsp;&nbsp;└ `done_list` | `process_done_item\[\]` | 已办列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `approver_id` | `string` | 单据ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 单据类型<br>**可选值有**：<br>- `1`: 审批单 - `5`: 表单 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 单据状态<br>**可选值有**：<br>- `3`: 已完成 - `2`: 拒绝 - `4`: 取消 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `links` | `process_link` | 单据地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `web_link` | `string` | web端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_link` | `string` | 飞书pc端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_link` | `string` | 飞书移动端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operator_id` | `string` | 操作人ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operator_name` | `dataengine_i18n` | 操作人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `node_name` | `dataengine_i18n` | 节点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 创建时间，Unix毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `complete_time` | `string` | 完成时间，Unix毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `node_definition_id` | `string` | 节点定义ID（注：在回退场景，同一个节点会对应多个节点实例） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `approval_opinion` | `string` | 审批意见 |
| &nbsp;&nbsp;└ `properties` | `int` | 普通流程或撤销流程等<br>**可选值有**：<br>- `1`: 普通流程 - `2`: 撤销流程，返回这个属性的前提是在审批中心我发起的页面进行撤销操作 - `3`: 更正流程，返回这个属性的前提是在审批中心我发起的页面进行更正操作 |
| &nbsp;&nbsp;└ `system_todos` | `process_system_todo_item\[\]` | 系统待办列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `approver_id` | `string` | 单据ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 单据类型<br>**可选值有**：<br>- `1`: 审批单 - `5`: 表单 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `links` | `process_link` | 单据地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `web_link` | `string` | web端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_link` | `string` | 飞书pc端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_link` | `string` | 飞书移动端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operator_name` | `dataengine_i18n` | 操作人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `node_name` | `dataengine_i18n` | 节点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 创建时间，Unix毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `node_definition_id` | `string` | 节点定义ID（注：在回退场景，同一个节点会对应多个节点实例） |
| &nbsp;&nbsp;└ `system_done_list` | `process_system_done_item\[\]` | 系统已办列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `approver_id` | `string` | 单据ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 单据类型<br>**可选值有**：<br>- `1`: 审批单 - `5`: 表单 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 单据状态<br>**可选值有**：<br>- `3`: 已完成 - `2`: 拒绝 - `4`: 取消 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `links` | `process_link` | 单据地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `web_link` | `string` | web端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_link` | `string` | 飞书pc端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_link` | `string` | 飞书移动端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operator_name` | `dataengine_i18n` | 操作人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `node_name` | `dataengine_i18n` | 节点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 创建时间，Unix毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `complete_time` | `string` | 完成时间，Unix毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `node_definition_id` | `string` | 节点定义ID（注：在回退场景，同一个节点会对应多个节点实例） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `approval_opinion` | `string` | 审批意见 |
| &nbsp;&nbsp;└ `comment_infos` | `process_comment_info\[\]` | 评论列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `commentor_id` | `string` | 评论人ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `commentor_name` | `dataengine_i18n` | 评论人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `comment_time` | `string` | 评论时间,Unix毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `comment_msg` | `string` | 评论内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `at_user_ids` | `string\[\]` | 在评论中被提及（@）到的人的id列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `file_count` | `int` | 评论中附件数量 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `image_count` | `int` | 评论中图片数量 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `comment_id` | `string` | 一条评论的唯一id |
| &nbsp;&nbsp;└ `original_process_id` | `string` | 更正或撤销流程的原流程ID |
| &nbsp;&nbsp;└ `is_last_completed_correct_process` | `boolean` | 是否最新的「已完成」的更正流程 |
| &nbsp;&nbsp;└ `process_name` | `dataengine_i18n` | 流程实例名称，取流程发起时的流程定义名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文值 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "process_id": "7278949005675988535",
        "status": 9,
        "flow_template_id": "leave",
        "flow_template_name": {
            "zh_cn": "中文",
            "en_us": "English"
        },
        "flow_definition_id": "people_6961286846093788680_7081951411982077732",
        "flow_definition_name": {
            "zh_cn": "中文",
            "en_us": "English"
        },
        "initiator_id": "7124991993901827628",
        "initiator_name": {
            "zh_cn": "中文",
            "en_us": "English"
        },
        "create_time": "1694769814036",
        "complete_time": "1694769814036",
        "start_links": {
            "web_link": "http://xxxx.com/xxx/xxx?a=b",
            "pc_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx",
            "mobile_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx"
        },
        "abstracts": [
            {
                "name": {
                    "zh_cn": "中文",
                    "en_us": "English"
                },
                "value": {
                    "zh_cn": "中文",
                    "en_us": "English"
                }
            }
        ],
        "todos": [
            {
                "approver_id": "7278949005675988535",
                "type": 1,
                "links": {
                    "web_link": "http://xxxx.com/xxx/xxx?a=b",
                    "pc_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx",
                    "mobile_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx"
                },
                "operator_id": "7124991993901827628",
                "operator_name": {
                    "zh_cn": "中文",
                    "en_us": "English"
                },
                "node_name": {
                    "zh_cn": "中文",
                    "en_us": "English"
                },
                "create_time": "1694769814036",
                "node_definition_id": "approval_d25b5eddfef"
            }
        ],
        "cc_list": [
            {
                "approver_id": "7278949005675988535",
                "links": {
                    "web_link": "http://xxxx.com/xxx/xxx?a=b",
                    "pc_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx",
                    "mobile_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx"
                },
                "operator_id": "7124991993901827628",
                "operator_name": {
                    "zh_cn": "中文",
                    "en_us": "English"
                },
                "node_name": {
                    "zh_cn": "中文",
                    "en_us": "English"
                },
                "create_time": "1694769814036",
                "node_definition_id": "approval_d25b5eddfef"
            }
        ],
        "done_list": [
            {
                "approver_id": "7278949005675988535",
                "type": 1,
                "status": 3,
                "links": {
                    "web_link": "http://xxxx.com/xxx/xxx?a=b",
                    "pc_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx",
                    "mobile_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx"
                },
                "operator_id": "7124991993901827628",
                "operator_name": {
                    "zh_cn": "中文",
                    "en_us": "English"
                },
                "node_name": {
                    "zh_cn": "中文",
                    "en_us": "English"
                },
                "create_time": "1694769814036",
                "complete_time": "1694769814036",
                "node_definition_id": "approval_d25b5eddfef",
                "approval_opinion": "审批意见"
            }
        ],
        "properties": 2,
        "system_todos": [
            {
                "approver_id": "7278949005675988535",
                "type": 1,
                "links": {
                    "web_link": "http://xxxx.com/xxx/xxx?a=b",
                    "pc_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx",
                    "mobile_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx"
                },
                "operator_name": {
                    "zh_cn": "中文",
                    "en_us": "English"
                },
                "node_name": {
                    "zh_cn": "中文",
                    "en_us": "English"
                },
                "create_time": "1694769814036",
                "node_definition_id": "approval_d25b5eddfef"
            }
        ],
        "system_done_list": [
            {
                "approver_id": "7278949005675988535",
                "type": 1,
                "status": 3,
                "links": {
                    "web_link": "http://xxxx.com/xxx/xxx?a=b",
                    "pc_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx",
                    "mobile_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx"
                },
                "operator_name": {
                    "zh_cn": "中文",
                    "en_us": "English"
                },
                "node_name": {
                    "zh_cn": "中文",
                    "en_us": "English"
                },
                "create_time": "1694769814036",
                "complete_time": "1694769814036",
                "node_definition_id": "approval_d25b5eddfef",
                "approval_opinion": "审批意见"
            }
        ],
        "comment_infos": [
            {
                "commentor_id": "7355397217231831060",
                "commentor_name": {
                    "zh_cn": "中文",
                    "en_us": "English"
                },
                "comment_time": "1694769814036",
                "comment_msg": "评论内容",
                "at_user_ids": [
                    "7355397217231831060"
                ],
                "file_count": 10,
                "image_count": 10,
                "comment_id": "7355397217231831060"
            }
        ],
        "original_process_id": "7278949005675988535",
        "is_last_completed_correct_process": false,
        "process_name": {
            "zh_cn": "中文",
            "en_us": "English"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1160500 | system error | 系统异常，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)协助排查 |
| 400 | 1160101 | invalid param | 参数错误，请按照接口字段说明自查 |


