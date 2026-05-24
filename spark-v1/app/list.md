---
title: "批量获取妙搭应用"
fullPath: "/uAjLw4CM/ukTMukTMukTM/spark-v1/app/list"
updateTime: "1779366594000"
---

# 批量获取妙搭应用

批量获取妙搭应用


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/spark/v1/apps |
| HTTP Method | GET |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `spark:app:read` 获取妙搭应用信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 每页返回的应用数量，取值范围为1-100，默认值为20<br>**示例值**：20 |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：eyJwYWdlX251bWJlciI6MiwiY29udGVudF9pZHMiOlsiMTIzNCIsIjU2NzgiXX0= |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `items` | `app\[\]` | 应用列表数据，包含当前页返回的所有妙搭应用的详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `app_id` | `string` | 应用唯一标识，系统自动生成，用于在接口中定位具体应用。可通过应用创建接口或开发者后台获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `app_type` | `string` | 应用类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 应用名称，用于在管理后台和前端展示，支持中英文，长度不超过64字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 应用功能说明，用于向用户介绍应用核心能力，长度不超过200字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `icon_url` | `string` | 应用图标访问地址，支持PNG/JPG格式，建议尺寸为128×128像素 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `string` | 应用创建时间，遵循ISO 8601 UTC格式，由系统自动生成 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_at` | `string` | 应用最后更新时间，遵循ISO 8601 UTC格式，应用信息变更时自动更新 |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "page_token": "eyJwYWdlX251bWJlciI6MiwiY29udGVudF9pZHMiOlsiMTIzNCIsIjU2NzgiXX0=",
        "items": [
            {
                "app_id": "app_7d2f8a4b1c9e6035",
                "app_type": "HTML",
                "name": "智能客服助手",
                "description": "提供7×24小时智能对话服务，支持常见问题自动解答与工单流转",
                "icon_url": "https://example.com/app-icons/customer-service.png",
                "created_at": "2026-05-18T10:00:00Z",
                "updated_at": "2026-06-20T14:30:00Z"
            }
        ],
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 3340001 | param is invalid | 输入参数不合法，请检查输入参数 |


