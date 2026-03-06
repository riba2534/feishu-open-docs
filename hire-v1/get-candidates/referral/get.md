---
title: "获取内推官网下职位广告详情"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/referral_website-job_post/get"
updateTime: "1724813287000"
---

# 获取内推官网下职位广告详情

根据职位广告 ID 获取内推官网下的职位广告详情，包含职位广告 ID 以及职位信息等。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/referral_websites/job_posts/:job_post_id |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:referral_website:readonly` 获取内推官网信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `job_post_id` | `string` | 职位广告 ID，可通过[获取内推官网下职位广告列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/referral_website-job_post/list)获取<br>**示例值**："6701528341100366094" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 指定查询结果中的部门 ID 类型。关于部门 ID 的详细介绍，可参见[部门ID说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/field-overview)。<br>**示例值**：open_department_id<br>**可选值有**：<br>- `open_department_id`: 由系统自动生成的部门 ID，ID 前缀固定为 od-，在租户内全局唯一。 - `department_id`: 支持用户自定义配置的部门 ID。自定义配置时可复用已删除的 department_id，因此在未删除的部门范围内 department_id 具有唯一性。<br>**默认值**：`open_department_id` |
| `job_level_id_type` | `string` | 否 | 此次调用中使用的「职级 ID」的类型<br>**示例值**：job_level_id<br>**可选值有**：<br>- `people_admin_job_level_id`: 「人力系统管理后台」适用的职级 ID。人力系统管理后台逐步下线中，建议不继续使用此 ID。 - `job_level_id`: 「飞书管理后台」适用的职级 ID，通过[获取租户职级列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_level/list)接口获取<br>**默认值**：`people_admin_job_level_id` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `job_post` | `portal_job_post` | 职位广告信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职位广告 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 职位名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_id` | `string` | 职位 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_code` | `string` | 职位编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_expire_time` | `string` | 职位到期时间，毫秒时间戳，空代表「长期有效」 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_active_status` | `int` | 职位状态<br>**可选值有**：<br>- `1`: 启用态 - `2`: 禁用态 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_process_type` | `int` | 职位流程类型<br>**可选值有**：<br>- `1`: 社招 - `2`: 校招 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_recruitment_type` | `id_name_object` | 雇佣类型，请参考[枚举常量介绍](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/enum) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 雇佣类型ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 雇佣类型名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_department` | `id_name_object` | 部门 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 部门ID，与`department_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 部门名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_type` | `id_name_object` | 职位类别 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职位类别ID，详情请参考：[获取职位类别列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_type/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 职位类别名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `min_job_level` | `id_name_object` | 最低职级 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 最低职级 ID，与入参`job_level_id_type` 类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 最低职级名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `max_job_level` | `id_name_object` | 最高职级 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 最高职级 ID，与入参`job_level_id_type` 类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 最高职级名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address` | `common_address` | 职位地址，废弃字段，请使用`address_list`字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职位地址ID，详情请参考：[获取地址列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 职位地址名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `district` | `code_name_object` | 区域信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 区域编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 区域名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city` | `code_name_object` | 城市信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 城市编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 城市名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `state` | `code_name_object` | 省份信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 省份编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 省份名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country` | `code_name_object` | 国家信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 国家编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 国家名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `min_salary` | `string` | 月薪范围-最低薪资，单位：K，精度：整数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `max_salary` | `string` | 月薪范围-最高薪资，单位：K，精度：整数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `required_degree` | `int` | 学历要求<br>**可选值有**：<br>- `1`: 小学及以上 - `2`: 初中及以上 - `3`: 专职及以上 - `4`: 高中及以上 - `5`: 大专及以上 - `6`: 本科及以上 - `7`: 硕士及以上 - `8`: 博士及以上 - `20`: 不限 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `experience` | `int` | 工作经验<br>**可选值有**：<br>- `1`: 不限 - `2`: 应届毕业生 - `3`: 1年以下 - `4`: 1-3年 - `5`: 3-5年 - `6`: 5-7年 - `7`: 7-10年 - `8`: 10年以上 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `headcount` | `int` | 招聘数量 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `high_light_list` | `id_name_object\[\]` | 职位亮点列表，详情请参考：[枚举常量介绍](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/enum) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职位亮点ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 职位亮点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 职位描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `requirement` | `string` | 职位要求 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `creator` | `id_name_object` | 创建人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 创建人ID，与`user_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 创建人名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 创建时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `modify_time` | `string` | 修改时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `website_job_post_customized_data\[\]` | 自定义字段列表，详情可参考：[获取职位模板](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_schema/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `website_job_post_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `website_job_post_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `website_job_post_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `website_job_post_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是毫秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_function` | `id_name_object` | 职能分类 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职能分类 ID，详情请查看：[获取职能分类列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_function/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 职能分类名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `subject` | `id_name_object` | 项目 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 项目ID，详情可参考：[获取项目列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/subject/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 项目名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address_list` | `common_address\[\]` | 职位地址列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职位地址ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 职位地址名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `district` | `code_name_object` | 区域信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 区域编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 区域名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city` | `code_name_object` | 城市信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 城市编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 城市名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `state` | `code_name_object` | 省份信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 省份编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 省份名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country` | `code_name_object` | 国家信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 国家编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 国家名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "SUCCESS",
    "data": {
        "job_post": {
            "id": "7174316547413000195",
            "title": "高级工程师招聘",
            "job_id": "7392894182636030258",
            "job_code": "A168688",
            "job_expire_time": "1722837278000",
            "job_active_status": 1,
            "job_process_type": 1,
            "job_recruitment_type": {
                "id": "101",
                "name": {
                    "zh_cn": "全职",
                    "en_us": "Full-time"
                }
            },
            "job_department": {
                "id": "od-7b2eb7561bfbe4cac5267c142762870a",
                "name": {
                    "zh_cn": "IT部门",
                    "en_us": "IT department"
                }
            },
            "job_type": {
                "id": "6791698585114724616",
                "name": {
                    "zh_cn": "互联网 / 电子 / 网游",
                    "en_us": "Internet / Electronics / Games"
                }
            },
            "min_job_level": {
                "id": "6890840777044265230",
                "name": {
                    "zh_cn": "级别-2",
                    "en_us": "level-2"
                }
            },
            "max_job_level": {
                "id": "6890840777044265230",
                "name": {
                    "zh_cn": "级别-5",
                    "en_us": "level-5"
                }
            },
            "address": {
                "id": "6583482347283472832",
                "name": {
                    "zh_cn": "抖音大厦",
                    "en_us": "Douyin Building"
                },
                "district": {
                    "code": "DS_1000002",
                    "name": {
                        "zh_cn": "大观区",
                        "en_us": "Daguan"
                    }
                },
                "city": {
                    "code": "CT_2",
                    "name": {
                        "zh_cn": "安庆",
                        "en_us": "Anqing"
                    }
                },
                "state": {
                    "code": "ST_2",
                    "name": {
                        "zh_cn": "安徽",
                        "en_us": "Anhui"
                    }
                },
                "country": {
                    "code": "CN_1",
                    "name": {
                        "zh_cn": "中国大陆",
                        "en_us": "Chinese Mainland"
                    }
                }
            },
            "min_salary": "5",
            "max_salary": "20",
            "required_degree": 1,
            "experience": 1,
            "headcount": 12,
            "high_light_list": [
                {
                    "id": "6732430418202593547",
                    "name": {
                        "zh_cn": "下午茶",
                        "en_us": "afternoon tea"
                    }
                }
            ],
            "description": "负责软件开发",
            "requirement": "有相关经验者优先",
            "creator": {
                "id": "ou_a512d829e05693f1cfaa419e17bd2d80",
                "name": {
                    "zh_cn": "张三",
                    "en_us": "zhangsan"
                }
            },
            "create_time": "1716791547691",
            "modify_time": "1716791547691",
            "customized_data_list": [
                {
                    "object_id": "7368811146881091852",
                    "name": {
                        "zh_cn": "集团数字化",
                        "en_us": "group digitization"
                    },
                    "object_type": 1,
                    "value": {
                        "content": "集团数字化是大方向",
                        "option": {
                            "key": "1",
                            "name": {
                                "zh_cn": "支持",
                                "en_us": "support"
                            }
                        },
                        "option_list": [
                            {
                                "key": "1",
                                "name": {
                                    "zh_cn": "强支持",
                                    "en_us": "strong support"
                                }
                            }
                        ],
                        "time_range": {
                            "start_time": "1716791547691",
                            "end_time": "1716891547691"
                        },
                        "time": "1625456721000",
                        "number": "88"
                    }
                }
            ],
            "job_function": {
                "id": "7281257045172308287",
                "name": {
                    "zh_cn": "技术",
                    "en_us": "technology"
                }
            },
            "subject": {
                "id": "7367286785368312075",
                "name": {
                    "zh_cn": "24年秋季招聘项目",
                    "en_us": "Fall '24 recruitment program"
                }
            },
            "address_list": [
                {
                    "id": "6583482347283472832",
                    "name": {
                        "zh_cn": "抖音大厦",
                        "en_us": "Douyin Building"
                    },
                    "district": {
                        "code": "DS_1000002",
                        "name": {
                            "zh_cn": "大观区",
                            "en_us": "daguan"
                        }
                    },
                    "city": {
                        "code": "CT_2",
                        "name": {
                            "zh_cn": "安庆",
                            "en_us": "Anqing"
                        }
                    },
                    "state": {
                        "code": "ST_2",
                        "name": {
                            "zh_cn": "安徽",
                            "en_us": "Anhui"
                        }
                    },
                    "country": {
                        "code": "CN_1",
                        "name": {
                            "zh_cn": "中国大陆",
                            "en_us": "Chinese Mainland"
                        }
                    }
                }
            ]
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |
| 404 | 1002509 | 职位广告未发布至官网 | 检查参数`job_post_id`对应的职位广告是否发布到官网上 |


