---
title: "查询人工任务"
fullPath: "/uAjLw4CM/ukTMukTMukTM/apaas-v1/user_task/query"
updateTime: "1741588202000"
---

# 查询人工任务列表

查询人工任务列表


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/apaas/v1/user_task/query |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | app_engine:approval:read |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `type` | `string` | 否 | 类型 - archived：已完成的 - pending：待处理的<br>**示例值**："pending" |
| `source` | `string` | 否 | 来源 - fromMe:我发起的 - assignMe:分配给我的 - CCMe：抄送我的<br>**示例值**："assignMe" |
| `limit` | `string` | 否 | 获取条数 - 最小值：1 - 最大值：50<br>**示例值**："10" |
| `offset` | `string` | 否 | 起始位置<br>**示例值**："0" |
| `start_time` | `string` | 否 | 开始时间（毫秒）<br>**示例值**："1730208758000" |
| `end_time` | `string` | 否 | 结束时间（毫秒）<br>**示例值**："1730208758000" |
| `api_ids` | `string\[\]` | 否 | 流程apiid列表，可以通过apaas流程列表页获取<br>**示例值**：["package_b40c28__c__action_aadfv6lfu6kai"]<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` |
| `kunlun_user_id` | `string` | 是 | kunlunUserID,可通过Apaas用户管理页面获取<br>**示例值**："1234" |


### 请求体示例

```json
{
    "type": "pending",
    "source": "assignMe",
    "limit": "10",
    "offset": "0",
    "start_time": "1730208758000",
    "end_time": "1730208758000",
    "api_ids": [
        "package_b40c28__c__action_aadfv6lfu6kai"
    ],
    "kunlun_user_id": "1234"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `count` | `string` | 总任务条数 |
| &nbsp;&nbsp;└ `tasks` | `user_task\[\]` | 任务信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `task_id` | `string` | 任务ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `task_start_time` | `string` | 任务开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `workflow_instance` | `user_task_wf_instance_type` | 流程实例 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 流程实例ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `label` | `i18n\[\]` | 流程对应的任务名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language_code` | `string` | 多语Code |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text` | `string` | 多语对应的任务名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `string` | 流程状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `initiator` | `user` | 发起人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户KunlunID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `summarys` | `user_task_summary_type\[\]` | 摘要信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_key` | `i18n` | 摘要名称（多语） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language_code` | `string` | 多语Code |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text` | `string` | 多语Code对应的文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_value` | `i18n\[\]` | 摘要值（多语） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language_code` | `string` | 多语Code |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text` | `string` | 多语Code对应的文本内容 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "count": "10",
        "tasks": [
            {
                "task_id": "1234",
                "task_start_time": "1234",
                "workflow_instance": {
                    "id": "1234",
                    "label": [
                        {
                            "language_code": "2052",
                            "text": "任务名称"
                        }
                    ],
                    "status": "in_process"
                },
                "initiator": {
                    "user_id": "1234",
                    "name": "发起人名称"
                },
                "summarys": [
                    {
                        "file_key": {
                            "language_code": "2052",
                            "text": "摘要名称"
                        },
                        "file_value": [
                            {
                                "language_code": "2052",
                                "text": "摘要值"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2320001 | param is invalid | 请检查输入参数 |


