---
title: "转交人工任务"
fullPath: "/uAjLw4CM/ukTMukTMukTM/apaas-v1/approval_task/transfer"
updateTime: "1710830998000"
---

# 转交人工任务

对于人工任务进行转交操作


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/apaas/v1/approval_tasks/:approval_task_id/transfer |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | app_engine:approval:write |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `approval_task_id` | `string` | 人工任务 ID<br>**示例值**："1785996265147395" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id` | `string` | 是 | 操作人 ID<br>**示例值**："1783981209205788" |
| `from_user_ids` | `string\[\]` | 否 | 原审批人id<br>**示例值**：["1783981209205788"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `20` |
| `to_user_ids` | `string\[\]` | 否 | 新审批人id<br>**示例值**：["1783981209205789"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `20` |
| `opinion` | `string` | 否 | 转交原因<br>**示例值**："转交" |


### 请求体示例

```json
{
    "user_id": "1783981209205788",
    "from_user_ids": [
        "1783981209205788"
    ],
    "to_user_ids": [
        "1783981209205789"
    ],
    "opinion": "转交"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {}
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2320001 | param is invalid | 请检查输入参数 |


