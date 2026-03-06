---
title: "批量查询部门调整内容"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/approval_groups/open_query_department_change_list_by_ids"
updateTime: "1763528815000"
---

# 批量查询部门调整内容

根据部门调整记录 ID 批量查询部门调整内容，如：部门调整类型、部门调整前后名称、部门调整前后角色信息 等


> **Warning**: - 延迟说明：数据库主从延迟2s以内，即：用户接收到流程状态变更消息后2s内调用此接口可能查询不到数据。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/approval_groups/open_query_department_change_list_by_ids |
| HTTP Method | POST |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:approval_groups.orgdraft_department_change:read` 获取组织架构调整部门调整内容 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID `corehr:orgrole_info:read` 获取组织角色 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `process_id` | `string` | 是 | 组织架构调整流程 ID， 用户通过『飞书人事-我的团队-组织架构』或『飞书 人事-人员管理-组织架构』 发起一个组织架构调整，并提交审批后，系统会根据管理员在审批流程中配置的规则，生成 一个或多个审批单据。<br>**示例值**：6893014062142064211 |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 此次调用中使用的部门 ID 类型<br>**示例值**：open_department_id<br>**可选值有**：<br>- `open_department_id`: 以 open_department_id 来标识部门 - `department_id`: 以 department_id 来标识部门 - `people_corehr_department_id`: 以 people_corehr_department_id 来标识部门<br>**默认值**：`open_department_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `department_change_ids` | `string\[\]` | 否 | 部门调整记录 ID 列表。调整记录详情可通过[【根据流程 ID 查询组织架构调整记录】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/approval_groups/get) 获取。  - 必须是查询参数process_id对应的流程下的部门调整记录ID。 - 未设置时查询到的部门调整记录为空。 - 返回的变更 ID 类型与 查询参数中的```department_id_type``` 一致。  <br>**示例值**：["6893014064442064111"]<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` |
| `need_department_path` | `boolean` | 否 | 是否返回部门全路径， 用于在组织架构调整中级联创建部门的场景， 由于上级部门还未生效， 因此返回全路径用于数据查询。<br>**示例值**：false<br>**默认值**：`false` |


### 请求体示例

```json
{
    "department_change_ids": [
        "6893014064442064111"
    ],
    "need_department_path": false
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `department_changes` | `department_change\[\]` | 部门调整记录信息列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_change_id` | `string` | 关联的部门调整记录 ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 部门 ID，对于在本次调整中新建的部门，在调整未生效时将返回为空。支持根据部门 ID 类型转换。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `draft_department_id` | `string` | 调整过程部门 ID 。固定返回people_corehr_department_id，不会根据部门 ID 类型进行转换。对于在本次调整中新建的部门，在调整未生效前会返回格式为 td_xxx 的过程部门 ID，生效后(数据写入成功，非部门生效状态)将返回正式的people_corehr_department_id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_change_type` | `string` | 调整类型<br>**可选值有**：<br>- `Unknown`: 未知 - `Create`: 新建 - `Modify`: 编辑 - `Inactive`: 停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_change_status` | `int` | 调整状态<br>**可选值有**：<br>- `0`: 发起审批，流程成功发起，并等待审批人审批。 - `1`: 审批通过。 - `2`: 审批被拒绝，审批未通过。 - `3`: 审批被撤销，用户主动撤销审批，调整会进入已撤销状态。 - `4`: 执行成功，调整已经执行成功。 - `5`: 执行失败，调整已经执行失败。 - `6`: 待执行，调整依赖其他流程完成，等待执行。字节租户或者商业化租户且配置拆分审批流(合单) 才会触发，调整所在审批单执行生效依赖另一个同时发起的还处于审批中状态审批单的执行结果。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `reorganization_info` | `reorganization_info` | 调整详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `original_department_names` | `i18n\[\]` | 原部门名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `target_department_names` | `i18n\[\]` | 调整后部门名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `original_department_code` | `string` | 原部门编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `target_department_code` | `string` | 调整后部门编码，  在新建部门场景下， 如果租户开通部门自动编码，该编码会为空值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `original_sub_type` | `enum` | 原部门类型，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)部门子类型（department_sub_type）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `target_sub_type` | `enum` | 调整后部门类型，枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)部门子类型（department_sub_type）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `original_department_manager` | `string` | 原部门负责人，详细信息可通过[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `target_department_manager` | `string` | 调整后部门负责人， 详细信息可通过[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `original_descriptions` | `i18n\[\]` | 原描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `target_descriptions` | `i18n\[\]` | 调整后描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `original_cost_center` | `cost_center` | 原默认成本中心 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_id` | `string` | 成本中心ID，可以通过[【搜索成本中心信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获取对应的成本中心信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_version_id` | `string` | 成本中心版本ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 成本中心名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码， 成本中心编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `parent_cost_center_id` | `string` | 上级成本中心ID，可以通过[【搜索成本中心信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获取对应的成本中心信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `managers` | `string\[\]` | 成本中心负责人ID 列表，详细信息可通过[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 成本中心描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 生效时间 - 日期格式： YYYY-MM-DD - 最小值： 1900-01-01 - 最大值：9999-12-31 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 过期时间 - 日期格式： YYYY-MM-DD - 最小值： 1900-01-01 - 最大值：9999-12-31 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 当前实体是否启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `operation_reason` | `string` | 操作原因 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `target_cost_center` | `cost_center` | 调整后默认成本中心 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_id` | `string` | 成本中心ID，可以通过[【搜索成本中心信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获取对应的成本中心信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_version_id` | `string` | 成本中心版本ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 成本中心名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `parent_cost_center_id` | `string` | 上级成本中心ID，可以通过[【搜索成本中心信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获取对应的成本中心信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `managers` | `string\[\]` | 成本中心负责人ID 列表，详细信息可通过[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 成本中心描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 生效时间 - 日期格式： YYYY-MM-DD - 最小值： 1900-01-01 - 最大值：9999-12-31 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 过期时间 - 日期格式： YYYY-MM-DD - 最小值： 1900-01-01 - 最大值：9999-12-31 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 当前实体是否启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `operation_reason` | `string` | 操作原因 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `original_is_confidential` | `boolean` | 原是否保密 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `target_is_confidential` | `boolean` | 调整后是否保密 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `original_staffing_mode_option` | `enum` | 原岗职模式 - 可通过[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)查询获取。请求参数：object_api_name=department；custom_api_name=staffing_model。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `target_staffing_mode_option` | `enum` | 调整后岗职模式 - 可通过[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)查询获取。请求参数：object_api_name=department；custom_api_name=staffing_model。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `original_parent_department_id` | `string` | 原上级部门 ID，支持根据部门 ID 类型转换 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `target_parent_department_id` | `string` | 调整后上级部门 ID，对于在本次调整中新建的部门，在调整未生效时将返回为空。支持根据部门 ID 类型转换。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `draft_target_parent_department_id` | `string` | 调整后上级部门过程 ID 。固定返回people_corehr_department_id，不会根据部门 ID 类型进行转换。对于在本次调整中新建的部门，在调整未生效前会返回格式为 td_xxx 的过程部门 ID，生效后将返回正式的people_corehr_department_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `original_department_id_path` | `orgdraft_department_id\[\]` | 原部门全路径，从根部门开始自上而下返回部门 ID 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 部门 ID ，对于在本次调整中新建的部门，在调整未生效时将返回为空。支持根据部门 ID 类型转换。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `draft_department_id` | `string` | 调整过程部门 ID ，固定返回people_corehr_department_id，不会根据部门 ID 类型进行转换。对于在本次调整中新建的部门，在调整未生效前会返回格式为 td_xxx 的过程部门 ID，生效后将返回正式的people_corehr_department_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `target_department_id_path` | `orgdraft_department_id\[\]` | 调整后部门全路径，从根部门开始自上而下返回部门 ID 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 部门 ID ，对于在本次调整中新建的部门，在调整未生效时将返回为空。支持根据部门 ID 类型转换 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `draft_department_id` | `string` | 调整过程部门 ID ，固定返回people_corehr_department_id，不会根据部门 ID 类型进行转换。对于在本次调整中新建的部门，在调整未生效前会返回格式为 td_xxx 的临时部门 ID，生效后将返回正式的people_corehr_department_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `change_field_pair\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `origin_value` | `custom_field_data` | 调整前 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型，详细见[获取自定义字段列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同。如：```("\"123\"", "\"123.23\"", "\"true\"", [\"id1\",\"id2\"], \"2006-01-02 15:04:05\")``` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `target_value` | `custom_field_data` | 调整后 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型，详细见[获取自定义字段列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同。如：```("\"123\"", "\"123.23\"", "\"true\"", [\"id1\",\"id2\"], \"2006-01-02 15:04:05\")``` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `orgrole_infos` | `orgrole_info\[\]` | 调整前后组织角色信息<br>**字段权限要求**： `corehr:orgrole_info:read` 获取组织角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `role_id` | `string` | 角色ID - 通过[【批量获取角色列表】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/security_group/list)获取角色其他信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `origin_orgroles` | `orgdraft_orgrole_assignment\[\]` | 原组织角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `grantee_id` | `string` | 授权用户id - 通过[【批量获取员工信息】](	https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/directory-v1/employee/mget)获取员工其他信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `management_scopes` | `orgrole_assignment.org\[\]` | 管理范围，组织角色为交叉角色时有值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `org_id` | `string` | 组织ID - 当org_type为location时，可以通过[【通过地点 ID 批量获取地点信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/location/batch_get)获取地点的其他信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `org_type` | `string` | 组织类型<br>**可选值有**：<br>- `department`: 部门 - `location`: 地点 - `custom_org_01`: 自定义组织 - `custom_org_02`: 自定义组织 - `custom_org_03`: 自定义组织 - `custom_org_04`: 自定义组织 - `custom_org_05`: 自定义组织 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `org_name` | `string` | 组织名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `target_orgroles` | `orgdraft_orgrole_assignment\[\]` | 新组织角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `grantee_id` | `string` | 授权用户id - 通过[【批量获取员工信息】](	https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/directory-v1/employee/mget)获取员工其他信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `management_scopes` | `orgrole_assignment.org\[\]` | 管理范围，组织角色为交叉角色时有值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `org_id` | `string` | 组织ID - 当org_type为location时，可以通过[【通过地点 ID 批量获取地点信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/location/batch_get)获取地点的其他信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `org_type` | `string` | 组织类型<br>**可选值有**：<br>- `department`: 部门 - `location`: 地点 - `custom_org_01`: 自定义组织 - `custom_org_02`: 自定义组织 - `custom_org_03`: 自定义组织 - `custom_org_04`: 自定义组织 - `custom_org_05`: 自定义组织 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `org_name` | `string` | 组织名称 |


### 响应体示例

```json
{
	"code": 0,
	"msg": "success",
	"data": {
		"department_changes": [{
			"department_change_id": "6991776076699549697",
			"department_id": "6966236934218579208",
			"draft_department_id": "3346236933198579208",
			"department_change_type": "Modify",
			"reorganization_info": {
				"original_department_names": [{
					"lang": "zh-CN",
					"value": "技术研发部"
				}],
				"target_department_names": [{
					"lang": "zh-CN",
					"value": "产品技术中心"
				}],
				"original_department_code": "D00000456",
				"target_department_code": "D00000456",
				"original_sub_type": {
					"enum_name": "division",
					"display": [{
						"lang": "zh-CN",
						"value": "系"
					}]
				},
				"target_sub_type": {
					"enum_name": "department",
					"display": [{
						"lang": "zh-CN",
						"value": "部门"
					}]
				},
				"original_department_manager": "6974648866876573198",
				"target_department_manager": "7013328578351842852",
				"original_descriptions": [{
					"lang": "zh-CN",
					"value": "负责公司核心系统的技术研发与维护，专注于后端架构搭建和性能优化"
				}],
				"target_descriptions": [{
					"lang": "zh-CN",
					"value": "统筹产品设计与技术研发工作，涵盖从需求分析到系统落地的全流程，推动产品技术一体化发展"
				}],
				"original_cost_center": {
					"cost_center_id": "6969828847121885087",
					"name": [{
						"lang": "zh-CN",
						"value": "研发成本中心 - 001"
					}]
				},
				"target_cost_center": {
					"cost_center_id": "696982884876585087",
					"name": [{
						"lang": "zh-CN",
						"value": "产品技术成本中心 - 002"
					}]
				},
				"original_is_confidential": true,
				"target_is_confidential": true,
				"original_parent_department_id": "6974659700705068581",
				"target_parent_department_id": "69746597007987678581",
				"draft_target_parent_department_id": "6966236933198579208",
				"original_department_id_path": [{
					"department_id": "6974612300705068581",
					"draft_department_id": "6974655643205068581"
				}],
				"target_department_id_path": [{
					"department_id": "6974634700705068581",
					"draft_department_id": "6974659700705068581"
				}],
				"original_staffing_mode_option": {
					"enum_name": "job",
					"display": [{
						"lang": "zh-CN",
						"value": "职务模式"
					}]
				},
				"target_staffing_mode_option": {
					"enum_name": "position",
					"display": [{
						"lang": "zh-CN",
						"value": "岗位模式"
					}]
				},
				"custom_fields": [{
					"origin_value": {
						"custom_api_name": "name",
						"name": {
							"zh_cn": "自定义姓名",
							"en_us": "Custom Name"
						},
						"type": 1,
						"value": "\"231\""
					},
					"target_value": {
						"custom_api_name": "name",
						"name": {
							"zh_cn": "自定义姓名",
							"en_us": "Custom Name"
						},
						"type": 1,
						"value": "\"231\""
					}
				}]
			}
		}]
	}
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 200 | 1162001 | Approval process not found | 审批流未找到。请检查审批流 ID 是否正确 |
| 200 | 1161000 | Adjustment draft not found | 调整草稿未找到。请检查部门调整记录 ID 是否正确 |


