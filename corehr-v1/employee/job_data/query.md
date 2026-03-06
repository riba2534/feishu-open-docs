---
title: "获取任职信息列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/employees-job_data/query"
updateTime: "1748347922000"
---

# 获取任职信息列表

获取任职信息列表。


> **Tip**: 该接口会按照应用拥有的「员工资源」的权限范围返回数据，请确定在「开发者后台 - 权限管理 - 数据权限」中已申请「员工资源」权限范围


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/employees/job_datas/query |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:employee.job_data:read` 查看员工的任职信息 `corehr:job_data:read` 查看任职信息 `corehr:job_data:write` 读写任职信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `corehr:employment.job:read` 获取员工的职务信息 `corehr:employment.job_level:read` 获取职务级别信息 `corehr:employment.pathway:read` 获取员工通道信息 `corehr:employment.pathway:write` 读写员工通道 `corehr:employment.position:read` 获取员工的岗位信息 `corehr:employment.position:write` 读写员工的岗位信息 `corehr:job_data.assignment_start_reason:read` 查看任职记录的原因字段 `corehr:employment.job_grade:write` 读写职等信息 `contact:user.employee_id:readonly` 获取用户 user ID `corehr:employment.job_level:write` 读写员工的职务级别信息 `corehr:employment.job_grade:read` 获取职等信息 `corehr:job_data.compensation_type:read` 获取薪资类型 `corehr:job_data.job_data_reason:read` 读取任职原因 `corehr:job_data.service_company:read` 获取任职公司 `corehr:job_data.work_shift:read` 获取排班信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 是 | 分页大小，最大 100<br>**示例值**：100<br>**数据校验规则**：<br>- 取值范围：`1` ～ `100` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：6891251722631890445 |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 此次调用中使用的部门 ID 类型<br>**示例值**：people_corehr_department_id<br>**可选值有**：<br>- `open_department_id`: 以 open_department_id 来标识部门 - `department_id`: 以 department_id 来标识部门 - `people_corehr_department_id`: 以 people_corehr_department_id 来标识部门<br>**默认值**：`people_corehr_department_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `get_all_version` | `boolean` | 否 | 是否获取所有版本的任职记录 - true 为获取员工所有版本的任职记录 - false 为仅获取当前生效的任职记录 - 默认为 false<br>**示例值**：false |
| `data_date` | `string` | 否 | 查看数据日期 - 与时间范围筛选为 AND 关系 - 默认为当天<br>**示例值**："2020-01-01" |
| `effective_date_start` | `string` | 否 | 生效日期 - 搜索范围开始 - 默认为空<br>**示例值**："2020-01-01" |
| `effective_date_end` | `string` | 否 | 生效日期 - 搜索范围结束 - 默认为空<br>**示例值**："2020-01-01" |
| `department_id` | `string` | 否 | 员工当前所在的部门 ID - 类型应与  department_id_type 一致<br>**示例值**："6891251722631890445" |
| `employment_ids` | `string\[\]` | 否 | 员工雇佣 ID 列表 - 类型应与 user_id_type 一致<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| `primary_job_data` | `boolean` | 否 | 是否仅查询主职 - true：仅返回 primary_job_data 为 true 的任职记录 - false：仅返回 primary_job_data 为 false 的任职记录 - 不传：返回全部<br>**示例值**：true |
| `assignment_start_reasons` | `string\[\]` | 否 | 业务类型（原：任职原因） - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：job_data   - custom_api_name：assignment_start_reason<br>**示例值**：["onboarding"]<br>**默认值**：`[]` |


### 请求体示例

```json
{
    "get_all_version": false,
    "data_date": "2020-01-01",
    "effective_date_start": "2020-01-01",
    "effective_date_end": "2020-01-01",
    "department_id": "6891251722631890445",
    "employment_ids": [
        "7140964208476371111"
    ],
    "primary_job_data": true,
    "assignment_start_reasons": [
        "onboarding"
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
| &nbsp;&nbsp;└ `items` | `employee_job_data\[\]` | 任职信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id` | `string` | 员工雇佣 ID - 类型与 user_id_type 一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_datas` | `job_data\[\]` | 任职记录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_data_id` | `string` | 任职信息 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `version_id` | `string` | 任职记录版本 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type_id` | `string` | 人员类型 ID，可通过[【查询单个人员类型】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `working_hours_type_id` | `string` | 工时制度 ID，可通过[【查询单个工时制度】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `work_location_id` | `string` | 工作地点 ID，可通过[【查询单个地点】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 部门 ID，可通过[【批量查询部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)接口查询详细信息 - 与 department_id_type 类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `position_id` | `string` | 岗位 ID - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**字段权限要求（满足任一）**： `corehr:employment.position:read` 获取员工的岗位信息 `corehr:employment.position:write` 读写员工的岗位信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_id` | `string` | 职务 ID，可通过[【查询单个职务】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job/get)获取详细信息<br>**字段权限要求（满足任一）**： `corehr:employment.job:read` 获取员工的职务信息 `corehr:employment.job_level:read` 获取职务级别信息 `corehr:employment.job_level:write` 读写员工的职务级别信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_level_id` | `string` | 职级 ID，可通过[【查询单个职级】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/get)获取详细信息<br>**字段权限要求（满足任一）**： `corehr:employment.job_level:read` 获取职务级别信息 `corehr:employment.job_level:write` 读写员工的职务级别信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_grade_id` | `string` | 职等 ID，可通过[【查询职等】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)获取详细信息<br>**字段权限要求（满足任一）**： `corehr:employment.job_grade:read` 获取职等信息 `corehr:employment.job_grade:write` 读写职等信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id` | `string` | 序列 ID，可通过[【查询单个序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `probation_start_date` | `string` | 试用期开始日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `probation_end_date` | `string` | 试用期结束日期（实际结束日期） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `primary_job_data` | `boolean` | 是否为主任职 - true：主职 - false：兼职，建议使用兼职相关接口 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id` | `string` | 雇佣 ID，可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取详细信息<br>- 与 user_id_type 类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 任职记录版本的生效时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 任职记录版本的失效时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `assignment_start_reason` | `enum` | 业务类型（原：任职原因） - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：job_data   - custom_api_name：assignment_start_reason<br>**字段权限要求**： `corehr:job_data.assignment_start_reason:read` 查看任职记录的原因字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `probation_expected_end_date` | `string` | 预计试用期结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `probation_outcome` | `enum` | 试用期结果 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：job_data   - custom_api_name：probation_outcome |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `direct_manager` | `basic_job_data` | 直属上级 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_data_id` | `string` | 任职信息 ID，可通过[【查询单个任职信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_data/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id` | `string` | 雇佣 ID，可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取详细信息<br>- 与 user_id_type 类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dotted_line_managers` | `basic_job_data\[\]` | 虚线上级 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_data_id` | `string` | 任职信息 ID，可通过[【查询单个任职信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_data/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id` | `string` | 雇佣 ID，可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取详细信息 - 与 user_id_type 类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `second_direct_manager` | `basic_job_data` | 第二实线主管 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_data_id` | `string` | 任职信息 ID，可通过[【查询单个任职信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_data/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id` | `string` | 雇佣 ID，可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取详细信息 - 与 user_id_type 类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_rates` | `job_data_cost_center\[\]` | 成本中心分摊信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_id` | `string` | 成本中心 ID，可以通过[搜索成本中心信息](https://open.feishu.cn/document/server-docs/corehr-v1/organization-management/cost_center/search)接口获取对应的成本中心信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rate` | `int` | 分摊比例(整数) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `new_rate` | `number(float)` | 分摊比例 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `work_shift` | `enum` | 排班类型，可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下： - object_api_name = "job_data" - custom_api_name = "work_shift"<br>**字段权限要求**： `corehr:job_data.work_shift:read` 获取排班信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `compensation_type` | `enum` | 薪资类型，可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下： - object_api_name = "job_data" - custom_api_name = "compensation_type"<br>**字段权限要求**： `corehr:job_data.compensation_type:read` 获取薪资类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `service_company` | `string` | 任职公司，可通过[【查询单个公司】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/get)获取详细信息<br>**字段权限要求**： `corehr:job_data.service_company:read` 获取任职公司 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `weekly_working_hours_v2` | `number(float)` | 周工作时长 V2 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `weekly_working_hours` | `int` | 周工作时长 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employee_subtype_id` | `string` | 人员子类型 ID - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_data_reason` | `enum` | 任职原因 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name = "job_data"   - custom_api_name = "job_data_reason"<br>**字段权限要求**： `corehr:job_data.job_data_reason:read` 读取任职原因 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pathway_id` | `string` | 通道 ID<br>**字段权限要求（满足任一）**： `corehr:employment.pathway:read` 获取员工通道信息 `corehr:employment.pathway:write` 读写员工通道 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "employment_id": "6893014062142064135",
                "job_datas": [
                    {
                        "job_data_id": "6890452208593372679",
                        "version_id": "6890452208593372697",
                        "employee_type_id": "6890452208593372679",
                        "working_hours_type_id": "6890452208593372679",
                        "work_location_id": "6890452208593372679",
                        "department_id": "6890452208593372679",
                        "position_id": "6890452208593372679",
                        "job_id": "6890452208593372679",
                        "job_level_id": "6890452208593372679",
                        "job_grade_id": "6890452208593372679",
                        "job_family_id": "1245678",
                        "probation_start_date": "2018-03-16T00:00:00",
                        "probation_end_date": "2019-05-24T00:00:00",
                        "primary_job_data": true,
                        "employment_id": "6893014062142064135",
                        "effective_time": "2020-05-01 00:00:00",
                        "expiration_time": "2020-05-02 00:00:00",
                        "assignment_start_reason": {
                            "enum_name": "onboarding",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        },
                        "probation_expected_end_date": "2006-01-02",
                        "probation_outcome": {
                            "enum_name": "example",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        },
                        "direct_manager": {
                            "job_data_id": "1000000",
                            "employment_id": "6893014062142064135"
                        },
                        "dotted_line_managers": [
                            {
                                "job_data_id": "1000000",
                                "employment_id": "6893014062142064135"
                            }
                        ],
                        "second_direct_manager": {
                            "job_data_id": "1000000",
                            "employment_id": "6893014062142064135"
                        },
                        "cost_center_rates": [
                            {
                                "cost_center_id": "6950635856373745165",
                                "rate": 100,
                                "new_rate": 50.2
                            }
                        ],
                        "work_shift": {
                            "enum_name": "example",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        },
                        "compensation_type": {
                            "enum_name": "example",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        },
                        "service_company": "6890452208593372680",
                        "weekly_working_hours_v2": 10.1,
                        "weekly_working_hours": 10,
                        "employee_subtype_id": "6890452208593372680",
                        "job_data_reason": {
                            "enum_name": "example_option",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "晋升"
                                }
                            ]
                        },
                        "pathway_id": "6890452208593372679"
                    }
                ]
            }
        ],
        "page_token": "eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0=",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1160013 | Param is invalid | 请检查参数格式是否错误 |
| 400 | 1160018 | AppID or LarkTenantID missing | 请检查 AppID 或 LarkTenantID 是否填写 |
| 400 | 1160023 | No authority error | 请检查是否有权限 |
| 500 | 1160999 | unknown error | 请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 500 | 1160997 | Unknown meta rpc error | 请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 500 | 1160998 | Unknown vault rpc error | 请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |


