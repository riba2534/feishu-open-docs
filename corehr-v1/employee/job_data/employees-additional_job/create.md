---
title: "创建兼职"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/employees-additional_job/create"
updateTime: "1747368251000"
---

# 创建兼职

创建员工的兼职


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/employees/additional_jobs |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:additional_job:write` 读写兼职信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID `corehr:additional_job.compensation_type:write` 读写兼职的薪资类型 `corehr:additional_job.job:write` 读写兼职的职务信息 `corehr:additional_job.job_level:write` 读写兼职的职级信息 `corehr:additional_job.position:write` 读写兼职的岗位 `corehr:additional_job.service_company:write` 读写兼职的任职公司 `corehr:additional_job.work_shift:write` 读写兼职的排班信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `client_token` | `string` | 否 | 操作的唯一标识，用于幂等校验，格式为标准的 UUIDV4。请求成功时，重复的 client_token 不会再创建、变更数据。<br>**示例值**：12454646 |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 此次调用中使用的部门 ID 类型<br>**示例值**：open_department_id<br>**可选值有**：<br>- `open_department_id`: 【飞书】用来在具体某个应用中标识一个部门，同一个 department_id 在不同应用中的 open_department_id 相同。 - `department_id`: 【飞书】用来标识租户内一个唯一的部门。 - `people_corehr_department_id`: 【飞书人事】用来标识「飞书人事」中的部门。<br>**默认值**：`open_department_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `employee_type_id` | `string` | 是 | 人员类型 ID，可通过[【批量查询人员类型】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/list)获取<br>**示例值**："6890452208593372679" |
| `working_hours_type_id` | `string` | 否 | 工时制度 ID，可通过[【批量查询工时制度】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/list)获取详细信息<br>**示例值**："6890452208593372679" |
| `work_location_id` | `string` | 否 | 工作地点 ID - 可通过[【批量查询地点】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)获取详细信息，并选择【地点用途】为工作地点（business_site）的记录<br>**示例值**："6890452208593372679" |
| `department_id` | `string` | 是 | 部门 ID，可通过[【批量查询部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)获取详细信息<br>类型与 department_id_type 一致<br>**示例值**："6890452208593372679" |
| `job_id` | `string` | 否 | 职务 ID，可通过[【批量查询职务】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/list)获取详细信息<br>**示例值**："6890452208593372679" |
| `job_level_id` | `string` | 否 | 职级 ID，可通过[【批量查询职级】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/list)获取详细信息<br>**示例值**："6890452208593372679" |
| `job_family_id` | `string` | 否 | 序列 ID，可通过[【批量查询序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/list)获取详细信息<br>**示例值**："1245678" |
| `employment_id` | `string` | 是 | 雇佣 ID，可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取详细信息<br>类型与 user_id_type 一致<br>**示例值**："6893014062142064135" |
| `start_date` | `string` | 是 | 兼职开始日期<br>**示例值**："2020-05-01" |
| `end_date` | `string` | 否 | 兼职结束日期，不可清空<br>**示例值**："2020-05-02" |
| `direct_manager_id` | `string` | 否 | 直属上级的雇佣ID，可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取详细信息<br>类型与 user_id_type 一致<br>**示例值**："6890452208593372680" |
| `dotted_line_manager_id` | `string` | 否 | 虚线上级的雇佣ID，可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取详细信息<br>类型与 user_id_type 一致<br>**示例值**："6890452208593372680" |
| `work_shift` | `enum` | 否 | 排班类型，可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下： - object_api_name = "job_data" - custom_api_name = "work_shift" |
| &nbsp;&nbsp;└ `enum_name` | `string` | 是 | 枚举值<br>**示例值**："phone_type" |
| `compensation_type` | `enum` | 否 | 薪资类型，可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下： - object_api_name = "job_data" - custom_api_name = "compensation_type" |
| &nbsp;&nbsp;└ `enum_name` | `string` | 是 | 枚举值<br>**示例值**："phone_type" |
| `service_company` | `string` | 否 | 任职公司，可通过[【批量查询公司】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)获取详细信息<br>**示例值**："6890452208593372680" |
| `weekly_working_hours` | `string` | 否 | 周工作时长【0~168】<br>**示例值**："5" |
| `work_calendar_id` | `string` | 否 | 工作日历 ID，可通过[【查询工作日历】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/leave/work_calendar)获取详细信息<br>**示例值**："6890452208593372680" |
| `position_id` | `string` | 否 | 岗位 ID<br>**示例值**："6890452208593372680" |
| `employee_subtype_id` | `string` | 否 | 人员子类型 ID<br>**示例值**："6890452208593372680" |


### 请求体示例

```json
{
    "employee_type_id": "6890452208593372679",
    "working_hours_type_id": "6890452208593372679",
    "work_location_id": "6890452208593372679",
    "department_id": "6890452208593372679",
    "job_id": "6890452208593372679",
    "job_level_id": "6890452208593372679",
    "job_family_id": "1245678",
    "employment_id": "6893014062142064135",
    "start_date": "2020-05-01",
    "end_date": "2020-05-02",
    "direct_manager_id": "6890452208593372680",
    "dotted_line_manager_id": "6890452208593372680",
    "work_shift": {
        "enum_name": "phone_type"
    },
    "compensation_type": {
        "enum_name": "phone_type"
    },
    "service_company": "6890452208593372680",
    "weekly_working_hours": "5",
    "work_calendar_id": "6890452208593372680",
    "position_id": "6890452208593372680",
    "employee_subtype_id": "6890452208593372680"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `additional_job` | `employees.additional_job_write_resp` | 兼职信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 兼职记录 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type_id` | `string` | 人员类型 ID，可通过[【查询单个人员类型】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `working_hours_type_id` | `string` | 工时制度 ID，可通过[【查询单个工时制度】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_location_id` | `string` | 工作地点 ID，可通过[【查询单个地点】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 部门 ID，可通过[【批量查询部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)获取详细信息<br>类型与 department_id_type 一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_id` | `string` | 职务 ID，可通过[【查询单个职务】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job/get)获取详细信息<br>**字段权限要求**： `corehr:additional_job.job:write` 读写兼职的职务信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_level_id` | `string` | 职级 ID，可通过[【查询单个职级】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/get)获取详细信息<br>**字段权限要求**： `corehr:additional_job.job_level:write` 读写兼职的职级信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id` | `string` | 序列 ID，可通过[【查询单个序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id` | `string` | 雇佣 ID，可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取详细信息<br>类型与 user_id_type 一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 兼职开始日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 兼职结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `direct_manager_id` | `string` | 直属上级的雇佣 ID，可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取详细信息<br>类型与 user_id_type 一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dotted_line_manager_id` | `string` | 虚线上级的雇佣 ID，可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取详细信息<br>类型与 user_id_type 一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_shift` | `enum` | 排班类型，可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下： - object_api_name = "job_data" - custom_api_name = "work_shift"<br>**字段权限要求**： `corehr:additional_job.work_shift:write` 读写兼职的排班信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `compensation_type` | `enum` | 薪资类型，可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下： - object_api_name = "job_data" - custom_api_name = "compensation_type"<br>**字段权限要求**： `corehr:additional_job.compensation_type:write` 读写兼职的薪资类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `service_company` | `string` | 任职公司，可通过[【查询单个公司】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/get)获取详细信息<br>**字段权限要求**： `corehr:additional_job.service_company:write` 读写兼职的任职公司 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `weekly_working_hours` | `string` | 周工作时长【0~168】 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_calendar_id` | `string` | 工作日历 ID，可通过[【查询工作日历】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/leave/work_calendar)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `position_id` | `string` | 岗位 ID<br>**字段权限要求**： `corehr:additional_job.position:write` 读写兼职的岗位 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_subtype_id` | `string` | 人员子类型 ID |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "additional_job": {
            "id": "6890452208593372679",
            "employee_type_id": "6890452208593372679",
            "working_hours_type_id": "6890452208593372679",
            "work_location_id": "6890452208593372679",
            "department_id": "6890452208593372679",
            "job_id": "6890452208593372679",
            "job_level_id": "6890452208593372679",
            "job_family_id": "1245678",
            "employment_id": "6893014062142064135",
            "start_date": "2020-05-01",
            "end_date": "2020-05-02",
            "direct_manager_id": "6890452208593372680",
            "dotted_line_manager_id": "6890452208593372680",
            "work_shift": {
                "enum_name": "phone_type",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ]
            },
            "compensation_type": {
                "enum_name": "phone_type",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "中文示例"
                    }
                ]
            },
            "service_company": "6890452208593372680",
            "weekly_working_hours": "5",
            "work_calendar_id": "6890452208593372680",
            "position_id": "6890452208593372680",
            "employee_subtype_id": "6890452208593372680"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 200 | 1160001 | 参数错误 | 请参考返回的错误信息修改传参 |
| 400 | 1160002 | 未知错误 | 请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |


