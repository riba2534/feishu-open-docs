---
title: "更新 e-HR 导入任务结果"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/ehr_import_task/patch"
updateTime: "1720618210000"
---

# 更新 e-HR 导入任务结果

在处理完[导入 e-HR](
https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/event/import-ehr)事件后，可调用该接口，更新  e-HR 导入任务结果。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/ehr_import_tasks/:ehr_import_task_id |
| HTTP Method | PATCH |
| 接口频率限制 | [50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:ehr_import` 更新导入 e-HR 任务 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `ehr_import_task_id` | `string` | 导入任务 ID，任务 ID 来源于导入 e-HR 事件中的 task_id，详情参考[导入 e-HR]( https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/event/import-ehr)<br>**示例值**："6914551145542568199" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `fail_reason` | `string` | 否 | 失败原因，仅在导入结果为失败时可用<br>**示例值**："当前 HC 不可用" |
| `redirect_url` | `string` | 否 | 跳转链接，若需返回跳转链接，请前往「飞书招聘」-「设置」-「生态对接」- 「e-HR / OA 办公系统」 - 「导入 e-HR」功能设置中开启「支持对接的 e-HR / OA 系统返回外部链接」开关<br>**示例值**："https://example.com" |
| `state` | `int` | 是 | 导入结果<br>**示例值**：2<br>**可选值有**：<br>- `1`: 导入成功 - `2`: 导入失败 |


### 请求体示例

```json
{
    "fail_reason": "当前 HC 不可用",
    "redirect_url": "https://example.com",
    "state": 2
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
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |


