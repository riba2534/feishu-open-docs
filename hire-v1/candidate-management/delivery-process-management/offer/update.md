---
title: "更新 Offer 信息"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer/update"
updateTime: "1753877023000"
---

# 更新 Offer 信息

更新 Offer 信息，包含基本信息、薪资信息、自定义信息。


## 注意事项
- 更新 Offer 时，除了本文中标注为必填的参数外，其余参数是否必填请参考[获取 Offer 申请表信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer_application_form/get)的参数定义
- 对系统中 Offer 进行更新时，若本次更新 Offer 字段中含有「修改需审批」的字段，更新后原 Offer 的审批会自动撤回，需要重新发起审批；修改需审批字段详情可查看：[获取 Offer 申请表信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer_application_form/get)接口中`need_approve`字段
- 当 Offer 状态为以下 2 种时， 不可更新 Offer：`Offer 已发送`、`Offer 被候选人接受`，Offer 状态详情可查看：[获取 Offer 详情](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer/get)
- 该接口会对原 Offer 内容进行全量覆盖更新，若非必填参数未填写则会清空原有内容，必填参数未填写会拦截报错。

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/offers/:offer_id |
| HTTP Method | PUT |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:offer` 更新 offer 信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `offer_id` | `string` | Offer ID，可通过[获取 Offer 列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer/list)接口获取<br>**示例值**："7016605170635213100" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_admin_id`: 以people_admin_id来识别用户<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 指定查询结果中的部门 ID 类型。关于部门 ID 的详细介绍，可参见[部门资源介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/field-overview)。<br>**示例值**：department_id<br>**可选值有**：<br>- `open_department_id`: 由系统自动生成的部门 ID， ID前缀固定为 `od-`，在租户内全局唯一。 - `department_id`: 支持用户自定义配置的部门 ID。自定义配置时可复用已删除的 department_id，因此在未删除的部门范围内，department_id 具有唯一性。<br>**默认值**：`open_department_id` |
| `job_level_id_type` | `string` | 否 | 此次调用中使用的「职级 ID」的类型<br>**示例值**：job_level_id<br>**可选值有**：<br>- `people_admin_job_level_id`: 「人力系统管理后台」适用的职级 ID。人力系统管理后台逐步下线中，建议不继续使用此 ID。 - `job_level_id`: 「飞书管理后台」适用的职级 ID，通过[获取租户职级列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_level/list)接口获取<br>**默认值**：`people_admin_job_level_id` |
| `job_family_id_type` | `string` | 否 | 此次调用中使用的「序列 ID」的类型<br>**示例值**：job_family_id<br>**可选值有**：<br>- `people_admin_job_category_id`: 「人力系统管理后台」适用的序列 ID。人力系统管理后台逐步下线中，建议不继续使用此 ID。 - `job_family_id`: 「飞书管理后台」适用的序列 ID，通过[获取租户序列列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_family/list)接口获取<br>**默认值**：`people_admin_job_category_id` |
| `employee_type_id_type` | `string` | 否 | 此次调用中使用的「人员类型 ID」的类型<br>**示例值**：employee_type_enum_id<br>**可选值有**：<br>- `people_admin_employee_type_id`: 「人力系统管理后台」适用的人员类型 ID。人力系统管理后台逐步下线中，建议不继续使用此 ID。 - `employee_type_enum_id`: 「飞书管理后台」适用的人员类型 ID，通过[查询人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list)接口获取<br>**默认值**：`people_admin_employee_type_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `schema_id` | `string` | 是 | Offer 申请表模板 ID，用于描述申请表单结构的元数据定义，即对申请表内容的描述。用户每一次更改 Offer 申请表模板信息，都会生成新的 schema_id，创建 Offer 时应传入最新的 schema_id，可先从[获取职位设置](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/config)中拿到offer申请表 ID，再从[获取 Offer 申请表信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer_application_form/get)接口中获取最新的模板 ID。<br>**示例值**："7013318077945596204" |
| `basic_info` | `offer_basic_info` | 是 | Offer 基本信息 |
| &nbsp;&nbsp;└ `department_id` | `string` | 是 | 部门 ID，与入参中的`department_id_type`类型一致，可通过[搜索部门](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/search)接口获取<br>**示例值**："od-6b394871807047c7023ebfc1ff37cd3a" |
| &nbsp;&nbsp;└ `leader_user_id` | `string` | 是 | 直属上级 ID，需与入参`user_id_type`类型一致<br>**示例值**："ou_ce613028fe74745421f5dc320bb9c709" |
| &nbsp;&nbsp;└ `employment_job_id` | `string` | 否 | 职务 ID，可通过[批量查询职务](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/list)获取，**请注意**：仅支持开通飞书人事企业版的租户使用<br>**示例值**："6807407987381831949" |
| &nbsp;&nbsp;└ `employee_type_id` | `string` | 否 | 人员类型 ID，需与入参`employee_type_id_type` 类型一致<br>**示例值**："6807407987381831949" |
| &nbsp;&nbsp;└ `job_family_id` | `string` | 否 | 职位序列 ID，需与入参`job_family_id_type` 类型一致<br>**示例值**："6807407987381831949" |
| &nbsp;&nbsp;└ `job_level_id` | `string` | 否 | 职位级别 ID，需与入参`job_level_id_type` 类型一致<br>**示例值**："6807407987381881101" |
| &nbsp;&nbsp;└ `probation_month` | `int` | 否 | 试用期（月）<br>**示例值**：3 |
| &nbsp;&nbsp;└ `contract_year` | `int` | 否 | 合同期(年)，推荐使用`contract_period`<br>**示例值**：3 |
| &nbsp;&nbsp;└ `contract_period` | `contract_period_info` | 否 | 合同期（年/月） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `period_type` | `int` | 是 | 合同周期类型<br>**示例值**：1<br>**可选值有**：<br>- `1`: 月 - `2`: 年 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `period` | `int` | 是 | 合同时长<br>**示例值**：3<br>**数据校验规则**：<br>- 取值范围：`0` ～ `100` |
| &nbsp;&nbsp;└ `expected_onboard_date` | `string` | 否 | 预计入职日期，格式为：{"date":"YYYY-MM-DD"}，使用时请注意转义<br>**示例值**："{\"date\":\"2022-04-07\"}" |
| &nbsp;&nbsp;└ `onboard_address_id` | `string` | 否 | 入职地点 ID，可通过[获取地址列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/list)接口获取<br>**示例值**："6897079709306259719" |
| &nbsp;&nbsp;└ `work_address_id` | `string` | 否 | 办公地点 ID，可通过[获取地址列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/list)接口获取<br>**示例值**："6897079709306259719" |
| &nbsp;&nbsp;└ `owner_user_id` | `string` | 是 | Offer负责人 ID，需与入参`user_id_type`类型一致<br>**示例值**："ou_ce613028fe74745421f5dc320bb9c709" |
| &nbsp;&nbsp;└ `recommended_words` | `string` | 否 | Offer 推荐语<br>**示例值**："十分优秀，推荐入职" |
| &nbsp;&nbsp;└ `job_requirement_id` | `string` | 否 | 招聘需求 ID，可通过[获取招聘需求列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_requirement/list)接口获取<br>**示例值**："6791698585114724616" |
| &nbsp;&nbsp;└ `job_process_type_id` | `int` | 否 | 招聘流程类型 ID**可选值**： - 1：社招 - 2：校招<br>**示例值**：2 |
| &nbsp;&nbsp;└ `attachment_id_list` | `string\[\]` | 否 | 附件 ID 列表，暂无获取附件 ID 的方式，请勿使用<br>**示例值**：["7159169181052061965"] |
| &nbsp;&nbsp;└ `common_attachment_id_list` | `string\[\]` | 否 | 通用附件 ID 列表，可使用[创建附件](https://open.larkoffice.com/document/ukTMukTMukTM/uIDN1YjLyQTN24iM0UjN/create_attachment)接口创建的附件<br>**示例值**：["7483412052430997804"] |
| &nbsp;&nbsp;└ `attachment_description` | `string` | 否 | 附件描述<br>**示例值**："张三的简历" |
| &nbsp;&nbsp;└ `operator_user_id` | `string` | 是 | Offer 操作人 ID，需与入参`user_id_type`类型一致<br>**示例值**："ou_ce613028fe74745421f5dc320bb9c709" |
| &nbsp;&nbsp;└ `position_id` | `string` | 否 | 岗位 ID，可通过[查询岗位信息](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/position/query) 获取（仅限飞书人事租户使用，若链接无法打开，则说明飞书人事未启用岗位，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)开通）<br>**示例值**："6897079709306259719" |
| &nbsp;&nbsp;└ `job_offered` | `string` | 否 | 入职职位<br>**示例值**："入职职位" |
| &nbsp;&nbsp;└ `job_grade_id` | `string` | 否 | 职等 ID，可通过[查询职等](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query) 获取（仅限飞书人事租户使用）<br>**示例值**："6897079709306259720" |
| &nbsp;&nbsp;└ `pathway_id` | `string` | 否 | 通道 ID<br>**示例值**："6897079709306259719" |
| `salary_info` | `offer_salary_info` | 否 | Offer 薪资信息 |
| &nbsp;&nbsp;└ `currency` | `string` | 是 | 币种<br>**示例值**："CNY" |
| &nbsp;&nbsp;└ `basic_salary` | `string` | 否 | 基本薪资，当启用 Offer 申请表中的「薪资信息」模块时，「基本工资」字段为必传项，支持小数点后两位<br>**示例值**："1000000" |
| &nbsp;&nbsp;└ `probation_salary_percentage` | `string` | 否 | 试用期百分比，支持小数点后两位<br>**示例值**："0.8" |
| &nbsp;&nbsp;└ `award_salary_multiple` | `string` | 否 | 年终奖月数，仅支持整数<br>**示例值**："3" |
| &nbsp;&nbsp;└ `option_shares` | `string` | 否 | 期权股数，仅支持整数<br>**示例值**："30" |
| &nbsp;&nbsp;└ `quarterly_bonus` | `string` | 否 | 季度奖金额，单位元、支持小数点后两位<br>**示例值**："3000" |
| &nbsp;&nbsp;└ `half_year_bonus` | `string` | 否 | 半年奖金额，单位元、支持小数点后两位<br>**示例值**："10000" |
| `customized_info_list` | `offer_customized_info\[\]` | 否 | 自定义信息，此字段更新为覆盖式更新，旧 Offer 中已存在字段不传则默认为删除，反之为新增 |
| &nbsp;&nbsp;└ `id` | `string` | 否 | 自定义字段 ID<br>**示例值**："6972464088568269100" |
| &nbsp;&nbsp;└ `value` | `string` | 否 | 自定义字段信息，以字符串形式传入，如： 1. 单行文本："xxx " 2. 多行文本："xxx " 3. 单选： "1" 4. 多选："[\"1\", \"2\"]" 5. 日期："{"date":"2022-01-01"}" 6. 年份选择："{"date":"2022"}" 7. 月份选择："{"date":"2022-01"}" 8. 数字："123" 9. 金额："123.1" 10. 公式："( [6872592813776914699] * 12 + 20 / 2 ) / [6872592813776914699] + 2000"，其中6872592813776914699为薪资字段 ID - 更多详细请查看：[获取 Offer 申请表信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer_application_form/get)<br>**示例值**："1" |


### 请求体示例

```json
{
    "schema_id": "7013318077945596204",
    "basic_info": {
        "department_id": "od-6b394871807047c7023ebfc1ff37cd3a",
        "leader_user_id": "ou_ce613028fe74745421f5dc320bb9c709",
        "employment_job_id": "6807407987381831949",
        "employee_type_id": "6807407987381831949",
        "job_family_id": "6807407987381831949",
        "job_level_id": "6807407987381881101",
        "probation_month": 3,
        "contract_year": 3,
        "contract_period": {
            "period_type": 1,
            "period": 3
        },
        "expected_onboard_date": "{\"date\":\"2022-04-07\"}",
        "onboard_address_id": "6897079709306259719",
        "work_address_id": "6897079709306259719",
        "owner_user_id": "ou_ce613028fe74745421f5dc320bb9c709",
        "recommended_words": "十分优秀，推荐入职",
        "job_requirement_id": "6791698585114724616",
        "job_process_type_id": 2,
        "attachment_id_list": [
            "7159169181052061965"
        ],
        "common_attachment_id_list": [
            "7483412052430997804"
        ],
        "attachment_description": "张三的简历",
        "operator_user_id": "ou_ce613028fe74745421f5dc320bb9c709",
        "position_id": "6897079709306259719",
        "job_offered": "入职职位",
        "job_grade_id": "6897079709306259720",
        "pathway_id": "6897079709306259719"
    },
    "salary_info": {
        "currency": "CNY",
        "basic_salary": "1000000",
        "probation_salary_percentage": "0.8",
        "award_salary_multiple": "3",
        "option_shares": "30",
        "quarterly_bonus": "3000",
        "half_year_bonus": "10000"
    },
    "customized_info_list": [
        {
            "id": "6972464088568269100",
            "value": "1"
        }
    ]
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `offer_info` | \- |
| &nbsp;&nbsp;└ `offer_id` | `string` | Offer ID，详情请查看：[获取 Offer 详情](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer/get) |
| &nbsp;&nbsp;└ `schema_id` | `string` | Offer 申请表模板 ID |
| &nbsp;&nbsp;└ `basic_info` | `offer_basic_info` | Offer 基本信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 部门 ID，与入参中的`department_id_type`类型一致，详情请查看[获取单个部门信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `leader_user_id` | `string` | 直属上级 ID，与入参`user_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_job_id` | `string` | 职务 ID，详情请查看[获取单个职务信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_title/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type_id` | `string` | 人员类型 ID，与入参`employee_type_id_type` 类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id` | `string` | 职位序列 ID，与入参`job_family_id_type` 类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_level_id` | `string` | 职位级别 ID，与入参`job_level_id_type` 类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `probation_month` | `int` | 试用期（月） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_year` | `int` | 合同期(年)，推荐使用`contract_period` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_period` | `contract_period_info` | 合同期（年/月） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `period_type` | `int` | 合同周期类型<br>**可选值有**：<br>- `1`: 月 - `2`: 年 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `period` | `int` | 合同时长 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expected_onboard_date` | `string` | 预计入职日期，格式为：{"date":"YYYY-MM-DD"}，使用时请注意转义 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `onboard_address_id` | `string` | 入职地点 ID，详情请查看：[获取地址列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_address_id` | `string` | 办公地点 ID，详情请查看：[获取地址列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `owner_user_id` | `string` | Offer 负责人 ID，与入参`user_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `recommended_words` | `string` | Offer 推荐语 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_requirement_id` | `string` | 招聘需求 ID，详情请查看：[获取招聘需求信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_requirement/list_by_id) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_process_type_id` | `int` | 招聘流程类型 ID**可选值**： - 1：社招 - 2：校招 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `attachment_id_list` | `string\[\]` | 附件 ID 列表（废弃） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `common_attachment_id_list` | `string\[\]` | 通用附件 ID 列表，可通过[获取附件信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get)接口获取附件的详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `attachment_description` | `string` | 附件描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operator_user_id` | `string` | Offer 操作人 ID，与入参`user_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `position_id` | `string` | 岗位 ID，可通过[查询岗位信息](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/position/query) 获取（仅限飞书人事租户使用，若链接无法打开，则说明飞书人事未启用岗位，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)开通） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_offered` | `string` | 入职职位 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_grade_id` | `string` | 职等 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `pathway_id` | `string` | 通道 ID |
| &nbsp;&nbsp;└ `salary_info` | `offer_salary_info` | Offer 薪资信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `currency` | `string` | 币种 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `basic_salary` | `string` | 基本薪资，支持小数点后两位 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `probation_salary_percentage` | `string` | 试用期百分比，支持小数点后两位 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `award_salary_multiple` | `string` | 年终奖月数，仅支持整数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `option_shares` | `string` | 期权股数，仅支持整数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `quarterly_bonus` | `string` | 季度奖金额，单位元、支持小数点后两位 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `half_year_bonus` | `string` | 半年奖金额，单位元、支持小数点后两位 |
| &nbsp;&nbsp;└ `customized_info_list` | `offer_customized_info\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 自定义字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 自定义字段信息 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "ok",
    "data": {
        "offer_id": "7016605170635213100",
        "schema_id": "7013318077945596204",
        "basic_info": {
            "department_id": "od-6b394871807047c7023ebfc1ff37cd3a",
            "leader_user_id": "ou_ce613028fe74745421f5dc320bb9c709",
            "employment_job_id": "6807407987381831949",
            "employee_type_id": "6807407987381831949",
            "job_family_id": "6807407987381831949",
            "job_level_id": "6807407987381881101",
            "probation_month": 3,
            "contract_year": 3,
            "contract_period": {
                "period_type": 1,
                "period": 3
            },
            "expected_onboard_date": "{\"date\":\"2022-04-07\"}",
            "onboard_address_id": "6897079709306259719",
            "work_address_id": "6897079709306259719",
            "owner_user_id": "ou_ce613028fe74745421f5dc320bb9c709",
            "recommended_words": "十分优秀，推荐入职",
            "job_requirement_id": "6791698585114724616",
            "job_process_type_id": 2,
            "attachment_id_list": [
                "7159169181052061965"
            ],
            "common_attachment_id_list": [
                "7483412052430997804"
            ],
            "attachment_description": "张三的简历",
            "operator_user_id": "ou_ce613028fe74745421f5dc320bb9c709",
            "position_id": "6897079709306259719",
            "job_offered": "入职职位",
            "job_grade_id": "6897079709306259720",
            "pathway_id": "6897079709306259719"
        },
        "salary_info": {
            "currency": "CNY",
            "basic_salary": "1000000",
            "probation_salary_percentage": "0.8",
            "award_salary_multiple": "3",
            "option_shares": "11",
            "quarterly_bonus": "3000",
            "half_year_bonus": "10000"
        },
        "customized_info_list": [
            {
                "id": "6972464088568269100",
                "value": "1"
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |
| 500 | 1002054 | 投递不存在 | 投递不存在，根据参数`offer_id `未找到对应投递，请检查参数或使用[获取 Offer 详情](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer/get)接口查询对应 Offer 是否存在，以及确认接口返回值`application_id ` |
| 500 | 1002055 | 投递已经终止 | Offer 对应投递已终止，不可被更新，详情可根据[获取 Offer 详情](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer/get)接口查看投递 ID，再根据[获取投递信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/get)接口查看投递状态 |
| 500 | 1002056 | 投递阶段异常 | 投递阶段异常，详情可根据[获取 Offer 详情](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer/get)接口查看投递 ID，再根据[获取投递信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/get)接口查看投递阶段是否异常 |
| 500 | 1002057 | Offer 申请表模板不是最新的版本 | Offer 申请表模板不是最新的版本，请检查`schema_id `参数是否正确 |
| 500 | 1002058 | Offer 附件不存在 | Offer 附件不存在，请检查 `attachment_id_list `参数是否正确 |
| 500 | 1002059 | Offer 申请表模板不存在 | Offer 申请表模板不存在，请检查`schema_id `参数是否正确 |
| 500 | 1002061 | 公式无效 | 公式无效，请检查`customized_info_list `参数中公式相关 |
| 500 | 1002064 | Offer 不存在 | Offer 不存在，请检查`offer_id `参数是否正确 |
| 500 | 1002066 | Offer 状态不支持更新 | Offer 当前状态不支持更新，可根据[获取 Offer 详情](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer/get)接口查看 Offer 状态 |
| 400 | 1002069 | 职务不存在 | 职务不存在，请检查`employment_job_id `参数是否正确 |
| 400 | 1002070 | 职务已停用 | 职务已停用，请检查`employment_job_id `参数是否正确 |
| 400 | 1002071 | 序列不存在 | 序列不存在，请检查`job_family_id `参数是否正确 |
| 400 | 1002072 | 序列已停用 | 序列已停用，请检查`job_family_id `参数是否正确 |
| 400 | 1002073 | 职级不存在 | 职级不存在，请检查`job_level_id `参数是否正确 |
| 400 | 1002074 | 职级已停用 | 职级已停用，请检查`job_level_id `参数是否正确 |
| 400 | 1002077 | 职务、序列不匹配 | 职务、序列不匹配，请检查`employment_job_id `、`job_family_id `参数是否正确 |
| 400 | 1002078 | 职务、职级不匹配 | 职务、职级不匹配，请检查`employment_job_id `、`job_level_id `参数是否正确 |
| 400 | 1002079 | 序列、职级不匹配(在序列与职级在生效时间内未查询到关联的生效职务) | 序列、职级不匹配，请检查`job_family_id `、`job_level_id `参数是否正确 |
| 400 | 1002082 | Offer 附件数量超过限制 | Offer 附件每个请求最多 20 个，请减少请求中的 Offer 附件数量 |
| 400 | 1002083 | Offer 附件对应的文件不存在 | 请检查附件 ID 是否合法 |


