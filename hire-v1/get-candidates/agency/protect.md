---
title: "设置猎头保护期"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/agency/protect"
updateTime: "1724725389000"
---

# 设置猎头保护期

设置指定人才的猎头保护期，当「飞书招聘」内置的保护期功能不满足需求时，客户可通过此接口自定义人才的保护期。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/agencies/protect |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:agency` 更新招聘猎头信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_admin_id`: 以people_admin_id来识别用户<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `talent_id` | `string` | 是 | 人才ID，可通过[通过手机号或邮箱获取人才 ID](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/batch_get_id)、[获取人才列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/list)接口获取<br>**示例值**："6962051712422398239" |
| `supplier_id` | `string` | 是 | 猎头供应商ID<br>**示例值**："6898173495386147079" |
| `consultant_id` | `string` | 是 | 猎头顾问ID，需与`user_id_type`类型一致<br>**示例值**："ou_f476cb099ac9227c9bae09ce46112579" |
| `protect_create_time` | `int` | 是 | 保护期创建时间（int64类型），毫秒时间戳<br>**示例值**：1610695587000 |
| `protect_expire_time` | `int` | 是 | 保护期过期时间（int64类型），毫秒时间戳<br>**示例值**：1626333987000 |
| `comment` | `string` | 否 | 推荐语<br>**示例值**："此候选人非常优秀，建议录用。" |
| `current_salary` | `string` | 否 | 当前薪资<br>**示例值**："15k * 13" |
| `expected_salary` | `string` | 否 | 预期薪资<br>**示例值**："18k * 16" |


### 请求体示例

```json
{
    "talent_id": "6962051712422398239",
    "supplier_id": "6898173495386147079",
    "consultant_id": "ou_f476cb099ac9227c9bae09ce46112579",
    "protect_create_time": 1610695587000,
    "protect_expire_time": 1626333987000,
    "comment": "此候选人非常优秀，建议录用。",
    "current_salary": "15k * 13",
    "expected_salary": "18k * 16"
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
    "msg": "ok",
    "data": {}
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |


