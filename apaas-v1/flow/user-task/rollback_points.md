---
title: "查询人工任务可退回的位置"
fullPath: "/uAjLw4CM/ukTMukTMukTM/apaas-v1/user_task/rollback_points"
updateTime: "1734512580000"
---

# 人工任务 - 查询可退回的位置

查询当前任务可以退回的位置


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/apaas/v1/user_tasks/:task_id/rollback_points |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | app_engine:approval:read |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `task_id` | `string` | 任务ID，可以通过[查询人工任务](query.md)获取<br>**示例值**："1234" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `operator_user_id` | `string` | 是 | 操作人kunlunUserID,可通过Apaas用户管理页面获取<br>**示例值**："1234" |


### 请求体示例

```json
{
    "operator_user_id": "1234"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `tasks` | `allowed_rollbaclk_task_item_type\[\]` | 任务列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 任务ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `activity_label` | `i18n\[\]` | 任务对应的名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language_code` | `string` | 多语Code |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text` | `string` | 多语对应的任务名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_start` | `boolean` | 是否开始节点 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "tasks": [
            {
                "id": "1234",
                "activity_label": [
                    {
                        "language_code": "2052",
                        "text": "人工任务名称"
                    }
                ],
                "is_start": false
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2320001 | param is invalid | 请检查输入参数 |


