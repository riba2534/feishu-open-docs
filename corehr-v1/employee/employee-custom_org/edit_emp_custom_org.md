---
title: "更新人员自定义组织变更记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee-custom_org/edit_emp_custom_org"
updateTime: "1774839439000"
---

# 更新人员自定义组织变更记录

更新指定员工的某一条自定义组织变更记录


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/custom_org/edit_emp_custom_org |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:employment.custom_org:write` 读写员工的自定义组织信息 |
| 字段权限要求 | &gt; **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 是 | 用户 ID 类型<br>**示例值**：people_corehr_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`people_corehr_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id` | `string` | 是 | 用户ID<br>**示例值**："00067" |
| `object_api_name` | `string` | 是 | 自定义组织类型编码<br>**示例值**："custom_org_03" |
| `job_data_custom_org_id` | `string` | 是 | 自定义组织ID<br>**示例值**："7293841029445207596" |
| `version_id` | `string` | 是 | 版本ID<br>**示例值**："7293841029445207593" |
| `custom_org_with_rates` | `custom_org_with_rate\[\]` | 是 | 自定义组织列表<br>**数据校验规则**：<br>- 长度范围：`1` ～ `20` |
| &nbsp;&nbsp;└ `id` | `string` | 是 | 自定义组织id<br>**示例值**："7382048365313261588" |
| &nbsp;&nbsp;└ `rate` | `string` | 否 | 比例<br>**示例值**："50.01" |
| `effective_time` | `string` | 是 | 生效时间<br>**示例值**："2024-06-15" |
| `start_reason` | `string` | 否 | 变更原因<br>**示例值**："编辑雇佣信息的自定义组织"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |


### 请求体示例

```json
{
    "user_id": "00067",
    "object_api_name": "custom_org_03",
    "job_data_custom_org_id": "7293841029445207596",
    "version_id": "7293841029445207593",
    "custom_org_with_rates": [
        {
            "id": "7382048365313261588",
            "rate": "50.01"
        }
    ],
    "effective_time": "2024-06-15",
    "start_reason": "编辑雇佣信息的自定义组织"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `data` | `string` | 添加成功 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "data": "success"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1160001 | param is invalid | 请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |


