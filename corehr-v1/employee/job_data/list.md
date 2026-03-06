---
title: "批量查询任职信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_data/list"
updateTime: "1735280066000"
---

# 批量查询任职信息

批量查询员工的任职信息


> **Tip**: 当前接口为历史版本。推荐使用新版接口，详情参见[批量查询员工任职信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employees-job_data/batch_get)、[获取任职信息列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employees-job_data/query)。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/job_datas |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:corehr:readonly` 获取核心人事信息 `corehr:job_data:read` 查看任职信息 `corehr:corehr` 更新核心人事信息 `corehr:job_data:write` 读写任职信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `corehr:employment.position:read` 获取员工的岗位信息 `corehr:employment.position:write` 读写员工的岗位信息 `contact:user.employee_id:readonly` 获取用户 user ID `corehr:job_data.compensation_type:read` 获取薪资类型 `corehr:job_data.job_data_reason:read` 读取任职原因 `corehr:job_data.service_company:read` 获取任职公司 `corehr:job_data.work_shift:read` 获取排班信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：6994718879515739656 |
| `page_size` | `string` | 是 | 分页大小<br>**示例值**：100 |
| `employment_id` | `string` | 否 | 雇佣 ID，可通过[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)获取 - 应与 user_id_type 类型一致<br>**示例值**：7072306364927985196 |
| `job_data_id_list` | `string\[\]` | 否 | 任职信息 ID 列表 - 默认查询全部任职信息<br>**示例值**：6919733291281024526<br>**数据校验规则**：<br>- 最大长度：`100` |
| `department_id` | `string` | 否 | 部门 ID - 应与 department_id_type 类型一致 - 默认为空<br>**示例值**：6887868781834536462 |
| `job_id` | `string` | 否 | 职务 ID - 默认为空<br>**示例值**：6893014062142064135 |
| `get_all_version` | `boolean` | 否 | 是否获取所有版本的任职记录 - true 为获取员工所有版本的任职记录 - false 为仅获取当前生效的任职记录 - 默认为 false<br>**示例值**：false |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：people_corehr_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`people_corehr_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 此次调用中使用的部门 ID 类型<br>**示例值**：open_department_id<br>**可选值有**：<br>- `open_department_id`: 以 open_department_id 来标识部门 - `department_id`: 以 department_id 来标识部门 - `people_corehr_department_id`: 以 people_corehr_department_id 来标识部门<br>**默认值**：`people_corehr_department_id` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `job_data\[\]` | 查询的任职信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 任职信息 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `version_id` | `string` | 任职记录版本 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_level_id` | `string` | 职务级别 ID，可通过[【查询单个职级】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/get) 获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_grade_id` | `string` | 职等 ID，可通过[【查询职等】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query) 获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type_id` | `string` | 人员类型 ID，可通过[【查询单个人员类型】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/get) 获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `working_hours_type_id` | `string` | 工时制度 ID，可通过[【查询单个工时制度】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/get) 获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_location_id` | `string` | 工作地点 ID，可通过[【查询单个地点】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/get) 获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 部门 ID，可通过[【批量查询部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)接口查询详细信息 - 与 department_id_type 类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_id` | `string` | 职务 ID，可通过[【查询单个职务】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job/get) 获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `probation_start_date` | `string` | 试用期开始日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `probation_end_date` | `string` | 试用期结束日期（实际结束日期） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `primary_job_data` | `boolean` | 是否为主任职 - true：主职 - false：兼职，建议使用兼职相关接口 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id` | `string` | 雇佣 ID，可通过[【批量查询员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)获取详细信息 - 与 user_id_type 类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 任职记录版本的生效时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 任职记录版本的失效时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id` | `string` | 序列 ID，可通过 [【查询单个序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/get) 获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `assignment_start_reason` | `enum` | 业务类型（原：任职原因） - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：job_data   - custom_api_name：assignment_start_reason |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `probation_expected_end_date` | `string` | 预计试用期结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `probation_outcome` | `enum` | 试用期结果 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：job_data   - custom_api_name：probation_outcome |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `weekly_working_hours` | `int` | 周工作时长 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `direct_manager_id` | `string` | 实线主管的任职记录ID，可通过[【查询单个任职信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_data/get) 获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dotted_line_manager_id_list` | `string\[\]` | 虚线主管的任职记录ID，可通过[【查询单个任职信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_data/get) 获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `second_direct_manager_id` | `string` | 第二实线主管的任职记录ID，可通过[【查询单个任职信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_data/get) 获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_rate` | `support_cost_center_item\[\]` | 成本中心分摊信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_id` | `string` | 成本中心 ID，可以通过[搜索成本中心信息](https://open.feishu.cn/document/server-docs/corehr-v1/organization-management/cost_center/search)接口获取对应的成本中心信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rate` | `int` | 分摊比例 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `weekly_working_hours_v2` | `number(float)` | 周工作时长v2 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_shift` | `enum` | 排班类型，可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下： - object_api_name = "job_data" - custom_api_name = "work_shift"<br>**字段权限要求**： `corehr:job_data.work_shift:read` 获取排班信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `compensation_type` | `enum` | 薪资类型，可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下： - object_api_name = "job_data" - custom_api_name = "compensation_type"<br>**字段权限要求**： `corehr:job_data.compensation_type:read` 获取薪资类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `service_company` | `string` | 任职公司，枚举值及详细信息可通过[【查询单个公司】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/get)接口查询获得<br>**字段权限要求**： `corehr:job_data.service_company:read` 获取任职公司 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_subtype_id` | `string` | 人员子类型 ID - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `position_id` | `string` | 岗位 ID - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**字段权限要求（满足任一）**： `corehr:employment.position:read` 获取员工的岗位信息 `corehr:employment.position:write` 读写员工的岗位信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_data_reason` | `enum` | 任职原因 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name = "job_data"   - custom_api_name = "job_data_reason"<br>**字段权限要求**： `corehr:job_data.job_data_reason:read` 读取任职原因 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "id": "6890452208593372679",
                "version_id": "6890452208593372697",
                "job_level_id": "6890452208593372679",
                "job_grade_id": "6890452208593372679",
                "employee_type_id": "6890452208593372679",
                "working_hours_type_id": "6890452208593372679",
                "work_location_id": "6890452208593372679",
                "department_id": "6890452208593372679",
                "job_id": "6890452208593372679",
                "probation_start_date": "2018-03-16",
                "probation_end_date": "2019-05-24",
                "primary_job_data": true,
                "employment_id": "6893014062142064135",
                "effective_time": "2020-05-01 00:00:00",
                "expiration_time": "2020-05-02 00:00:00",
                "job_family_id": "1245678",
                "assignment_start_reason": {
                    "enum_name": "type_1",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "张三"
                        }
                    ]
                },
                "probation_expected_end_date": "2006-01-02",
                "probation_outcome": {
                    "enum_name": "type_1",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "张三"
                        }
                    ]
                },
                "weekly_working_hours": 30,
                "direct_manager_id": "6890452208593372679",
                "dotted_line_manager_id_list": [
                    "6890452208593372681"
                ],
                "second_direct_manager_id": "6890452208593372679",
                "cost_center_rate": [
                    {
                        "cost_center_id": "6950635856373745165",
                        "rate": 100
                    }
                ],
                "weekly_working_hours_v2": 37.5,
                "work_shift": {
                    "enum_name": "example",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "example"
                        }
                    ]
                },
                "compensation_type": {
                    "enum_name": "example",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "example"
                        }
                    ]
                },
                "service_company": "6890452208593372680",
                "employee_subtype_id": "6890452208593372680",
                "position_id": "6890452208593372679",
                "job_data_reason": {
                    "enum_name": "example_option",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "晋升"
                        }
                    ]
                }
            }
        ],
        "has_more": true,
        "page_token": "1234452132"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1160004 | request ID repeat | request ID 重复，请检查传入参数 |
| 400 | 1160019 | The sum of cost center apportionment ratio should be 100. | 成本中心分摊比率之和应为100 |
| 400 | 1160003 | record is deleted by others | 记录被其他人删除 |
| 500 | 1160999 | unknown error | 请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 500 | 1160997 | unknown meta rpc error | 请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 500 | 1160998 | unknown vault rpc | 请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |


