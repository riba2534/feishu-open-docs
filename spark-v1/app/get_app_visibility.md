---
title: "获取妙搭应用可用范围"
fullPath: "/uAjLw4CM/ukTMukTMukTM/spark-v1/app/get_app_visibility"
updateTime: "1779366584000"
---

# 获取妙搭应用可用范围


获取妙搭应用可用范围


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/spark/v1/apps/:app_id/access-scope |
| HTTP Method | GET |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `spark:app.access_scope:read` 获取妙搭应用可用范围 |
| 字段权限要求 | &gt; **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_id` | `string` | 妙搭应用唯一标识，通过应用创建接口或妙搭管理后台获取<br>**示例值**："app_4k6af8utt2s0n" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `scope` | `string` | 当前可见范围类型，枚举值为 All / Tenant / Range |
| &nbsp;&nbsp;└ `users` | `string\[\]` | 仅 Scope=Range 时返回，授权用户 open_id 列表 |
| &nbsp;&nbsp;└ `departments` | `string\[\]` | 仅 Scope=Range 时返回，授权部门 department_id 列表 |
| &nbsp;&nbsp;└ `chats` | `string\[\]` | 仅 Scope=Range 时返回，授权群聊 chat_id 列表 |
| &nbsp;&nbsp;└ `apply_config` | `apply_config` | ApplyConfig 当前申请访问配置（含审批人）；未启用申请时为 nil |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `enabled` | `boolean` | 控制审批流程是否启用。设为true时，提交申请后将触发配置的审批流程；设为false时，申请将直接通过无需审批。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `approvers` | `string\[\]` | 仅支持配置一个用户 open_id |
| &nbsp;&nbsp;└ `require_login` | `boolean` |  |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "scope": "Range",
        "users": [
            "ou_75e71dde59ef1cbbaf25875b20cc54ef"
        ],
        "departments": [
            "od-3f65aa8f59e512bfabde0d71e04c26d7"
        ],
        "chats": [
            "oc_aa8b35fdab3813ef837f91b8ffe61ec6"
        ],
        "apply_config": {
            "enabled": true,
            "approvers": [
                "ou_75e71dde59ef1cbbaf25875b20cc54ef"
            ]
        },
        "require_login": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 3340001 | param is invalid | 输入参数不合法，请检查输入参数 |
| 409 | 3340002 | app not published | 应用尚未发布，请先发布应用后再操作可用范围 |


