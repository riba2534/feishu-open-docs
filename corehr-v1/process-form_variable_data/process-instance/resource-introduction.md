---
title: "流程实例资源介绍"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/process-form_variable_data/process-instance/resource-introduction"
updateTime: "1734434181000"
---

# 资源介绍

## 资源定义

流程实例：是指用户在业务功能或者飞书人事的审批中心发起的具体流程，process_id 是其唯一标识。

流程定义：是指管理员在设置侧配置的流程，类似流程模板，flow_definition_id 是其唯一标识。用户发起的流程是按照对应的流程定义的配置生成。

## 字段说明


| 名称 | 类型 | 描述 |
| --- | --- | --- |
| process_id | string | 流程实例ID |
| status | int | 流程状态            **可选值有：**            - `1`：进行中 - `2`：拒绝 - `4`：撤回 - `8`：撤销 - `9`：已完成 |
| flow_template_id | string | 业务类型ID |
| flow_template_name | dataengine_i18n | 业务类型名称 |
| &nbsp;&nbsp;└ zh_cn | string | 中文值 |
| &nbsp;&nbsp;└ en_us | string | 英文值 |
| flow_definition_id | string | 流程定义ID |
| flow_definition_name | dataengine_i18n | 流程定义名称 |
| &nbsp;&nbsp;└ zh_cn | string | 中文值 |
| &nbsp;&nbsp;└ en_us | string | 英文值 |
| initiator_id | string | 流程发起人ID |
| initiator_name | dataengine_i18n | 流程发起人姓名 |
| &nbsp;&nbsp;└ zh_cn | string | 中文值 |
| &nbsp;&nbsp;└ en_us | string | 英文值 |
| create_time | string | 流程发起时间，Unix毫秒时间戳 |
| complete_time | string | 流程结束时间，Unix毫秒时间戳 |
| start_links | process_link | 发起单据地址 |
| &nbsp;&nbsp;└ web_link | string | web端单据详情页地址 |
| &nbsp;&nbsp;└ pc_link | string | 飞书pc端单据详情页地址 |
| &nbsp;&nbsp;└ mobile_link | string | 飞书移动端单据详情页地址 |
| abstracts | process_abstract_item[] | 流程摘要，会随着流程流转发生变化 |
| &nbsp;&nbsp;└ name | dataengine_i18n | 摘要标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ zh_cn | string | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ en_us | string | 英文值 |
| &nbsp;&nbsp;└ value | dataengine_i18n | 摘要值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ zh_cn | string | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ en_us | string | 英文值 |
| todos | process_todo_item[] | 待办列表 |
| &nbsp;&nbsp;└ approver_id | string | 单据ID |
| &nbsp;&nbsp;└ type | int | 单据类型            **可选值有：**            - `1`：审批单 - `5`：表单 |
| &nbsp;&nbsp;└ links | process_link | 发起单据地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ web_link | string | web端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ pc_link | string | 飞书pc端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ mobile_link | string | 飞书移动端单据详情页地址 |
| &nbsp;&nbsp;└ operator_id | string | 操作人ID |
| &nbsp;&nbsp;└ operator_name | dataengine_i18n | 操作人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ zh_cn | string | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ en_us | string | 英文值 |
| &nbsp;&nbsp;└ node_name | dataengine_i18n | 节点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ zh_cn | string | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ en_us | string | 英文值 |
| &nbsp;&nbsp;└ create_time | string | 创建时间，Unix毫秒时间戳 |
| &nbsp;&nbsp;└ node_definition_id | string | 节点定义ID（注：在回退场景，同一个节点会对应多个节点实例） |
| cc_list | process_cc_item[] | 抄送列表 |
| &nbsp;&nbsp;└ approver_id | string | 单据ID |
| &nbsp;&nbsp;└ links | process_link | 发起单据地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ web_link | string | web端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ pc_link | string | 飞书pc端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ mobile_link | string | 飞书移动端单据详情页地址 |
| &nbsp;&nbsp;└ operator_id | string | 操作人ID |
| &nbsp;&nbsp;└ operator_name | dataengine_i18n | 操作人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ zh_cn | string | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ en_us | string | 英文值 |
| &nbsp;&nbsp;└ node_name | dataengine_i18n | 节点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ zh_cn | string | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ en_us | string | 英文值 |
| &nbsp;&nbsp;└ create_time | string | 创建时间，Unix毫秒时间戳 |
| &nbsp;&nbsp;└ node_definition_id | string | 节点定义ID（注：在回退场景，同一个节点会对应多个节点实例） |
| done_list | process_done_item[] | 已办列表 |
| &nbsp;&nbsp;└ approver_id | string | 单据ID |
| &nbsp;&nbsp;└ type | int | 单据类型            **可选值有：**            - `1`：审批单 - `5`：表单 |
| &nbsp;&nbsp;└ status | int | 单据状态            **可选值有：**            - `3`：已完成 - `2`：拒绝 - `4`：取消 |
| &nbsp;&nbsp;└ links | process_link | 发起单据地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ web_link | string | web端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ pc_link | string | 飞书pc端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ mobile_link | string | 飞书移动端单据详情页地址 |
| &nbsp;&nbsp;└ operator_id | string | 操作人ID |
| &nbsp;&nbsp;└ operator_name | dataengine_i18n | 操作人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ zh_cn | string | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ en_us | string | 英文值 |
| &nbsp;&nbsp;└ node_name | dataengine_i18n | 节点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ zh_cn | string | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ en_us | string | 英文值 |
| &nbsp;&nbsp;└ create_time | string | 创建时间，Unix毫秒时间戳 |
| &nbsp;&nbsp;└ complete_time | string | 完成时间，Unix毫秒时间戳 |
| &nbsp;&nbsp;└ node_definition_id | string | 节点定义ID（注：在回退场景，同一个节点会对应多个节点实例） |
| properties | int | 普通流程或撤销流程等            **可选值有：**            - `1`：普通流程 - `2`：撤销流程 |
| system_todos | process_system_todo_item[] | 系统待办列表 |
| &nbsp;&nbsp;└ approver_id | string | 单据ID |
| &nbsp;&nbsp;└ type | int | 单据类型            **可选值有：**            - `1`：审批单 - `5`：表单 |
| &nbsp;&nbsp;└ links | process_link | 发起单据地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ web_link | string | web端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ pc_link | string | 飞书pc端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ mobile_link | string | 飞书移动端单据详情页地址 |
| &nbsp;&nbsp;└ operator_name | dataengine_i18n | 操作人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ zh_cn | string | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ en_us | string | 英文值 |
| &nbsp;&nbsp;└ node_name | dataengine_i18n | 节点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ zh_cn | string | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ en_us | string | 英文值 |
| &nbsp;&nbsp;└ create_time | string | 创建时间，Unix毫秒时间戳 |
| &nbsp;&nbsp;└ node_definition_id | string | 节点定义ID（注：在回退场景，同一个节点会对应多个节点实例） |
| system_done_list | process_system_done_item[] | 系统已办列表 |
| &nbsp;&nbsp;└ approver_id | string | 单据ID |
| &nbsp;&nbsp;└ type | int | 单据类型            **可选值有：**            - `1`：审批单 - `5`：表单 |
| &nbsp;&nbsp;└ status | int | 单据状态            **可选值有：**            - `3`：已完成 - `2`：拒绝 - `4`：取消 |
| &nbsp;&nbsp;└ links | process_link | 发起单据地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ web_link | string | web端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ pc_link | string | 飞书pc端单据详情页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ mobile_link | string | 飞书移动端单据详情页地址 |
| &nbsp;&nbsp;└ operator_name | dataengine_i18n | 操作人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ zh_cn | string | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ en_us | string | 英文值 |
| &nbsp;&nbsp;└ node_name | dataengine_i18n | 节点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ zh_cn | string | 中文值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ en_us | string | 英文值 |
| &nbsp;&nbsp;└ create_time | string | 创建时间，Unix毫秒时间戳 |
| &nbsp;&nbsp;└ complete_time | string | 完成时间，Unix毫秒时间戳 |
| &nbsp;&nbsp;└ node_definition_id | string | 节点定义ID（注：在回退场景，同一个节点会对应多个节点实例） |


## 数据示例


```json 
{
    "process_id": "7278949005675988535",
    "status": 1,
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
            "node_definition_id": "approval_d25b5eddfef"
        }
    ],
    "properties": 1,
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
            "node_definition_id": "approval_d25b5eddfef"
        }
    ]
}
``` 


