---
title: "添加人员"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/create"
updateTime: "1750141589000"
---

# 添加人员

支持在单个接口中进行人员全信息添加，包括人员的基本信息，雇佣信息，入职任职记录及其他分组信息


> **Tip**: - 此接口参数校验规则与【人事系统-人员档案配置】的校验规则一致，字段是否必填以【人事系统-人员档案配置】为准。建议参照【飞书人事-我的团队-添加人员】页面来传参
> - 若开启工号自动编码规则则无需输入人员“工号”，系统将自动进行工号生成；若手动输入工号，则会按照手动输入工号内容进行人员档案建立


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/employees |
| HTTP Method | POST |
| 接口频率限制 | [20 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:employee.add:write` 添加人员 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `client_token` | `string` | 否 | 操作的唯一标识，用于幂等的进行更新操作，格式为标准的 UUIDV4。此值为空表示将发起一次新的请求，此值非空表示幂等的进行更新操作。<br>**示例值**：fe599b60-450f-46ff-b2ef-9f6675625b97<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` 字符 |
| `rehire` | `boolean` | 否 | 是否为离职重聘 - false：系统直接标为非离职重聘人员，不再做重复判断 - true：要求 rehire_employment_id<br>**示例值**：true |
| `rehire_employment_id` | `string` | 否 | 离职重聘员工雇佣 ID<br>可通过[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取<br>**示例值**：7140964208476371111 |
| `force_submit` | `boolean` | 否 | 是否强制提交 - true：是，跳过超编等校验 - false：否，被拦截报错<br>**示例值**：false<br>**默认值**：`false` |
| `ignore_working_hours_type_rule` | `boolean` | 否 | 是否忽略工时制度自动生成规则 - 值为 false 时，以下字段必填：   - emp_contract_record.first_party   - employment_record.work_location   - employment_record.employee_type   - employment_record.job_family   - employment_record.job   - employment_record.job_level   - employment_record.department<br>**示例值**：true<br>**默认值**：`false` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `personal_info` | `profile_setting_personal_info` | 否 | 个人信息 |
| &nbsp;&nbsp;└ `personal_basic_info` | `profile_setting_personal_basic_info` | 否 | 基本信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `legal_name` | `profile_setting_name` | 否 | 法定姓名。 - [【飞书人事姓名填写规则】](https://bytedance.larkoffice.com/wiki/Am1Zwgjj0imm8OkfICucBqRDnbh) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `additional_name_type` | `string` | 否 | 补充姓名类型<br>枚举值可以通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下： - object_api_name = "person_name" - custom_api_name = "additional_name_type"<br>**示例值**："emergency_contact_name" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region` | `string` | 否 | 国家 / 地区 ID<br>如果填写了法定姓名对象，则该字段必填<br>可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)接口获取<br>**示例值**："6862995757234914824" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_name` | `string` | 否 | 全名<br>**示例值**："王大帅" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hereditary` | `string` | 否 | 姓氏称谓<br>**示例值**："王" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `middle_name` | `string` | 否 | 中间名<br>**示例值**："大" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `secondary` | `string` | 否 | 第二姓氏<br>**示例值**："王" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `social` | `string` | 否 | 尊称<br>枚举值可以通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下： - object_api_name = "person_name"  - custom_api_name = "social"<br>**示例值**："ii" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tertiary` | `string` | 否 | 婚后姓氏<br>**示例值**："王" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_first_name_2` | `string` | 否 | 名 - 第二本地文字<br>**示例值**："五" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_middle_name` | `string` | 否 | 本地中间名<br>**示例值**："大" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_primary` | `string` | 否 | 姓 - 本地文字<br>**示例值**："黄" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_primary_2` | `string` | 否 | 姓 - 第二本地文字<br>**示例值**："王" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_secondary` | `string` | 否 | 第二姓氏 - 本地文字<br>**示例值**："王" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 否 | 头衔<br>枚举值可以通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下： - object_api_name = "person_name"  - custom_api_name = "title"<br>**示例值**："Mr" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_first_name` | `string` | 否 | 名 - 本地文字<br>**示例值**："四" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_local_name` | `string` | 否 | 自定义姓名（本地文字）<br>**示例值**："王大帅" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_western_name` | `string` | 否 | 自定义姓名（西方文字）<br>**示例值**："王大帅" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `first_name` | `string` | 否 | 名<br>**示例值**："帅" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name_primary` | `string` | 否 | 姓<br>**示例值**："王" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `preferred_name` | `profile_setting_name` | 否 | 常用姓名。 - [【飞书人事姓名填写规则】](https://bytedance.larkoffice.com/wiki/Am1Zwgjj0imm8OkfICucBqRDnbh) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `additional_name_type` | `string` | 否 | 补充姓名类型<br>枚举值可以通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "person_name"  - custom_api_name = "additional_name_type"<br>**示例值**："emergency_contact_name" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region` | `string` | 否 | 国家 / 地区 ID<br>如果填写了常用姓名对象，则该字段必填<br>可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)接口获取<br>**示例值**："6862995757234914824" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `full_name` | `string` | 否 | 全名<br>**示例值**："王大帅" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hereditary` | `string` | 否 | 姓氏称谓<br>**示例值**："王" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `middle_name` | `string` | 否 | 中间名<br>**示例值**："大" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `secondary` | `string` | 否 | 第二姓氏<br>**示例值**："王" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `social` | `string` | 否 | 尊称<br>枚举值可以通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "person_name"  - custom_api_name = "social"<br>**示例值**："ii" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tertiary` | `string` | 否 | 婚后姓氏<br>**示例值**："王" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_first_name_2` | `string` | 否 | 名 - 第二本地文字<br>**示例值**："五" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_middle_name` | `string` | 否 | 本地中间名<br>**示例值**："大" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_primary` | `string` | 否 | 姓 - 本地文字<br>**示例值**："黄" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_primary_2` | `string` | 否 | 姓 - 第二本地文字<br>**示例值**："王" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_secondary` | `string` | 否 | 第二姓氏 - 本地文字<br>**示例值**："王" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 否 | 头衔<br>枚举值可以通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "person_name"  - custom_api_name = "title"<br>**示例值**："mr" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_first_name` | `string` | 否 | 名 - 本地文字<br>**示例值**："四" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_local_name` | `string` | 否 | 自定义姓名（本地文字）<br>**示例值**："王大帅" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_western_name` | `string` | 否 | 自定义姓名（西方文字）<br>**示例值**："王大帅" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `first_name` | `string` | 否 | 名<br>**示例值**："帅" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name_primary` | `string` | 否 | 姓<br>**示例值**："王" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `additional_name` | `string` | 否 | 别名<br>**示例值**："王帅" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `gender` | `string` | 否 | 性别<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "person"  - custom_api_name = "gender"<br>**示例值**："female" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `nationality_v2` | `string` | 否 | 国籍 ID<br>可通过[【查询国籍信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-nationality/search)接口获取<br>**示例值**："6862995757234914826" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ethnicity_race` | `string` | 否 | 民族 / 种族<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "person"  - custom_api_name = "ethnicity_race"<br>**示例值**："han" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `phone` | `profile_setting_phone` | 否 | 个人电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `international_area_code` | `string` | 否 | 国际电话区号<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "phone"  - custom_api_name = "international_area_code"<br>**示例值**："86_china" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 否 | 电话号码<br>如果填写了个人电话对象，则该字段必填<br>**示例值**："13000000000" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 否 | 个人邮箱<br>**示例值**："1234567@example.feishu.cn" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `date_of_birth` | `string` | 否 | 出生日期<br>**示例值**："2006-01-02" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `marital_status` | `string` | 否 | 婚姻状况<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "person"  - custom_api_name = "marital_status"<br>**示例值**："married" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_disabled` | `boolean` | 否 | 是否残疾<br>**示例值**：false |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `disable_card_number` | `string` | 否 | 残疾证号<br>is_disabled 为 true 时必填<br>**示例值**："92838277746172888312" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_martyr_family` | `boolean` | 否 | 是否为烈属<br>**示例值**：false |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `martyr_card_number` | `string` | 否 | 烈属证号<br>is_martyr_family 为 true 时必填<br>**示例值**："00001" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_old_alone` | `boolean` | 否 | 是否为孤老<br>**示例值**：false |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `born_country_region` | `string` | 否 | 出生国家/地区<br>**示例值**："6862995757234914825" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `political_affiliation` | `string` | 否 | 政治面貌<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "person_info_chn"  - custom_api_name = "political_affiliation"<br>**示例值**："other" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `native_region` | `string` | 否 | 籍贯（省份/行政区 ID）<br>可通过[【查询省份/行政区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)接口获取<br>**示例值**："6862995757234914827" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `date_entered_workforce` | `string` | 否 | 参加工作日期<br>**示例值**："2006-01-02" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `first_entry_time` | `string` | 否 | 首次入境日期<br>**示例值**："2006-01-02" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `leave_time` | `string` | 否 | 预计离境日期<br>**示例值**："2006-01-02" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `profile_setting_custom_field\[\]` | 否 | 自定义字段 - 请参考[自定义字段说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："custom_field_1__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 否 | 字段值<br>是 JSON 转义后的字符串，根据元数据定义不同，字段格式不同。使用方式可参考[【操作手册】如何通过 OpenAPI 维护自定义字段](https://feishu.feishu.cn/docx/QlUudBfCtosWMbxx3vxcOFDknn7)<br>**示例值**："123" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `additional_nationalities` | `string\[\]` | 否 | 其他国籍（地区）ID<br>**示例值**：["6862995757234914827"] |
| &nbsp;&nbsp;└ `emergency_contacts` | `profile_setting_emergency_contact\[\]` | 否 | 紧急联系人<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `legal_name` | `string` | 否 | 姓名<br>**示例值**："王大帅" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `relationship` | `string` | 否 | 关系<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "emergency_contact"  - custom_api_name = "relationship"<br>**示例值**："parent" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary` | `boolean` | 否 | 主要联系人<br>**示例值**：true |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `phone` | `profile_setting_phone` | 否 | 电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `international_area_code` | `string` | 否 | 国际电话区号<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "phone"  - custom_api_name = "international_area_code"<br>**示例值**："86_china" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 否 | 电话号码<br>如果填写了电话对象，则该字段必填<br>**示例值**："13000000000" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 否 | 邮箱<br>**示例值**："1234567@example.feishu.cn" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address` | `profile_setting_address` | 否 | 地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_type` | `string` | 否 | 地址类型<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "address"  - custom_api_name = "address_type"<br>**示例值**："home_address" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region` | `string` | 否 | 国家 / 地区 ID<br>如果填写了地址对象，则该字段必填<br>可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)接口获取<br>**示例值**："6862995757234914824" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region` | `string` | 否 | 主要行政区 ID<br>可通过[【查询省份/行政区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)接口获取<br>**示例值**："6863326815667095047" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_subdivision_1` | `string` | 否 | 主要行政区往下细分 1 层的行政区<br>**示例值**："行政区1" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_subdivision_2` | `string` | 否 | 主要行政区往下细分 2 层的行政区<br>**示例值**："行政区2" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_v2` | `string` | 否 | 城市V2 ID<br>可通过[【查询城市信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-city/search)接口获取<br>**示例值**："6862995757234914829" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_text` | `string` | 否 | 城市（文本）<br>**示例值**："北京市" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_city_text` | `string` | 否 | 城市（仅文本，非拉丁语系的本地文字）<br>**示例值**："北京市" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_subdivision_1` | `string` | 否 | 城市往下细分 1 层的行政区<br>**示例值**："行政区 1" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_subdivision_2` | `string` | 否 | 城市往下细分 2 层的行政区<br>**示例值**："行政区 2" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `district_v2` | `string` | 否 | 区/县 V2 ID<br>可通过[【查询区/县信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-district/search)接口获取<br>**示例值**："6862995757234914831" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `postal_code` | `string` | 否 | 邮政编码<br>**示例值**："611530" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_1` | `string` | 否 | 地址行 1<br>如果填写了地址对象，则该字段必填<br>**示例值**："丹佛测试地址 - 纽埃时区" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_1` | `string` | 否 | 地址行 1（非拉丁语系的本地文字）<br>**示例值**："丹佛测试地址 - 纽埃时区" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_2` | `string` | 否 | 地址行 2<br>**示例值**："PoewH" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_2` | `string` | 否 | 地址行 2（非拉丁语系的本地文字）<br>**示例值**："PoewH" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_3` | `string` | 否 | 地址行 3<br>**示例值**："PoewH" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_3` | `string` | 否 | 地址行 3（非拉丁语系的本地文字）<br>**示例值**："PoewH" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_4` | `string` | 否 | 地址行 4<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_5` | `string` | 否 | 地址行 5（非拉丁语系的本地文字）<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_6` | `string` | 否 | 地址行 6<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_6` | `string` | 否 | 地址行 6（非拉丁语系的本地文字）<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_7` | `string` | 否 | 地址行 7<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_7` | `string` | 否 | 地址行 7（非拉丁语系的本地文字）<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_8` | `string` | 否 | 地址行 8<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_8` | `string` | 否 | 地址行 8（非拉丁语系的本地文字）<br>**示例值**："rafSu" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_9` | `string` | 否 | 地址行 9<br>**示例值**："McPRG" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_9` | `string` | 否 | 地址行 9（非拉丁语系的本地文字）<br>**示例值**："McPRG" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_4` | `string` | 否 | 地址行 4（非拉丁语系的本地文字）<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_5` | `string` | 否 | 地址行 5<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `profile_setting_custom_field\[\]` | 否 | 自定义字段 - 请参考[自定义字段说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："custom_field_1__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 否 | 字段值<br>是 JSON 转义后的字符串，根据元数据定义不同，字段格式不同。使用方式可参考[【操作手册】如何通过 OpenAPI 维护自定义字段](https://feishu.feishu.cn/docx/QlUudBfCtosWMbxx3vxcOFDknn7)<br>**示例值**："123" |
| &nbsp;&nbsp;└ `bank_accounts` | `profile_setting_bank_account\[\]` | 否 | 银行账户<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `country_region` | `string` | 否 | 国家 / 地区 ID<br>可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)接口获取<br>**示例值**："6862995757234914824" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `bank_name` | `string` | 否 | 银行名称<br>**示例值**："中国农业银行" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `branch_name` | `string` | 否 | 支行名称<br>**示例值**："中国农业银行支行" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `account_holder` | `string` | 否 | 开户人姓名<br>如果填写了银行账号对象，则该字段必填<br>**示例值**："孟十五" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `bank_account_number` | `string` | 否 | 银行账号<br>如果填写了银行账号对象，则该字段必填<br>**示例值**："6231200000001223" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `bank_account_usages` | `string\[\]` | 否 | 银行卡用途<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "bank_account"  - custom_api_name = "bank_account_usage"<br>**示例值**：["payment"]<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `bank_account_type` | `string` | 否 | 银行卡类型<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "bank_account"  - custom_api_name = "bank_account_type"<br>**示例值**："savings" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `bank_id` | `string` | 否 | 银行 ID<br>可通过[【查询银行信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-bank/search)接口获取<br>**示例值**："6862995757234914832" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `branch_id` | `string` | 否 | 银行支行 ID<br>可通过[【查询支行信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-bank_branch/search)接口获取<br>**示例值**："6862995757234914833" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `payment_type` | `string` | 否 | 分配方式，枚举值<br>**示例值**："percent,balance,amount"<br>**可选值有**：<br>- `percent`: 按比例分配 - `amount`: 按金额分配 - `balance`: 默认卡 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `payment_rate` | `string` | 否 | 分配比例，0～100，保留两位小数<br>**示例值**："80.28" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `payment_amount` | `string` | 否 | 分配金额，保留两位小数<br>**示例值**："5000" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `priority` | `string` | 否 | 优先级，不能低于0<br>**示例值**："1" |
| &nbsp;&nbsp;└ `nationals` | `profile_setting_national\[\]` | 否 | 证件<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `country_region` | `string` | 否 | 国家 / 地区 ID<br>如果填写了证件对象，则该字段必填<br>可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)接口获取<br>**示例值**："6862995757234914824" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `national_id_type` | `string` | 否 | 国家证件类型 ID<br>如果填写了证件对象，则该字段必填<br>可通过[【批量查询国家证件类型】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/national_id_type/list)接口获取<br>**示例值**："6863330041896371725" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `national_id_number` | `string` | 否 | 证件号码<br>如果填写了证件对象，则该字段必填<br>**示例值**："1231131333" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `issued_date` | `string` | 否 | 证件签发日期<br>**示例值**："2020-04-01" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `issued_by` | `string` | 否 | 证件签发机构<br>**示例值**："北京市公安局" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_date` | `string` | 否 | 证件到期日期<br>**示例值**："2020-05-21" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `profile_setting_custom_field\[\]` | 否 | 自定义字段 - 请参考[自定义字段说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："custom_field_1__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 否 | 字段值<br>是 JSON 转义后的字符串，根据元数据定义不同，字段格式不同。使用方式可参考[【操作手册】如何通过 OpenAPI 维护自定义字段](https://feishu.feishu.cn/docx/QlUudBfCtosWMbxx3vxcOFDknn7)<br>**示例值**："123" |
| &nbsp;&nbsp;└ `resident_taxes` | `profile_setting_resident_tax\[\]` | 否 | 居民身份信息<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `year_resident_tax` | `string` | 否 | 年度<br>如果填写了居民身份信息对象，则该字段必填<br>**示例值**："2006-01-02" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tax_country_region` | `string` | 否 | 国家 / 地区 ID<br>如果填写了居民身份信息对象，则该字段必填<br>可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)接口获取<br>**示例值**："6862995757234914824" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `resident_status` | `string` | 否 | 居民身份<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "resident_tax"  - custom_api_name = "resident_status"<br>**示例值**："tax_residence" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `profile_setting_custom_field\[\]` | 否 | 自定义字段 - 请参考[自定义字段说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："custom_field_1__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 否 | 字段值<br>是 JSON 转义后的字符串，根据元数据定义不同，字段格式不同。使用方式可参考[【操作手册】如何通过 OpenAPI 维护自定义字段](https://feishu.feishu.cn/docx/QlUudBfCtosWMbxx3vxcOFDknn7)<br>**示例值**："123" |
| &nbsp;&nbsp;└ `dependents` | `profile_setting_dependent\[\]` | 否 | 家庭成员<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `legal_name` | `string` | 否 | 姓名<br>**示例值**："王大帅" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `date_of_birth` | `string` | 否 | 生日<br>**示例值**："2006-01-02" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `relationship_with_dependent` | `string` | 否 | 关系<br>如果填写了家庭成员对象，则该字段必填<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "dependent"  - custom_api_name ="relationship_with_dependent"<br>**示例值**："parent" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `gender` | `string` | 否 | 性别<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "dependent"  - custom_api_name = "gender"<br>**示例值**："female" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `phone` | `profile_setting_phone` | 否 | 电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `international_area_code` | `string` | 否 | 国际电话区号<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "phone"  - custom_api_name = "international_area_code"<br>**示例值**："86_china" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 否 | 电话号码<br>**示例值**："13000000000" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job` | `string` | 否 | 岗位<br>**示例值**："岗位" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `child_birth_certificates` | `profile_setting_file\[\]` | 否 | 出生证明<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 否 | 文件 ID<br>- 可通过[【上传文件】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/person/upload)接口获取 - 只传该字段即可，大小、类型等字段可以不传递<br>**示例值**："150018109586e8ea745e47ae8feb3722dbe1d03a181336393633393133303431393831343930373235150200" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mime_type` | `string` | 否 | 文件 MIME 类型<br>**示例值**："zip" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 否 | 文件名<br>**示例值**："附件.zip" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `size` | `string` | 否 | 文件大小（KB）<br>**示例值**："1000" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 否 | 文件 Token<br>**示例值**："0a423bc7ea7c4a439d066bf070616782" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employer` | `string` | 否 | 工作单位<br>**示例值**："飞书" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `profile_setting_custom_field\[\]` | 否 | 自定义字段 - 请参考[自定义字段说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："custom_field_1__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 否 | 字段值<br>是 JSON 转义后的字符串，根据元数据定义不同，字段格式不同。使用方式可参考[【操作手册】如何通过 OpenAPI 维护自定义字段](https://feishu.feishu.cn/docx/QlUudBfCtosWMbxx3vxcOFDknn7)<br>**示例值**："123" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address` | `profile_setting_address` | 否 | 联系地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_type` | `string` | 否 | 地址类型<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "address"  - custom_api_name = "address_type"<br>**示例值**："home_address" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country_region` | `string` | 否 | 国家 / 地区 ID<br>可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)接口获取<br>**示例值**："6862995757234914824" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region` | `string` | 否 | 主要行政区 ID<br>可通过[【查询省份/行政区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)接口获取<br>**示例值**："6863326815667095047" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_subdivision_1` | `string` | 否 | 主要行政区往下细分 1 层的行政区<br>**示例值**："行政区 1" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `region_subdivision_2` | `string` | 否 | 主要行政区往下细分 2 层的行政区<br>**示例值**："行政区 2" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_v2` | `string` | 否 | 城市 V2 ID<br>可通过[【查询城市信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-city/search)接口获取<br>**示例值**："6862995757234914829" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_text` | `string` | 否 | 城市（文本）<br>**示例值**："北京市" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_city_text` | `string` | 否 | 城市（仅文本，非拉丁语系的本地文字）<br>**示例值**："北京市" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_subdivision_1` | `string` | 否 | 城市往下细分 1 层的行政区<br>**示例值**："行政区 1" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_subdivision_2` | `string` | 否 | 城市往下细分 2 层的行政区<br>**示例值**："行政区 2" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `district_v2` | `string` | 否 | 区/县 V2 ID<br>可通过[【查询区/县信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-district/search)接口获取<br>**示例值**："6862995757234914831" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `postal_code` | `string` | 否 | 邮政编码<br>**示例值**："611530" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_1` | `string` | 否 | 地址行 1<br>**示例值**："丹佛测试地址 - 纽埃时区" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_1` | `string` | 否 | 地址行 1（非拉丁语系的本地文字）<br>**示例值**："丹佛测试地址 - 纽埃时区" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_2` | `string` | 否 | 地址行 2<br>**示例值**："PoewH" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_2` | `string` | 否 | 地址行 2（非拉丁语系的本地文字）<br>**示例值**："PoewH" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_3` | `string` | 否 | 地址行 3<br>**示例值**："PoewH" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_3` | `string` | 否 | 地址行 3（非拉丁语系的本地文字）<br>**示例值**："PoewH" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_4` | `string` | 否 | 地址行 4<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_5` | `string` | 否 | 地址行 5（非拉丁语系的本地文字）<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_6` | `string` | 否 | 地址行 6<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_6` | `string` | 否 | 地址行 6（非拉丁语系的本地文字）<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_7` | `string` | 否 | 地址行 7<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_7` | `string` | 否 | 地址行 7（非拉丁语系的本地文字）<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_8` | `string` | 否 | 地址行 8<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_8` | `string` | 否 | 地址行 8（非拉丁语系的本地文字）<br>**示例值**："rafSu" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_9` | `string` | 否 | 地址行 9<br>**示例值**："McPRG" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_9` | `string` | 否 | 地址行 9（非拉丁语系的本地文字）<br>**示例值**："McPRG" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_4` | `string` | 否 | 地址行 4（非拉丁语系的本地文字）<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_5` | `string` | 否 | 地址行 5<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;└ `hukou` | `profile_setting_hukou` | 否 | 户口 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `hukou_type` | `string` | 否 | 户口类型<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "person_info_chn"  - custom_api_name = "hukou_type"<br>**示例值**："local_urban_residence" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `hukou_location` | `string` | 否 | 户口所在地<br>**示例值**："北京" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `profile_setting_custom_field\[\]` | 否 | 自定义字段 - 请参考[自定义字段说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："custom_field_1__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 否 | 字段值<br>是 JSON 转义后的字符串，根据元数据定义不同，字段格式不同。使用方式可参考[【操作手册】如何通过 OpenAPI 维护自定义字段](https://feishu.feishu.cn/docx/QlUudBfCtosWMbxx3vxcOFDknn7)<br>**示例值**："123" |
| &nbsp;&nbsp;└ `contact_addresses` | `profile_setting_address\[\]` | 否 | 联系地址<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address_type` | `string` | 否 | 地址类型<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "address"  - custom_api_name = "address_type"<br>**示例值**："home_address" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `country_region` | `string` | 否 | 国家 / 地区 ID<br>如果填写了地址对象，则该字段必填<br>可通过[【查询国家/地区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)接口获取<br>**示例值**："6862995757234914824" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `region` | `string` | 否 | 主要行政区 ID<br>可通过[【查询省份/行政区信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)接口获取<br>**示例值**："6863326815667095047" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `region_subdivision_1` | `string` | 否 | 主要行政区往下细分 1 层的行政区<br>**示例值**："行政区 1" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `region_subdivision_2` | `string` | 否 | 主要行政区往下细分 2 层的行政区<br>**示例值**："行政区 2" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `city_v2` | `string` | 否 | 城市 V2 ID<br>可通过[【查询城市信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-city/search)接口获取<br>**示例值**："6862995757234914829" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `city_text` | `string` | 否 | 城市（文本）<br>**示例值**："北京市" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `local_city_text` | `string` | 否 | 城市（仅文本，非拉丁语系的本地文字）<br>**示例值**："北京市" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `city_subdivision_1` | `string` | 否 | 城市往下细分 1 层的行政区<br>**示例值**："行政区 1" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `city_subdivision_2` | `string` | 否 | 城市往下细分 2 层的行政区<br>**示例值**："行政区 2" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `district_v2` | `string` | 否 | 区/县 V2 ID<br>可通过[【查询区/县信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-district/search)接口获取<br>**示例值**："6862995757234914831" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `postal_code` | `string` | 否 | 邮政编码<br>**示例值**："611530" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_1` | `string` | 否 | 地址行 1<br>如果填写了地址对象，则该字段必填<br>**示例值**："丹佛测试地址 - 纽埃时区" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_1` | `string` | 否 | 地址行 1（非拉丁语系的本地文字）<br>**示例值**："丹佛测试地址 - 纽埃时区" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_2` | `string` | 否 | 地址行 2<br>**示例值**："PoewH" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_2` | `string` | 否 | 地址行 2（非拉丁语系的本地文字）<br>**示例值**："PoewH" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_3` | `string` | 否 | 地址行 3<br>**示例值**："PoewH" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_3` | `string` | 否 | 地址行 3（非拉丁语系的本地文字）<br>**示例值**："PoewH" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_4` | `string` | 否 | 地址行 4<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_5` | `string` | 否 | 地址行 5（非拉丁语系的本地文字）<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_6` | `string` | 否 | 地址行 6<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_6` | `string` | 否 | 地址行 6（非拉丁语系的本地文字）<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_7` | `string` | 否 | 地址行 7<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_7` | `string` | 否 | 地址行 7（非拉丁语系的本地文字）<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_8` | `string` | 否 | 地址行 8<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_8` | `string` | 否 | 地址行 8（非拉丁语系的本地文字）<br>**示例值**："rafSu" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_9` | `string` | 否 | 地址行 9<br>**示例值**："McPRG" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_9` | `string` | 否 | 地址行 9（非拉丁语系的本地文字）<br>**示例值**："McPRG" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `local_address_line_4` | `string` | 否 | 地址行 4（非拉丁语系的本地文字）<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address_line_5` | `string` | 否 | 地址行 5<br>**示例值**："jmwJc" |
| &nbsp;&nbsp;└ `custom_groups` | `profile_setting_custom_group\[\]` | 否 | 自定义分组<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `group_name` | `string` | 否 | 分组名<br>**示例值**："custom_obj__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `items` | `profile_setting_custom_group_item\[\]` | 否 | 分组数据<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `profile_setting_custom_field\[\]` | 否 | 自定义字段 - 请参考[自定义字段说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："custom_field_1__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 否 | 字段值<br>是 JSON 转义后的字符串，根据元数据定义不同，字段格式不同。使用方式可参考[【操作手册】如何通过 OpenAPI 维护自定义字段](https://feishu.feishu.cn/docx/QlUudBfCtosWMbxx3vxcOFDknn7)<br>**示例值**："123" |
| &nbsp;&nbsp;└ `citizenship_statuses` | `profile_setting_citizenship_status\[\]` | 否 | 公民身份列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `country_region` | `string` | 否 | 国家/地区ID<br>**示例值**："7324333990030034476" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `citizenship_status` | `string` | 否 | 公民身份类型<br>**示例值**："公民" |
| `employment_info` | `profile_setting_employment_info` | 否 | 工作信息 |
| &nbsp;&nbsp;└ `basic_info` | `profile_setting_employment_basic_info` | 否 | 基本信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_number` | `string` | 否 | 员工编号<br>**示例值**："1000000" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 否 | 入职日期<br>**示例值**："2021-01-01" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `regular_employee_start_date` | `string` | 否 | 转正式员工日期<br>**示例值**："2021-02-01" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `seniority_date` | `string` | 否 | 资历起算日期<br>**示例值**："2020-01-01" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_email` | `string` | 否 | 工作邮箱<br>**示例值**："12456@test.com" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `phone` | `profile_setting_phone` | 否 | 工作电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `international_area_code` | `string` | 否 | 国际电话区号<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "phone"  - custom_api_name = "international_area_code"<br>**示例值**："86_china" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 否 | 电话号码<br>如果填写了工作电话对象，则该字段必填<br>**示例值**："13000000000" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_geo` | `string` | 否 | 数据驻留地<br>开通了飞书数据驻留服务的企业，该字段为必填<br>**示例值**："cn" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `profile_setting_custom_field\[\]` | 否 | 自定义字段 - 请参考[自定义字段说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："custom_field_1__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 否 | 字段值<br>是 JSON 转义后的字符串，根据元数据定义不同，字段格式不同。使用方式 - 请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**示例值**："123" |
| &nbsp;&nbsp;└ `probation_info` | `profile_setting_probation_info` | 否 | 试用期信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `probation_start_date` | `string` | 否 | 试用期开始日期<br>**示例值**："2021-01-01" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `probation_expected_end_date` | `string` | 否 | 试用期预计结束日期<br>**示例值**："2021-02-01" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `actual_probation_end_date` | `string` | 否 | 试用期实际结束日期<br>**示例值**："2021-02-01" |
| &nbsp;&nbsp;└ `employment_record` | `profile_setting_employment_record` | 否 | 任职记录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type` | `string` | 否 | 人员类型 ID<br>可通过[【批量查询人员类型】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/list)接口获取<br>**示例值**："6890452208593372679" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `string` | 否 | 部门 ID<br>可通过[【批量查询部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)接口获取<br>**示例值**："6890452208593372679" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `direct_manager` | `string` | 否 | 直属上级雇佣 ID<br>可通过[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取<br>**示例值**："6893014062142064135" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `working_hours_type` | `string` | 否 | 工时制度 ID<br>可通过[【批量查询工时制度】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/list)接口获取<br>**示例值**："6890452208593372600" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cost_centers` | `profile_setting_cost_center\[\]` | 否 | 成本中心分摊信息<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 否 | 支持的成本中心 ID，详细信息可通过[【搜索成本中心信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口查询获得<br>**示例值**："6950635856373745165" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rate` | `int` | 否 | 分摊比例<br>**示例值**：100<br>**数据校验规则**：<br>- 取值范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `direct_manager_effective_time` | `string` | 否 | 直属上级入职日期<br>**示例值**："2020-01-01" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dotted_line_manager` | `string` | 否 | 虚线上级雇佣 ID<br>可通过[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取<br>**示例值**："6893014062142064136" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dotted_line_manager_effective_time` | `string` | 否 | 虚线上级入职日期<br>**示例值**："2020-01-01" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job` | `string` | 否 | 职务 ID<br>可通过[【批量查询职务】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/list)接口获取<br>**示例值**："6890452208593372679" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_family` | `string` | 否 | 序列 ID<br>可通过[【批量查询序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/list)接口获取<br>**示例值**："6890452208593372680" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_level` | `string` | 否 | 职级 ID<br>可通过[【批量查询职级】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/list)接口获取<br>**示例值**："6890452208593372681" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_grade` | `string` | 否 | 职等 ID<br>可通过[【查询职等】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)接口获取<br>**示例值**："6890452208593372682" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_location` | `string` | 否 | 工作地点 ID<br>可通过[【批量查询地点】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)接口获取<br>**示例值**："6890452208593372683" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `weekly_working_hours` | `int` | 否 | 周工作时长<br>**示例值**：100<br>**数据校验规则**：<br>- 取值范围：`0` ～ `168` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `position` | `string` | 否 | 岗位ID<br>**示例值**："6890452208593372684" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `pathway` | `string` | 否 | 通道ID<br>**示例值**："6890452208593372684" |
| &nbsp;&nbsp;└ `emp_contract_record` | `profile_setting_emp_contract_record` | 否 | 合同记录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_number` | `string` | 否 | 合同协议编号<br>**示例值**："6919737965274990093" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_type` | `string` | 否 | 合同类型<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "contract"  - custom_api_name = "contract_type"<br>**示例值**："labor_contract" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `first_party` | `string` | 否 | 甲方公司 ID<br>引用 Company 的 ID，详细信息可通过[【批量查询公司】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)接口查询获得<br>**示例值**："6892686614112241165" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 否 | 合同开始日期<br>如果填写了合同对象，则该字段必填<br>**示例值**："2006-01-02" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `duration_type` | `string` | 否 | 期限类型<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "contract"  - custom_api_name = "duration_type"<br>**示例值**："fixed_term" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_end_date` | `string` | 否 | 合同结束日期<br>**示例值**："2050-01-01" |
| &nbsp;&nbsp;└ `custom_groups` | `profile_setting_custom_group\[\]` | 否 | 自定义分组<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `group_name` | `string` | 否 | 分组名<br>**示例值**："custom_obj__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `items` | `profile_setting_custom_group_item\[\]` | 否 | 分组数据<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `profile_setting_custom_field\[\]` | 否 | 自定义字段 - 请参考[自定义字段说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："custom_field_1__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 否 | 字段值<br>是 JSON 转义后的字符串，根据元数据定义不同，字段格式不同。使用方式可参考[【操作手册】如何通过 OpenAPI 维护自定义字段](https://feishu.feishu.cn/docx/QlUudBfCtosWMbxx3vxcOFDknn7)<br>**示例值**："123" |
| &nbsp;&nbsp;└ `custom_org_groups` | `job_data_custom_org\[\]` | 否 | 自定义组织记录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 是 | 生效时间<br>**示例值**："2024-07-02" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start_reason` | `string` | 否 | 原因<br>**示例值**："新增人员"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_org_with_rates` | `create_emp_custom_org\[\]` | 是 | 自定义组织列表<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 是 | 自定义组织ID<br>**示例值**："7260357352426782739" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rate` | `number(float)` | 否 | 比例 如果是非比例的可不填写<br>**示例值**：50.1<br>**数据校验规则**：<br>- 取值范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `object_api_name` | `string` | 是 | 自定义组织类型<br>**示例值**："custom_org_01" |
| &nbsp;&nbsp;└ `seniority_adjust_informations` | `seniority_adjust_information_edit\[\]` | 否 | 司龄调整信息<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `seniority_adjustment_type` | `string` | 是 | 调整类型 - 可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：   - object_api_name：seniority_adjust_information   - custom_api_name：seniority_adjustment_type<br>**示例值**："increase"<br>**可选值有**：<br>- `increase`: 增加 - `decrease`: 减少 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 否 | 开始日期 - 格式： yyyy-mm-dd<br>**示例值**："2024-01-01" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 否 | 结束日期 - 格式： yyyy-mm-dd<br>**示例值**："2024-01-02" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `reasons_for_seniority_adjustment` | `string` | 否 | 调整原因<br>**示例值**："工厂停产需要减去半年工龄" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `seniority_adjustment` | `number(float)` | 是 | 调整值 - 精确度：两位小数 - 单位：年<br>**示例值**：1.01<br>**数据校验规则**：<br>- 取值范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `profile_setting_custom_field\[\]` | 否 | 自定义字段 - 具体支持的对象请参考[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**数据校验规则**：<br>- 长度范围：`0` ～ `180` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："custom_field_1__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 否 | 字段值, 是 json 转义后的字符串，根据元数据定义不同，字段格式不同。使用方式可参考【操作手册】如何通过 OpenAPI 维护自定义字段<br>**示例值**："[\"custom_enum_0__c\"]" |
| &nbsp;&nbsp;└ `default_cost_center` | `default_cost_center_record` | 否 | 默认成本中心 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `reason` | `string` | 否 | 变更原因<br>**示例值**："默认成本中心变更" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_inherit` | `boolean` | 否 | 是否继承<br>**示例值**：true |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_id` | `cost_center_id` | 否 | 默认成本中心 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_id` | `string` | 否 | 成本中心<br>**示例值**："7382048365313261588" |
| &nbsp;&nbsp;└ `cost_allocation` | `cost_allocation` | 否 | 成本分摊 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 否 | 分摊生效日期<br>**示例值**："2025-01-01" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 否 | 分摊失效日期<br>**示例值**："2025-02-01" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_rates` | `job_data_cost_center\[\]` | 否 | 成本分摊信息<br>**数据校验规则**：<br>- 长度范围：`0` ～ `50` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_id` | `string` | 否 | 成本中心 ID，可以通过【查询单个成本中心信息】接口获取对应的成本中心信息<br>**示例值**："6950635856373745165" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rate` | `int` | 否 | 分摊比例(整数)<br>**示例值**：100 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `new_rate` | `number(float)` | 否 | 分摊比例<br>**示例值**：50.2 |
| `career` | `profile_setting_career` | 否 | 履历信息 |
| &nbsp;&nbsp;└ `educations` | `profile_setting_education\[\]` | 否 | 教育经历<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `school` | `string` | 否 | 学校<br>**示例值**："北京大学" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `school_enum` | `string` | 否 | 学校<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "education"  - custom_api_name = "school_name"<br>**示例值**："school-177" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 否 | 开始日期<br>**示例值**："2011-09-01" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 否 | 结束日期<br>**示例值**："2015-06-30" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `level_of_education` | `string` | 否 | 学历<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "education"  - custom_api_name = "level_of_education"<br>**示例值**："masters_degree" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `field_of_study` | `string` | 否 | 专业<br>**示例值**："软件工程" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `degree` | `string` | 否 | 学位<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "education"  - custom_api_name = "degree"<br>**示例值**："bachelors_degree" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `field_of_study_enum` | `string` | 否 | 专业<br>枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：  - object_api_name = "education" - custom_api_name = "field_of_study_name"<br>**示例值**："field_of_study-2" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `profile_setting_custom_field\[\]` | 否 | 自定义字段 - 请参考[自定义字段说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："custom_field_1__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 否 | 字段值<br>是 JSON 转义后的字符串，根据元数据定义不同，字段格式不同。使用方式可参考[【操作手册】如何通过 OpenAPI 维护自定义字段](https://feishu.feishu.cn/docx/QlUudBfCtosWMbxx3vxcOFDknn7)<br>**示例值**："123" |
| &nbsp;&nbsp;└ `work_experiences` | `profile_setting_work_experience\[\]` | 否 | 工作经历<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `company_organization` | `profile_setting_i18n` | 否 | 公司 / 组织 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 否 | 中文<br>**示例值**："中文名" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 否 | 英文<br>**示例值**："english name" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `profile_setting_i18n` | 否 | 部门 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 否 | 中文<br>**示例值**："中文名" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 否 | 英文<br>**示例值**："english name" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 否 | 开始日期<br>**示例值**："2020-01-01" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 否 | 结束日期<br>**示例值**："2020-02-01" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job` | `profile_setting_i18n` | 否 | 岗位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 否 | 中文<br>**示例值**："中文名" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 否 | 英文<br>**示例值**："english name" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `profile_setting_i18n` | 否 | 工作描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 否 | 中文<br>**示例值**："中文名" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 否 | 英文<br>**示例值**："english name" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `profile_setting_custom_field\[\]` | 否 | 自定义字段 - 请参考[自定义字段说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："custom_field_1__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 否 | 字段值<br>是 JSON 转义后的字符串，根据元数据定义不同，字段格式不同。使用方式可参考[【操作手册】如何通过 OpenAPI 维护自定义字段](https://feishu.feishu.cn/docx/QlUudBfCtosWMbxx3vxcOFDknn7)<br>**示例值**："123" |
| &nbsp;&nbsp;└ `custom_groups` | `profile_setting_custom_group\[\]` | 否 | 自定义分组<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `group_name` | `string` | 否 | 分组名<br>**示例值**："custom_obj__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `items` | `profile_setting_custom_group_item\[\]` | 否 | 分组数据<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `profile_setting_custom_field\[\]` | 否 | 自定义字段 - 请参考[自定义字段说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："custom_field_1__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 否 | 字段值<br>是 JSON 转义后的字符串，根据元数据定义不同，字段格式不同。使用方式可参考[【操作手册】如何通过 OpenAPI 维护自定义字段](https://feishu.feishu.cn/docx/QlUudBfCtosWMbxx3vxcOFDknn7)<br>**示例值**："123" |
| `data_attachment` | `profile_setting_data_attachment` | 否 | 资料附件 |
| &nbsp;&nbsp;└ `personal_records` | `profile_setting_personal_record\[\]` | 否 | 资料附件记录<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `profile_type` | `string` | 否 | 资料类型<br>- 枚举值可通过[【获取字段详情】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：    - object_api_name = "personal_profile"    - custom_api_name = "profile_type" - 仅 【飞书人事-档案配置-资料附件】存在的字段编码可用<br>**示例值**："profile_type_1" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `files` | `profile_setting_file\[\]` | 否 | 文件列表<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 否 | 文件 ID<br>- 可通过[【上传文件】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/person/upload)接口获取 - 只传该字段即可，大小、类型等字段可以不传递<br>**示例值**："150018109586e8ea745e47ae8feb3722dbe1d03a181336393633393133303431393831343930373235150200" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mime_type` | `string` | 否 | 文件 MIME 类型<br>**示例值**："zip" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 否 | 文件名<br>**示例值**："附件.zip" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `size` | `string` | 否 | 文件大小（KB）<br>**示例值**："1000" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 否 | 文件 Token<br>**示例值**："0a423bc7ea7c4a439d066bf070616782" |
| &nbsp;&nbsp;└ `custom_groups` | `profile_setting_custom_group\[\]` | 否 | 自定义分组<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `group_name` | `string` | 否 | 分组名<br>**示例值**："custom_obj__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `items` | `profile_setting_custom_group_item\[\]` | 否 | 分组数据<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `profile_setting_custom_field\[\]` | 否 | 自定义字段 - 请参考[自定义字段说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名<br>**示例值**："custom_field_1__c" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 否 | 字段值<br>是 JSON 转义后的字符串，根据元数据定义不同，字段格式不同。使用方式可参考[【操作手册】如何通过 OpenAPI 维护自定义字段](https://feishu.feishu.cn/docx/QlUudBfCtosWMbxx3vxcOFDknn7)<br>**示例值**："123" |


### 请求体示例

```json
{
    "personal_info": {
        "personal_basic_info": {
            "legal_name": {
                "additional_name_type": "emergency_contact_name",
                "country_region": "6862995757234914824",
                "full_name": "王大帅",
                "hereditary": "王",
                "middle_name": "大",
                "secondary": "王",
                "social": "ii",
                "tertiary": "王",
                "local_first_name_2": "五",
                "local_middle_name": "大",
                "local_primary": "黄",
                "local_primary_2": "王",
                "local_secondary": "王",
                "title": "Mr",
                "local_first_name": "四",
                "custom_local_name": "王大帅",
                "custom_western_name": "王大帅",
                "first_name": "帅",
                "name_primary": "王"
            },
            "preferred_name": {
                "additional_name_type": "emergency_contact_name",
                "country_region": "6862995757234914824",
                "full_name": "王大帅",
                "hereditary": "王",
                "middle_name": "大",
                "secondary": "王",
                "social": "ii",
                "tertiary": "王",
                "local_first_name_2": "五",
                "local_middle_name": "大",
                "local_primary": "黄",
                "local_primary_2": "王",
                "local_secondary": "王",
                "title": "mr",
                "local_first_name": "四",
                "custom_local_name": "王大帅",
                "custom_western_name": "王大帅",
                "first_name": "帅",
                "name_primary": "王"
            },
            "additional_name": "王帅",
            "gender": "female",
            "nationality_v2": "6862995757234914826",
            "ethnicity_race": "han",
            "phone": {
                "international_area_code": "86_china",
                "phone_number": "13000000000"
            },
            "email": "1234567@example.feishu.cn",
            "date_of_birth": "2006-01-02",
            "marital_status": "married",
            "is_disabled": false,
            "disable_card_number": "92838277746172888312",
            "is_martyr_family": false,
            "martyr_card_number": "00001",
            "is_old_alone": false,
            "born_country_region": "6862995757234914825",
            "political_affiliation": "other",
            "native_region": "6862995757234914827",
            "date_entered_workforce": "2006-01-02",
            "first_entry_time": "2006-01-02",
            "leave_time": "2006-01-02",
            "custom_fields": [
                {
                    "field_name": "custom_field_1__c",
                    "value": "123"
                }
            ],
            "additional_nationalities": [
                "6862995757234914827"
            ]
        },
        "emergency_contacts": [
            {
                "legal_name": "王大帅",
                "relationship": "parent",
                "is_primary": true,
                "phone": {
                    "international_area_code": "86_china",
                    "phone_number": "13000000000"
                },
                "email": "1234567@example.feishu.cn",
                "address": {
                    "address_type": "home_address",
                    "country_region": "6862995757234914824",
                    "region": "6863326815667095047",
                    "region_subdivision_1": "行政区1",
                    "region_subdivision_2": "行政区2",
                    "city_v2": "6862995757234914829",
                    "city_text": "北京市",
                    "local_city_text": "北京市",
                    "city_subdivision_1": "行政区 1",
                    "city_subdivision_2": "行政区 2",
                    "district_v2": "6862995757234914831",
                    "postal_code": "611530",
                    "address_line_1": "丹佛测试地址 - 纽埃时区",
                    "local_address_line_1": "丹佛测试地址 - 纽埃时区",
                    "address_line_2": "PoewH",
                    "local_address_line_2": "PoewH",
                    "address_line_3": "PoewH",
                    "local_address_line_3": "PoewH",
                    "address_line_4": "jmwJc",
                    "local_address_line_5": "jmwJc",
                    "address_line_6": "jmwJc",
                    "local_address_line_6": "jmwJc",
                    "address_line_7": "jmwJc",
                    "local_address_line_7": "jmwJc",
                    "address_line_8": "jmwJc",
                    "local_address_line_8": "rafSu",
                    "address_line_9": "McPRG",
                    "local_address_line_9": "McPRG",
                    "local_address_line_4": "jmwJc",
                    "address_line_5": "jmwJc"
                },
                "custom_fields": [
                    {
                        "field_name": "custom_field_1__c",
                        "value": "123"
                    }
                ]
            }
        ],
        "bank_accounts": [
            {
                "country_region": "6862995757234914824",
                "bank_name": "中国农业银行",
                "branch_name": "中国农业银行支行",
                "account_holder": "孟十五",
                "bank_account_number": "6231200000001223",
                "bank_account_usages": [
                    "payment"
                ],
                "bank_account_type": "savings",
                "bank_id": "6862995757234914832",
                "branch_id": "6862995757234914833",
                "payment_type": "percent,balance,amount",
                "payment_rate": "80.28",
                "payment_amount": "5000",
                "priority": "1"
            }
        ],
        "nationals": [
            {
                "country_region": "6862995757234914824",
                "national_id_type": "6863330041896371725",
                "national_id_number": "1231131333",
                "issued_date": "2020-04-01",
                "issued_by": "北京市公安局",
                "expiration_date": "2020-05-21",
                "custom_fields": [
                    {
                        "field_name": "custom_field_1__c",
                        "value": "123"
                    }
                ]
            }
        ],
        "resident_taxes": [
            {
                "year_resident_tax": "2006-01-02",
                "tax_country_region": "6862995757234914824",
                "resident_status": "tax_residence",
                "custom_fields": [
                    {
                        "field_name": "custom_field_1__c",
                        "value": "123"
                    }
                ]
            }
        ],
        "dependents": [
            {
                "legal_name": "王大帅",
                "date_of_birth": "2006-01-02",
                "relationship_with_dependent": "parent",
                "gender": "female",
                "phone": {
                    "international_area_code": "86_china",
                    "phone_number": "13000000000"
                },
                "job": "岗位",
                "child_birth_certificates": [
                    {
                        "file_id": "150018109586e8ea745e47ae8feb3722dbe1d03a181336393633393133303431393831343930373235150200",
                        "mime_type": "zip",
                        "name": "附件.zip",
                        "size": "1000",
                        "token": "0a423bc7ea7c4a439d066bf070616782"
                    }
                ],
                "employer": "飞书",
                "custom_fields": [
                    {
                        "field_name": "custom_field_1__c",
                        "value": "123"
                    }
                ],
                "address": {
                    "address_type": "home_address",
                    "country_region": "6862995757234914824",
                    "region": "6863326815667095047",
                    "region_subdivision_1": "行政区 1",
                    "region_subdivision_2": "行政区 2",
                    "city_v2": "6862995757234914829",
                    "city_text": "北京市",
                    "local_city_text": "北京市",
                    "city_subdivision_1": "行政区 1",
                    "city_subdivision_2": "行政区 2",
                    "district_v2": "6862995757234914831",
                    "postal_code": "611530",
                    "address_line_1": "丹佛测试地址 - 纽埃时区",
                    "local_address_line_1": "丹佛测试地址 - 纽埃时区",
                    "address_line_2": "PoewH",
                    "local_address_line_2": "PoewH",
                    "address_line_3": "PoewH",
                    "local_address_line_3": "PoewH",
                    "address_line_4": "jmwJc",
                    "local_address_line_5": "jmwJc",
                    "address_line_6": "jmwJc",
                    "local_address_line_6": "jmwJc",
                    "address_line_7": "jmwJc",
                    "local_address_line_7": "jmwJc",
                    "address_line_8": "jmwJc",
                    "local_address_line_8": "rafSu",
                    "address_line_9": "McPRG",
                    "local_address_line_9": "McPRG",
                    "local_address_line_4": "jmwJc",
                    "address_line_5": "jmwJc"
                }
            }
        ],
        "hukou": {
            "hukou_type": "local_urban_residence",
            "hukou_location": "北京",
            "custom_fields": [
                {
                    "field_name": "custom_field_1__c",
                    "value": "123"
                }
            ]
        },
        "contact_addresses": [
            {
                "address_type": "home_address",
                "country_region": "6862995757234914824",
                "region": "6863326815667095047",
                "region_subdivision_1": "行政区 1",
                "region_subdivision_2": "行政区 2",
                "city_v2": "6862995757234914829",
                "city_text": "北京市",
                "local_city_text": "北京市",
                "city_subdivision_1": "行政区 1",
                "city_subdivision_2": "行政区 2",
                "district_v2": "6862995757234914831",
                "postal_code": "611530",
                "address_line_1": "丹佛测试地址 - 纽埃时区",
                "local_address_line_1": "丹佛测试地址 - 纽埃时区",
                "address_line_2": "PoewH",
                "local_address_line_2": "PoewH",
                "address_line_3": "PoewH",
                "local_address_line_3": "PoewH",
                "address_line_4": "jmwJc",
                "local_address_line_5": "jmwJc",
                "address_line_6": "jmwJc",
                "local_address_line_6": "jmwJc",
                "address_line_7": "jmwJc",
                "local_address_line_7": "jmwJc",
                "address_line_8": "jmwJc",
                "local_address_line_8": "rafSu",
                "address_line_9": "McPRG",
                "local_address_line_9": "McPRG",
                "local_address_line_4": "jmwJc",
                "address_line_5": "jmwJc"
            }
        ],
        "custom_groups": [
            {
                "group_name": "custom_obj__c",
                "items": [
                    {
                        "custom_fields": [
                            {
                                "field_name": "custom_field_1__c",
                                "value": "123"
                            }
                        ]
                    }
                ]
            }
        ],
        "citizenship_statuses": [
            {
                "country_region": "7324333990030034476",
                "citizenship_status": "公民"
            }
        ]
    },
    "employment_info": {
        "basic_info": {
            "employee_number": "1000000",
            "effective_time": "2021-01-01",
            "regular_employee_start_date": "2021-02-01",
            "seniority_date": "2020-01-01",
            "work_email": "12456@test.com",
            "phone": {
                "international_area_code": "86_china",
                "phone_number": "13000000000"
            },
            "user_geo": "cn",
            "custom_fields": [
                {
                    "field_name": "custom_field_1__c",
                    "value": "123"
                }
            ]
        },
        "probation_info": {
            "probation_start_date": "2021-01-01",
            "probation_expected_end_date": "2021-02-01",
            "actual_probation_end_date": "2021-02-01"
        },
        "employment_record": {
            "employee_type": "6890452208593372679",
            "department": "6890452208593372679",
            "direct_manager": "6893014062142064135",
            "working_hours_type": "6890452208593372600",
            "cost_centers": [
                {
                    "id": "6950635856373745165",
                    "rate": 100
                }
            ],
            "direct_manager_effective_time": "2020-01-01",
            "dotted_line_manager": "6893014062142064136",
            "dotted_line_manager_effective_time": "2020-01-01",
            "job": "6890452208593372679",
            "job_family": "6890452208593372680",
            "job_level": "6890452208593372681",
            "job_grade": "6890452208593372682",
            "work_location": "6890452208593372683",
            "weekly_working_hours": 100,
            "position": "6890452208593372684",
            "pathway": "6890452208593372684"
        },
        "emp_contract_record": {
            "contract_number": "6919737965274990093",
            "contract_type": "labor_contract",
            "first_party": "6892686614112241165",
            "effective_time": "2006-01-02",
            "duration_type": "fixed_term",
            "contract_end_date": "2050-01-01"
        },
        "custom_groups": [
            {
                "group_name": "custom_obj__c",
                "items": [
                    {
                        "custom_fields": [
                            {
                                "field_name": "custom_field_1__c",
                                "value": "123"
                            }
                        ]
                    }
                ]
            }
        ],
        "custom_org_groups": [
            {
                "effective_time": "2024-07-02",
                "start_reason": "新增人员",
                "custom_org_with_rates": [
                    {
                        "id": "7260357352426782739",
                        "rate": 50.1
                    }
                ],
                "object_api_name": "custom_org_01"
            }
        ],
        "seniority_adjust_informations": [
            {
                "seniority_adjustment_type": "increase",
                "start_date": "2024-01-01",
                "end_date": "2024-01-02",
                "reasons_for_seniority_adjustment": "工厂停产需要减去半年工龄",
                "seniority_adjustment": 1.01,
                "custom_fields": [
                    {
                        "field_name": "custom_field_1__c",
                        "value": "[\"custom_enum_0__c\"]"
                    }
                ]
            }
        ],
        "default_cost_center": {
            "reason": "默认成本中心变更",
            "is_inherit": true,
            "cost_center_id": {
                "wk_id": "7382048365313261588"
            }
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
        }
    },
    "career": {
        "educations": [
            {
                "school": "北京大学",
                "school_enum": "school-177",
                "start_date": "2011-09-01",
                "end_date": "2015-06-30",
                "level_of_education": "masters_degree",
                "field_of_study": "软件工程",
                "degree": "bachelors_degree",
                "field_of_study_enum": "field_of_study-2",
                "custom_fields": [
                    {
                        "field_name": "custom_field_1__c",
                        "value": "123"
                    }
                ]
            }
        ],
        "work_experiences": [
            {
                "company_organization": {
                    "zh_cn": "中文名",
                    "en_us": "english name"
                },
                "department": {
                    "zh_cn": "中文名",
                    "en_us": "english name"
                },
                "start_date": "2020-01-01",
                "end_date": "2020-02-01",
                "job": {
                    "zh_cn": "中文名",
                    "en_us": "english name"
                },
                "description": {
                    "zh_cn": "中文名",
                    "en_us": "english name"
                },
                "custom_fields": [
                    {
                        "field_name": "custom_field_1__c",
                        "value": "123"
                    }
                ]
            }
        ],
        "custom_groups": [
            {
                "group_name": "custom_obj__c",
                "items": [
                    {
                        "custom_fields": [
                            {
                                "field_name": "custom_field_1__c",
                                "value": "123"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "data_attachment": {
        "personal_records": [
            {
                "profile_type": "profile_type_1",
                "files": [
                    {
                        "file_id": "150018109586e8ea745e47ae8feb3722dbe1d03a181336393633393133303431393831343930373235150200",
                        "mime_type": "zip",
                        "name": "附件.zip",
                        "size": "1000",
                        "token": "0a423bc7ea7c4a439d066bf070616782"
                    }
                ]
            }
        ],
        "custom_groups": [
            {
                "group_name": "custom_obj__c",
                "items": [
                    {
                        "custom_fields": [
                            {
                                "field_name": "custom_field_1__c",
                                "value": "123"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `employment_id` | `string` | 雇佣信息 ID<br>可通过[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取详细信息 |
| &nbsp;&nbsp;└ `contract_id` | `string` | 合同 ID<br>可通过[【批量查询合同】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息 |
| &nbsp;&nbsp;└ `job_data_id` | `string` | 任职信息 ID<br>可通过[【批量查询员工任职信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employees-job_data/batch_get)接口获取详细信息 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "employment_id": "6862995757234914824",
        "contract_id": "6862995757234914824",
        "job_data_id": "6862995757234914824"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1160001 | 系统错误。请稍后重试或联系技术支持。 | 请稍后重试或联系[技术支持](https://applink.feishu.cn/TLJpeNdW)。 |
| 400 | 1160002 | 参数校验失败 | 请按照错误返回提示，修改信息后重新提交。 |
| 400 | 1160003 | 数据过期 | 人员表单字段必填要求发生变化，请按照必填要求重新提交。 |
| 400 | 1160004 | 业务规则校验失败 | 请按照错误返回提示，修改信息后重新提交。 |
| 400 | 1160005 | 业务规则校验失败 | 请按照错误返回提示，修改信息后重新提交。 |
| 400 | 1160006 | 需要超编确认 | 可用的编制规划数不足，需进行超编确认，若允许超编请设置 “force_submit” 为 true 确认人员添加 |
| 400 | 1160007 | 不允许超编 | 可用的编制规划数不足，禁止提交。 |
| 400 | 1160008 | 幂等 token 重复 | token 信息重复 |


