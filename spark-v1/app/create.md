---
title: "创建妙搭应用"
fullPath: "/uAjLw4CM/ukTMukTMukTM/spark-v1/app/create"
updateTime: "1779366624000"
---

# 创建妙搭应用

创建妙搭应用


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/spark/v1/apps |
| HTTP Method | POST |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `spark:app:write` 创建与更新妙搭应用 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | `string` | 是 | 应用名称<br>**示例值**："智能客服助手" |
| `app_type` | `string` | 否 | 应用类型<br>可选值：HTML<br>**示例值**："HTML" |
| `description` | `string` | 否 | 应用描述<br>**示例值**："提供7×24小时智能对话服务，支持常见问题自动解答与工单流转" |
| `icon_url` | `string` | 否 | 应用图标地址<br>**示例值**："https://example.com/app-icons/customer-service.png" |


### 请求体示例

```json
{
    "name": "智能客服助手",
    "app_type": "HTML",
    "description": "提供7×24小时智能对话服务，支持常见问题自动解答与工单流转",
    "icon_url": "https://example.com/app-icons/customer-service.png"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `app` | `app` | 妙搭应用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `app_id` | `string` | 应用唯一标识，系统自动生成，用于在接口中定位具体应用。可通过应用创建接口或开发者后台获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `app_type` | `string` | 应用类型 可选值：HTML |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 应用名称，用于在管理后台和前端展示，支持中英文，长度不超过64字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 应用功能说明，用于向用户介绍应用核心能力，长度不超过200字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `icon_url` | `string` | 应用图标访问地址，支持PNG/JPG格式，建议尺寸为128×128像素 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `string` | 应用创建时间，遵循ISO 8601 UTC格式，由系统自动生成 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_at` | `string` | 应用最后更新时间，遵循ISO 8601 UTC格式，应用信息变更时自动更新 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "app": {
            "app_id": "app_7d2f8a4b1c9e6035",
            "app_type": " HTML",
            "name": "智能客服助手",
            "description": "提供7×24小时智能对话服务，支持常见问题自动解答与工单流转",
            "icon_url": "https://example.com/app-icons/customer-service.png",
            "created_at": "2026-05-18T10:00:00Z",
            "updated_at": "2026-06-20T14:30:00Z"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 3340001 | param is invalid | 输入参数不合法，请检查输入参数 |


