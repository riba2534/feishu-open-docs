---
title: "创建外派信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/employees-international_assignment/create"
updateTime: "1749438625000"
---

# 创建外派

为员工添加外派记录，包括外派信息、任职信息


> **Tip**: - 文档中的必填字段，不可为空。
> - 部门岗职模式，会影响岗位、职务等字段的必填校验
> - 外派信息相关字段，会基于【飞书人事-人员档案配置】进行必填校验


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/employees/international_assignments |
| HTTP Method | POST |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:employees.international_assignment:write` 读写外派信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID `corehr:employment.international_assignment.compensation_type:write` 读写外派薪资类型 `corehr:employment.international_assignment.custom_field:write` 读写外派自定义字段 `corehr:employment.international_assignment.job:write` 读写外派职务 `corehr:employment.international_assignment.job_grade:write` 读写外派职等 `corehr:employment.international_assignment.job_level:write` 读写外派职级 `corehr:employment.international_assignment.position:write` 读写外派岗位 `corehr:employment.international_assignment.service_company:write` 读写外派公司 `corehr:employment.international_assignment.weekly_working_hours:write` 读写外派周工作时长 `corehr:employment.international_assignment.work_calendar:write` 读写外派工作日历 `corehr:employment.international_assignment.work_location:write` 读写外派地点 `corehr:employment.international_assignment.work_shift:write` 读写外派排班类型 `corehr:employment.international_assignment.working_hours_type:write` 读写外派工时制度 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `client_token` | `string` | 否 | 幂等标识，服务端会忽略 client_token 重复的请求<br>**示例值**：12454646<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` 字符 |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 此次调用中使用的部门 ID 类型<br>**示例值**：open_department_id<br>**可选值有**：<br>- `open_department_id`: 以 open_department_id 来标识部门 - `department_id`: 以 department_id 来标识部门 - `people_corehr_department_id`: 以 people_corehr_department_id 来标识部门<br>**默认值**：`open_department_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_location_id` | `string` | 是 | 外派工作地点 ID   - 可通过[【批量查询地点】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)获取，并选择【地点用途】为外派地点（international_assignment）的记录<br>**示例值**："7127921432117937708" |
| `service_company` | `string` | 否 | 外派任职公司 ID - 可通过[【批量查询公司】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)获取<br>**示例值**："7127921432117937708" |
| `work_shift` | `string` | 否 | 排班类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：job_data   - custom_api_name：work_shift<br>**示例值**："work_shift" |
| `weekly_working_hours_v2` | `number(float)` | 否 | 周工作时长 - 限制两位小数<br>**示例值**：8<br>**数据校验规则**：<br>- 取值范围：`0` ～ `168` |
| `working_hours_type_id` | `string` | 否 | 工时制度ID -  可通过[【批量查询工时制度】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/list)获取<br>**示例值**："7127921432117937708" |
| `employee_type_id` | `string` | 否 | 人员类型ID - 可通过[【批量查询人员类型】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/list)获取<br>**示例值**："7127921432117937708" |
| `department_id` | `string` | 否 | 部门 ID - 可通过[【批量查询部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)获取 - 类型与 department_id_type 一致<br>**示例值**："7127921432117937708" |
| `job_id` | `string` | 否 | 职务 ID - 可通过[【批量查询职务】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/list)获取<br>**示例值**："7127921432117937708" |
| `job_family_id` | `string` | 否 | 序列 ID - 可通过[【批量查询序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/list)获取<br>**示例值**："7127921432117937708" |
| `job_level_id` | `string` | 否 | 职级 ID - 可通过[【批量查询职级】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/list)获取<br>**示例值**："7127921432117937708" |
| `job_grade_id` | `string` | 否 | 职等 ID - 可通过[【查询职等】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)获取<br>**示例值**："7127921432117937708" |
| `compensation_type` | `string` | 否 | 薪资类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：job_data   - custom_api_name：compensation_type<br>**示例值**："daily" |
| `direct_manager_id` | `string` | 否 | 直属上级雇佣 ID - 可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取 - 类型与 user_id_type 一致<br>**示例值**："7127921432117937708" |
| `dotted_line_manager_id` | `string` | 否 | 虚线上级雇佣 ID - 可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取 - 类型与 user_id_type 一致<br>**示例值**："7127921432117937708" |
| `work_calendar_id` | `string` | 否 | 工作日历 ID - 可通过[【查询工作日历】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/leave/work_calendar)获取<br>**示例值**："7127921432117937708" |
| `position_id` | `string` | 否 | 岗位 ID - 功能灰度中，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**示例值**："7127921432117937708" |
| `employment_id` | `string` | 是 | 雇佣 ID - 可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取 - 类型与 user_id_type 一致 - 需要是在职人员的雇佣 ID<br>**示例值**："7127921432117937708" |
| `custom_fields` | `object_field_data\[\]` | 否 | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**数据校验规则**：<br>- 长度范围：`0` ～ `180` |
| &nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："name" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(123, 123.23, true, [\"id1\",\"id2\], 2006-01-02 15:04:05])<br>**示例值**："Sandy" |
| `international_assignment_reason` | `string` | 否 | 外派原因说明<br>**示例值**："xxx 项目派遣"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `5000` 字符 |
| `description` | `string` | 否 | 备注<br>**示例值**："xxx 项目"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `10000` 字符 |
| `international_assignment_expected_end_date` | `string` | 否 | 预计结束日期 - 格式：yyyy-mm-dd<br>**示例值**："2024-01-02" |
| `international_assignment_type` | `string` | 是 | 外派类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：international_assignment   - custom_api_name：international_assignment_type<br>**示例值**："global_assignment" |
| `effective_time` | `string` | 是 | 开始日期 - 格式：yyyy-mm-dd<br>**示例值**："2024-01-02" |
| `expiration_time` | `string` | 否 | 结束日期 - 格式：yyyy-mm-dd<br>**示例值**："2024-01-02" |


### 请求体示例

```json
{
    "work_location_id": "7127921432117937708",
    "service_company": "7127921432117937708",
    "work_shift": "work_shift",
    "weekly_working_hours_v2": 8,
    "working_hours_type_id": "7127921432117937708",
    "employee_type_id": "7127921432117937708",
    "department_id": "7127921432117937708",
    "job_id": "7127921432117937708",
    "job_family_id": "7127921432117937708",
    "job_level_id": "7127921432117937708",
    "job_grade_id": "7127921432117937708",
    "compensation_type": "daily",
    "direct_manager_id": "7127921432117937708",
    "dotted_line_manager_id": "7127921432117937708",
    "work_calendar_id": "7127921432117937708",
    "position_id": "7127921432117937708",
    "employment_id": "7127921432117937708",
    "custom_fields": [
        {
            "field_name": "name",
            "value": "Sandy"
        }
    ],
    "international_assignment_reason": "xxx 项目派遣",
    "description": "xxx 项目",
    "international_assignment_expected_end_date": "2024-01-02",
    "international_assignment_type": "global_assignment",
    "effective_time": "2024-01-02",
    "expiration_time": "2024-01-02"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `international_assignment` | `employees.international_assignment_resp` | 外派信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_location_id` | `string` | 外派工作地点 ID   - 可通过[【查询单个地点】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/get)获取详细信息<br>**字段权限要求**： `corehr:employment.international_assignment.work_location:write` 读写外派地点 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `service_company` | `string` | 外派任职公司 ID - 可通过[【查询单个公司】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/get)获取详细信息<br>**字段权限要求**： `corehr:employment.international_assignment.service_company:write` 读写外派公司 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_shift` | `enum` | 排班类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：job_data   - custom_api_name：work_shift<br>**字段权限要求**： `corehr:employment.international_assignment.work_shift:write` 读写外派排班类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `working_hours_type_id` | `string` | 工时制度ID -  可通过[【查询单个工时制度】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/get)获取详细信息<br>**字段权限要求**： `corehr:employment.international_assignment.working_hours_type:write` 读写外派工时制度 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type_id` | `string` | 人员类型ID - 可通过[【查询单个人员类型】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `weekly_working_hours_v2` | `number(float)` | 周工作时长<br>**字段权限要求**： `corehr:employment.international_assignment.weekly_working_hours:write` 读写外派周工作时长 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 部门 ID - 可通过[【查询单个部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)获取详细信息 - 类型与 department_id_type 一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_id` | `string` | 职务 ID - 可通过[【查询单个职务】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job/get)获取详细信息<br>**字段权限要求**： `corehr:employment.international_assignment.job:write` 读写外派职务 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id` | `string` | 序列 ID - 可通过[【查询单个序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/get)获取详细信息<br>**字段权限要求**： `corehr:employment.international_assignment.job_level:write` 读写外派职级 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_level_id` | `string` | 职级 ID - 可通过[【查询单个职级】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_grade_id` | `string` | 职等 ID - 可通过[【查询职等】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)获取详细信息<br>**字段权限要求**： `corehr:employment.international_assignment.job_grade:write` 读写外派职等 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `compensation_type` | `enum` | 薪资类型  - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：job_data   - custom_api_name：compensation_type<br>**字段权限要求**： `corehr:employment.international_assignment.compensation_type:write` 读写外派薪资类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `direct_manager_id` | `string` | 直属上级雇佣 ID - 可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取详细信息 - 类型与 user_id_type 一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dotted_line_manager_id` | `string` | 虚线上级雇佣 ID - 可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取详细信息 - 类型与 user_id_type 一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_calendar_id` | `string` | 工作日历 ID - 可通过[【查询工作日历】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/leave/work_calendar)获取详细信息<br>**字段权限要求**： `corehr:employment.international_assignment.work_calendar:write` 读写外派工作日历 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `position_id` | `string` | 岗位 ID - 功能灰度中，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**字段权限要求**： `corehr:employment.international_assignment.position:write` 读写外派岗位 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id` | `string` | 雇佣 ID - 可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取详细信息 - 类型与 user_id_type 一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**字段权限要求**： `corehr:employment.international_assignment.custom_field:write` 读写外派自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(123, 123.23, true, [\"id1\",\"id2\], 2006-01-02 15:04:05]) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `international_assignment_reason` | `string` | 外派原因说明 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 备注 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `international_assignment_expected_end_date` | `string` | 预计结束日期 - 格式：yyyy-mm-dd |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `international_assignment_status` | `enum` | 外派状态 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：international_assignment   - custom_api_name：international_assignment_status |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `international_assignment_type` | `enum` | 外派类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：international_assignment   - custom_api_name：international_assignment_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 开始日期 - 格式：yyyy-mm-dd |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 结束日期 - 格式：yyyy-mm-dd - 在外派未结束时，该值默认为 9999-12-31 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 外派ID |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "international_assignment": {
            "work_location_id": "7127921432117937708",
            "service_company": "7127921432117937708",
            "work_shift": {
                "enum_name": "phone_type",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ]
            },
            "working_hours_type_id": "7127921432117937708",
            "employee_type_id": "7127921432117937708",
            "weekly_working_hours_v2": 8,
            "department_id": "7127921432117937708",
            "job_id": "7127921432117937708",
            "job_family_id": "7127921432117937708",
            "job_level_id": "7127921432117937708",
            "job_grade_id": "7127921432117937708",
            "compensation_type": {
                "enum_name": "phone_type",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ]
            },
            "direct_manager_id": "7127921432117937708",
            "dotted_line_manager_id": "7127921432117937708",
            "work_calendar_id": "7127921432117937708",
            "position_id": "7127921432117937708",
            "employment_id": "7127921432117937708",
            "custom_fields": [
                {
                    "field_name": "name",
                    "value": "Sandy"
                }
            ],
            "international_assignment_reason": "xxx 项目派遣",
            "description": "xxx 项目",
            "international_assignment_expected_end_date": "2024-01-02",
            "international_assignment_status": {
                "enum_name": "phone_type",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ]
            },
            "international_assignment_type": {
                "enum_name": "phone_type",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ]
            },
            "effective_time": "2024-01-02",
            "expiration_time": "2024-01-02",
            "id": "7127921432117937708"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1160001 | 参数错误 | 请检查参数，必要情况请参照【飞书人事-档案配置】 |
| 500 | 1160002 | 未知错误 | 请重试或联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |


