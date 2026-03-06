---
title: "查询待入职信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/pre_hire/query"
updateTime: "1756127417000"
---

# 查询待入职

该接口用于根据待入职人员 ID(支持批量)查询待入职人员信息，信息包含姓名、手机号等个人信息和任职信息。
- 延迟说明：数据库主从延迟 2s 以内，即：直接创建待入职后2s内调用此接口可能查询不到数据。
- 性能说明：本接口返回数据量较多，查询时请控制每批次数量（<10）和适当减少查询字段数(<50)


> **Tip**: 该接口会按照应用拥有的「待入职人员」的权限范围返回数据，请提前在「开发者后台 - 权限管理 - 数据权限-飞书人事(企业版)数据权限范围」中申请「待入职人员」权限范围


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/pre_hires/query |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:pre_hire:read_only` 查询待入职信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `corehr:contract.company:read` 获取合同主体信息 `corehr:contract.period:read` 获取合同期限信息 `corehr:employment.compensation_type:read` 查看员工的薪资类型信息 `corehr:employment.custom_field:read` 获取雇佣信息自定义字段信息 `corehr:employment.has_offer_salary:read` 查看是否有 Offer 薪酬 `corehr:employment.job:read` 获取员工的职务信息 `corehr:employment.job_level:read` 获取职务级别信息 `corehr:employment.non_compete_covenant:read` 查看竞业状态 `corehr:employment.pay_group:read` 获取薪资组信息 `corehr:employment.position:read` 获取员工的岗位信息 `corehr:employment.position:write` 读写员工的岗位信息 `corehr:employment.recruitment_project_id:read` 查看待入职的招聘项目 `corehr:person.address:read` 读取个人地址信息 `corehr:person.address:write` 读写个人地址信息 `corehr:person.bank_account:read` 获取银行账号列表信息 `corehr:person.bank_account:write` 读写银行账号信息 `corehr:person.born_country_region:read` 获取出生国家/地区信息 `corehr:person.custom_field:read` 获取个人信息自定义字段信息 `corehr:person.date_entered_workforce:read` 获取参加工作日期 `corehr:person.date_entered_workforce:write` 读写参加工作日期 `corehr:person.date_of_birth:read` 获取生日信息 `corehr:person.date_of_birth:write` 读写生日信息 `corehr:person.dependent:read` 获取家庭成员信息 `corehr:person.dependent:write` 读写家庭成员信息 `corehr:person.education:read` 获取教育经历信息 `corehr:person.education:write` 读写教育经历信息 `corehr:person.email:read` 获取个人邮箱信息 `corehr:person.email:write` 读写个人邮箱信息 `corehr:person.emergency_contact:read` 获取紧急联系人信息 `corehr:person.emergency_contact:write` 读写紧急联系人信息 `corehr:person.gender:read` 获取性别信息 `corehr:person.gender:write` 读写性别信息 `corehr:person.hukou:read` 获取户口信息 `corehr:person.hukou:write` 读写户口信息 `corehr:person.is_disabled:read` 获取残疾信息 `corehr:person.is_old_alone:read` 获取孤老信息 `corehr:person.legal_name:read` 获取法定姓名信息 `corehr:person.legal_name:write` 读写法定姓名信息 `corehr:person.marital_status:read` 获取婚姻状况信息 `corehr:person.marital_status:write` 读写婚姻状况信息 `corehr:person.martyr_family:read` 获取烈属信息 `corehr:person.martyr_family:write` 读写烈属信息 `corehr:person.national_id:read` 获取证件信息 `corehr:person.national_id:write` 读写证件信息 `corehr:person.nationality:read` 获取国籍信息 `corehr:person.native_region:read` 获取籍贯信息 `corehr:person.native_region:write` 读写籍贯信息 `corehr:person.passport_number:read` 获取护照号码 `corehr:person.personal_profile:read` 获取个人资料信息 `corehr:person.personal_profile:write` 读写个人资料信息 `corehr:person.phone:read` 获取个人手机号信息 `corehr:person.phone:write` 读写个人手机号信息 `corehr:person.political_affiliation:read` 获取政治面貌信息 `corehr:person.race:read` 获取民族/种族信息 `corehr:person.religion:read` 查看宗教信仰信息 `corehr:person.resident_tax:read` 获取居民身份信息 `corehr:person.resident_tax:write` 读写居民身份信息 `corehr:person.resident_tax_custom_field:read` 获取居民身份自定义字段信息 `corehr:person.resident_tax_custom_field:write` 读写居民身份自定义字段信息 `corehr:person.work_experience:read` 获取工作履历信息 `corehr:person.work_experience:write` 读写工作履历信息 `corehr:pre_hire.abnormal_reason_field:read` 获取待入职的异常信息 `corehr:pre_hire.check_in_data:read` 获取待入职人员的签到数据 `corehr:pre_hire.company_manual_updated:read` 查看待入职是否被更新过公司主体 `corehr:pre_hire.company_sponsored_visa:read` 查看签证要求 `corehr:pre_hire.cost_center:read` 查看待入职人员的成本中心信息 `corehr:pre_hire.flow_id:read` 获取入职流程 `corehr:pre_hire.office_address:read` 获取办公地址 `corehr:pre_hire.onboarding_address:read` 获取入职地址 `corehr:pre_hire.suspected_rehiring:read` 获取是否疑似重聘 `corehr:pre_hire.working_calendar:read` 获取工作日历 `corehr:employment.compensation_type:write` 读写员工的薪资类型信息 `corehr:employment.job_level:write` 读写员工的职务级别信息 `corehr:person.nationality:write` 读写国籍信息 `contact:user.employee_id:readonly` 获取用户 user ID `corehr:person.is_disabled:write` 读写残疾信息 `corehr:employment.non_compete_covenant:write` 读写竞业状态 `corehr:pre_hire.background_check_order_account_name:read` 获取待入职人员背调账号名称 `corehr:pre_hire.background_check_order_complete_time:read` 获取待入职人员背调完成时间 `corehr:pre_hire.background_check_order_id:read` 获取待入职人员背调订单ID `corehr:pre_hire.background_check_order_name:read` 获取待入职人员背调名称 `corehr:pre_hire.background_check_order_package_name:read` 获取待入职人员背调套餐 `corehr:pre_hire.background_check_order_result:read` 获取待入职人员背调结果 `corehr:pre_hire.background_check_order_start_time:read` 获取待入职人员背调开始时间 `corehr:pre_hire.background_check_order_status:read` 获取待入职人员背调状态 `corehr:pre_hire.background_check_order_supplier_name:read` 获取待入职人员背调供应商 `corehr:person.is_old_alone:write` 读写孤老信息 `corehr:contract.period:write` 读写合同期限信息 `corehr:person.born_country_region:write` 读写出生国家/地区信息 `corehr:pre_hire.contract_file_id:read` 待入职员工合同文件ID `corehr:contract.company:write` 读写合同主体信息 `corehr:pre_hire.cost_center:write` 读写待入职人员的成本中心信息 `corehr:pre_hire.dotted_line_manager:read` 获取待入职人员虚线上级 `corehr:person.custom_field:write` 读写个人信息中的自定义字段信息 `corehr:employment.job_grade:read` 获取职等信息 `corehr:employment.job_grade:write` 读写职等信息 `corehr:pre_hire.seniority_adjust_information:read` 获取待入职人员司龄调整信息 `corehr:person.religion:write` 读写宗教信仰信息 `corehr:job_data.work_shift:read` 获取排班信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 是 | 分页大小，最大 10<br>**示例值**：10<br>**数据校验规则**：<br>- 取值范围：`1` ～ `10` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：6891251722631890445 |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 此次调用中使用的部门 ID 类型<br>**示例值**：open_department_id<br>**可选值有**：<br>- `open_department_id`: 以 open_department_id 来标识部门 - `department_id`: 以 department_id 来标识部门 - `people_corehr_department_id`: 以 people_corehr_department_id 来标识部门<br>**默认值**：`open_department_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `pre_hire_ids` | `string\[\]` | 否 | 待入职人员 ID 列表<br>**示例值**：["7094136522860922112"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `10` |
| `fields` | `string\[\]` | 否 | 返回数据的字段列表，填写方式： - 为空时只返回 pre_hire_id - 不为空时按照传入的字段返回数据，数据结构可以参考response的数据结构，格式示例如下：     - person_info（个人信息） 字段：person_info.gender，person_info.age     - employment_info（雇佣信息） 字段：employment_info.department     - onboarding_info（入职信息） 字段：onboarding_info.onboarding_date     - probation_info（试用期信息） 字段：probation_info.probation_period     - contract_info（合同信息） 字段：contract_info.contract_type - 如果要返回所有下级，只用传上级结构体名称，例如 person_info - 返回数据越多，查询接口性能越慢，请按需填写返回字段<br>**示例值**：["employment_info.department"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |


### 请求体示例

```json
{
    "pre_hire_ids": [
        "7094136522860922112"
    ],
    "fields": [
        "employment_info.department"
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
| &nbsp;&nbsp;└ `items` | `pre_hire\[\]` | 查询待入职的信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `person_info` | `person_info` | 个人信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `person_id` | `string` | 个人信息 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 个人电话<br>**字段权限要求（满足任一）**： `corehr:person.phone:read` 获取个人手机号信息 `corehr:person.phone:write` 读写个人手机号信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `legal_name` | `string` | 法定姓名<br>**字段权限要求（满足任一）**： `corehr:person.legal_name:read` 获取法定姓名信息 `corehr:person.legal_name:write` 读写法定姓名信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `preferred_name` | `string` | 常用名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `preferred_local_full_name` | `string` | 常用本地全名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `preferred_english_full_name` | `string` | 常用英文全名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name_list` | `person_name\[\]` | 姓名列表<br>**字段权限要求（满足任一）**： `corehr:person.legal_name:read` 获取法定姓名信息 `corehr:person.legal_name:write` 读写法定姓名信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_primary` | `string` | 姓 - 本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_first_name` | `string` | 名 - 本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区，可以通过接口[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name_type` | `enum` | 姓名类型，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)姓名类型（name_type）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_first_name_2` | `string` | 名 - 第二本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_primary_2` | `string` | 姓 - 第二本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `additional_name` | `string` | 别名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `additional_name_type` | `enum` | 补充姓名类型，枚举值可查询[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：additional_name_type - object_api_name：person_name |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `social` | `enum` | 尊称，枚举值可查询[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：social - object_api_name：person_name |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `enum` | 头衔，枚举值可查询[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：title - object_api_name：person_name |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_middle_name` | `string` | 本地中间名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_secondary` | `string` | 第二姓氏 - 本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_name_local_and_western_script` | `string` | 展示姓名（本地和西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_name_local_script` | `string` | 展示姓名（本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_name_western_script` | `string` | 展示姓名（西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `gender` | `enum` | 性别，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)性别（gendar）枚举定义获得<br>**字段权限要求（满足任一）**： `corehr:person.gender:read` 获取性别信息 `corehr:person.gender:write` 读写性别信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date_of_birth` | `string` | 出生日期<br>**字段权限要求（满足任一）**： `corehr:person.date_of_birth:read` 获取生日信息 `corehr:person.date_of_birth:write` 读写生日信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `nationality_id_v2` | `string` | 国籍，可以通过[查询国籍信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-nationality/search)接口获取<br>**字段权限要求（满足任一）**： `corehr:person.nationality:read` 获取国籍信息 `corehr:person.nationality:write` 读写国籍信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `race` | `enum` | 民族，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)民族（race）枚举定义获得<br>**字段权限要求**： `corehr:person.race:read` 获取民族/种族信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `marital_status` | `enum` | 婚姻状况，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)婚姻状况（marital_status）枚举定义获得<br>**字段权限要求（满足任一）**： `corehr:person.marital_status:read` 获取婚姻状况信息 `corehr:person.marital_status:write` 读写婚姻状况信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_list` | `phone\[\]` | 电话列表，只有当满足下面所有条件时，电话在个人信息页才可见<br>**字段权限要求（满足任一）**： `corehr:person.phone:read` 获取个人手机号信息 `corehr:person.phone:write` 读写个人手机号信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `international_area_code` | `enum` | 国家区号，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)手机区号（international_area_code）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `formatted_phone_number` | `string` | 完整电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `device_type` | `enum` | 设备类型，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)设备类型（device_type）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_usage` | `enum` | 电话用途，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)电话用途（phone_usage）枚举定义获得 |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区，可以通过接口[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_id` | `string` | 主要行政区ID 可以通过[查询省份/行政区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)接口获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_id` | `string` | 城市（该字段待作废，请勿使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `distinct_id` | `string` | 区/县（该字段待作废，请勿使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_id_v2` | `string` | 城市，可以通过接口[查询城市信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-city/search)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `district_id_v2` | `string` | 区/县，可以通过接口[查询区/县信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-district/search)获取详情 |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_type_list` | `enum\[\]` | 地址类型，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)地址类型（address_type）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 值类型说明： - 1：文本 Text，“文本”和“超链接”属于该类型 - 2：布尔 Boolean - 3：数字 Number - 4：枚举 Option，“单选”和“多选”为该类型 - 5：查找 Lookup，“人员（单选）”、“人员（多选）”和个人信息中的自定义分组为该类型 - 6：自动编码 Autonumber - 7：日期时间 Datetime - 8：附件 Attachment，“附件单选”和“附件多选”为该类型 - 9：图片 Image - 10：计算字段 Calculated - 11：反向查找 Backlookup |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email_list` | `email\[\]` | 邮箱列表<br>**字段权限要求（满足任一）**： `corehr:person.email:read` 获取个人邮箱信息 `corehr:person.email:write` 读写个人邮箱信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 邮箱地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 是否为主要邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 是否为公开邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email_usage` | `enum` | 邮箱用途，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)邮箱用途（email_usage）枚举定义获得 |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 开始日期，时间格式为 2023-09-01 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 结束日期，时间格式为 2023-09-01 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 值类型说明： - 1：文本 Text，“文本”和“超链接”属于该类型 - 2：布尔 Boolean - 3：数字 Number - 4：枚举 Option，“单选”和“多选”为该类型 - 5：查找 Lookup，“人员（单选）”、“人员（多选）”和个人信息中的自定义分组为该类型 - 6：自动编码 Autonumber - 7：日期时间 Datetime - 8：附件 Attachment，“附件单选”和“附件多选”为该类型 - 9：图片 Image - 10：计算字段 Calculated - 11：反向查找 Backlookup |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `education_list` | `education\[\]` | 教育经历列表<br>**字段权限要求（满足任一）**： `corehr:person.education:read` 获取教育经历信息 `corehr:person.education:write` 读写教育经历信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `school` | `i18n\[\]` | 学校 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `level_of_education` | `enum` | 学历，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)学历（level_of_education）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 开始日期，时间格式为 2023-09-01 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 结束日期，时间格式为 2023-09-01 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_of_study` | `i18n\[\]` | 专业 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `degree` | `enum` | 学位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `school_name` | `enum` | 学校名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_of_study_name` | `enum` | 专业名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家地区ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expected_end_date` | `string` | 预期结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 值类型说明： - 1：文本 Text，“文本”和“超链接”属于该类型 - 2：布尔 Boolean - 3：数字 Number - 4：枚举 Option，“单选”和“多选”为该类型 - 5：查找 Lookup，“人员（单选）”、“人员（多选）”和个人信息中的自定义分组为该类型 - 6：自动编码 Autonumber - 7：日期时间 Datetime - 8：附件 Attachment，“附件单选”和“附件多选”为该类型 - 9：图片 Image - 10：计算字段 Calculated - 11：反向查找 Backlookup |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bank_account_list` | `bank_account\[\]` | 银行账户<br>**字段权限要求（满足任一）**： `corehr:person.bank_account:read` 获取银行账号列表信息 `corehr:person.bank_account:write` 读写银行账号信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bank_name` | `string` | 银行名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bank_account_number` | `string` | 银行账号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `account_holder` | `string` | 开户人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `branch_name` | `string` | 支行名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区，可以通过接口[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bank_account_usage` | `enum\[\]` | 银行卡用途，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)银行卡用途（bank_account_usage）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bank_account_type` | `enum` | 银行卡类型，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)银行卡类型（bank_account_type）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `payment_type` | `enum` | 分配方式，枚举值可通过文档【飞书人事枚举常量】分配方式（Payment Type）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `payment_rate` | `string` | 分配比例 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `payment_amount` | `string` | 分配金额 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `priority` | `int` | 分配优先级 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `currency_id` | `string` | 货币id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 值类型说明： - 1：文本 Text，“文本”和“超链接”属于该类型 - 2：布尔 Boolean - 3：数字 Number - 4：枚举 Option，“单选”和“多选”为该类型 - 5：查找 Lookup，“人员（单选）”、“人员（多选）”和个人信息中的自定义分组为该类型 - 6：自动编码 Autonumber - 7：日期时间 Datetime - 8：附件 Attachment，“附件单选”和“附件多选”为该类型 - 9：图片 Image - 10：计算字段 Calculated - 11：反向查找 Backlookup |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `national_id_list` | `national_id\[\]` | 证件<br>**字段权限要求（满足任一）**： `corehr:person.national_id:read` 获取证件信息 `corehr:person.national_id:write` 读写证件信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `national_id_type_id` | `string` | 国家证件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `national_id_number` | `string` | 证件号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `issue_date` | `string` | 证件签发日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_date` | `string` | 证件到期日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区，可以通过接口[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `issued_by` | `string` | 证件签发机构 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 值类型说明： - 1：文本 Text，“文本”和“超链接”属于该类型 - 2：布尔 Boolean - 3：数字 Number - 4：枚举 Option，“单选”和“多选”为该类型 - 5：查找 Lookup，“人员（单选）”、“人员（多选）”和个人信息中的自定义分组为该类型 - 6：自动编码 Autonumber - 7：日期时间 Datetime - 8：附件 Attachment，“附件单选”和“附件多选”为该类型 - 9：图片 Image - 10：计算字段 Calculated - 11：反向查找 Backlookup |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dependent_list` | `dependent\[\]` | 家庭成员列表<br>**字段权限要求（满足任一）**： `corehr:person.dependent:read` 获取家庭成员信息 `corehr:person.dependent:write` 读写家庭成员信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `person_name` | 姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_primary` | `string` | 姓 - 本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_first_name` | `string` | 名 - 本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区，可以通过接口[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name_type` | `enum` | 姓名类型，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)姓名类型（name_type）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_first_name_2` | `string` | 名 - 第二本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_primary_2` | `string` | 姓 - 第二本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `additional_name` | `string` | 别名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `additional_name_type` | `enum` | 补充姓名类型，枚举值可查询[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：additional_name_type - object_api_name：person_name |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `social` | `enum` | 尊称，枚举值可查询[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：social - object_api_name：person_name |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `enum` | 头衔，枚举值可查询[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：title - object_api_name：person_name |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `gender` | `enum` | 性别 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date_of_birth` | `string` | 生日 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `national_id_list` | `national_id\[\]` | 证件号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `national_id_type_id` | `string` | 国家证件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `national_id_number` | `string` | 证件号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `issue_date` | `string` | 证件签发日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_date` | `string` | 证件到期日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区，可以通过接口[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `issued_by` | `string` | 证件签发机构 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 值类型说明： - 1：文本 Text，“文本”和“超链接”属于该类型 - 2：布尔 Boolean - 3：数字 Number - 4：枚举 Option，“单选”和“多选”为该类型 - 5：查找 Lookup，“人员（单选）”、“人员（多选）”和个人信息中的自定义分组为该类型 - 6：自动编码 Autonumber - 7：日期时间 Datetime - 8：附件 Attachment，“附件单选”和“附件多选”为该类型 - 9：图片 Image - 10：计算字段 Calculated - 11：反向查找 Backlookup |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `spouses_working_status` | `enum` | 配偶工作状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_this_person_covered_by_health_insurance` | `boolean` | 包含家属医疗保险 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_this_person_allowed_for_tax_deduction` | `boolean` | 允许家属抵扣税款 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 值类型说明： - 1：文本 Text，“文本”和“超链接”属于该类型 - 2：布尔 Boolean - 3：数字 Number - 4：枚举 Option，“单选”和“多选”为该类型 - 5：查找 Lookup，“人员（单选）”、“人员（多选）”和个人信息中的自定义分组为该类型 - 6：自动编码 Autonumber - 7：日期时间 Datetime - 8：附件 Attachment，“附件单选”和“附件多选”为该类型 - 9：图片 Image - 10：计算字段 Calculated - 11：反向查找 Backlookup |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dependent_name` | `string` | 家庭成员姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employer` | `string` | 工作单位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job` | `string` | 岗位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone` | `phone` | 电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `international_area_code` | `enum` | 国家区号，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)手机区号（international_area_code）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `formatted_phone_number` | `string` | 完整电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `device_type` | `enum` | 设备类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_usage` | `enum` | 电话用途，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)电话用途（phone_usage）枚举定义获得 |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区，可以通过接口[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_id` | `string` | 主要行政区ID 可以通过[查询省份/行政区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)接口获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_id` | `string` | 城市（该字段待作废，请勿使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `distinct_id` | `string` | 区/县（该字段待作废，请勿使用） |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_type_list` | `enum\[\]` | 地址类型，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)地址类型（address_type）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 值类型说明： - 1：文本 Text，“文本”和“超链接”属于该类型 - 2：布尔 Boolean - 3：数字 Number - 4：枚举 Option，“单选”和“多选”为该类型 - 5：查找 Lookup，“人员（单选）”、“人员（多选）”和个人信息中的自定义分组为该类型 - 6：自动编码 Autonumber - 7：日期时间 Datetime - 8：附件 Attachment，“附件单选”和“附件多选”为该类型 - 9：图片 Image - 10：计算字段 Calculated - 11：反向查找 Backlookup |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `birth_certificate_of_child` | `file\[\]` | 出生证明 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 上传文件ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 文件名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `emergency_contact_list` | `emergency_contact\[\]` | 紧急联系人列表<br>**字段权限要求（满足任一）**： `corehr:person.emergency_contact:read` 获取紧急联系人信息 `corehr:person.emergency_contact:write` 读写紧急联系人信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `person_name` | 姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_primary` | `string` | 姓 - 本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_first_name` | `string` | 名 - 本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区，可以通过接口[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name_type` | `enum` | 姓名类型，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)姓名类型（name_type）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_first_name_2` | `string` | 名 - 第二本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_primary_2` | `string` | 姓 - 第二本地文字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `additional_name` | `string` | 别名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `additional_name_type` | `enum` | 补充姓名类型，枚举值可查询[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：additional_name_type - object_api_name：person_name |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `social` | `enum` | 尊称，枚举值可查询[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：social - object_api_name：person_name |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `enum` | 头衔，枚举值可查询[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：title - object_api_name：person_name |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `international_area_code` | `enum` | 国家区号，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)手机区号（international_area_code）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `formatted_phone_number` | `string` | 完整电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `device_type` | `enum` | 设备类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_usage` | `enum` | 电话用途 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_list` | `phone\[\]` | 电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `international_area_code` | `enum` | 国家区号，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)手机区号（international_area_code）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `formatted_phone_number` | `string` | 完整电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `device_type` | `enum` | 设备类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_usage` | `enum` | 电话用途 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `legal_name` | `string` | 法定姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 值类型说明： - 1：文本 Text，“文本”和“超链接”属于该类型 - 2：布尔 Boolean - 3：数字 Number - 4：枚举 Option，“单选”和“多选”为该类型 - 5：查找 Lookup，“人员（单选）”、“人员（多选）”和个人信息中的自定义分组为该类型 - 6：自动编码 Autonumber - 7：日期时间 Datetime - 8：附件 Attachment，“附件单选”和“附件多选”为该类型 - 9：图片 Image - 10：计算字段 Calculated - 11：反向查找 Backlookup |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要联系人,若有多个联系人，只能有一个联系人的「is_primary」为true |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date_entered_workforce` | `string` | 参加工作日期<br>**字段权限要求（满足任一）**： `corehr:person.date_entered_workforce:read` 获取参加工作日期 `corehr:person.date_entered_workforce:write` 读写参加工作日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `working_years` | `int` | 工龄 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `profile_image_id` | `string` | 头像资源的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email_address` | `string` | 邮箱地址<br>**字段权限要求（满足任一）**： `corehr:person.email:read` 获取个人邮箱信息 `corehr:person.email:write` 读写个人邮箱信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `age` | `int` | 年龄<br>**字段权限要求（满足任一）**： `corehr:person.date_of_birth:read` 获取生日信息 `corehr:person.date_of_birth:write` 读写生日信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `highest_level_of_education` | `education` | 最高学历教育经历<br>**字段权限要求（满足任一）**： `corehr:person.education:read` 获取教育经历信息 `corehr:person.education:write` 读写教育经历信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `school` | `i18n\[\]` | 学校 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `level_of_education` | `enum` | 学历，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)学历（level_of_education）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 开始日期，时间格式为 2023-09-01 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 结束日期，时间格式为 2023-09-01 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_of_study` | `i18n\[\]` | 专业 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `degree` | `enum` | 学位，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)学位（degree）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `school_name` | `enum` | 学校名称，枚举值可查询[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：school_name - object_api_name：education |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_of_study_name` | `enum` | 专业名称，枚举值可查询[获取字段详情](/ssl：ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：field_of_study_name - object_api_name：education |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区，可以通过接口[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expected_end_date` | `string` | 预期结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 值类型说明： - 1：文本 Text，“文本”和“超链接”属于该类型 - 2：布尔 Boolean - 3：数字 Number - 4：枚举 Option，“单选”和“多选”为该类型 - 5：查找 Lookup，“人员（单选）”、“人员（多选）”和个人信息中的自定义分组为该类型 - 6：自动编码 Autonumber - 7：日期时间 Datetime - 8：附件 Attachment，“附件单选”和“附件多选”为该类型 - 9：图片 Image - 10：计算字段 Calculated - 11：反向查找 Backlookup |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `highest_degree_of_education` | `education` | 最高学位教育经历<br>**字段权限要求（满足任一）**： `corehr:person.education:read` 获取教育经历信息 `corehr:person.education:write` 读写教育经历信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `school` | `i18n\[\]` | 学校 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `level_of_education` | `enum` | 学历，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)学历（level_of_education）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 开始日期，时间格式为 2023-09-01 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 结束日期，时间格式为 2023-09-01 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_of_study` | `i18n\[\]` | 专业 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `degree` | `enum` | 学位，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)学位（degree）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `school_name` | `enum` | 学校名称，枚举值可查询[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：school_name - object_api_name：education |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_of_study_name` | `enum` | 专业名称，枚举值可查询[获取字段详情](/ssl：ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：field_of_study_name - object_api_name：education |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区，可以通过接口[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expected_end_date` | `string` | 预期结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 值类型说明： - 1：文本 Text，“文本”和“超链接”属于该类型 - 2：布尔 Boolean - 3：数字 Number - 4：枚举 Option，“单选”和“多选”为该类型 - 5：查找 Lookup，“人员（单选）”、“人员（多选）”和个人信息中的自定义分组为该类型 - 6：自动编码 Autonumber - 7：日期时间 Datetime - 8：附件 Attachment，“附件单选”和“附件多选”为该类型 - 9：图片 Image - 10：计算字段 Calculated - 11：反向查找 Backlookup |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `personal_profile` | `personal_profile\[\]` | 个人资料附件<br>**字段权限要求（满足任一）**： `corehr:person.personal_profile:read` 获取个人资料信息 `corehr:person.personal_profile:write` 读写个人资料信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `personal_profile_type` | `enum` | 资料类型，枚举值可查询[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：profile_type - object_api_name：personal_profile |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `files` | `file\[\]` | 文件列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 文件ID，文件内容可通过[下载文件](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/file/get)接口获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 文件名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `talent_id` | `string` | 人才 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段<br>**字段权限要求（满足任一）**： `corehr:person.custom_field:read` 获取个人信息自定义字段信息 `corehr:person.custom_field:write` 读写个人信息中的自定义字段信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 值类型说明： - 1：文本 Text，“文本”和“超链接”属于该类型 - 2：布尔 Boolean - 3：数字 Number - 4：枚举 Option，“单选”和“多选”为该类型 - 5：查找 Lookup，“人员（单选）”、“人员（多选）”和个人信息中的自定义分组为该类型 - 6：自动编码 Autonumber - 7：日期时间 Datetime - 8：附件 Attachment，“附件单选”和“附件多选”为该类型 - 9：图片 Image - 10：计算字段 Calculated - 11：反向查找 Backlookup |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `national_id_number` | `string` | 居民身份证件号码<br>**字段权限要求（满足任一）**： `corehr:person.national_id:read` 获取证件信息 `corehr:person.national_id:write` 读写证件信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `family_address` | `string` | 家庭地址<br>**字段权限要求（满足任一）**： `corehr:person.address:read` 读取个人地址信息 `corehr:person.address:write` 读写个人地址信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `person_info_chns` | `person_info_chn\[\]` | 个人附加信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `native_region` | `string` | 籍贯 ID，可以通过[查询省份/行政区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)接口获取详情<br>**字段权限要求（满足任一）**： `corehr:person.native_region:read` 获取籍贯信息 `corehr:person.native_region:write` 读写籍贯信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hukou_type` | `enum` | 户口类型，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)户口类型（hukou_type）枚举定义获得<br>**字段权限要求（满足任一）**： `corehr:person.hukou:read` 获取户口信息 `corehr:person.hukou:write` 读写户口信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hukou_location` | `string` | 户口所在地<br>**字段权限要求（满足任一）**： `corehr:person.hukou:read` 获取户口信息 `corehr:person.hukou:write` 读写户口信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `political_affiliations` | `enum\[\]` | 政治面貌，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)政治面貌（political_affiliation）枚举定义获得<br>**字段权限要求**： `corehr:person.political_affiliation:read` 获取政治面貌信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `born_country_region` | `string` | 出生国家/地区，可以通过接口[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取详情<br>**字段权限要求（满足任一）**： `corehr:person.born_country_region:read` 获取出生国家/地区信息 `corehr:person.born_country_region:write` 读写出生国家/地区信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_disabled` | `boolean` | 是否残疾<br>**字段权限要求（满足任一）**： `corehr:person.is_disabled:read` 获取残疾信息 `corehr:person.is_disabled:write` 读写残疾信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `disable_card_number` | `string` | 残疾证号<br>**字段权限要求（满足任一）**： `corehr:person.is_disabled:read` 获取残疾信息 `corehr:person.is_disabled:write` 读写残疾信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_martyr_family` | `boolean` | 是否烈属<br>**字段权限要求（满足任一）**： `corehr:person.martyr_family:read` 获取烈属信息 `corehr:person.martyr_family:write` 读写烈属信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `martyr_card_number` | `string` | 烈属证号<br>**字段权限要求（满足任一）**： `corehr:person.martyr_family:read` 获取烈属信息 `corehr:person.martyr_family:write` 读写烈属信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_old_alone` | `boolean` | 是否孤老<br>**字段权限要求（满足任一）**： `corehr:person.is_old_alone:read` 获取孤老信息 `corehr:person.is_old_alone:write` 读写孤老信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `resident_taxes` | `resident_tax\[\]` | 居民身份信息<br>**字段权限要求（满足任一）**： `corehr:person.resident_tax:read` 获取居民身份信息 `corehr:person.resident_tax:write` 读写居民身份信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `year_resident_tax` | `string` | 年度 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `resident_status` | `enum` | resident_status 居民身份，枚举值可查询[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：resident_status - object_api_name：resident_tax |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tax_country_region_id` | `string` | 国家/地区，可以通过接口[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段<br>**字段权限要求（满足任一）**： `corehr:person.resident_tax_custom_field:read` 获取居民身份自定义字段信息 `corehr:person.resident_tax_custom_field:write` 读写居民身份自定义字段信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(123, 123.23, true, [\"id1\",\"id2\], 2006-01-02 15:04:05]) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `religion` | `enum` | 宗教信仰，枚举值可查询[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：religion - object_api_name：person<br>**字段权限要求（满足任一）**： `corehr:person.religion:read` 查看宗教信仰信息 `corehr:person.religion:write` 读写宗教信仰信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `working_years_v2` | `number(float)` | 工龄 （单位：年）浮点类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `string` | 个人信息 创建时间，时间格式为 2023-09-01 13:21:12 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `updated_at` | `string` | 个人信息 更新时间，时间格式为 2023-09-01 13:21:12 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `created_by` | `string` | 个人信息 创建人，可以通过[批量查询员工信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)接口获取详情，user_id_type使用people_corehr_id类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `updated_by` | `string` | 个人信息 更新人，可以通过[批量查询员工信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)接口获取详情，user_id_type使用people_corehr_id类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bank_account_number` | `string` | 银行卡号<br>**字段权限要求（满足任一）**： `corehr:person.bank_account:read` 获取银行账号列表信息 `corehr:person.bank_account:write` 读写银行账号信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `passport_number` | `string` | 护照号码<br>**字段权限要求**： `corehr:person.passport_number:read` 获取护照号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `former_employer` | `i18n\[\]` | 上家公司<br>**字段权限要求（满足任一）**： `corehr:person.work_experience:read` 获取工作履历信息 `corehr:person.work_experience:write` 读写工作履历信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_info` | `pre_hire_employment_info` | 工作信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 部门 ID ，可以通过[搜索部门信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/search)接口获取详情<br>ID转换：支持根据department_id_type进行ID转换，返回department_id_type对应的类型的ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_rates` | `job_data_cost_center\[\]` | 成本中心分摊信息 - 待废弃，建议使用cost_allocation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_id` | `string` | 成本中心 ID，可以通过[搜索成本中心信息](https://open.feishu.cn/document/server-docs/corehr-v1/organization-management/cost_center/search)接口获取对应的成本中心信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rate` | `int` | 分摊比例(整数) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `new_rate` | `number(float)` | 分摊比例 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `office_location_id` | `string` | 办公地点 ID，详细信息可通过[查询地点](https://open.feishu.cn/document/server-docs/corehr-v1/organization-management/location/get)接口获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `work_location_id` | `string` | 工作地点id ，可通过[批量查询地点](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)接口获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `work_station` | `string` | 工位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `worker_id` | `string` | 工号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `compensation_type` | `enum` | 薪资类型，枚举值可查询[获取字段详情](https://open.feishu.cn/document/server-docs/corehr-v1/basic-infomation/custom_field/get_by_param)接口获取，按如下参数查询即可：  - custom_api_name：compensation_type  - object_api_name：pre_hire<br>**字段权限要求（满足任一）**： `corehr:employment.compensation_type:read` 查看员工的薪资类型信息 `corehr:employment.compensation_type:write` 读写员工的薪资类型信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `direct_leader_id` | `string` | 直属上级雇佣 ID，可以通过[搜索员工信息](https://open.feishu.cn/document/server-docs/corehr-v1/employee/search)接口获取详情<br>ID转换：支持根据user_id_type进行ID转换，返回user_id_type对应的类型的ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dotted_line_manager_id` | `string` | 虚线上级雇佣 ID ， 可以通过【搜索员工信息】接口获取 - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>ID转换：支持根据user_id_type进行ID转换，返回user_id_type对应的类型的ID。<br>**字段权限要求**： `corehr:pre_hire.dotted_line_manager:read` 获取待入职人员虚线上级 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_id` | `string` | 职务 ID ,可以通过[查询职务](https://open.feishu.cn/document/server-docs/corehr-v1/job-management/job/get)接口获取详情<br>**字段权限要求（满足任一）**： `corehr:employment.job:read` 获取员工的职务信息 `corehr:employment.job_level:read` 获取职务级别信息 `corehr:employment.job_level:write` 读写员工的职务级别信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id` | `string` | 序列 ID，可以通过[查询序列](https://open.feishu.cn/document/server-docs/corehr-v1/job-management/job_family/get)接口获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_level_id` | `string` | 职级 ID，可以通过[查询职级](https://open.feishu.cn/document/server-docs/corehr-v1/job-management/job_level/get)接口获取详情<br>**字段权限要求（满足任一）**： `corehr:employment.job_level:read` 获取职务级别信息 `corehr:employment.job_level:write` 读写员工的职务级别信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_grade_id` | `string` | 职等 ID<br>**字段权限要求（满足任一）**： `corehr:employment.job_grade:read` 获取职等信息 `corehr:employment.job_grade:write` 读写职等信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_title` | `string` | 职务头衔<br>**字段权限要求（满足任一）**： `corehr:employment.job_level:read` 获取职务级别信息 `corehr:employment.job_level:write` 读写员工的职务级别信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type_id` | `string` | 人员类型 ID ，可以通过招聘[查询人员类型](https://open.feishu.cn/document/server-docs/corehr-v1/basic-infomation/employee_type/get)接口获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employee_subtype_id` | `string` | 人员子类型 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employment_type` | `string` | 雇佣类型， 枚举值可查询[获取字段详情](https://open.feishu.cn/document/server-docs/corehr-v1/basic-infomation/custom_field/get_by_param)接口获取，按如下参数查询即可：  - object_api_name = pre_hire - custom_api_name = employment_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `work_email` | `string` | 工作邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `company_id` | `string` | 公司 ID , 详细信息可通过[查询单个公司](https://open.feishu.cn/document/server-docs/corehr-v1/organization-management/company/get)接口获得<br>**字段权限要求（满足任一）**： `corehr:contract.company:read` 获取合同主体信息 `corehr:contract.company:write` 读写合同主体信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `social_security_city_id` | `string` | 社保城市 ID ，详细信息可通过[查询地点](https://open.feishu.cn/document/server-docs/corehr-v1/organization-management/location/get)接口获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `non_compete_covenant` | `boolean` | 是否包含竞业条款<br>**字段权限要求（满足任一）**： `corehr:employment.non_compete_covenant:read` 查看竞业状态 `corehr:employment.non_compete_covenant:write` 读写竞业状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `weekly_working_hours` | `int` | 周工作时长（单位：小时） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rehire` | `string` | 是否离职重聘<br>**可选值有**：<br>- `to_be_confirmed`: 待确认，系统会判断该员工是否存在历史雇佣记录，如果存在且需要二次确认时会调用失败，并返回历史雇佣记录 - `no`: 否，系统直接标为非离职重聘人员，不再做重复判断 - `yes`: 是，要求历史雇佣信息 ID 必填 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rehire_employment_id` | `string` | 历史雇佣信息 ID ，雇佣信息详细信息可以通过[查询单个雇佣信息](https://open.feishu.cn/document/server-docs/corehr-v1/employee/employment/get) 获得，系统会检验当前雇佣信息的合法性，要求：  - 雇佣信息为该人员最后一次雇佣记录  - 雇佣信息的雇员状态 = "terminated"  - 该人员不存在其他待入职记录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `working_hours_type` | `string` | 工时制度 ID ，可通过[查询单个工时制度](https://open.feishu.cn/document/server-docs/corehr-v1/basic-infomation/working_hours_type/get)接口获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `weekly_working_hours_v2` | `number(float)` | 周工作时长v2（单位：小时）浮点类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `office_address` | `address` | 办公地址<br>**字段权限要求**： `corehr:pre_hire.office_address:read` 获取办公地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_local_script` | `string` | 完整地址（本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_western_script` | `string` | 完整地址（西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_id` | `string` | 地址 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区，可以通过接口[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_id` | `string` | 主要行政区ID 可以通过[查询省份/行政区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)接口获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_id` | `string` | 城市（该字段待作废，请勿使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `distinct_id` | `string` | 区/县（该字段待作废，请勿使用） |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_type_list` | `enum\[\]` | 地址类型，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)地址类型（address_type）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 值类型说明： - 1：文本 Text，“文本”和“超链接”属于该类型 - 2：布尔 Boolean - 3：数字 Number - 4：枚举 Option，“单选”和“多选”为该类型 - 5：查找 Lookup，“人员（单选）”、“人员（多选）”和个人信息中的自定义分组为该类型 - 6：自动编码 Autonumber - 7：日期时间 Datetime - 8：附件 Attachment，“附件单选”和“附件多选”为该类型 - 9：图片 Image - 10：计算字段 Calculated - 11：反向查找 Backlookup |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `working_calendar_id` | `string` | 工作日历ID，可以通过[查询工作日历](https://open.larkoffice.com/document/server-docs/calendar-v4/calendar/get)接口获取详情<br>**字段权限要求**： `corehr:pre_hire.working_calendar:read` 获取工作日历 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `updated_at` | `string` | 更新时间，时间格式为 2023-09-01 13:21:12 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `suspected_rehiring` | `boolean` | 是否疑似重聘<br>**字段权限要求**： `corehr:pre_hire.suspected_rehiring:read` 获取是否疑似重聘 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `condition_worker` | `boolean` | 是否外部人员 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段<br>**字段权限要求**： `corehr:employment.custom_field:read` 获取雇佣信息自定义字段信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 值类型说明： - 1：文本 Text，“文本”和“超链接”属于该类型 - 2：布尔 Boolean - 3：数字 Number - 4：枚举 Option，“单选”和“多选”为该类型 - 5：查找 Lookup，“人员（单选）”、“人员（多选）”和个人信息中的自定义分组为该类型 - 6：自动编码 Autonumber - 7：日期时间 Datetime - 8：附件 Attachment，“附件单选”和“附件多选”为该类型 - 9：图片 Image - 10：计算字段 Calculated - 11：反向查找 Backlookup |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `position_id` | `string` | 岗位 ID，可以通过[查询岗位信息]接口获取详情 - 部门的岗职模式会影响岗位数据，在职务模式和岗位模式下，岗位id是必填 - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**字段权限要求（满足任一）**： `corehr:employment.position:read` 获取员工的岗位信息 `corehr:employment.position:write` 读写员工的岗位信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `company_manual_updated` | `boolean` | 公司主体是否被手动修改<br>**字段权限要求**： `corehr:pre_hire.company_manual_updated:read` 查看待入职是否被更新过公司主体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pay_group` | `pre_hire_pay_group_info` | 薪资组信息<br>**字段权限要求**： `corehr:employment.pay_group:read` 获取薪资组信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 薪资组名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 薪资组 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `whether_the_information_is_abnormal` | `boolean` | 是否信息异常<br>**字段权限要求**： `corehr:pre_hire.abnormal_reason_field:read` 获取待入职的异常信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `abnormal_reason` | `pre_hire_abnormal_reason\[\]` | 异常原因列表<br>**字段权限要求**： `corehr:pre_hire.abnormal_reason_field:read` 获取待入职的异常信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `descriptions` | `i18n\[\]` | 异常信息描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `has_offer_salary` | `boolean` | 是否有 Offer 薪酬<br>**字段权限要求**： `corehr:employment.has_offer_salary:read` 查看是否有 Offer 薪酬 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `recruitment_project_id` | `string` | 招聘项目 ID<br>**字段权限要求**： `corehr:employment.recruitment_project_id:read` 查看待入职的招聘项目 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `work_shift` | `enum` | 排班类型，枚举值可查询[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：work_shift - object_api_name：pre_hire<br>**字段权限要求**： `corehr:job_data.work_shift:read` 获取排班信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `string` | 创建时间，时间格式为 2023-09-01 13:21:12 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `created_by` | `string` | 待入职信息 创建人，可以通过[批量查询员工信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)接口获取详情，user_id_type使用people_corehr_id类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `updated_by` | `string` | 待入职信息 更新人，可以通过[批量查询员工信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)接口获取详情，user_id_type使用people_corehr_id类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `seniority_date` | `string` | 司龄起算日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_check_order_id` | `string` | 背调订单ID - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**字段权限要求**： `corehr:pre_hire.background_check_order_id:read` 获取待入职人员背调订单ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_check_order_name` | `string` | 背调名称 - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**字段权限要求**： `corehr:pre_hire.background_check_order_name:read` 获取待入职人员背调名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_check_order_package_name` | `string` | 背调套餐 - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**字段权限要求**： `corehr:pre_hire.background_check_order_package_name:read` 获取待入职人员背调套餐 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_check_order_result` | `string` | 背调结果 - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**字段权限要求**： `corehr:pre_hire.background_check_order_result:read` 获取待入职人员背调结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_check_order_supplier_name` | `string` | 背调供应商 - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**字段权限要求**： `corehr:pre_hire.background_check_order_supplier_name:read` 获取待入职人员背调供应商 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_check_order_account_name` | `string` | 背调账号名称 - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**字段权限要求**： `corehr:pre_hire.background_check_order_account_name:read` 获取待入职人员背调账号名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_check_order_start_time` | `string` | 背调开始时间 - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**字段权限要求**： `corehr:pre_hire.background_check_order_start_time:read` 获取待入职人员背调开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_check_order_complete_time` | `string` | 背调完成时间 - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**字段权限要求**： `corehr:pre_hire.background_check_order_complete_time:read` 获取待入职人员背调完成时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `background_check_order_status` | `enum` | 背调状态，枚举值可查询[获取字段详情](https://open.feishu.cn/document/server-docs/corehr-v1/basic-infomation/custom_field/get_by_param)接口获取，按如下参数查询即可：  - object_api_name = pre_hire - custom_api_name = background_check_order_status - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)<br>**字段权限要求**： `corehr:pre_hire.background_check_order_status:read` 获取待入职人员背调状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `seniority_adjust_information_list` | `prehire_seniority_adjust_information_query\[\]` | 司龄调整信息 - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `seniority_adjustment` | `number(float)` | 调整值 - 精确度：两位小数 - 单位：年 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `seniority_adjustment_type` | `enum` | 调整类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：seniority_adjust_information   - custom_api_name：seniority_adjustment_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reasons_for_seniority_adjustment` | `string` | 司龄调整原因 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 开始日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notice_period_positive_voluntary` | `notice_period_detail` | 转正后通知期（主动离职） - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `int` | 数值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value_unit` | `string` | 单位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notice_period_probation_involuntary` | `notice_period_detail` | 试用期内通知期（被动离职） - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `int` | 数值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value_unit` | `string` | 单位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notice_period_positive_involuntary` | `notice_period_detail` | 转正后通知期（被动离职） - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `int` | 数值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value_unit` | `string` | 单位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `notice_period_probation_voluntary` | `notice_period_detail` | 试用期内通知期（主动离职) - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `int` | 数值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value_unit` | `string` | 单位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `working_hours_type_manual_updated` | `boolean` | 工时制度是否被手动修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_over_due` | `boolean` | 入职任务是否逾期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `task_completed` | `boolean` | 入职任务是否完成，暂不推荐使用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expected_graduate_date` | `string` | 预计毕业日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `service_company` | `string` | 任职公司 ID , 详细信息可通过[查询单个公司](https://open.feishu.cn/document/server-docs/corehr-v1/organization-management/company/get)接口获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pathway` | `string` | 通道 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `default_cost_center` | `default_cost_center` | 默认成本中心 - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_id` | `string` | 成本中心 ID，可以通过[搜索成本中心信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 生效日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_herit` | `boolean` | 是否继承岗位/部门的默认成本中心 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `inherit_source` | `string` | 继承来源 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_allocation` | `cost_allocation` | 成本分摊 - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 分摊生效日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 分摊失效日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_rates` | `job_data_cost_center\[\]` | 成本分摊信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_id` | `string` | 成本中心 ID，可以通过[搜索成本中心信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rate` | `int` | 分摊比例(整数) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `new_rate` | `number(float)` | 分摊比例 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reuse_feishu_account` | `string` | 是否复用飞书账号 - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reused_feishu_account_id` | `string` | 复用的飞书账号，返回Lark Union ID - 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `onboarding_info` | `pre_hire_onboarding_info` | 入职信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `offer_id` | `string` | Offer ID，可以通过招聘[获取 Offer 列表](https://open.feishu.cn/document/server-docs/hire-v1/candidate-management/delivery-process-management/offer/list)接口获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `offer_hr_id` | `string` | Offer HR 的 雇佣 ID，可以通过[批量查询员工信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)接口获取详情，user_id_type使用people_corehr_id类型<br>ID转换：不支持根据user_id_type进行ID转换，返回people_corehr_id 类型的ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `offer_hr_id_v2` | `string` | Offer hr 的 雇佣 ID,ID可以根据user_id_type转换成对应ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `entry_mode` | `string` | 入职方式，枚举值可查询[获取字段详情](https://open.feishu.cn/document/server-docs/corehr-v1/basic-infomation/custom_field/get_by_param)接口获取，按如下参数查询即可：  - object_api_name = pre_hire  - custom_api_name = onboarding_method |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `onboarding_date` | `string` | 入职日期，时间格式为 2023-09-01 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ats_application_id` | `string` | 招聘投递 ID ，详细信息可以通过招聘[获取投递信息](https://open.feishu.cn/document/server-docs/hire-v1/candidate-management/delivery-process-management/application/get)接口查询获得详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `recruitment_type` | `string` | 招聘来源 ，枚举值可查询[获取字段详情](https://open.feishu.cn/document/server-docs/corehr-v1/basic-infomation/custom_field/get_by_param)接口获取，按如下参数查询即可：  - object_api_name = pre_hire - custom_api_name = recruitment_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `onboarding_location_id` | `string` | 入职地点 ID，详细信息可通过[查询单个地点](https://open.feishu.cn/document/server-docs/corehr-v1/organization-management/location/get)接口获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `company_sponsored_visa` | `boolean` | 需要公司办理签证<br>**字段权限要求**： `corehr:pre_hire.company_sponsored_visa:read` 查看签证要求 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `onboarding_status` | `string` | 入职状态<br>**可选值有**：<br>- `preboarding`: 待入职 - `deleted`: 已删除 - `day_one`: 准备就绪 - `withdrawn`: 已撤销 - `completed`: 已完成 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `onboarding_task_list` | `onboarding_task\[\]` | 入职任务列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `task_name` | `string` | 任务名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `task_status` | `string` | 任务状态<br>**可选值有**：<br>- `initiating`: 发起中 - `terminated`: 已终止 - `exception`: 异常 - `in_progress`: 进行中 - `not_started`: 未开始 - `skipped`: 已跳过 - `uninitialized`: 未初始化 - `failed`: 已失败 - `in_review`: 审核中 - `rejected`: 已退回 - `completed`: 已完成 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `operator_id` | `string` | 当前操作人雇佣 ID，可以通过[批量查询员工信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)接口获取详情，user_id_type使用people_corehr_id类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `task_code` | `string` | 任务code |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `onboarding_address` | `address` | 入职地址<br>**字段权限要求**： `corehr:pre_hire.onboarding_address:read` 获取入职地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_local_script` | `string` | 完整地址（本地文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_address_western_script` | `string` | 完整地址（西方文字） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_id` | `string` | 地址 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 国家 / 地区，可以通过接口[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_id` | `string` | 主要行政区ID 可以通过[查询省份/行政区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)接口获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_id` | `string` | 城市（该字段待作废，请勿使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `distinct_id` | `string` | 区/县（该字段待作废，请勿使用） |
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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_type_list` | `enum\[\]` | 地址类型，枚举值可通过文档[枚举常量介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)地址类型（address_type）枚举定义获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 主要地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_public` | `boolean` | 公开地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_api_name` | `string` | 自定义字段 apiname，即自定义字段的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `custom_name` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 自定义字段类型 值类型说明： - 1：文本 Text，“文本”和“超链接”属于该类型 - 2：布尔 Boolean - 3：数字 Number - 4：枚举 Option，“单选”和“多选”为该类型 - 5：查找 Lookup，“人员（单选）”、“人员（多选）”和个人信息中的自定义分组为该类型 - 6：自动编码 Autonumber - 7：日期时间 Datetime - 8：附件 Attachment，“附件单选”和“附件多选”为该类型 - 9：图片 Image - 10：计算字段 Calculated - 11：反向查找 Backlookup |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `flow_name` | `i18n\[\]` | 入职流程<br>**字段权限要求**： `corehr:pre_hire.flow_id:read` 获取入职流程 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `flow_id` | `string` | 入职流程 ID<br>**字段权限要求**： `corehr:pre_hire.flow_id:read` 获取入职流程 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `check_in_time` | `string` | 签到时间，时间格式为 2023-09-01 13:21:12<br>**字段权限要求**： `corehr:pre_hire.check_in_data:read` 获取待入职人员的签到数据 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `check_in_method` | `enum` | 招聘来源，枚举值可查询[获取字段详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： - custom_api_name：check_in_method - object_api_name：pre_hire<br>**字段权限要求**： `corehr:pre_hire.check_in_data:read` 获取待入职人员的签到数据 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言编码（IETF BCP 47） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `probation_info` | `pre_hire_probation_info` | 试用期信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `probation_start_date` | `string` | 试用期开始日期，时间格式为 2023-09-01 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `probation_end_date` | `string` | 试用期结束日期，时间格式为 2023-09-01 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `probation_period` | `int` | 试用期时长（单位：天） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_info` | `pre_hire_contract_info` | 合同信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contract_start_date` | `string` | 合同开始日期，时间格式为 2023-09-01<br>**字段权限要求（满足任一）**： `corehr:contract.period:read` 获取合同期限信息 `corehr:contract.period:write` 读写合同期限信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contract_end_date` | `string` | 合同结束日期，时间格式为 2023-09-01<br>**字段权限要求（满足任一）**： `corehr:contract.period:read` 获取合同期限信息 `corehr:contract.period:write` 读写合同期限信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contract_type` | `string` | 合同类型，枚举值可查询[获取字段详情](https://open.feishu.cn/document/server-docs/corehr-v1/basic-infomation/custom_field/get_by_param)接口获取，按如下参数查询即可：  - object_api_name = pre_hire - custom_api_name = contract_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `duration_type` | `string` | 期限类型，枚举值可查询[获取字段详情](https://open.feishu.cn/document/server-docs/corehr-v1/basic-infomation/custom_field/get_by_param)接口获取，按如下参数查询即可：  - object_api_name = pre_hire - custom_api_name = duration_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `signing_type` | `string` | 签订类型，枚举值可查询[获取字段详情](https://open.feishu.cn/document/server-docs/corehr-v1/basic-infomation/custom_field/get_by_param)接口获取，按如下参数查询即可：  - object_api_name = pre_hire - custom_api_name = signing_type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contract_file_ids` | `string\[\]` | 合同文件<br>**字段权限要求**： `corehr:pre_hire.contract_file_id:read` 待入职员工合同文件ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `pre_hire_id` | `string` | 待入职 id |
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
                "person_info": {
                    "person_id": "6919733936050406926",
                    "phone_number": "13649211111",
                    "legal_name": "张三",
                    "preferred_name": "刘梓新(Henry)",
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
                            ]
                        }
                    ],
                    "email_list": [
                        {
                            "email": "1234567@bytedance.com",
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
                                "enum_name": "phone_type",
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
                            "is_primary": true
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
                    "person_info_chns": [
                        {
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
                            ]
                        }
                    ],
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
                    "religion": {
                        "enum_name": "phone_type",
                        "display": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ]
                    },
                    "working_years_v2": 2.1,
                    "created_at": "2023-09-01 13:21:12",
                    "updated_at": "2022-01-02",
                    "created_by": "69928404442626824",
                    "updated_by": "69928404442626824",
                    "bank_account_number": "69928404442626824",
                    "passport_number": "6919733936050406926",
                    "former_employer": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ]
                },
                "employment_info": {
                    "department_id": "7147562782945478177",
                    "cost_center_rates": [
                        {
                            "cost_center_id": "6950635856373745165",
                            "rate": 100,
                            "new_rate": 50.2
                        }
                    ],
                    "office_location_id": "6977976687350924832",
                    "work_location_id": "6977976687350924832",
                    "work_station": "ABC123",
                    "worker_id": "1234567",
                    "compensation_type": {
                        "enum_name": "phone_type",
                        "display": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ]
                    },
                    "direct_leader_id": "7032210902531327521",
                    "dotted_line_manager_id": "7032210902531327521",
                    "job_id": "6977976735715378724",
                    "job_family_id": "6977972856625939999",
                    "job_level_id": "6977971894960145950",
                    "job_grade_id": "6977971894960145950",
                    "job_title": "java",
                    "employee_type_id": "6977973225846343171",
                    "employee_subtype_id": "6977973225846343171",
                    "employment_type": "employee",
                    "work_email": "joshua@bytedance.com",
                    "company_id": "6738317738688661772",
                    "social_security_city_id": "6977973225846343171",
                    "non_compete_covenant": true,
                    "weekly_working_hours": 8,
                    "rehire": "no",
                    "rehire_employment_id": "6977973225846343172",
                    "working_hours_type": "6977973225846343171",
                    "weekly_working_hours_v2": 8.5,
                    "office_address": {
                        "full_address_local_script": "中国北京北京",
                        "full_address_western_script": "Beijing, Beijing, China,",
                        "address_id": "6989822217869624863",
                        "country_region_id": "6862995757234914824",
                        "region_id": "6863326815667095047",
                        "city_id": "6863333254578046471",
                        "distinct_id": "6863333516579440141",
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
                    "working_calendar_id": "6977973225846343173",
                    "updated_at": "2023-09-01 13:21:12",
                    "suspected_rehiring": false,
                    "condition_worker": false,
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
                    "position_id": "6977976735715373452",
                    "company_manual_updated": true,
                    "pay_group": {
                        "name": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ],
                        "id": "1234566"
                    },
                    "whether_the_information_is_abnormal": true,
                    "abnormal_reason": [
                        {
                            "descriptions": [
                                {
                                    "lang": "zh-CN",
                                    "value": "中文示例"
                                }
                            ]
                        }
                    ],
                    "has_offer_salary": true,
                    "recruitment_project_id": "23214213152",
                    "work_shift": {
                        "enum_name": "phone_type",
                        "display": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ]
                    },
                    "created_at": "2023-01-10 10:29",
                    "created_by": "69928404442626824",
                    "updated_by": "69928404442626824",
                    "seniority_date": "2023-01-10",
                    "background_check_order_id": "123",
                    "background_check_order_name": "xxx",
                    "background_check_order_package_name": "xxx",
                    "background_check_order_result": "通过",
                    "background_check_order_supplier_name": "xxx",
                    "background_check_order_account_name": "xxx",
                    "background_check_order_start_time": "2023-01-10 10:29",
                    "background_check_order_complete_time": "2023-01-10 10:29",
                    "background_check_order_status": {
                        "enum_name": "phone_type",
                        "display": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ]
                    },
                    "seniority_adjust_information_list": [
                        {
                            "seniority_adjustment": 0.5,
                            "seniority_adjustment_type": {
                                "enum_name": "phone_type",
                                "display": [
                                    {
                                        "lang": "zh-CN",
                                        "value": "中文示例"
                                    }
                                ]
                            },
                            "reasons_for_seniority_adjustment": "工厂停产需要减去半年工龄",
                            "start_date": "2024-05-19",
                            "end_date": "2024-11-18",
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
                    "notice_period_positive_voluntary": {
                        "wk_id": "4698019107896524633",
                        "value": 1,
                        "value_unit": "月",
                        "name": {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    },
                    "notice_period_probation_involuntary": {
                        "wk_id": "4698019107896524633",
                        "value": 1,
                        "value_unit": "月",
                        "name": {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    },
                    "notice_period_positive_involuntary": {
                        "wk_id": "4698019107896524633",
                        "value": 1,
                        "value_unit": "月",
                        "name": {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    },
                    "notice_period_probation_voluntary": {
                        "wk_id": "4698019107896524633",
                        "value": 1,
                        "value_unit": "月",
                        "name": {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    },
                    "working_hours_type_manual_updated": true,
                    "is_over_due": true,
                    "task_completed": true,
                    "expected_graduate_date": "2023-01-10",
                    "service_company": "6738317738688661772",
                    "pathway": "7460865381179115052",
                    "default_cost_center": {
                        "cost_center_id": "6950635856373745165",
                        "effective_time": "2025-01-01",
                        "is_herit": false,
                        "inherit_source": "department"
                    },
                    "cost_allocation": {
                        "effective_time": "2025-01-01",
                        "expiration_time": "2025-02-01",
                        "cost_center_rates": [
                            {
                                "cost_center_id": "6950635856373745165",
                                "rate": 100,
                                "new_rate": 50.2
                            }
                        ]
                    },
                    "reuse_feishu_account": "reuse",
                    "reused_feishu_account_id": "6738317738688661772"
                },
                "onboarding_info": {
                    "offer_id": "7032210902531327521",
                    "offer_hr_id": "7032210902531327521",
                    "offer_hr_id_v2": "7032210902531327521",
                    "entry_mode": "onsite",
                    "onboarding_date": "2022-10-08",
                    "ats_application_id": "7140946969586010376",
                    "recruitment_type": "recent_graduates",
                    "onboarding_location_id": "6977976687350924832",
                    "company_sponsored_visa": true,
                    "onboarding_status": "preboarding",
                    "onboarding_task_list": [
                        {
                            "task_name": "task_1",
                            "task_status": "task_1",
                            "operator_id": "7032210902531327521",
                            "task_code": "task_11"
                        }
                    ],
                    "onboarding_address": {
                        "full_address_local_script": "中国北京北京",
                        "full_address_western_script": "Beijing, Beijing, China,",
                        "address_id": "6989822217869624863",
                        "country_region_id": "6862995757234914824",
                        "region_id": "6863326815667095047",
                        "city_id": "6863333254578046471",
                        "distinct_id": "6863333516579440141",
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
                    "flow_name": [
                        {
                            "lang": "zh-CN",
                            "value": "中文示例"
                        }
                    ],
                    "flow_id": "2342352325",
                    "check_in_time": "2023-09-01 13:21:12",
                    "check_in_method": {
                        "enum_name": "phone_type",
                        "display": [
                            {
                                "lang": "zh-CN",
                                "value": "中文示例"
                            }
                        ]
                    }
                },
                "probation_info": {
                    "probation_start_date": "2022-07-29",
                    "probation_end_date": "2023-04-07",
                    "probation_period": 6
                },
                "contract_info": {
                    "contract_start_date": "2022-10-08",
                    "contract_end_date": "2025-10-07",
                    "contract_type": "labor_contract",
                    "duration_type": "fixed_term",
                    "signing_type": "renewed",
                    "contract_file_ids": [
                        "6890452208593372141"
                    ]
                },
                "pre_hire_id": "7032210902531327521"
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
| 503 | 1161204 | Requset timeout | 超时，请重试 |
| 429 | 1161604 | QPS over limit | 由于限流而操作失败，请降低调用频率 |


