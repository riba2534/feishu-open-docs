---
title: "搜索员工信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search"
updateTime: "1758684092000"
---

# 搜索员工信息

查询员工的工作信息、个人信息等数据


> **Tip**: - 该接口会按照应用拥有的「员工数据」的权限范围返回数据，请确定在「开发者后台 - 权限管理 - 数据权限」中有申请「员工资源」权限范围
> - 接口已升级，推荐使用，性能更优。
> 如需继续使用旧版本接口，可点击[ 查询单个雇佣信息](https://open.feishu.cn/document/server-docs/corehr-v1/employee/employment/get) [ 查询单个个人信息](https://open.feishu.cn/document/server-docs/corehr-v1/employee/person/get)
> - 本接口关联数据库更新存在5分钟延迟，若希望获取刚更新的数据内容请延缓请求
> - 当员工未完成入职时，该接口将无法查询到该员工数据，如【待入职】【撤销入职】【删除雇佣】等情况
> - 部分计算字段是在凌晨零点进行计算，建议不要在零点时间段进行查询


> **Warning**: - 请求体入参不填写默认为空
> - 所有筛选项可一起使用，之间为 AND 关系
> - 字段未返回请检查：字段权限、用户该字段有值，以及飞书人事档案配置中字段是否启用
> - 在人事系统开启【复用工号】后，存在一个工号对应多个员工的情况，请勿依赖工号做唯一性检查
> - 基于 `id_type` 类型字段（如 employment_id），在部分转换失败（ID映射不存在）的场景会返回 lark_id，无法区分值是否为对应 `id_type`。新增相关 xxx_id_v2 的字段，在转换失败时返回空值，用于区分是否转换成功；正常情况下两个字段的值是没有区别的，建议使用 id_v2 的字段


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/employees/search |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:employee:read` 获取员工信息 `corehr:employee:write` 读写员工信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `corehr:contract.period:read` 获取合同期限信息 `corehr:employee.all_bp:read` 查看员工的全部 BP 信息 `corehr:employee.bp:read` 查看员工的部分 BP 信息 `corehr:employment.assignment:read` 获取员工外派信息 `corehr:employment.custom_field:read` 获取雇佣信息自定义字段信息 `corehr:employment.custom_org_field:read` 获取员工的自定义组织信息 `corehr:employment.custom_org_field:write` 读写员工的自定义组织信息 `corehr:employment.job:read` 获取员工的职务信息 `corehr:employment.job_level:read` 获取职务级别信息 `corehr:employment.offboarding_reason:read` 获取员工离职原因 `corehr:employment.pathway:read` 获取员工通道信息 `corehr:employment.pathway:write` 读写员工通道 `corehr:employment.pay_group:read` 获取薪资组信息 `corehr:employment.position:read` 获取员工的岗位信息 `corehr:employment.position:write` 读写员工的岗位信息 `corehr:job.job_level:read` 获取职务中的职级信息 `corehr:person.additional_name:read` 获取别名信息 `corehr:person.additional_name:write` 读写别名信息 `corehr:person.address:read` 读取个人地址信息 `corehr:person.address:write` 读写个人地址信息 `corehr:person.bank_account:read` 获取银行账号列表信息 `corehr:person.bank_account:write` 读写银行账号信息 `corehr:person.born_country_region:read` 获取出生国家/地区信息 `corehr:person.custom_field:read` 获取个人信息自定义字段信息 `corehr:person.date_entered_workforce:read` 获取参加工作日期 `corehr:person.date_entered_workforce:write` 读写参加工作日期 `corehr:person.date_of_birth:read` 获取生日信息 `corehr:person.date_of_birth:write` 读写生日信息 `corehr:person.dependent:read` 获取家庭成员信息 `corehr:person.dependent:write` 读写家庭成员信息 `corehr:person.education:read` 获取教育经历信息 `corehr:person.education:write` 读写教育经历信息 `corehr:person.email:read` 获取个人邮箱信息 `corehr:person.email:write` 读写个人邮箱信息 `corehr:person.emergency_contact:read` 获取紧急联系人信息 `corehr:person.emergency_contact:write` 读写紧急联系人信息 `corehr:person.entry_leave_time:read` 获取出入境日期信息 `corehr:person.gender:read` 获取性别信息 `corehr:person.gender:write` 读写性别信息 `corehr:person.hukou:read` 获取户口信息 `corehr:person.hukou:write` 读写户口信息 `corehr:person.is_disabled:read` 获取残疾信息 `corehr:person.is_old_alone:read` 获取孤老信息 `corehr:person.legal_name:read` 获取法定姓名信息 `corehr:person.legal_name:write` 读写法定姓名信息 `corehr:person.marital_status:read` 获取婚姻状况信息 `corehr:person.marital_status:write` 读写婚姻状况信息 `corehr:person.martyr_family:read` 获取烈属信息 `corehr:person.martyr_family:write` 读写烈属信息 `corehr:person.national_id:read` 获取证件信息 `corehr:person.national_id:write` 读写证件信息 `corehr:person.nationality:read` 获取国籍信息 `corehr:person.native_region:read` 获取籍贯信息 `corehr:person.native_region:write` 读写籍贯信息 `corehr:person.personal_profile:read` 获取个人资料信息 `corehr:person.personal_profile:write` 读写个人资料信息 `corehr:person.phone:read` 获取个人手机号信息 `corehr:person.phone:write` 读写个人手机号信息 `corehr:person.political_affiliation:read` 获取政治面貌信息 `corehr:person.race:read` 获取民族/种族信息 `corehr:person.religion:read` 查看宗教信仰信息 `corehr:person.resident_tax:read` 获取居民身份信息 `corehr:person.resident_tax:write` 读写居民身份信息 `corehr:person.resident_tax_custom_field:read` 获取居民身份自定义字段信息 `corehr:person.resident_tax_custom_field:write` 读写居民身份自定义字段信息 `corehr:person.work_experience:read` 获取工作履历信息 `corehr:person.work_experience:write` 读写工作履历信息 `corehr:employment.job_grade:read` 获取职等信息 `corehr:employment.job_grade:write` 读写职等信息 `corehr:person.born_country_region:write` 读写出生国家/地区信息 `corehr:person.nationality:write` 读写国籍信息 `corehr:person.entry_leave_time:write` 读写出入境日期信息 `corehr:employment.seniority_adjust_information:read` 获取员工司龄调整信息 `corehr:person.custom_field:write` 读写个人信息中的自定义字段信息 `corehr:employment.seniority_adjust_information:write` 读写员工司龄调整信息 `corehr:employment.contract_type:read` 获取员工合同类型 `corehr:job_data.compensation_type:read` 获取薪资类型 `corehr:person.is_disabled:write` 读写残疾信息 `corehr:person.political_affiliation:write` 读写个人政治面貌信息 `corehr:job_data.service_company:read` 获取任职公司 `corehr:person.is_old_alone:write` 读写孤老信息 `corehr:person.religion:write` 读写宗教信仰信息 `corehr:job_data.work_shift:read` 获取排班信息 `corehr:employment.job_level:write` 读写员工的职务级别信息 `corehr:contract.period:write` 读写合同期限信息 `corehr:employment.archive_cpst_plan:read` 获取员工薪资方案 `contact:user.employee_id:readonly` 获取用户 user ID `corehr:employment.assignment_pay_group:read` 获取员工所属外派薪资组 |

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
| `department_id_type` | `string` | 否 | 此次调用中使用的部门 ID 类型<br>**示例值**：open_department_id<br>**可选值有**：<br>- `open_department_id`: 以 open_department_id 来标识部门 - `department_id`: 以 department_id 来标识部门 - `people_corehr_department_id`: 以 people_corehr_department_id 来标识部门<br>**默认值**：`open_department_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `fields` | `string\[\]` | 否 | 需要查询的字段列表 - 参考[【字段下钻】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/query-employment-fields) - 为空时仅返回 employment_id<br>**示例值**：["person_info.phone_number"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `employment_id_list` | `string\[\]` | 否 | 雇佣 ID 列表 - 在  [【创建雇佣】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employment/create) 返回的 ID - ID类型应于 user_id_type 一致<br>**示例值**：["7140964208476371111"] |
| `employee_number_list` | `string\[\]` | 否 | 工号列表，是在[【创建雇佣】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employment/create)时主动传递的或者自动生成的工号<br>**示例值**：["100001"] |
| `work_email` | `string` | 否 | 邮箱，精确匹配查询<br>**示例值**："13312345678@qq.com" |
| `phone_number` | `string` | 否 | 个人电话，精确匹配查询 - 字段权限要求：   - `corehr:person.phone.search:read` 使用个人电话搜索<br>**示例值**："16760342300" |
| `key_word` | `string` | 否 | 搜索关键字，支持对邮箱、工号和姓名的模糊匹配 - 模糊搜索基于相关性返回，返回数据不固定，请勿依赖此字段翻页查询<br>**示例值**："张三" |
| `employment_status` | `string` | 否 | 雇佣状态<br>**示例值**："hired"<br>**可选值有**：<br>- `hired`: 在职 - `terminated`: 离职 |
| `employee_type_id` | `string` | 否 | 人员类型 ID，可通过[【批量查询人员类型】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/list) 接口获取<br>**示例值**："6971090097697521314" |
| `department_id_list` | `string\[\]` | 否 | 部门 ID，根据员工主职的直接部门查询，可以通过[【批量查询部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get) API 获取 部门 ID - ID 类型应与 department_id_type 一致<br>**示例值**：["7140964208476371111"] |
| `direct_manager_id_list` | `string\[\]` | 否 | 直接上级的雇佣 ID，根据员工主职的直接上级查询 - 可基于当前接口获取员工的直属上级雇佣ID - 可基于[【创建雇佣】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employment/create)时返回的雇佣ID - ID 类型应与 user_id_type 一致<br>**示例值**：["7027024823985117820"] |
| `dotted_line_manager_id_list` | `string\[\]` | 否 | 虚线上级的雇佣 ID，根据员工主职的虚线上级查询 - 可基于当前接口获取员工的虚线上级雇佣ID - 可基于[【创建雇佣】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employment/create)时返回的雇佣ID - ID 类型应与 user_id_type 一致<br>**示例值**：["7027024823985117820"] |
| `regular_employee_start_date_start` | `string` | 否 | 转正式员工日期-搜索范围开始<br>**示例值**："2020-01-01" |
| `regular_employee_start_date_end` | `string` | 否 | 转正式员工日期-搜索范围结束<br>**示例值**："2020-01-01" |
| `effective_time_start` | `string` | 否 | 入职日期-搜索范围开始，需要与搜索范围结束一同使用<br>**示例值**："2020-01-01" |
| `effective_time_end` | `string` | 否 | 入职日期-搜索范围结束<br>**示例值**："2020-01-01" |
| `work_location_id_list_include_sub` | `string\[\]` | 否 | 工作地点 ID 列表，查询属于该工作地点及下级工作地点的员工 - 可通过 [【批量查询地点】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list) 接口获取<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `preferred_english_full_name_list` | `string\[\]` | 否 | 常用英文全名精确搜索<br>**示例值**：["Sandy"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `preferred_local_full_name_list` | `string\[\]` | 否 | 常用本地全名精确搜索<br>**示例值**：["小明"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `national_id_number_list` | `string\[\]` | 否 | 居民身份证件号码精确搜索 - 字段权限要求：   - `corehr:person.national_id.search:read` 使用身份证号搜索<br>**示例值**：["110100xxxxxxxxxxxx"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `phone_number_list` | `string\[\]` | 否 | 个人电话列表，精确匹配查询 - 字段权限要求：   - `corehr:person.phone.search:read` 使用个人电话搜索<br>**示例值**：["16760342300"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `email_address_list` | `string\[\]` | 否 | 工作邮箱地址列表，精确匹配查询<br>**示例值**：["xxx@xxx.com"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `department_id_list_include_sub` | `string\[\]` | 否 | 部门 ID 列表，查询属于该部门及下级部门的员工 - 可通过[【批量查询部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get) 获取 - ID 类型应与 department_id_type 一致<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `additional_national_id_number_list` | `string\[\]` | 否 | 其他国籍ID列表，精准匹配查询 - 字段权限要求   - `corehr:person.additional_nationalities:read` 读取员工其他国籍 - 可以调用[【查询国籍信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-nationality/search)接口，获取对应数据。<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `citizenship_status_list` | `string\[\]` | 否 | 公民身份类型列表，精确匹配查询 -相关信息可以参考：[公民身份数据](https://bytedance.larkoffice.com/wiki/VEEaw1GyhiaNJAkQt4pc8HTxnKe) - 字段权限要求   - `corehr:person.citizenship_status:read` 读取员工公民身份<br>**示例值**：["公民（中国大陆）"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `cost_center_id_list` | `string\[\]` | 否 | 成本中心 ID 列表 - 可通过 [【搜索成本中心信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search) 获取<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `service_company_list` | `string\[\]` | 否 | 任职公司 ID 列表 - [【批量查询公司】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)获取 - 字段权限要求：   - `corehr:job_data.service_company:read` 读取员工任职公司<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `service_company_list_include_sub` | `string\[\]` | 否 | 任职公司 ID 列表（含下级） - [【批量查询公司】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)获取 - 字段权限要求：   - `corehr:job_data.service_company:read` 读取员工任职公司<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `job_family_id_list` | `string\[\]` | 否 | 序列 ID 列表  - [【批量查询序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/list)获取<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `job_family_id_list_include_sub` | `string\[\]` | 否 | 序列 ID 列表（含下级）  - [【批量查询序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/list)获取<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `job_level_id_list` | `string\[\]` | 否 | 职级 ID 列表 - 可通过[【批量查询职级】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/list)获取 - 字段权限要求：   - `corehr:employment.job_level:read` 读取员工职级<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `job_grade_id_list` | `string\[\]` | 否 | 职等 ID 列表 - 可通过[【查询职等】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)获取 - 字段权限要求：   - `corehr:employment.job_grade:read` 读取员工职等<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `job_id_list` | `string\[\]` | 否 | 职务 ID 列表 - 可通过[【批量查询职务】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/list)获取 - 字段权限要求：   - `corehr:employment.job:read` 读取员工职务<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `position_id_list` | `string\[\]` | 否 | 岗位 ID 列表  - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)  - 字段权限要求：     - `corehr:employment.position:read` 读取员工岗位<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `position_id_list_include_sub` | `string\[\]` | 否 | 岗位 ID 列表（含下级）  - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/T8NjPznGe61S)  - 字段权限要求：     - `corehr:employment.position:read` 读取员工岗位<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `working_hours_type_id_list` | `string\[\]` | 否 | 工时制度 ID 列表 - 可通过[【批量查询工时制度】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/list)获取<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `nationality_id_list` | `string\[\]` | 否 | 国籍 ID 列表 - 可通过[【查询国籍信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-nationality/search)获取  - 字段权限要求：     - `corehr:person.nationality:read` 读取员工国籍<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `pay_group_id_list` | `string\[\]` | 否 | 员工所属薪资组 ID 列表  - 可通过 [【获取薪资组基本信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/payroll-v1/paygroup/list) 获取  - 字段权限要求：     - `corehr:employment.pay_group:read` 读取员工薪资组<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `assignment_pay_group_id_list` | `string\[\]` | 否 | 员工所属外派薪资组 ID 列表 - 可通过 [【获取薪资组基本信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/payroll-v1/paygroup/list) 获取 - 字段权限要求：     - `corehr:employment.assignment_pay_group:read` 读取员工外派薪资组<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `contract_type_list` | `string\[\]` | 否 | 员工当前合同类型列表 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)查询   - object_api_name：contract   - custom_api_name：contract_type - 字段权限要求：     - `corehr:employment.contract_type:read` 读取员工当前合同类型<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `archive_cpst_plan_id_list` | `string\[\]` | 否 | 员工当前所属薪资方案 ID 列表 - 可通过[【批量查询薪资方案】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/compensation-v1/plan/list)获取 - 字段权限要求：    - `corehr:employment.archive_cpst_plan:read` 读取员工当前薪资方案<br>**示例值**：["7140964208476371111"]<br>**数据校验规则**：<br>- 最大长度：`100` |


### 请求体示例

```json
{
    "fields": [
        "person_info.phone_number"
    ],
    "employment_id_list": [
        "7140964208476371111"
    ],
    "employee_number_list": [
        "100001"
    ],
    "work_email": "13312345678@qq.com",
    "phone_number": "16760342300",
    "key_word": "张三",
    "employment_status": "hired",
    "employee_type_id": "6971090097697521314",
    "department_id_list": [
        "7140964208476371111"
    ],
    "direct_manager_id_list": [
        "7027024823985117820"
    ],
    "dotted_line_manager_id_list": [
        "7027024823985117820"
    ],
    "regular_employee_start_date_start": "2020-01-01",
    "regular_employee_start_date_end": "2020-01-01",
    "effective_time_start": "2020-01-01",
    "effective_time_end": "2020-01-01",
    "work_location_id_list_include_sub": [
        "7140964208476371111"
    ],
    "preferred_english_full_name_list": [
        "Sandy"
    ],
    "preferred_local_full_name_list": [
        "小明"
    ],
    "national_id_number_list": [
        "110100xxxxxxxxxxxx"
    ],
    "phone_number_list": [
        "16760342300"
    ],
    "email_address_list": [
        "xxx@xxx.com"
    ],
    "department_id_list_include_sub": [
        "7140964208476371111"
    ],
    "additional_national_id_number_list": [
        "7140964208476371111"
    ],
    "citizenship_status_list": [
        "公民（中国大陆）"
    ],
    "cost_center_id_list": [
        "7140964208476371111"
    ],
    "service_company_list": [
        "7140964208476371111"
    ],
    "service_company_list_include_sub": [
        "7140964208476371111"
    ],
    "job_family_id_list": [
        "7140964208476371111"
    ],
    "job_family_id_list_include_sub": [
        "7140964208476371111"
    ],
    "job_level_id_list": [
        "7140964208476371111"
    ],
    "job_grade_id_list": [
        "7140964208476371111"
    ],
    "job_id_list": [
        "7140964208476371111"
    ],
    "position_id_list": [
        "7140964208476371111"
    ],
    "position_id_list_include_sub": [
        "7140964208476371111"
    ],
    "working_hours_type_id_list": [
        "7140964208476371111"
    ],
    "nationality_id_list": [
        "7140964208476371111"
    ],
    "pay_group_id_list": [
        "7140964208476371111"
    ],
    "assignment_pay_group_id_list": [
        "7140964208476371111"
    ],
    "contract_type_list": [
        "7140964208476371111"
    ],
    "archive_cpst_plan_id_list": [
        "7140964208476371111"
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
| &nbsp;&nbsp;└ `items` | `employee\[\]` | 查询的雇佣信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id` | `string` | 雇佣 ID，类型与 user_id_type 一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id_v2` | `string` | 雇佣 ID - 类型与 user_id_type 一致，转换失败时返回空值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ats_application_id` | `string` | 招聘投递 ID ，详细信息可以通过[【获取投递信息】](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/get)接口查询 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `prehire_id` | `string` | 待入职 ID，可通过[【查询单个待入职】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/pre_hire/get)获取信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_number` | `string` | 工号，在[【创建雇佣】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employment/create) 是指定的或者自动生成的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type_id` | `string` | 人员类型 ID，详细信息可通过[【查询单个人员类型】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/get)接口查询 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_subtype_id` | `string` | 人员子类型 ID - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 部门 ID，详细信息可通过[【查询单个部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/get)接口查询 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_id_v2` | `string` | 部门 ID - 可通过 [【查询单个部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)获取详细信息 - 类型与 department_id_type 一致，转换失败时返回空值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_level_id` | `string` | 职级 ID，详细信息可通过[【获取单个职级】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/get)接口查询<br>**字段权限要求（满足任一）**： `corehr:employment.job_level:read` 获取职务级别信息 `corehr:employment.job_level:write` 读写员工的职务级别信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_level` | `employee.job_level` | 职级<br>**字段权限要求（满足任一）**： `corehr:employment.job_level:read` 获取职务级别信息 `corehr:employment.job_level:write` 读写员工的职务级别信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职级 ID，可通过[【查询单个职级】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/get)获取详细信息<br>- 与 job_level_id 值相同 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `level_order` | `int` | 职级数值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `pathway_id` | `string` | 通道 ID<br>**字段权限要求（满足任一）**： `corehr:employment.pathway:read` 获取员工通道信息 `corehr:employment.pathway:write` 读写员工通道 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `pathway` | `employee.pathway` | 通道<br>**字段权限要求（满足任一）**： `corehr:employment.pathway:read` 获取员工通道信息 `corehr:employment.pathway:write` 读写员工通道 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 通道 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_grade_id` | `string` | 职等 ID，可用于[【查询职等】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)<br>**字段权限要求（满足任一）**： `corehr:employment.job_grade:read` 获取职等信息 `corehr:employment.job_grade:write` 读写职等信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_location_id` | `string` | 工作地点 ID，详细信息可通过[【查询单个地点】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/get)接口查询 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id` | `string` | 序列 ID，详细信息可通过[【查询单个序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/get)接口查询 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_family` | `employee.job_family` | 序列 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 序列 ID，可通过[【查询单个序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/get)获取详细信息<br>- 与 job_family_id 值相同 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 是否启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `parent_id` | `string` | 上级序列，可通过[【查询单个序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 生效时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 失效时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `position_id` | `string` | 岗位 ID，功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**字段权限要求（满足任一）**： `corehr:employment.position:read` 获取员工的岗位信息 `corehr:employment.position:write` 读写员工的岗位信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `position` | `position` | 岗位，功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**字段权限要求（满足任一）**： `corehr:employment.position:read` 获取员工的岗位信息 `corehr:employment.position:write` 读写员工的岗位信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `position_id` | `string` | 岗位 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `names` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `descriptions` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_id` | `string` | 职务 ID，详细信息可通过[【查询单个职务】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/get)接口查询<br>**字段权限要求（满足任一）**： `corehr:employment.job:read` 获取员工的职务信息 `corehr:employment.job_level:read` 获取职务级别信息 `corehr:employment.job_level:write` 读写员工的职务级别信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job` | `job` | 职务<br>**字段权限要求（满足任一）**： `corehr:employment.job:read` 获取员工的职务信息 `corehr:employment.job_level:read` 获取职务级别信息 `corehr:employment.job_level:write` 读写员工的职务级别信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 实体在CoreHR内部的唯一键 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_title` | `i18n\[\]` | 职务头衔 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pathway_id` | `string` | 通道ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id_list` | `string\[\]` | 序列 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_level_id_list` | `string\[\]` | 职级<br>**字段权限要求**： `corehr:job.job_level:read` 获取职务中的职级信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `working_hours_type_id` | `string` | 工时制度，引用WorkingHoursType的ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 生效时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 失效时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(123, 123.23, true, [\"id1\",\"id2\], 2006-01-02 15:04:05]) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `company_id` | `string` | 所属公司 ID，详细信息可通过[【查询单个公司】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/get)接口查询 - 当前生效的合同中的公司 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `working_hours_type_id` | `string` | 工时制度 ID，详细信息可通过[【查询单个工时制度】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/get)接口查询 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tenure` | `string` | 司龄 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `seniority_date` | `string` | 司龄起算日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_date` | `string` | 当前雇佣记录的入职日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `primary_employment` | `boolean` | 是否是主雇佣信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `probation_period` | `int` | 试用期时长（月） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `on_probation` | `boolean` | 是否在试用期中 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `probation_end_date` | `string` | 试用期结束日期（实际结束日期） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `direct_manager_id` | `string` | 直接上级的雇佣 ID - 类型与 user_id_type 一致 - 请使用 direct_manager_id_v2 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dotted_line_manager_id` | `string` | 虚线上级的雇佣 ID  - 类型与 user_id_type 一致  - 请使用 dotted_line_manager_id_v2 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `direct_manager_id_v2` | `string` | 直接上级的雇佣 ID - 类型与 user_id_type 一致，转换失败返回空值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dotted_line_manager_id_v2` | `string` | 虚线上级的雇佣 ID - 类型与 user_id_type 一致，转换失败返回空值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_type` | `enum` | 雇佣类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：employment   - custom_api_name：employment_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_status` | `enum` | 雇佣状态 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：employment   - custom_api_name：employment_status |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_date` | `string` | 离职日期，即员工的最后一个工作日，最后一个工作日时员工的雇佣状态仍为“在职”，次日凌晨将更改为“离职” |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `reason_for_offboarding` | `enum` | 离职原因 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：employment   - custom_api_name：reason_for_offboarding<br>**字段权限要求**： `corehr:employment.offboarding_reason:read` 获取员工离职原因 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `email_address` | `string` | 工作邮箱地址 - 计算字段，取自work_email_list 中   - email_usage: work   - is_primary: true |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_email_list` | `work_email\[\]` | 工作邮箱列表，只有当邮箱满足下面所有条件时，才在个人信息页面可见 - email_usage: work - is_primary: true |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 邮箱地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email_usage` | `enum` | 邮箱用途 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name: email   - custom_api_name：email_usage |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_list` | `job_data_cost_center\[\]` | 成本中心列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_id` | `string` | 成本中心 ID，可以通过[搜索成本中心信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获取对应的成本中心信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rate` | `int` | 分摊比例(整数) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `new_rate` | `number(float)` | 分摊比例 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `rehire` | `enum` | 是否离职重聘，枚举如下： - no：否 - yes：是 - to_be_confirmed：待确定 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `rehire_employment_id` | `string` | 历史雇佣信息 ID，可通过此接口查询详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `person_info` | `person_info` | 基本个人信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `person_id` | `string` | 个人信息 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 个人电话 - 该值取自 person_info.phone_list 中满足以下条件的个人电话   - is_primary=true   - device_type=mobile_phone   - phone_usage=home<br>**字段权限要求（满足任一）**： `corehr:person.phone:read` 获取个人手机号信息 `corehr:person.phone:write` 读写个人手机号信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `legal_name` | `string` | 法定姓名<br>**字段权限要求（满足任一）**： `corehr:person.legal_name:read` 获取法定姓名信息 `corehr:person.legal_name:write` 读写法定姓名信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `preferred_name` | `string` | 常用名 - 基于 local_primary、local_first_name、name_primary、first_name 等字段计算获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `additional_name` | `string` | 别名<br>**字段权限要求（满足任一）**： `corehr:person.additional_name:read` 获取别名信息 `corehr:person.additional_name:write` 读写别名信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `preferred_local_full_name` | `string` | 常用本地全名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `preferred_english_full_name` | `string` | 常用英文全名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name_list` | `person_name\[\]` | 姓名列表<br>**字段权限要求（满足任一）**： `corehr:person.legal_name:read` 获取法定姓名信息 `corehr:person.legal_name:write` 读写法定姓名信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_primary` | `string` | 姓 - 本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_first_name` | `string` | 名 - 本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家/地区 - 可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name_type` | `enum` | 姓名类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：person_name   - custom_api_name：name_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_first_name_2` | `string` | 名 - 第二本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_primary_2` | `string` | 姓 - 第二本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `additional_name` | `string` | 别名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `additional_name_type` | `enum` | 补充姓名类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：person_name   - custom_api_name：additional_name_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `first_name` | `string` | 名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_name` | `string` | 全名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hereditary` | `string` | 姓氏称谓 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_name` | `string` | 自定义姓名（未传入时，姓名将默认根据所属国家 / 地区规则对相关姓、名字段拼接） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_local_name` | `string` | 本地文字的自定义姓名（未传入时，本地文字的姓名将默认根据所属国家 / 地区规则对本地文字的相关姓、名字段拼接） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `middle_name` | `string` | 中间名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name_primary` | `string` | 姓 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `secondary` | `string` | 第二姓氏 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tertiary` | `string` | 婚后姓氏 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `social` | `enum` | 尊称 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：person_name     - custom_api_name：social |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `enum` | 头衔 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：person_name     - custom_api_name：title |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_middle_name` | `string` | 本地中间名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_secondary` | `string` | 第二姓氏 - 本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_name_local_and_western_script` | `string` | 展示姓名（本地和西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_name_local_script` | `string` | 展示姓名（本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_name_western_script` | `string` | 展示姓名（西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `gender` | `enum` | 性别 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：    - object_api_name：person   - custom_api_name：gender <br>**字段权限要求（满足任一）**： `corehr:person.gender:read` 获取性别信息 `corehr:person.gender:write` 读写性别信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date_of_birth` | `string` | 出生日期<br>**字段权限要求（满足任一）**： `corehr:person.date_of_birth:read` 获取生日信息 `corehr:person.date_of_birth:write` 读写生日信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `nationality_id_v2` | `string` | 国籍 ID，可通过[【查询国籍信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-nationality/search)查询<br>**字段权限要求（满足任一）**： `corehr:person.nationality:read` 获取国籍信息 `corehr:person.nationality:write` 读写国籍信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `race` | `enum` | 民族 / 种族 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：person    - custom_api_name：ethnicity_race <br>**字段权限要求**： `corehr:person.race:read` 获取民族/种族信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `marital_status` | `enum` | 婚姻状况 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：person  - custom_api_name：marital_status<br>**字段权限要求（满足任一）**： `corehr:person.marital_status:read` 获取婚姻状况信息 `corehr:person.marital_status:write` 读写婚姻状况信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_list` | `phone\[\]` | 电话列表<br>**字段权限要求（满足任一）**： `corehr:person.phone:read` 获取个人手机号信息 `corehr:person.phone:write` 读写个人手机号信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `international_area_code` | `enum` | 国家区号， - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：phone   - custom_api_name：international_area_code |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `formatted_phone_number` | `string` | 完整电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `device_type` | `enum` | 设备类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name：phone  - custom_api_name：device_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_usage` | `enum` | 电话用途 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name：phone  - custom_api_name：phone_usage |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_list` | `address\[\]` | 地址列表<br>**字段权限要求（满足任一）**： `corehr:person.address:read` 读取个人地址信息 `corehr:person.address:write` 读写个人地址信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_local_script` | `string` | 完整地址（本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_western_script` | `string` | 完整地址（西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_id` | `string` | 地址 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家/地区 - 可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_id` | `string` | 主要行政区 - 可通过[【查询省份/主要行政区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_id` | `string` | 城市（该字段待作废，请勿使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `distinct_id` | `string` | 区/县（该字段待作废，请勿使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_id_v2` | `string` | 城市 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `district_id_v2` | `string` | 区/县 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line1` | `string` | 地址行 1 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line2` | `string` | 地址行 2 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line3` | `string` | 地址行 3 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line4` | `string` | 地址行 4 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line5` | `string` | 地址行 5 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line6` | `string` | 地址行 6 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line7` | `string` | 地址行 7 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line8` | `string` | 地址行 8 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line9` | `string` | 地址行 9 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line1` | `string` | 地址行 1（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line2` | `string` | 地址行 2（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line3` | `string` | 地址行 3（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line4` | `string` | 地址行 4（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line5` | `string` | 地址行 5（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line6` | `string` | 地址行 6（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line7` | `string` | 地址行 7（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line8` | `string` | 地址行 8（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line9` | `string` | 地址行 9（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `postal_code` | `string` | 邮政编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_type_list` | `enum\[\]` | 地址类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_subdivision_1` | `string` | 城市往下细分 1 层的行政区 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_subdivision_2` | `string` | 城市往下细分 2 层的行政区 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_subdivision_1` | `string` | 主要行政区往下细分 1 层的行政区 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_subdivision_2` | `string` | 主要行政区往下细分 2 层的行政区 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email_list` | `email\[\]` | 邮箱列表 - 请使用 work_email_list 获取工作邮箱<br>**字段权限要求（满足任一）**： `corehr:person.email:read` 获取个人邮箱信息 `corehr:person.email:write` 读写个人邮箱信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 邮箱地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 是否为主要邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 是否为公开邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email_usage` | `enum` | 邮箱用途 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name: email   - custom_api_name：email_usage |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `work_experience_list` | `work_experience_info\[\]` | 工作经历列表<br>**字段权限要求（满足任一）**： `corehr:person.work_experience:read` 获取工作履历信息 `corehr:person.work_experience:write` 读写工作履历信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `company_organization` | `i18n\[\]` | 公司 / 组织 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `i18n\[\]` | 部门 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job` | `i18n\[\]` | 岗位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 工作描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 开始日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `education_list` | `education\[\]` | 教育经历列表<br>**字段权限要求（满足任一）**： `corehr:person.education:read` 获取教育经历信息 `corehr:person.education:write` 读写教育经历信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `school` | `i18n\[\]` | 学校 - 自定义名称时返回该字段 - 下拉框选择的返回 school_name 字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `level_of_education` | `enum` | 学历 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 开始日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_of_study` | `i18n\[\]` | 专业 - 自定义名称时返回该字段 - 下拉框选择的返回 field_of_study_name 字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `degree` | `enum` | 学位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `school_name` | `enum` | 学校名称 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：education   - custom_api_name：school_name - 自定义名称时返回 school 字段 - 下拉框选择的返回该字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_of_study_name` | `enum` | 专业名称 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：education   - custom_api_name：field_of_study_name - 自定义名称时返回 field_of_study 字段 - 下拉框选择的返回该字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家地区ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expected_end_date` | `string` | 预期结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bank_account_list` | `bank_account\[\]` | 银行账户<br>**字段权限要求（满足任一）**： `corehr:person.bank_account:read` 获取银行账号列表信息 `corehr:person.bank_account:write` 读写银行账号信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bank_name` | `string` | 银行名称。当在飞书人事找不到银行下拉选项，手动填写文本时，请通过此字段获取结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bank_account_number` | `string` | 银行账号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `account_holder` | `string` | 开户人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `branch_name` | `string` | 支行名称。当在飞书人事找不到支行下拉选项，手动填写文本时，请通过此字段获取结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bank_id_v2` | `string` | 银行 ID，详细信息可通过[【查询银行信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-bank/search)查询。当在飞书人事选择具体银行下拉选项时，请通过此字段获取结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `branch_id_v2` | `string` | 支行 ID，要求必须为填入银行的支行，详细信息可通过[【查询支行信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-bank_branch/search)查询。当在飞书人事选择具体支行下拉选项时，请通过此字段获取结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家/地区 - 可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bank_account_usage` | `enum\[\]` | 银行卡用途 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name: bank_account   - custom_api_name: bank_account_usage |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bank_account_type` | `enum` | 银行卡类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name: bank_account   - custom_api_name: bank_account_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `payment_type` | `enum` | 分配方式 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name: bank_account   - custom_api_name: payment_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `payment_rate` | `string` | 分配比例 - 数字类型，最多精确两位小数 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `payment_amount` | `string` | 分配金额 - 数字类型，最多精确两位小数 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `priority` | `int` | 分配优先级 - 升序，即该值越小，优先级越高 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `currency_id` | `string` | 货币id，可通过[【查询货币信息v2】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-currency/search)查询 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `IBAN` | `string` | 国际银行账号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `national_id_list` | `national_id\[\]` | 证件<br>**字段权限要求（满足任一）**： `corehr:person.national_id:read` 获取证件信息 `corehr:person.national_id:write` 读写证件信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `national_id_type_id` | `string` | 国家证件类型，可通过[【查询单个国家证件类型】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/national_id_type/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `national_id_number` | `string` | 证件号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `issue_date` | `string` | 证件签发日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_date` | `string` | 证件到期日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家/地区 - 可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `issued_by` | `string` | 证件签发机构 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dependent_list` | `dependent\[\]` | 家庭成员列表<br>**字段权限要求（满足任一）**： `corehr:person.dependent:read` 获取家庭成员信息 `corehr:person.dependent:write` 读写家庭成员信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `person_name` | 姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_primary` | `string` | 姓 - 本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_first_name` | `string` | 名 - 本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家/地区 - 可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name_type` | `enum` | 姓名类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：person_name   - custom_api_name：name_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_first_name_2` | `string` | 名 - 第二本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_primary_2` | `string` | 姓 - 第二本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `additional_name` | `string` | 别名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `additional_name_type` | `enum` | 补充姓名类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：person_name   - custom_api_name：additional_name_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `first_name` | `string` | 名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_name` | `string` | 全名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hereditary` | `string` | 姓氏称谓 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_name` | `string` | 自定义姓名（未传入时，姓名将默认根据所属国家 / 地区规则对相关姓、名字段拼接） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_local_name` | `string` | 本地文字的自定义姓名（未传入时，本地文字的姓名将默认根据所属国家 / 地区规则对本地文字的相关姓、名字段拼接） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `middle_name` | `string` | 中间名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name_primary` | `string` | 姓 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `secondary` | `string` | 第二姓氏 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tertiary` | `string` | 婚后姓氏 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `social` | `enum` | 尊称 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：person_name     - custom_api_name：social |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `enum` | 头衔 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：person_name     - custom_api_name：title |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_middle_name` | `string` | 本地中间名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_secondary` | `string` | 第二姓氏 - 本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_name_local_and_western_script` | `string` | 展示姓名（本地和西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_name_local_script` | `string` | 展示姓名（本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_name_western_script` | `string` | 展示姓名（西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `relationship` | `enum` | 关系 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `gender` | `enum` | 性别 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：    - object_api_name：person   - custom_api_name：gender |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date_of_birth` | `string` | 生日 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `nationality_id_v2` | `string` | 国籍 ID，可通过[【查询国籍信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-nationality/search)查询 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `national_id_list` | `national_id\[\]` | 证件号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `national_id_type_id` | `string` | 国家证件类型，可通过[【查询单个国家证件类型】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/national_id_type/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `national_id_number` | `string` | 证件号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `issue_date` | `string` | 证件签发日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_date` | `string` | 证件到期日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家/地区 - 可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `issued_by` | `string` | 证件签发机构 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `spouses_working_status` | `enum` | 配偶工作状态 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：dependent   - custom_api_name：spouses_working_status |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_this_person_covered_by_health_insurance` | `boolean` | 包含家属医疗保险 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_this_person_allowed_for_tax_deduction` | `boolean` | 允许家属抵扣税款 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dependent_name` | `string` | 家庭成员姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employer` | `string` | 工作单位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job` | `string` | 岗位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone` | `phone` | 电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `international_area_code` | `enum` | 国家区号， - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：phone   - custom_api_name：international_area_code |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `formatted_phone_number` | `string` | 完整电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `device_type` | `enum` | 设备类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name：phone  - custom_api_name：device_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_usage` | `enum` | 电话用途 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name：phone  - custom_api_name：phone_usage |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address` | `address` | 联系地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_local_script` | `string` | 完整地址（本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_western_script` | `string` | 完整地址（西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_id` | `string` | 地址 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家/地区 - 可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_id` | `string` | 主要行政区 - 可通过[【查询省份/主要行政区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_id` | `string` | 城市（该字段待作废，请勿使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `distinct_id` | `string` | 区/县（该字段待作废，请勿使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_id_v2` | `string` | 城市 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `district_id_v2` | `string` | 区/县 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line1` | `string` | 地址行 1 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line2` | `string` | 地址行 2 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line3` | `string` | 地址行 3 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line4` | `string` | 地址行 4 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line5` | `string` | 地址行 5 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line6` | `string` | 地址行 6 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line7` | `string` | 地址行 7 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line8` | `string` | 地址行 8 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line9` | `string` | 地址行 9 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line1` | `string` | 地址行 1（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line2` | `string` | 地址行 2（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line3` | `string` | 地址行 3（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line4` | `string` | 地址行 4（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line5` | `string` | 地址行 5（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line6` | `string` | 地址行 6（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line7` | `string` | 地址行 7（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line8` | `string` | 地址行 8（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line9` | `string` | 地址行 9（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `postal_code` | `string` | 邮政编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_type_list` | `enum\[\]` | 地址类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `birth_certificate_of_child` | `file\[\]` | 出生证明 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 上传文件ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 文件名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `emergency_contact_list` | `emergency_contact\[\]` | 紧急联系人列表<br>**字段权限要求（满足任一）**： `corehr:person.emergency_contact:read` 获取紧急联系人信息 `corehr:person.emergency_contact:write` 读写紧急联系人信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `person_name` | 姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_primary` | `string` | 姓 - 本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_first_name` | `string` | 名 - 本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家/地区 - 可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name_type` | `enum` | 姓名类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：person_name   - custom_api_name：name_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_first_name_2` | `string` | 名 - 第二本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_primary_2` | `string` | 姓 - 第二本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `additional_name` | `string` | 别名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `additional_name_type` | `enum` | 补充姓名类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：person_name   - custom_api_name：additional_name_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `first_name` | `string` | 名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_name` | `string` | 全名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hereditary` | `string` | 姓氏称谓 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_name` | `string` | 自定义姓名（未传入时，姓名将默认根据所属国家 / 地区规则对相关姓、名字段拼接） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_local_name` | `string` | 本地文字的自定义姓名（未传入时，本地文字的姓名将默认根据所属国家 / 地区规则对本地文字的相关姓、名字段拼接） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `middle_name` | `string` | 中间名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name_primary` | `string` | 姓 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `secondary` | `string` | 第二姓氏 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tertiary` | `string` | 婚后姓氏 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `social` | `enum` | 尊称 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：person_name     - custom_api_name：social |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `enum` | 头衔 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：person_name     - custom_api_name：title |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_middle_name` | `string` | 本地中间名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_secondary` | `string` | 第二姓氏 - 本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_name_local_and_western_script` | `string` | 展示姓名（本地和西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_name_local_script` | `string` | 展示姓名（本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_name_western_script` | `string` | 展示姓名（西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `relationship` | `enum` | 关系 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_ist` | `phone\[\]` | 电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `international_area_code` | `enum` | 国家区号， - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：phone   - custom_api_name：international_area_code |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `formatted_phone_number` | `string` | 完整电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `device_type` | `enum` | 设备类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name：phone  - custom_api_name：device_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_usage` | `enum` | 电话用途 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name：phone  - custom_api_name：phone_usage |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_list` | `phone\[\]` | 电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `international_area_code` | `enum` | 国家区号， - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：phone   - custom_api_name：international_area_code |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `formatted_phone_number` | `string` | 完整电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `device_type` | `enum` | 设备类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name：phone  - custom_api_name：device_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_usage` | `enum` | 电话用途 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name：phone  - custom_api_name：phone_usage |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `legal_name` | `string` | 法定姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address` | `address` | 联系地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_local_script` | `string` | 完整地址（本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_western_script` | `string` | 完整地址（西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_id` | `string` | 地址 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家/地区 - 可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_id` | `string` | 主要行政区 - 可通过[【查询省份/主要行政区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_id` | `string` | 城市（该字段待作废，请勿使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `distinct_id` | `string` | 区/县（该字段待作废，请勿使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_id_v2` | `string` | 城市 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `district_id_v2` | `string` | 区/县 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line1` | `string` | 地址行 1 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line2` | `string` | 地址行 2 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line3` | `string` | 地址行 3 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line4` | `string` | 地址行 4 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line5` | `string` | 地址行 5 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line6` | `string` | 地址行 6 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line7` | `string` | 地址行 7 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line8` | `string` | 地址行 8 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line9` | `string` | 地址行 9 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line1` | `string` | 地址行 1（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line2` | `string` | 地址行 2（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line3` | `string` | 地址行 3（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line4` | `string` | 地址行 4（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line5` | `string` | 地址行 5（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line6` | `string` | 地址行 6（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line7` | `string` | 地址行 7（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line8` | `string` | 地址行 8（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line9` | `string` | 地址行 9（非拉丁语系的本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `postal_code` | `string` | 邮政编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_type_list` | `enum\[\]` | 地址类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date_entered_workforce` | `string` | 参加工作日期<br>**字段权限要求（满足任一）**： `corehr:person.date_entered_workforce:read` 获取参加工作日期 `corehr:person.date_entered_workforce:write` 读写参加工作日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `working_years` | `int` | 工龄 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `profile_image_id` | `string` | 头像资源的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email_address` | `string` | 个人邮箱地址 - 计算字段，取自 person_info.email_list 中   - email_usage: home   - is_primary: true<br>**字段权限要求（满足任一）**： `corehr:person.email:read` 获取个人邮箱信息 `corehr:person.email:write` 读写个人邮箱信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `age` | `int` | 年龄<br>**字段权限要求（满足任一）**： `corehr:person.date_of_birth:read` 获取生日信息 `corehr:person.date_of_birth:write` 读写生日信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `highest_level_of_education` | `education` | 最高学历教育经历<br>**字段权限要求（满足任一）**： `corehr:person.education:read` 获取教育经历信息 `corehr:person.education:write` 读写教育经历信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `school` | `i18n\[\]` | 学校 - 自定义名称时返回该字段 - 下拉框选择的返回 school_name 字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `level_of_education` | `enum` | 学历 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 开始日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_of_study` | `i18n\[\]` | 专业 - 自定义名称时返回该字段 - 下拉框选择的返回 field_of_study_name 字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `degree` | `enum` | 学位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `school_name` | `enum` | 学校名称 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：education   - custom_api_name：school_name - 自定义名称时返回 school 字段 - 下拉框选择的返回该字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_of_study_name` | `enum` | 专业名称 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：education   - custom_api_name：field_of_study_name - 自定义名称时返回 field_of_study 字段 - 下拉框选择的返回该字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家地区ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expected_end_date` | `string` | 预期结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `highest_degree_of_education` | `education` | 最高学位教育经历<br>**字段权限要求（满足任一）**： `corehr:person.education:read` 获取教育经历信息 `corehr:person.education:write` 读写教育经历信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `school` | `i18n\[\]` | 学校 - 自定义名称时返回该字段 - 下拉框选择的返回 school_name 枚举字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `level_of_education` | `enum` | 学历 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 开始日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_of_study` | `i18n\[\]` | 专业 - 自定义名称时返回该字段 - 下拉框选择的返回 field_of_study_name 字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `degree` | `enum` | 学位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `school_name` | `enum` | 学校名称 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：education   - custom_api_name：school_name - 自定义名称时返回 school 字段 - 下拉框选择的返回该字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_of_study_name` | `enum` | 专业名称 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：education   - custom_api_name：field_of_study_name - 自定义名称时返回 field_of_study 字段 - 下拉框选择的返回该字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家地区ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expected_end_date` | `string` | 预期结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `personal_profile` | `personal_profile\[\]` | 个人资料附件<br>**字段权限要求（满足任一）**： `corehr:person.personal_profile:read` 获取个人资料信息 `corehr:person.personal_profile:write` 读写个人资料信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `personal_profile_type` | `enum` | 资料类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `files` | `file\[\]` | 上传文件列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 上传文件ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 文件名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `native_region` | `string` | 籍贯 ID<br>**字段权限要求（满足任一）**： `corehr:person.native_region:read` 获取籍贯信息 `corehr:person.native_region:write` 读写籍贯信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hukou_type` | `enum` | 户口类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name: person_info_chn   - custom_api_name: hukou_type<br>**字段权限要求（满足任一）**： `corehr:person.hukou:read` 获取户口信息 `corehr:person.hukou:write` 读写户口信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hukou_location` | `string` | 户口所在地<br>**字段权限要求（满足任一）**： `corehr:person.hukou:read` 获取户口信息 `corehr:person.hukou:write` 读写户口信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `political_affiliations` | `enum\[\]` | 政治面貌 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name：person_info_chn  - custom_api_name：political_affiliation <br>**字段权限要求（满足任一）**： `corehr:person.political_affiliation:read` 获取政治面貌信息 `corehr:person.political_affiliation:write` 读写个人政治面貌信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `talent_id` | `string` | 人才 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**字段权限要求（满足任一）**： `corehr:person.custom_field:read` 获取个人信息自定义字段信息 `corehr:person.custom_field:write` 读写个人信息中的自定义字段信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `national_id_number` | `string` | 居民身份证件号码<br>**字段权限要求（满足任一）**： `corehr:person.national_id:read` 获取证件信息 `corehr:person.national_id:write` 读写证件信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `family_address` | `string` | 家庭地址<br>**字段权限要求（满足任一）**： `corehr:person.address:read` 读取个人地址信息 `corehr:person.address:write` 读写个人地址信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `born_country_region` | `string` | 出生国家/地区<br>**字段权限要求（满足任一）**： `corehr:person.born_country_region:read` 获取出生国家/地区信息 `corehr:person.born_country_region:write` 读写出生国家/地区信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_disabled` | `boolean` | 是否残疾<br>**字段权限要求（满足任一）**： `corehr:person.is_disabled:read` 获取残疾信息 `corehr:person.is_disabled:write` 读写残疾信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `disable_card_number` | `string` | 残疾证号<br>**字段权限要求（满足任一）**： `corehr:person.is_disabled:read` 获取残疾信息 `corehr:person.is_disabled:write` 读写残疾信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_martyr_family` | `boolean` | 是否烈属<br>**字段权限要求（满足任一）**： `corehr:person.martyr_family:read` 获取烈属信息 `corehr:person.martyr_family:write` 读写烈属信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `martyr_card_number` | `string` | 烈属证号<br>**字段权限要求（满足任一）**： `corehr:person.martyr_family:read` 获取烈属信息 `corehr:person.martyr_family:write` 读写烈属信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_old_alone` | `boolean` | 是否孤老<br>**字段权限要求（满足任一）**： `corehr:person.is_old_alone:read` 获取孤老信息 `corehr:person.is_old_alone:write` 读写孤老信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `resident_taxes` | `resident_tax\[\]` | 居民身份信息<br>**字段权限要求（满足任一）**： `corehr:person.resident_tax:read` 获取居民身份信息 `corehr:person.resident_tax:write` 读写居民身份信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `year_resident_tax` | `string` | 年度 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `resident_status` | `enum` | 居民身份 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name: resident_tax  - custom_api_name: resident_status |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tax_country_region_id` | `string` | 国家/地区 - 可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**字段权限要求（满足任一）**： `corehr:person.resident_tax_custom_field:read` 获取居民身份自定义字段信息 `corehr:person.resident_tax_custom_field:write` 读写居民身份自定义字段信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(123, 123.23, true, [\"id1\",\"id2\], 2006-01-02 15:04:05]) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `first_entry_time` | `string` | 首次入境日期<br>**字段权限要求（满足任一）**： `corehr:person.entry_leave_time:read` 获取出入境日期信息 `corehr:person.entry_leave_time:write` 读写出入境日期信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `leave_time` | `string` | 预计离境日期<br>**字段权限要求（满足任一）**： `corehr:person.entry_leave_time:read` 获取出入境日期信息 `corehr:person.entry_leave_time:write` 读写出入境日期信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `religion` | `enum` | 宗教信仰 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name：person   - custom_api_name：religion<br>**字段权限要求（满足任一）**： `corehr:person.religion:read` 查看宗教信仰信息 `corehr:person.religion:write` 读写宗教信仰信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `working_years_v2` | `number(float)` | 工龄 浮点类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**字段权限要求**： `corehr:employment.custom_field:read` 获取雇佣信息自定义字段信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `noncompete_status` | `enum` | 竞业状态 - 可通过[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：employment   - custom_api_name：noncompete_status |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `past_offboarding` | `boolean` | 是否历史离职人员 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `regular_employee_start_date` | `string` | 转正式日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `external_id` | `string` | 外部系统 ID , 可存储租户系统中的员工 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `times_employed` | `int` | 入职次数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `recruitment_type` | `enum` | 招聘来源 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：employment   - custom_api_name：recruitment_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_url` | `string` | 员工头像 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `primary_contract_id` | `string` | 主合同 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_start_date` | `string` | 主合同开始日期<br>**字段权限要求（满足任一）**： `corehr:contract.period:read` 获取合同期限信息 `corehr:contract.period:write` 读写合同期限信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_end_date` | `string` | 主合同到期日期<br>**字段权限要求（满足任一）**： `corehr:contract.period:read` 获取合同期限信息 `corehr:contract.period:write` 读写合同期限信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_expected_end_date` | `string` | 主合同预计到期日期<br>**字段权限要求（满足任一）**： `corehr:contract.period:read` 获取合同期限信息 `corehr:contract.period:write` 读写合同期限信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `pay_group_id` | `string` | 所属薪资组 ID<br>**字段权限要求**： `corehr:employment.pay_group:read` 获取薪资组信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `assignment_pay_group_id` | `string` | 所属外派薪资组 ID<br>**字段权限要求**： `corehr:employment.assignment_pay_group:read` 获取员工所属外派薪资组 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `international_assignment` | `boolean` | 是否外派<br>**字段权限要求**： `corehr:employment.assignment:read` 获取员工外派信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_calendar_id` | `string` | 工作日历 ID - 可通过[【查询工作日历】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/leave/work_calendar)查询 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `basic_department` | 部门基本信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 部门 ID - 类型与 department_id_type 一致，转换失败时返回空值 - 请使用 id_v2 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id_v2` | `string` | 部门 ID - 类型与 department_id_type 一致，转换失败时返回空值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_name` | `i18n\[\]` | 部门名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `direct_manager` | `basic_employee` | 直接上级基本信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id` | `string` | 雇佣 ID - 类型与 user_id_type 一致 - 请使用 employment_id_v2 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id_v2` | `string` | 雇佣 ID - 类型与 user_id_type 一致，转换失败时返回空值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employee_number` | `string` | 工号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email_address` | `string` | 邮箱地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `person_info` | `basic_person_info` | 基本个人信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `person_id` | `string` | 个人信息 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `preferred_name` | `string` | 常用名 - 基于 local_primary、local_first_name、name_primary、first_name 等字段计算获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `preferred_local_full_name` | `string` | 常用本地全名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `preferred_english_full_name` | `string` | 常用英文全名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dotted_line_manager` | `basic_employee` | 虚线上级基本信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id` | `string` | 雇佣 ID - 类型与 user_id_type 一致 - 请使用 employment_id_v2 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id_v2` | `string` | 雇佣 ID - 类型与 user_id_type 一致，转换失败时返回空值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employee_number` | `string` | 工号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email_address` | `string` | 邮箱地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `person_info` | `basic_person_info` | 基本个人信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `person_id` | `string` | 个人信息 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `preferred_name` | `string` | 常用名 - 基于 local_primary、local_first_name、name_primary、first_name 等字段计算获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `preferred_local_full_name` | `string` | 常用本地全名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `preferred_english_full_name` | `string` | 常用英文全名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `time_zone` | `string` | 时区 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `service_company` | `string` | 任职公司<br>**字段权限要求**： `corehr:job_data.service_company:read` 获取任职公司 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `compensation_type` | `enum` | 薪资类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：job_data   - custom_api_name：compensation_type<br>**字段权限要求**： `corehr:job_data.compensation_type:read` 获取薪资类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_shift` | `enum` | 排班类型<br>**字段权限要求**： `corehr:job_data.work_shift:read` 获取排班信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_org` | `string` | 自定义组织 - 功能灰度中，有需要请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**字段权限要求（满足任一）**： `corehr:employment.custom_org_field:read` 获取员工的自定义组织信息 `corehr:employment.custom_org_field:write` 读写员工的自定义组织信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `seniority_adjust_information_list` | `seniority_adjust_information\[\]` | 司龄调整信息<br>**字段权限要求（满足任一）**： `corehr:employment.seniority_adjust_information:read` 获取员工司龄调整信息 `corehr:employment.seniority_adjust_information:write` 读写员工司龄调整信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `seniority_adjustment_type` | `enum` | 调整类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：seniority_adjust_information   - custom_api_name：seniority_adjustment_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 开始日期 - 格式： yyyy-mm-dd |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 结束日期 - 格式： yyyy-mm-dd |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `seniority_adjustment` | `number(float)` | 调整值 - 精确度：两位小数 - 单位：年 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reasons_for_seniority_adjustment` | `string` | 调整原因 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 - 具体支持的对象请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_direct_bps` | `employment_bp` | 员工直属 BP 信息，当员工所在部门、属地无 BP 时，会上钻找到最近的 BP<br>**字段权限要求**： `corehr:employee.bp:read` 查看员工的部分 BP 信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hrbp_ids` | `string\[\]` | 员工直属 HRBP 雇佣 ID，若员工是部门负责人，且同部门 HRBP 在权限中配置了 HRBP 不可见部门负责人，则在结果中不会出现该 HRBP - 类型与 user_id_type 一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `location_bp_ids` | `string\[\]` | 员工直属属地 BP 雇佣 ID - 类型与 user_id_type 一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_all_bps` | `employment_bp` | 员工全部 BP 信息<br>**字段权限要求**： `corehr:employee.all_bp:read` 查看员工的全部 BP 信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hrbp_ids` | `string\[\]` | 员工所在部门及上级部门全部 HRBP 雇佣 ID - 类型与 user_id_type 一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `location_bp_ids` | `string\[\]` | 员工所在部门及上级部门全部属地 BP 雇佣 ID - 类型与 user_id_type 一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_type` | `enum` | 当前所属合同类型 - 可通过[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)查询   - object_api_name：contract   - custom_api_name：contract_type<br>**字段权限要求**： `corehr:employment.contract_type:read` 获取员工合同类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `archive_cpst_plan_id` | `string` | 当前所属薪资方案 ID - 可结合[批量查询薪资方案](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/compensation-v1/plan/list)接口使用<br>**字段权限要求**： `corehr:employment.archive_cpst_plan:read` 获取员工薪资方案 |
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
                "employment_id_v2": "6893014062142064135",
                "ats_application_id": "6838119494196871234",
                "prehire_id": "7023239238976141133",
                "employee_number": "1000000",
                "employee_type_id": "6971090097697521314",
                "employee_subtype_id": "6971090097697521317",
                "department_id": "6893014062142064135",
                "department_id_v2": "6893014062142064135",
                "job_level_id": "6893014062142064135",
                "job_level": {
                    "id": "4692446793125560154",
                    "level_order": 9999,
                    "code": "VQzo/BSonp8l6PmcZ+VlDhkd2595LMkhyBAGX6HAlCY=",
                    "name": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ],
                    "description": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ],
                    "active": true,
                    "custom_fields": [
                        {
                            "custom_api_name": "name",
                            "name": {
                                "zh_cn": "自定义姓名",
                                "en_us": "Custom Name"
                            },
                            "type": 1,
                            "value": "\"231\""
                        }
                    ]
                },
                "pathway_id": "6893014062142064135",
                "pathway": {
                    "id": "4692446793125560154",
                    "code": "VQzo/BSonp8l6PmcZ+VlDhkd2595LMkhyBAGX6HAlCY=",
                    "name": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ],
                    "description": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ],
                    "active": true,
                    "custom_fields": [
                        {
                            "custom_api_name": "name",
                            "name": {
                                "zh_cn": "自定义姓名",
                                "en_us": "Custom Name"
                            },
                            "type": 1,
                            "value": "\"231\""
                        }
                    ]
                },
                "job_grade_id": "6893014062142064135",
                "work_location_id": "6893014062142064135",
                "job_family_id": "6893014062142064135",
                "job_family": {
                    "id": "4698019107896524633",
                    "name": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ],
                    "active": true,
                    "parent_id": "4698020757495316313",
                    "effective_time": "2020-05-01 00:00:00",
                    "expiration_time": "2020-05-02 00:00:00",
                    "code": "123456",
                    "custom_fields": [
                        {
                            "custom_api_name": "name",
                            "name": {
                                "zh_cn": "自定义姓名",
                                "en_us": "Custom Name"
                            },
                            "type": 1,
                            "value": "\"231\""
                        }
                    ]
                },
                "position_id": "6893014062142064135",
                "position": {
                    "position_id": "4692446793125560154",
                    "code": "A01234",
                    "names": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ],
                    "descriptions": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ],
                    "active": true
                },
                "job_id": "6893014062142064135",
                "job": {
                    "id": "4698040628992333549",
                    "code": "JP422119",
                    "name": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ],
                    "description": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ],
                    "active": true,
                    "job_title": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ],
                    "pathway_id": "4719519211875096301",
                    "job_family_id_list": [
                        "4719519211875096301"
                    ],
                    "job_level_id_list": [
                        "4719519212005299950"
                    ],
                    "working_hours_type_id": "6890452208593372679",
                    "effective_time": "2020-01-01 00:00:00",
                    "expiration_time": "2021-01-01 00:00:00",
                    "custom_fields": [
                        {
                            "field_name": "name",
                            "value": "Sandy"
                        }
                    ]
                },
                "company_id": "6893014062142064135",
                "working_hours_type_id": "6893014062142064135",
                "tenure": "0.01",
                "seniority_date": "2021-03-16",
                "effective_date": "2021-03-16",
                "primary_employment": true,
                "probation_period": 16,
                "on_probation": true,
                "probation_end_date": "2022-08-01",
                "direct_manager_id": "7027024823985411287",
                "dotted_line_manager_id": "7027024823985411782",
                "direct_manager_id_v2": "7027024823985411287",
                "dotted_line_manager_id_v2": "7027024823985411782",
                "employment_type": {
                    "enum_name": "phone_type",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "employment_status": {
                    "enum_name": "phone_type",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "expiration_date": "2022-08-16",
                "reason_for_offboarding": {
                    "enum_name": "phone_type",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "email_address": "test@163.com",
                "work_email_list": [
                    {
                        "email": "1234567@example.feishu.cn",
                        "email_usage": {
                            "enum_name": "phone_type",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        }
                    }
                ],
                "cost_center_list": [
                    {
                        "cost_center_id": "6950635856373745165",
                        "rate": 100,
                        "new_rate": 50.2
                    }
                ],
                "rehire": {
                    "enum_name": "phone_type",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "rehire_employment_id": "7164286667866966659",
                "person_info": {
                    "person_id": "6919733936050406926",
                    "phone_number": "13649211111",
                    "legal_name": "张三",
                    "preferred_name": "刘梓新(Henry)",
                    "additional_name": "梓新",
                    "preferred_local_full_name": "刘梓新",
                    "preferred_english_full_name": "Henry",
                    "name_list": [
                        {
                            "local_primary": "黄",
                            "local_first_name": "四",
                            "country_region_id": "6862995757234914824",
                            "name_type": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "local_first_name_2": "五",
                            "local_primary_2": "王",
                            "additional_name": "别名",
                            "additional_name_type": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "first_name": "帅",
                            "full_name": "王大帅",
                            "hereditary": "王",
                            "custom_name": "王大帅",
                            "custom_local_name": "王大帅",
                            "middle_name": "大",
                            "name_primary": "王",
                            "secondary": "王",
                            "tertiary": "王",
                            "social": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "title": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "local_middle_name": "大",
                            "local_secondary": "王",
                            "display_name_local_and_western_script": "王大帅",
                            "display_name_local_script": "王大帅",
                            "display_name_western_script": "王大帅"
                        }
                    ],
                    "gender": {
                        "enum_name": "phone_type",
                        "display": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ]
                    },
                    "date_of_birth": "2020-01-01",
                    "nationality_id_v2": "6862995757234914821",
                    "race": {
                        "enum_name": "phone_type",
                        "display": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ]
                    },
                    "marital_status": {
                        "enum_name": "phone_type",
                        "display": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ]
                    },
                    "phone_list": [
                        {
                            "international_area_code": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "phone_number": "010-12345678",
                            "formatted_phone_number": "+86 010-12345678",
                            "device_type": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "phone_usage": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "is_primary": true,
                            "is_public": true
                        }
                    ],
                    "address_list": [
                        {
                            "full_address_local_script": "中国北京北京",
                            "full_address_western_script": "Beijing, Beijing, China,",
                            "address_id": "6989822217869624863",
                            "country_region_id": "6862995757234914824",
                            "region_id": "6863326815667095047",
                            "city_id": "6863333254578046471",
                            "distinct_id": "6863333516579440141",
                            "city_id_v2": "6863333254578046471",
                            "district_id_v2": "6863333516579440141",
                            "address_line1": "丹佛测试地址-纽埃时区",
                            "address_line2": "PoewH",
                            "address_line3": "PoewH",
                            "address_line4": "jmwJc",
                            "address_line5": "jmwJc",
                            "address_line6": "jmwJc",
                            "address_line7": "jmwJc",
                            "address_line8": "rafSu",
                            "address_line9": "McPRG",
                            "local_address_line1": "丹佛测试地址-纽埃时区",
                            "local_address_line2": "PoewH",
                            "local_address_line3": "PoewH",
                            "local_address_line4": "jmwJc",
                            "local_address_line5": "jmwJc",
                            "local_address_line6": "jmwJc",
                            "local_address_line7": "jmwJc",
                            "local_address_line8": "rafSu",
                            "local_address_line9": "McPRG",
                            "postal_code": "611530",
                            "address_type_list": [
                                {
                                    "enum_name": "phone_type",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                }
                            ],
                            "is_primary": true,
                            "is_public": true,
                            "custom_fields": [
                                {
                                    "custom_api_name": "name",
                                    "name": {
                                        "zh_cn": "自定义姓名",
                                        "en_us": "Custom Name"
                                    },
                                    "type": 1,
                                    "value": "\"231\""
                                }
                            ],
                            "city_subdivision_1": "123",
                            "city_subdivision_2": "123",
                            "region_subdivision_1": "123",
                            "region_subdivision_2": "123"
                        }
                    ],
                    "email_list": [
                        {
                            "email": "1234567@example.feishu.cn",
                            "is_primary": true,
                            "is_public": true,
                            "email_usage": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            }
                        }
                    ],
                    "work_experience_list": [
                        {
                            "company_organization": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ],
                            "department": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ],
                            "job": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ],
                            "description": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ],
                            "start_date": "2020-01-01",
                            "end_date": "2020-01-01",
                            "custom_fields": [
                                {
                                    "custom_api_name": "name",
                                    "name": {
                                        "zh_cn": "自定义姓名",
                                        "en_us": "Custom Name"
                                    },
                                    "type": 1,
                                    "value": "\"231\""
                                }
                            ]
                        }
                    ],
                    "education_list": [
                        {
                            "school": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ],
                            "level_of_education": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "start_date": "2011-09-01",
                            "end_date": "2015-06-30",
                            "field_of_study": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ],
                            "degree": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "school_name": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "field_of_study_name": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "country_region_id": "1",
                            "expected_end_date": "2011-09-01",
                            "custom_fields": [
                                {
                                    "custom_api_name": "name",
                                    "name": {
                                        "zh_cn": "自定义姓名",
                                        "en_us": "Custom Name"
                                    },
                                    "type": 1,
                                    "value": "\"231\""
                                }
                            ]
                        }
                    ],
                    "bank_account_list": [
                        {
                            "bank_name": "中国农业银行",
                            "bank_account_number": "6231200000001223",
                            "account_holder": "孟十五",
                            "branch_name": "中国农业银行支行",
                            "bank_id_v2": "MDBH00000001",
                            "branch_id_v2": "MDBK00000017",
                            "country_region_id": "12",
                            "bank_account_usage": [
                                {
                                    "enum_name": "phone_type",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                }
                            ],
                            "bank_account_type": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "payment_type": {
                                "enum_name": "blance",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "payment_rate": "70.21",
                            "payment_amount": "5000",
                            "priority": 1,
                            "currency_id": "12",
                            "IBAN": "CH56 0483 5012 3456 7800 9",
                            "custom_fields": [
                                {
                                    "custom_api_name": "name",
                                    "name": {
                                        "zh_cn": "自定义姓名",
                                        "en_us": "Custom Name"
                                    },
                                    "type": 1,
                                    "value": "\"231\""
                                }
                            ]
                        }
                    ],
                    "national_id_list": [
                        {
                            "national_id_type_id": "6863330041896371725",
                            "national_id_number": "1231131333",
                            "issue_date": "2020-04-01",
                            "expiration_date": "2020-05-21",
                            "country_region_id": "6862995757234914824",
                            "issued_by": "北京市公安局",
                            "custom_fields": [
                                {
                                    "custom_api_name": "name",
                                    "name": {
                                        "zh_cn": "自定义姓名",
                                        "en_us": "Custom Name"
                                    },
                                    "type": 1,
                                    "value": "\"231\""
                                }
                            ]
                        }
                    ],
                    "dependent_list": [
                        {
                            "id": "123",
                            "name": {
                                "local_primary": "黄",
                                "local_first_name": "四",
                                "country_region_id": "6862995757234914824",
                                "name_type": {
                                    "enum_name": "phone_type",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                },
                                "local_first_name_2": "五",
                                "local_primary_2": "王",
                                "additional_name": "别名",
                                "additional_name_type": {
                                    "enum_name": "phone_type",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                },
                                "first_name": "帅",
                                "full_name": "王大帅",
                                "hereditary": "王",
                                "custom_name": "王大帅",
                                "custom_local_name": "王大帅",
                                "middle_name": "大",
                                "name_primary": "王",
                                "secondary": "王",
                                "tertiary": "王",
                                "social": {
                                    "enum_name": "phone_type",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                },
                                "title": {
                                    "enum_name": "phone_type",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                },
                                "local_middle_name": "大",
                                "local_secondary": "王",
                                "display_name_local_and_western_script": "王大帅",
                                "display_name_local_script": "王大帅",
                                "display_name_western_script": "王大帅"
                            },
                            "relationship": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "gender": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "date_of_birth": "2020-01-01",
                            "nationality_id_v2": "6862995745046267401",
                            "national_id_list": [
                                {
                                    "national_id_type_id": "6863330041896371725",
                                    "national_id_number": "1231131333",
                                    "issue_date": "2020-04-01",
                                    "expiration_date": "2020-05-21",
                                    "country_region_id": "6862995757234914824",
                                    "issued_by": "北京市公安局",
                                    "custom_fields": [
                                        {
                                            "custom_api_name": "name",
                                            "name": {
                                                "zh_cn": "自定义姓名",
                                                "en_us": "Custom Name"
                                            },
                                            "type": 1,
                                            "value": "\"231\""
                                        }
                                    ]
                                }
                            ],
                            "spouses_working_status": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "is_this_person_covered_by_health_insurance": true,
                            "is_this_person_allowed_for_tax_deduction": false,
                            "custom_fields": [
                                {
                                    "custom_api_name": "name",
                                    "name": {
                                        "zh_cn": "自定义姓名",
                                        "en_us": "Custom Name"
                                    },
                                    "type": 1,
                                    "value": "\"231\""
                                }
                            ],
                            "dependent_name": "张三",
                            "employer": "海淀区交警大队",
                            "job": "保安",
                            "phone": {
                                "international_area_code": {
                                    "enum_name": "phone_type",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                },
                                "phone_number": "010-12345678",
                                "formatted_phone_number": "+86 010-12345678",
                                "device_type": {
                                    "enum_name": "phone_type",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                },
                                "phone_usage": {
                                    "enum_name": "phone_type",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                },
                                "is_primary": true,
                                "is_public": true
                            },
                            "address": {
                                "full_address_local_script": "中国北京北京",
                                "full_address_western_script": "Beijing, Beijing, China,",
                                "address_id": "6989822217869624863",
                                "country_region_id": "6862995757234914824",
                                "region_id": "6863326815667095047",
                                "city_id": "6863333254578046471",
                                "distinct_id": "6863333516579440141",
                                "city_id_v2": "6863333254578046471",
                                "district_id_v2": "6863333516579440141",
                                "address_line1": "丹佛测试地址-纽埃时区",
                                "address_line2": "PoewH",
                                "address_line3": "PoewH",
                                "address_line4": "jmwJc",
                                "address_line5": "jmwJc",
                                "address_line6": "jmwJc",
                                "address_line7": "jmwJc",
                                "address_line8": "rafSu",
                                "address_line9": "McPRG",
                                "local_address_line1": "丹佛测试地址-纽埃时区",
                                "local_address_line2": "PoewH",
                                "local_address_line3": "PoewH",
                                "local_address_line4": "jmwJc",
                                "local_address_line5": "jmwJc",
                                "local_address_line6": "jmwJc",
                                "local_address_line7": "jmwJc",
                                "local_address_line8": "rafSu",
                                "local_address_line9": "McPRG",
                                "postal_code": "611530",
                                "address_type_list": [
                                    {
                                        "enum_name": "phone_type",
                                        "display": [
                                            {
                                                "lang": "zh-CN",
                                                "value": "中文示例"
                                            }
                                        ]
                                    }
                                ],
                                "is_primary": true,
                                "is_public": true,
                                "custom_fields": [
                                    {
                                        "custom_api_name": "name",
                                        "name": {
                                            "zh_cn": "自定义姓名",
                                            "en_us": "Custom Name"
                                        },
                                        "type": 1,
                                        "value": "\"231\""
                                    }
                                ]
                            },
                            "birth_certificate_of_child": [
                                {
                                    "id": "150018109586e8ea745e47ae8feb3722dbe1d03a181336393633393133303431393831343930373235150200",
                                    "name": "document.txt"
                                }
                            ]
                        }
                    ],
                    "emergency_contact_list": [
                        {
                            "id": "123",
                            "name": {
                                "local_primary": "黄",
                                "local_first_name": "四",
                                "country_region_id": "6862995757234914824",
                                "name_type": {
                                    "enum_name": "phone_type",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                },
                                "local_first_name_2": "五",
                                "local_primary_2": "王",
                                "additional_name": "别名",
                                "additional_name_type": {
                                    "enum_name": "phone_type",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                },
                                "first_name": "帅",
                                "full_name": "王大帅",
                                "hereditary": "王",
                                "custom_name": "王大帅",
                                "custom_local_name": "王大帅",
                                "middle_name": "大",
                                "name_primary": "王",
                                "secondary": "王",
                                "tertiary": "王",
                                "social": {
                                    "enum_name": "phone_type",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                },
                                "title": {
                                    "enum_name": "phone_type",
                                    "display": [
                                        {
                                            "lang": "zh-CN",
                                            "value": "中文示例"
                                        }
                                    ]
                                },
                                "local_middle_name": "大",
                                "local_secondary": "王",
                                "display_name_local_and_western_script": "王大帅",
                                "display_name_local_script": "王大帅",
                                "display_name_western_script": "王大帅"
                            },
                            "relationship": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "phone_ist": [
                                {
                                    "international_area_code": {
                                        "enum_name": "phone_type",
                                        "display": [
                                            {
                                                "lang": "zh-CN",
                                                "value": "中文示例"
                                            }
                                        ]
                                    },
                                    "phone_number": "010-12345678",
                                    "formatted_phone_number": "+86 010-12345678",
                                    "device_type": {
                                        "enum_name": "phone_type",
                                        "display": [
                                            {
                                                "lang": "zh-CN",
                                                "value": "中文示例"
                                            }
                                        ]
                                    },
                                    "phone_usage": {
                                        "enum_name": "phone_type",
                                        "display": [
                                            {
                                                "lang": "zh-CN",
                                                "value": "中文示例"
                                            }
                                        ]
                                    },
                                    "is_primary": true,
                                    "is_public": true
                                }
                            ],
                            "phone_list": [
                                {
                                    "international_area_code": {
                                        "enum_name": "phone_type",
                                        "display": [
                                            {
                                                "lang": "zh-CN",
                                                "value": "中文示例"
                                            }
                                        ]
                                    },
                                    "phone_number": "010-12345678",
                                    "formatted_phone_number": "+86 010-12345678",
                                    "device_type": {
                                        "enum_name": "phone_type",
                                        "display": [
                                            {
                                                "lang": "zh-CN",
                                                "value": "中文示例"
                                            }
                                        ]
                                    },
                                    "phone_usage": {
                                        "enum_name": "phone_type",
                                        "display": [
                                            {
                                                "lang": "zh-CN",
                                                "value": "中文示例"
                                            }
                                        ]
                                    },
                                    "is_primary": true,
                                    "is_public": true
                                }
                            ],
                            "legal_name": "张三",
                            "custom_fields": [
                                {
                                    "custom_api_name": "name",
                                    "name": {
                                        "zh_cn": "自定义姓名",
                                        "en_us": "Custom Name"
                                    },
                                    "type": 1,
                                    "value": "\"231\""
                                }
                            ],
                            "address": {
                                "full_address_local_script": "中国北京北京",
                                "full_address_western_script": "Beijing, Beijing, China,",
                                "address_id": "6989822217869624863",
                                "country_region_id": "6862995757234914824",
                                "region_id": "6863326815667095047",
                                "city_id": "6863333254578046471",
                                "distinct_id": "6863333516579440141",
                                "city_id_v2": "6863333254578046471",
                                "district_id_v2": "6863333516579440141",
                                "address_line1": "丹佛测试地址-纽埃时区",
                                "address_line2": "PoewH",
                                "address_line3": "PoewH",
                                "address_line4": "jmwJc",
                                "address_line5": "jmwJc",
                                "address_line6": "jmwJc",
                                "address_line7": "jmwJc",
                                "address_line8": "rafSu",
                                "address_line9": "McPRG",
                                "local_address_line1": "丹佛测试地址-纽埃时区",
                                "local_address_line2": "PoewH",
                                "local_address_line3": "PoewH",
                                "local_address_line4": "jmwJc",
                                "local_address_line5": "jmwJc",
                                "local_address_line6": "jmwJc",
                                "local_address_line7": "jmwJc",
                                "local_address_line8": "rafSu",
                                "local_address_line9": "McPRG",
                                "postal_code": "611530",
                                "address_type_list": [
                                    {
                                        "enum_name": "phone_type",
                                        "display": [
                                            {
                                                "lang": "zh-CN",
                                                "value": "中文示例"
                                            }
                                        ]
                                    }
                                ],
                                "is_primary": true,
                                "is_public": true,
                                "custom_fields": [
                                    {
                                        "custom_api_name": "name",
                                        "name": {
                                            "zh_cn": "自定义姓名",
                                            "en_us": "Custom Name"
                                        },
                                        "type": 1,
                                        "value": "\"231\""
                                    }
                                ]
                            }
                        }
                    ],
                    "date_entered_workforce": "2020-10-01",
                    "working_years": 2,
                    "profile_image_id": "dfysuc8x76dsfsw",
                    "email_address": "test@163.com",
                    "age": 22,
                    "highest_level_of_education": {
                        "school": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ],
                        "level_of_education": {
                            "enum_name": "phone_type",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        },
                        "start_date": "2011-09-01",
                        "end_date": "2015-06-30",
                        "field_of_study": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ],
                        "degree": {
                            "enum_name": "phone_type",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        },
                        "school_name": {
                            "enum_name": "phone_type",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        },
                        "field_of_study_name": {
                            "enum_name": "phone_type",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        },
                        "country_region_id": "1",
                        "expected_end_date": "2011-09-01",
                        "custom_fields": [
                            {
                                "custom_api_name": "name",
                                "name": {
                                    "zh_cn": "自定义姓名",
                                    "en_us": "Custom Name"
                                },
                                "type": 1,
                                "value": "\"231\""
                            }
                        ]
                    },
                    "highest_degree_of_education": {
                        "school": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ],
                        "level_of_education": {
                            "enum_name": "phone_type",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        },
                        "start_date": "2011-09-01",
                        "end_date": "2015-06-30",
                        "field_of_study": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ],
                        "degree": {
                            "enum_name": "phone_type",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        },
                        "school_name": {
                            "enum_name": "phone_type",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        },
                        "field_of_study_name": {
                            "enum_name": "phone_type",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        },
                        "country_region_id": "1",
                        "expected_end_date": "2011-09-01",
                        "custom_fields": [
                            {
                                "custom_api_name": "name",
                                "name": {
                                    "zh_cn": "自定义姓名",
                                    "en_us": "Custom Name"
                                },
                                "type": 1,
                                "value": "\"231\""
                            }
                        ]
                    },
                    "personal_profile": [
                        {
                            "personal_profile_type": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "files": [
                                {
                                    "id": "150018109586e8ea745e47ae8feb3722dbe1d03a181336393633393133303431393831343930373235150200",
                                    "name": "document.txt"
                                }
                            ]
                        }
                    ],
                    "native_region": "6863326262618752111",
                    "hukou_type": {
                        "enum_name": "phone_type",
                        "display": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ]
                    },
                    "hukou_location": "山东省平阴县",
                    "political_affiliations": [
                        {
                            "enum_name": "phone_type",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        }
                    ],
                    "talent_id": "6863326262618752123",
                    "custom_fields": [
                        {
                            "custom_api_name": "name",
                            "name": {
                                "zh_cn": "自定义姓名",
                                "en_us": "Custom Name"
                            },
                            "type": 1,
                            "value": "\"231\""
                        }
                    ],
                    "national_id_number": "11010000000000",
                    "family_address": "6863326262618752123",
                    "born_country_region": "中国",
                    "is_disabled": true,
                    "disable_card_number": "1110000",
                    "is_martyr_family": true,
                    "martyr_card_number": "1110000",
                    "is_old_alone": true,
                    "resident_taxes": [
                        {
                            "year_resident_tax": "2023",
                            "resident_status": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "tax_country_region_id": "中国",
                            "custom_fields": [
                                {
                                    "field_name": "name",
                                    "value": "Sandy"
                                }
                            ]
                        }
                    ],
                    "first_entry_time": "2021-01-02",
                    "leave_time": "2022-01-02",
                    "religion": {
                        "enum_name": "phone_type",
                        "display": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ]
                    },
                    "working_years_v2": 2.1
                },
                "custom_fields": [
                    {
                        "custom_api_name": "name",
                        "name": {
                            "zh_cn": "自定义姓名",
                            "en_us": "Custom Name"
                        },
                        "type": 1,
                        "value": "\"231\""
                    }
                ],
                "noncompete_status": {
                    "enum_name": "phone_type",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "past_offboarding": true,
                "regular_employee_start_date": "2020-01-01",
                "external_id": "10000000",
                "times_employed": 16,
                "recruitment_type": {
                    "enum_name": "phone_type",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "avatar_url": "https://internal-api-lark-file.feishu-boe.cn/static-resource/v1/v2_a550d36b-28ef-48ad-9e50-58004beb386j~?image_size=noop&cut_type=&quality=&format=png&sticker_format=.webp",
                "primary_contract_id": "7164286667866966659",
                "contract_start_date": "2020-01-01",
                "contract_end_date": "2020-01-01",
                "contract_expected_end_date": "2020-01-01",
                "pay_group_id": "7164286667866966659",
                "assignment_pay_group_id": "7164286667866966659",
                "international_assignment": true,
                "work_calendar_id": "7164286667866966659",
                "department": {
                    "id": "4719456877659520852",
                    "id_v2": "4719456877659520852",
                    "department_name": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "direct_manager": {
                    "employment_id": "6893014062142064135",
                    "employment_id_v2": "6893014062142064135",
                    "employee_number": "1000000",
                    "email_address": "test@163.com",
                    "person_info": {
                        "person_id": "6919733936050406926",
                        "preferred_name": "刘梓新",
                        "preferred_local_full_name": "刘梓新",
                        "preferred_english_full_name": "Henry"
                    }
                },
                "dotted_line_manager": {
                    "employment_id": "6893014062142064135",
                    "employment_id_v2": "6893014062142064135",
                    "employee_number": "1000000",
                    "email_address": "test@163.com",
                    "person_info": {
                        "person_id": "6919733936050406926",
                        "preferred_name": "刘梓新",
                        "preferred_local_full_name": "刘梓新",
                        "preferred_english_full_name": "Henry"
                    }
                },
                "time_zone": "Asia/Shanghai",
                "service_company": "7174374910734141112",
                "compensation_type": {
                    "enum_name": "phone_type",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "work_shift": {
                    "enum_name": "phone_type",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "custom_org": "{\"custom_org_02\":[{\"id\":\"1\",\"rate\":\"99\"}]}",
                "seniority_adjust_information_list": [
                    {
                        "seniority_adjustment_type": {
                            "enum_name": "phone_type",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        },
                        "start_date": "2024-01-01",
                        "end_date": "2024-10-01",
                        "seniority_adjustment": 1.01,
                        "reasons_for_seniority_adjustment": "工厂停产需要减去半年工龄",
                        "custom_fields": [
                            {
                                "custom_api_name": "name",
                                "name": {
                                    "zh_cn": "自定义姓名",
                                    "en_us": "Custom Name"
                                },
                                "type": 1,
                                "value": "\"231\""
                            }
                        ]
                    }
                ],
                "employment_direct_bps": {
                    "hrbp_ids": [
                        "6863326262618752123"
                    ],
                    "location_bp_ids": [
                        "6863326262618752123"
                    ]
                },
                "employment_all_bps": {
                    "hrbp_ids": [
                        "6863326262618752123"
                    ],
                    "location_bp_ids": [
                        "6863326262618752123"
                    ]
                },
                "contract_type": {
                    "enum_name": "phone_type",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "archive_cpst_plan_id": "123456789"
            }
        ],
        "page_token": "eyJldV9uYyI6IlswLFwiNjk2MTI4Njg0NjA5Mzc4ODY4MC03MjExMDM0ODcxMjA3OTUzOTc1XCJdIn0",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1160102 | Param is invalid | 参数错误，请检查入参 |
| 400 | 1160103 | no permission | 无权限，请检查权限配置 |


