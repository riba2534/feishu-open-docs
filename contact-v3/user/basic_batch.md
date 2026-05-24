---
title: "通过 ID 获取用户姓名"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/basic_batch"
updateTime: "1773746788000"
---

# 获取用户姓名

根据用户 ID 获取用户姓名，仅返回核心信息（姓名），不含扩展字段及敏感信息。


> **Warning**: 本接口不校验[通讯录授权范围](https://open.larkoffice.com/document/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)，将直接根据传入的用户 ID 返回对应基础信息（姓名），不受数据权限范围限制。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/contact/v3/users/basic_batch |
| HTTP Method | POST |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `contact:user.basic_profile:readonly` 获取用户的基本信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_ids` | `string\[\]` | 是 | 用户 ID。ID 类型与查询参数 `user_id_type` 保持一致。<br>**示例值**：["ou_b3b46653c99f1f6177a478974bdabb72"]<br>**数据校验规则**：<br>- 长度范围：`1` ～ `10` |


### 请求体示例

```json
{
    "user_ids": [
        "ou_b3b46653c99f1f6177a478974bdabb72"
    ]
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `users` | `basic_user\[\]` | 用户信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `i18n_name` | 用户国际化名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 日文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "users": [
            {
                "user_id": "ou_b3b46653c99f1f6177a478974bdabb72",
                "name": "张三",
                "i18n_name": {
                    "zh_cn": "张三",
                    "ja_jp": "佐藤はるか",
                    "en_us": "Jason Zhang"
                }
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 40001 | param is invalid | 参数错误，请对照接口文档修改输入参数后重试。 |


