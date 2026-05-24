---
title: "取消用户迁移"
fullPath: "/uAjLw4CM/ukTMukTMukTM/security_and_compliance-v1/user_migration/cancel"
updateTime: "1773718666000"
---

# 取消用户迁移任务

取消用户迁移任务，仅能对未启动迁移的用户做此操作。用户迁移状态可通过「获取单个用户迁移状态」查询。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/security_and_compliance/v1/user_migrations/cancel |
| HTTP Method | POST |
| 接口频率限制 | [10 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `security_and_compliance:user_migration` 创建、更新用户数据迁移 `security_and_compliance:user_migration:multi-geo` 查询、更新员工的数据驻留地 |
| 字段权限要求 | &gt; **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 是 | 用户 ID 类型<br>**示例值**：user_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_ids` | `string\[\]` | 是 | 取消迁移用户 ID 列表<br>**示例值**：["7064408494200487xxx"]<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` |


### 请求体示例

```json
{
    "user_ids": [
        "7064408494200487xxx"
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
| 400 | 1781001 | Invalid request parameter | 修正请求参数 |
| 403 | 1781002 | The operator has no permission to operate the data residency service | 操作人没有数据驻留服务操作权限。请在管理员后台为操作人开通权限，参考[管理员创建管理员角色及分配权限](https://www.feishu.cn/hc/zh-CN/articles/360043495213) |
| 400 | 1781003 | The tenant has not activated the data service | 租户未开通数据服务，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)开通「数据驻留服务」 |
| 500 | 1782001 | Internal server error | 服务器内部错误，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 500 | 1782002 | User migration task does not exist | 用户迁移不存在。请检查用户 ID 是否正确填写，如仍有疑虑请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 500 | 1783001 | The user migration task cannot be cancelled | 用户已被迁移至目标地理位置。如确需取消，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 500 | 1782004 | The system or other user is operating on the user specified in the request | 请稍后重试 |


