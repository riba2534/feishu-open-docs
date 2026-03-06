---
title: "查询规则"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/report/report-v1/rule/query"
updateTime: "1704195335000"
---

# 查询规则

查询规则。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/report/v1/rules/query |
| HTTP Method | GET |
| 接口频率限制 | [特殊频控](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `report:rule:readonly` 查看汇报规则 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `rule_name` | `string` | 是 | 规则名称<br>**示例值**：工作月报 |
| `include_deleted` | `int` | 否 | 是否包括已删除，默认未删除<br>**示例值**：0<br>**可选值有**：<br>- `0`: 不包括已删除 - `1`: 包括已删除<br>**数据校验规则**：<br>- 取值范围：`0` ～ `1` |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `rules` | `rule\[\]` | 规则列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `rule_id` | `string` | 规则唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 规则名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `icon_name` | `string` | 规则图标 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `int` | 创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `creator_user_id` | `string` | 创建人ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `creator_user_name` | `string` | 创建人名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `owner_user_id` | `string` | 规则所有者ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `owner_user_name` | `string` | 规则所有者名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `form_schema` | `form_field\[\]` | 表单定义 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 字段类型<br>**可选值有**：<br>- `text`: 文本 - `number`: 数字 - `dropdown`: 单选 - `image`: 图片 - `attachement`: 附件 - `multiSelect`: 多选 - `address`: 地址 - `datetime`: 时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_deleted` | `int` | 规则是否已删除<br>**可选值有**：<br>- `0`: 未删除 - `1`: 已删除 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `need_report_user_ids` | `string\[\]` | 需要汇报的用户ID列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `need_report_department_ids` | `string\[\]` | 需要汇报的部门ID列表（如果id为0，表示全员） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `need_report_chat_ids` | `string\[\]` | 需要汇报的群ID列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cc_user_ids` | `string\[\]` | 抄送用户ID列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cc_department_ids` | `string\[\]` | 抄送部门ID列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `to_user_ids` | `string\[\]` | 汇报对象用户ID列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `to_chat_ids` | `string\[\]` | 汇报对象群ID列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `to_leaders` | `int\[\]` | 上级汇报对象，0表示第一级，依次类推，最大为5表示第六级 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `to_department_owners` | `int\[\]` | 部门负责人汇报对象，0表示第一级，依次类推，最大为5表示第六级 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `manager_user_ids` | `string\[\]` | 规则管理员用户ID列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cc_chat_ids` | `string\[\]` | 抄送群ID列表 |


### 响应体示例

```json
{"code":0,
"msg":"success",
"data":{"rules":[{"rule_id":"6894788526240432147",
"name":"工作月报",
"icon_name":"日报",
"created_at":1622427266,
"creator_user_id":"ou_133f0b6d0f097cf7d7ba00b38fffb110",
"creator_user_name":"张三",
"owner_user_id":"ou_133f0b6d0f097cf7d7ba00b38fffb111",
"owner_user_name":"张三",
"form_schema":[{
    "name": "ou_133f0b6d0f097cf7d7ba00b38fffb112",
    "type": "张三"
}],
"is_deleted":0,
"need_report_user_ids":["["ou_d6a515a55c77ca0b5b6c6ca0dd628c85","ou_d6a5b5a55c77ca0b5b616c10dd628c55"]"],
"need_report_department_ids":["["od_d6s5b5a55c77ca0b5e6c6ca0dd628c85","od_d6a5b5a55c77ca0b5b6c6ca0dd628c55"]"],
"need_report_chat_ids":["["ou_d6a515a55c77ca0b5b6c6ca0dd628c85","ou_d6a5b5a55c77ca0b5b616ca0dd628c55"]"],
"cc_user_ids":["["ou_d6a5b5a55c77ca0b5b6c6c10dd628c85","ou_d6a5b5a55c77ca0b5b6c6ca0d6628c55"]"],
"cc_department_ids":["["od_d6a5b5a55c77ca0b5e6c6ca0dd628c85","od_d6a5b5a55c77ca0b5b6c6ch0dd628c55"]"],
"to_user_ids":["["ou_d6a5b5a55c77ca0b5b6c6ca0dd628c85","ou_d6a5b5a55c77ca0b5b6c6ca0dd628c55"]"],
"to_chat_ids":["["oc_d6a5b5a55c77ca0b5b6c6ca0fd628c85","oc_d6a5b5a55c77ca0b5b6c1ca0dd628c55"]"],
"to_leaders":[[0,2,3]],
"to_department_owners":[[0,1,2]],
"manager_user_ids":["["ou_d6a5b5a55c77ca0b5b6c6ca0dd628c85","ou_d6a5b5a55c77ca0b5b6c6ca0dd628c55"]"],
"cc_chat_ids":["["oc_d6a5b5a55c77ca0b5b6c6ca0fd628c85","oc_d6a5b5a55c77ca0b5b6c1ca0dd628c55"]"]}]}}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1430001 | tenant key  not exist | 确认参数正确性 |


