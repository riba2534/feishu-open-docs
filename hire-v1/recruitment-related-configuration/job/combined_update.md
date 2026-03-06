---
title: "更新职位"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/combined_update"
updateTime: "1725955133000"
---

# 更新职位

更新职位信息。


## 注意事项

- 调用此接口前，需先打开「飞书招聘」-「设置」-「职位管理」-「职位设置」-「通过API同步职位开关」开关。

- 该接口为全量更新，若字段没有填充值，则原有值将会被清空。

- 字段是否必填，将以「飞书招聘」-「设置」-「职位管理」-「职位字段管理」中的设置为准。

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/jobs/:job_id/combined_update |
| HTTP Method | POST |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:job` 更新职位信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `job_id` | `string` | 职位 ID，可通过 [获取职位列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/list) 接口获取<br>**示例值**："6960663240925956660" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 指定查询结果中的部门 ID 类型。关于部门 ID 的详细介绍，可参见[部门资源介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/field-overview)。<br>**示例值**：open_department_id<br>**可选值有**：<br>- `open_department_id`: 由系统自动生成的部门 ID， ID前缀固定为 `od-`，在租户内全局唯一。 - `department_id`: 支持用户自定义配置的部门 ID。自定义配置时可复用已删除的 department_id，因此在未删除的部门范围内，department_id 具有唯一性。<br>**默认值**：`open_department_id` |
| `job_level_id_type` | `string` | 否 | 此次调用中使用的「职级 ID」的类型<br>**示例值**：people_admin_job_level_id<br>**可选值有**：<br>- `people_admin_job_level_id`: 「人力系统管理后台」适用的职级 ID。人力系统管理后台逐步下线中，建议不继续使用此 ID。 - `job_level_id`: 「飞书管理后台」适用的职级 ID，可通过 [获取租户职级列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_level/list) 接口获取<br>**默认值**：`people_admin_job_level_id` |
| `job_family_id_type` | `string` | 否 | 此次调用中使用的「序列 ID」的类型<br>**示例值**：people_admin_job_category_id<br>**可选值有**：<br>- `people_admin_job_category_id`: 「人力系统管理后台」适用的序列 ID。人力系统管理后台逐步下线中，建议不继续使用此 ID。 - `job_family_id`: 「飞书管理后台」适用的序列 ID，可通过 [获取租户序列列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_family/list) 接口获取<br>**默认值**：`people_admin_job_category_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `id` | `string` | 否 | 职位 ID，可通过 [获取职位列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/list) 接口获取<br>**示例值**："6960663240925956576" |
| `experience` | `int` | 否 | 工作经验要求<br>**示例值**：1<br>**可选值有**：<br>- `1`: 不限 - `2`: 应届毕业生 - `3`: 1年以下 - `4`: 1-3年 - `5`: 3-5年 - `6`: 5-7年 - `7`: 7-10年 - `8`: 10年以上 |
| `expiry_time` | `int` | 否 | 到期日期，此字段已废弃，请使用expiry_timestamp<br>**示例值**：1622484739 |
| `customized_data_list` | `combined_job_object_value_map\[\]` | 否 | 自定义字段 - 注意：更新时会全量覆盖 |
| &nbsp;&nbsp;└ `object_id` | `string` | 否 | 自定义字段 ID，可通过[获取职位模板](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_schema/list)接口获取<br>**示例值**："6960663240925956549" |
| &nbsp;&nbsp;└ `value` | `string` | 否 | 自定义字段值，请参考本文「自定义字段数据格式说明」。<br>**示例值**："自定义内容" |
| `min_level_id` | `string` | 否 | 最低职级 ID，需与入参`job_level_id_type` 类型一致<br>**示例值**："6960663240925956547" |
| `min_salary` | `int` | 否 | 最低薪资，单位：K<br>**示例值**：1000 |
| `title` | `string` | 否 | 职位名称<br>**示例值**："后端研发" |
| `job_managers` | `job.manager` | 是 | 职位管理者列表 |
| &nbsp;&nbsp;└ `id` | `string` | 否 | 职位 ID（废弃字段，请忽略）<br>**示例值**："1618209327096" |
| &nbsp;&nbsp;└ `recruiter_id` | `string` | 是 | 招聘负责人 ID，需与入参`user_id_type`类型一致<br>**示例值**："ou_efk39117c300506837def50545420c6a" |
| &nbsp;&nbsp;└ `hiring_manager_id_list` | `string\[\]` | 是 | 用人经理 ID 列表，需与入参`user_id_type`类型一致<br>**示例值**：["on_94a1ee5551019f18cd73d9f111898cf2"] |
| &nbsp;&nbsp;└ `assistant_id_list` | `string\[\]` | 否 | 协助人 ID 列表，需与入参`user_id_type`类型一致<br>**示例值**：["on_94a1ee5551019f18cd73d9f111898cf2"] |
| `job_process_id` | `string` | 否 | 招聘流程，可通过[获取招聘流程信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_process/list)接口获取<br>**示例值**："6960663240925956554" |
| `subject_id` | `string` | 否 | 项目 ID，可通过[获取项目列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/subject/list)接口获取<br>**示例值**："6960663240925956555" |
| `job_function_id` | `string` | 否 | 职能分类ID，可通过[获取职能分类列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_function/list)接口获取<br>**示例值**："6960663240925956555" |
| `department_id` | `string` | 否 | 部门 ID，需与入参中的`department_id_type`类型一致<br>**示例值**："od-b2fafdce6fc5800b574ba5b0e2798b36" |
| `head_count` | `int` | 否 | 招聘数量<br>**示例值**：100 |
| `is_never_expired` | `boolean` | 是 | 是否长期有效<br>**示例值**：false |
| `max_salary` | `int` | 否 | 最高薪资，单位：K<br>**示例值**：2000 |
| `requirement` | `string` | 否 | 职位要求<br>**示例值**："熟悉后端研发" |
| `description` | `string` | 否 | 职位描述<br>**示例值**："后端研发岗位描述" |
| `highlight_list` | `string\[\]` | 否 | 职位亮点 ID 列表， 详情请查看：[枚举常量介绍](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/enum)中「职位亮点枚举定义」<br>**示例值**：["6887476508052523278"] |
| `job_type_id` | `string` | 是 | 职位类别ID，可通过[获取职位类别列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_type/list)接口获取<br>**示例值**："6960663240925956551" |
| `max_level_id` | `string` | 否 | 最高职级 ID，需与入参`job_level_id_type` 类型一致<br>**示例值**："6960663240925956548" |
| `required_degree` | `int` | 否 | 学历要求<br>**示例值**：20<br>**可选值有**：<br>- `1`: 小学及以上 - `2`: 初中及以上 - `3`: 专职及以上 - `4`: 高中及以上 - `5`: 大专及以上 - `6`: 本科及以上 - `7`: 硕士及以上 - `8`: 博士及以上 - `20`: 不限 |
| `job_category_id` | `string` | 否 | 序列 ID，需与入参`job_family_id_type` 类型一致<br>**示例值**："6960663240925956550" |
| `address_id_list` | `string\[\]` | 否 | 工作地点 ID 列表，可通过[获取地址列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/list)接口获取<br>**示例值**：["6960663240925956553"] |
| `job_attribute` | `int` | 否 | 职位属性<br>**示例值**：6960663240925956554<br>**可选值有**：<br>- `1`: 实体职位 - `2`: 虚拟职位 |
| `expiry_timestamp` | `string` | 否 | 到期时间，毫秒时间戳，如果`is_never_expired`字段选择true，则不会实际使用该字段的值，职位为长期有效<br>**示例值**："1622484739955" |
| `target_major_id_list` | `string\[\]` | 否 | 目标专业 ID 列表，可通过[「分页批量查询专业」](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/mdm-v3/major/list)获取<br>**示例值**：["MDMJ00000067"] |


### 自定义字段数据格式说明
-  单选：`"1"`
-  多选：`"[\"1\", \"2\"]"`
-  单行：`"单行文本"`
-  多行：`"多行文本"`
-  数字：`"1"`
-  月份选择：`"1627379423000"`
-  年份选择：`"1627379423000"`
-  日期选择：`"1627379423000"`
-  附件：`"[{\"file_id\": \"7250161881116838204\"},{\"file_id\": \"7250161808660826429\"}]"`
-  时间段：`"[\"1577808000000\", \"1612108800000\"]"`


### 请求体示例

```json
{
    "id": "6960663240925956576",
    "experience": 1,
    "expiry_time": 1622484739,
    "customized_data_list": [
        {
            "object_id": "6960663240925956549",
            "value": "自定义内容"
        }
    ],
    "min_level_id": "6960663240925956547",
    "min_salary": 1000,
    "title": "后端研发",
    "job_managers": {
        "id": "1618209327096",
        "recruiter_id": "ou_efk39117c300506837def50545420c6a",
        "hiring_manager_id_list": [
            "on_94a1ee5551019f18cd73d9f111898cf2"
        ],
        "assistant_id_list": [
            "on_94a1ee5551019f18cd73d9f111898cf2"
        ]
    },
    "job_process_id": "6960663240925956554",
    "subject_id": "6960663240925956555",
    "job_function_id": "6960663240925956555",
    "department_id": "od-b2fafdce6fc5800b574ba5b0e2798b36",
    "head_count": 100,
    "is_never_expired": false,
    "max_salary": 2000,
    "requirement": "熟悉后端研发",
    "description": "后端研发岗位描述",
    "highlight_list": [
        "6887476508052523278"
    ],
    "job_type_id": "6960663240925956551",
    "max_level_id": "6960663240925956548",
    "required_degree": 20,
    "job_category_id": "6960663240925956550",
    "address_id_list": [
        "6960663240925956553"
    ],
    "job_attribute": 6960663240925956554,
    "expiry_timestamp": "1622484739955",
    "target_major_id_list": [
        "MDMJ00000067"
    ]
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `combined_job_result` | \- |
| &nbsp;&nbsp;└ `default_job_post` | `combined_job_result_default_job_post` | 职位广告 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 默认职位广告的 ID，可通过[职位发布至官网](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/advertisement/publish)接口 发布至官网 |
| &nbsp;&nbsp;└ `job` | `job` | 职位 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职位 ID，详情请查看：[获取职位信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 职位名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 职位描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 职位编号 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `requirement` | `string` | 职位要求 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `recruitment_type` | `job_recruitment_type` | 雇佣类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 雇佣类型 ID，详情请参考：[枚举常量介绍](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/enum)中「职位性质/雇佣类型（recruitment_type）枚举定义」 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 雇佣类型中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 雇佣类型英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 雇佣类型启用状态<br>**可选值有**：<br>- `1`: 启用 - `2`: 未启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `job_department` | 部门 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 部门 ID，与入参中的`department_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 部门中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 部门英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `city` | `job_city` | 工作城市 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_code` | `string` | 工作城市码，详情请查看：[查询地点列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 工作城市中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 工作城市英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `min_job_level` | `job_level` | 最低职级 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职级 ID，与入参`job_level_id_type` 类型一致，详情请查看：[获取租户职级列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_level/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 职级中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 职级英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 职级启用状态<br>**可选值有**：<br>- `1`: 启用 - `2`: 未启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `max_job_level` | `job_level` | 最高职级 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职级 ID，与入参`job_level_id_type` 类型一致，详情请查看：[获取租户职级列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_level/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 职级中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 职级英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 职级启用状态<br>**可选值有**：<br>- `1`: 启用 - `2`: 未启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `highlight_list` | `job_highlight\[\]` | 职位亮点 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职位亮点列表，详情请查看：[枚举常量介绍](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/enum)中职位亮枚举定义」 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 职位亮点中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 职位亮点英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_category` | `job_category` | 职位序列 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职位序列 ID，与入参`job_family_id_type` 类型一致，详情请查看[获取租户序列列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_family/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 职位序列中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 职位序列英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 职位序列启用状态<br>**可选值有**：<br>- `1`: 启用 - `2`: 未启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_type` | `job_type` | 职位类别 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职位类别 ID，详情请查看：[获取职位类别列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_type/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 职位类别中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 职位类别英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 启用状态<br>**可选值有**：<br>- `1`: 启用 - `2`: 未启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 创建人ID，若为空则为系统或其他对接系统创建，与入参`user_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `int` | 创建时间，此字段已废弃，请使用create_timestamp |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `update_time` | `int` | 更新时间，此字段已废弃，请使用update_timestamp |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `process_type` | `int` | 招聘流程类型<br>**可选值有**：<br>- `1`: 社招流程 - `2`: 校招流程 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `process_id` | `string` | 招聘流程 ID，详情请查看：[获取招聘流程信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_process/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `process_name` | `string` | 招聘流程中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `process_en_name` | `string` | 招聘流程英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `job_customized_data\[\]` | 自定义字段列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 字段中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 字段英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `job_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `job_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `job_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `job_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是毫秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_function` | `id_name_object` | 职能分类 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职能 ID，详情请查看：[获取职能分类列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_function/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 职能名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 职能中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 职能英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `subject` | `id_name_object` | 项目 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 项目 ID，详情请查看：[获取项目列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/subject/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 项目名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 项目中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 项目英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `head_count` | `int` | 招聘数量 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `experience` | `int` | 工作经验要求<br>**可选值有**：<br>- `1`: 不限 - `2`: 应届毕业生 - `3`: 1年以下 - `4`: 1-3年 - `5`: 3-5年 - `6`: 5-7年 - `7`: 7-10年 - `8`: 10年以上 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiry_time` | `int` | 到期日期，此字段已废弃，请使用expiry_timestamp |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `min_salary` | `int` | 最低薪资，单位：K |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `max_salary` | `int` | 最高薪资，单位：K |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `required_degree` | `int` | 学历要求<br>**可选值有**：<br>- `1`: 小学及以上 - `2`: 初中及以上 - `3`: 专职及以上 - `4`: 高中及以上 - `5`: 大专及以上 - `6`: 本科及以上 - `7`: 硕士及以上 - `8`: 博士及以上 - `20`: 不限 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `city_list` | `code_name_object\[\]` | 工作城市列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 城市编码，详情请查看：[查询地点列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 城市名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 城市中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 城市英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_attribute` | `int` | 职位属性<br>**可选值有**：<br>- `1`: 实体职位 - `2`: 虚拟职位 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_timestamp` | `string` | 创建时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `update_timestamp` | `string` | 更新时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiry_timestamp` | `string` | 到期时间，毫秒时间戳，如果`is_never_expired`字段选择true，则不会实际使用该字段的值，职位为长期有效 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `target_major_list` | `target_major_info\[\]` | 目标专业列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 目标专业 ID，详情请查看：[「根据主数据编码批量获取专业」](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/mdm-v3/batch_major/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 目标专业中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 目标专业英文名称 |
| &nbsp;&nbsp;└ `job_manager` | `job.manager` | 职位负责人 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职位 ID，详情请查看：[获取职位信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `recruiter_id` | `string` | 招聘负责人 ID，与入参`user_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `hiring_manager_id_list` | `string\[\]` | 用人经理 ID 列表，与入参`user_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `assistant_id_list` | `string\[\]` | 协助人 ID 列表，与入参`user_id_type`类型一致 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "ok",
    "data": {
        "default_job_post": {
            "id": "6960663240925956568"
        },
        "job": {
            "id": "7281257045172308287",
            "title": "测试职位",
            "description": "这是一个测试职位",
            "code": "Z88",
            "requirement": "要求高学历人才",
            "recruitment_type": {
                "id": "7281257045172308287",
                "zh_name": "全职",
                "en_name": "FullTime",
                "active_status": 1
            },
            "department": {
                "id": "7281257045172308287",
                "zh_name": "字节跳动",
                "en_name": "Bytedance"
            },
            "city": {
                "city_code": "CT_20",
                "zh_name": "成都",
                "en_name": "Chengdu"
            },
            "min_job_level": {
                "id": "7281257045172308287",
                "zh_name": "级别-2",
                "en_name": "level-2",
                "active_status": 1
            },
            "max_job_level": {
                "id": "7281257045172308287",
                "zh_name": "级别-2",
                "en_name": "level-2",
                "active_status": 1
            },
            "highlight_list": [
                {
                    "id": "7281257045172308287",
                    "zh_name": "团队氛围好",
                    "en_name": "Positive team atmosphere"
                }
            ],
            "job_category": {
                "id": "7281257045172308287",
                "zh_name": "序列-A",
                "en_name": "category-A",
                "active_status": 1
            },
            "job_type": {
                "id": "6890840777044265230",
                "zh_name": "金融",
                "en_name": "Finance"
            },
            "active_status": 1,
            "create_user_id": "7281257045172308287",
            "create_time": 1617170925462,
            "update_time": 1617170925462,
            "process_type": 1,
            "process_id": "1",
            "process_name": "流程中文名",
            "process_en_name": "流程英文名",
            "customized_data_list": [
                {
                    "object_id": "7281257045172308287",
                    "name": {
                        "zh_cn": "字段 1",
                        "en_us": "field 1"
                    },
                    "object_type": 1,
                    "value": {
                        "content": "这是一个单行文本",
                        "option": {
                            "key": "7281257045172308287",
                            "name": {
                                "zh_cn": "选项 A",
                                "en_us": "Option A"
                            }
                        },
                        "option_list": [
                            {
                                "key": "7281257045172308287",
                                "name": {
                                    "zh_cn": "选项 A",
                                    "en_us": "Option A"
                                }
                            }
                        ],
                        "time_range": {
                            "start_time": "1622484739955",
                            "end_time": "1622484739955"
                        },
                        "time": "1625456721000",
                        "number": "111"
                    }
                }
            ],
            "job_function": {
                "id": "7281257045172308287",
                "name": {
                    "zh_cn": "测试职能",
                    "en_us": "test job function"
                }
            },
            "subject": {
                "id": "7281257045172308287",
                "name": {
                    "zh_cn": "测试项目",
                    "en_us": "test subject"
                }
            },
            "head_count": 100,
            "experience": 1,
            "expiry_time": 1622484739955,
            "min_salary": 10,
            "max_salary": 20,
            "required_degree": 1,
            "city_list": [
                {
                    "code": "CT_223",
                    "name": {
                        "zh_cn": "成都",
                        "en_us": "Chengdu"
                    }
                }
            ],
            "job_attribute": 1,
            "create_timestamp": "1617170925462",
            "update_timestamp": "1617170925462",
            "expiry_timestamp": "1622484739955",
            "target_major_list": [
                {
                    "id": "MDMJ00000067",
                    "zh_name": "考古",
                    "en_name": "archeology"
                }
            ]
        },
        "job_manager": {
            "id": "1618209327096",
            "recruiter_id": "ou_efk39117c300506837def50545420c6a",
            "hiring_manager_id_list": [
                "on_94a1ee5551019f18cd73d9f111898cf2"
            ],
            "assistant_id_list": [
                "on_94a1ee5551019f18cd73d9f111898cf2"
            ]
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。 |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |
| 400 | 1002613 | 「通过API同步职位开关」尚未打开，仅支持在招聘系统中新建、编辑或关闭职位 | 请确认职位同步开关是否已开启；路径：「飞书招聘」-「设置」-「职位管理」-「职位设置」-「通过API同步职位开关」 |
| 400 | 1002615 | 职位已有候选人投递，不可更改该职位流程 | 请检查`job_id`参数是否正确，并可通过[获取投递列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/list)接口，查询职位已有候选人。 |
| 400 | 1002603 | 职位类别不存在 | 职位类别不存在，请检查`job_type_id `参数是否正确 |
| 400 | 1002604 | 雇佣类型不存在 | 雇佣类型不存在，请检查`recruitment_type `参数是否正确 |
| 400 | 1002605 | 序列不存在 | 序列不存在，请检查`job_category_id `参数是否正确 |
| 400 | 1002606 | 级别不存在 | 级别不存在，请检查`max_level_id `或`min_level_id `参数是否正确 |
| 400 | 1002607 | 职位亮点不存在 | 职位亮点不存在，请检查`highlight_list `参数是否正确 |
| 400 | 1002608 | 项目不存在 | 项目不存在，请检查`subject_id `参数是否正确 |
| 400 | 1002609 | 职位已关闭 | 职位已关闭，请通过[获取职位信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/get)接口查看职位关闭状态 |
| 400 | 1002622 | 目标专业不存在 | 目标专业不存在，请检查`target_major_id_list `参数是否正确 |
| 400 | 1002623 | 选择「不限专业」时不可设置其他目标专业 | 选择「不限专业」时不可设置其他目标专业，请检查`target_major_id_list `参数是否还额外设置其他目标专业 |
| 400 | 1002630 | 职位职级已停用 | 职位职级已停用，请检查`max_level_id `或`min_level_id `参数是否正确 |
| 400 | 1002631 | 当前职位正在处理投递锁定，不可修改 | 当前职位正在处理职位换项目投递锁定任务，不可修改，请稍后重试。 |


