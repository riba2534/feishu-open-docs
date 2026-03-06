---
title: "获取人才信息"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/get"
updateTime: "1764644266000"
---

# 获取人才信息

根据人才 ID 获取人才信息。


> **Tip**: 本接口不再更新，推荐使用新接口：[获取人才详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/hire-v2/talent/get)


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/talents/:talent_id |
| HTTP Method | GET |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:talent:readonly` 获取人才信息 `hire:talent` 更新人才信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `talent_id` | `string` | 人才ID，可通过[获取人才列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/list)接口获取<br>**示例值**："6891560630172518670" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_admin_id`: 以 people_admin_id 来识别用户<br>**默认值**：`people_admin_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `talent` | `talent` | 人才信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 人才ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_in_agency_period` | `boolean` | 是否在猎头保护期<br>**可选值有**：<br>- `false`: 未在猎头保护期 - `true`: 在猎头保护期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_onboarded` | `boolean` | 是否已入职<br>**可选值有**：<br>- `false`: 未入职 - `true`: 已入职 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `basic_info` | `talent_basic_info` | 基础信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile` | `string` | 手机 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_code` | `string` | 手机国家区号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_country_code` | `string` | 手机国家代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `experience_years` | `int` | 工作年限 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `age` | `int` | 年龄 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `nationality` | `talent_nationality` | 国籍 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `nationality_code` | `string` | 国家编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `gender` | `int` | 性别<br>**可选值有**：<br>- `1`: 男 - `2`: 女 - `3`: 保密 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `current_city` | `talent_city_info` | 所在地点 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_code` | `string` | 城市码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hometown_city` | `talent_city_info` | 家乡 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_code` | `string` | 城市码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `preferred_city_list` | `talent_city_info\[\]` | 意向地点 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city_code` | `string` | 城市码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `identification_type` | `int` | 证件类型<br>**可选值有**：<br>- `1`: 中国 - 居民身份证 - `2`: 护照 - `3`: 中国 - 港澳居民居住证 - `4`: 中国 - 台湾居民来往大陆通行证 - `5`: 其他 - `6`: 中国 - 港澳居民来往内地通行证 - `9`: 中国 - 台湾居民居住证 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `identification_number` | `string` | 证件号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `birthday` | `int` | 生日 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `creator_id` | `string` | 创建人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `marital_status` | `int` | 婚姻状况<br>**可选值有**：<br>- `1`: 已婚 - `2`: 未婚 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `current_home_address` | `string` | 家庭住址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日选择 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `modify_time` | `string` | 修改时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hukou_location_code` | `string` | 户口所在地 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `education_list` | `talent_education_info\[\]` | 教育经历 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `degree` | `int` | 学位<br>**可选值有**：<br>- `1`: 小学 - `2`: 初中 - `3`: 专职 - `4`: 高中 - `5`: 大专 - `6`: 本科 - `7`: 硕士 - `11`: MBA - `8`: 博士 - `9`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `school` | `string` | 学校 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_of_study` | `string` | 专业 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time_v2` | `string` | 结束时间-新，无「至今」传值。建议使用此字段，避免模糊的毕业时间影响候选人筛选 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `education_type` | `int` | 学历类型<br>**可选值有**：<br>- `1`: 海外及港台 - `2`: 统招全日制 - `3`: 非全日制 - `4`: 自考 - `5`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `academic_ranking` | `int` | 成绩排名<br>**可选值有**：<br>- `5`: 前 5 % - `10`: 前 10 % - `20`: 前 20 % - `30`: 前 30 % - `50`: 前 50 % - `-1`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tag_list` | `int\[\]` | 教育经历标签<br>**可选值有**：<br>- `1`: 985学校 - `2`: 211学校 - `3`: 一本 - `4`: 国外院校QS200 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日选择 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `career_list` | `talent_career_info\[\]` | 工作经历 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `company` | `string` | 公司名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 职位名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `desc` | `string` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `career_type` | `int` | 经历类型<br>**可选值有**：<br>- `1`: 实习经历 - `2`: 工作经历 - `3`: 兼职经历 - `4`: 其他经历 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tag_list` | `int\[\]` | 工作经历标签<br>**可选值有**：<br>- `5`: BAT - `6`: TMD - `14`: 互联网100强 - `10`: 互联网大厂 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日选择 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `project_list` | `talent_project_info\[\]` | 项目经历 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 项目名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `role` | `string` | 项目角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `string` | 项目链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `desc` | `string` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日选择 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `works_list` | `talent_works_info\[\]` | 作品 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `string` | 作品链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `desc` | `string` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 作品附件名称，若需获取作品附件预览信息可调用「获取附件预览信息」接口 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日选择 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `award_list` | `talent_award_info\[\]` | 获奖 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 获奖名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `award_time` | `string` | 获奖时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `desc` | `string` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日选择 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `language_list` | `talent_language_info\[\]` | 语言能力 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 语言<br>**可选值有**：<br>- `1`: 英语 - `2`: 法语 - `3`: 日语 - `4`: 韩语 - `5`: 德语 - `6`: 俄语 - `7`: 西班牙语 - `8`: 葡萄牙语 - `9`: 阿拉伯语 - `10`: 印地语 - `11`: 印度斯坦语 - `12`: 孟加拉语 - `13`: 豪萨语 - `14`: 旁遮普语 - `15`: 波斯语 - `16`: 斯瓦西里语 - `17`: 泰卢固语 - `18`: 土耳其语 - `19`: 意大利语 - `20`: 爪哇语 - `21`: 泰米尔语 - `22`: 马拉地语 - `23`: 越南语 - `24`: 普通话 - `25`: 粤语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `proficiency` | `int` | 精通程度<br>**可选值有**：<br>- `1`: 入门 - `2`: 日常会话 - `3`: 商务会话 - `4`: 无障碍沟通 - `5`: 母语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日选择 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sns_list` | `talent_sns_info\[\]` | 社交账号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sns_type` | `int` | 社交平台<br>**可选值有**：<br>- `1`: 领英 - `2`: 脉脉 - `3`: 微信 - `4`: 微博 - `5`: Github - `6`: 知乎 - `7`: 脸书 - `8`: 推特 - `9`: Whatsapp - `10`: 个人网站 - `11`: QQ |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `string` | URL/ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日选择 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `resume_source_list` | `talent_resume_source\[\]` | 简历来源 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `interview_registration_list` | `talent_interview_registration_simple\[\]` | 面试登记表<br>> **Tip**: 推荐使用 registration_list 字段获取完整登记表列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `registration_time` | `int` | 创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `download_url` | `string` | 下载链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `registration_list` | `registration_basic_info\[\]` | 登记表列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `registration_time` | `int` | 创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `download_url` | `string` | 下载链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `scenario` | `int` | 登记表场景<br>**可选值有**：<br>- `5`: 面试登记表 - `6`: 入职登记表 - `14`: 信息更新登记表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `resume_attachment_id_list` | `string\[\]` | 简历附件id列表（按照简历创建时间降序） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data\[\]` | 自定义模块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 模块 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 模块名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `children` | `talent_customized_data_child\[\]` | 模块下的字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日选择 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `top_degree` | `int` | 最高学历<br>**可选值有**：<br>- `1`: 小学 - `2`: 初中 - `3`: 专职 - `4`: 高中 - `5`: 大专 - `6`: 本科 - `7`: 硕士 - `8`: 博士 - `9`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `first_degree` | `int` | 第一学历<br>**可选值有**：<br>- `1`: 低于大专 - `2`: 大专 - `3`: 本科 - `4`: 硕士 - `5`: 博士 - `6`: 其他 - `7`: 无 |


### 响应体示例

```json
{"code":0,
"msg":"ok",
"data":{"talent":{"id":"6891560630172518670",
"is_in_agency_period":true,
"is_onboarded":true,
"basic_info":{"name":"测试",
"mobile":"182900291190",
"mobile_code":"86",
"mobile_country_code":"CN_1",
"email":"16xx1@126.com",
"experience_years":5,
"age":22,
"nationality":{"nationality_code":"CN_183",
"zh_name":"测试",
"en_name":"test"},
"gender":1,
"current_city":{"city_code":"CN_183",
"zh_name":"测试",
"en_name":"test"},
"hometown_city":{"city_code":"CN_183",
"zh_name":"测试",
"en_name":"test"},
"preferred_city_list":[{
    "city_code": "CN_183",
    "zh_name": "测试",
    "en_name": "test"
}],
"identification_type":1,
"identification_number":"511699199x1x111234",
"birthday":1687872017,
"creator_id":"ou-xxx",
"marital_status":1,
"current_home_address":"南京路1号",
"customized_data_list":[{
    "object_id": "xxxx",
    "name": {
        "zh_cn": "测试",
        "en_us": "test"
    },
    "object_type": 1,
    "value": {
        "content": "text",
        "option": {
            "key": "AA",
            "name": {
                "zh_cn": "测试",
                "en_us": "test"
            }
        },
        "option_list": [
            {
                "key": "AA",
                "name": {
                    "zh_cn": "测试",
                    "en_us": "test"
                }
            }
        ],
        "time_range": {
            "start_time": "1625456721",
            "end_time": "1625656721"
        },
        "time": "1625456721",
        "number": "111",
        "customized_attachment": [
            {
                "file_id": "7140517838785481004",
                "name": "1.13测试1的面试记录.pdf",
                "content_type": "application/pdf",
                "file_size": 16615
            }
        ]
    }
}],
"modify_time":"1634801678103",
"hukou_location_code":"CN_1"},
"education_list":[{"id":"6891560630172518670",
"degree":1,
"school":"湘港大学",
"field_of_study":"考古",
"start_time":"1990-01",
"end_time":"1994-01",
"end_time_v2":"1687180087000",
"education_type":1,
"academic_ranking":5,
"tag_list":[-],
"customized_data_list":[{
    "object_id": "xxxx",
    "name": {
        "zh_cn": "测试",
        "en_us": "test"
    },
    "object_type": 1,
    "value": {
        "content": "text",
        "option": {
            "key": "AA",
            "name": {
                "zh_cn": "测试",
                "en_us": "test"
            }
        },
        "option_list": [
            {
                "key": "AA",
                "name": {
                    "zh_cn": "测试",
                    "en_us": "test"
                }
            }
        ],
        "time_range": {
            "start_time": "1625456721",
            "end_time": "1625656721"
        },
        "time": "1625456721",
        "number": "111",
        "customized_attachment": [
            {
                "file_id": "7140517838785481004",
                "name": "1.13测试1的面试记录.pdf",
                "content_type": "application/pdf",
                "file_size": 16615
            }
        ]
    }
}]}],
"career_list":[{
    "id": "6891560630172518670",
    "company": "测试公司",
    "title": "高级工程师",
    "desc": "测试",
    "start_time": "1990-01",
    "end_time": "1994-01",
    "career_type": 1,
    "tag_list": [
        6
    ],
    "customized_data_list": [
        {
            "object_id": "xxxx",
            "name": {
                "zh_cn": "测试",
                "en_us": "test"
            },
            "object_type": 1,
            "value": {
                "content": "text",
                "option": {
                    "key": "AA",
                    "name": {
                        "zh_cn": "测试",
                        "en_us": "test"
                    }
                },
                "option_list": [
                    {
                        "key": "AA",
                        "name": {
                            "zh_cn": "测试",
                            "en_us": "test"
                        }
                    }
                ],
                "time_range": {
                    "start_time": "1625456721",
                    "end_time": "1625656721"
                },
                "time": "1625456721",
                "number": "111",
                "customized_attachment": [
                    {
                        "file_id": "7140517838785481004",
                        "name": "1.13测试1的面试记录.pdf",
                        "content_type": "application/pdf",
                        "file_size": 16615
                    }
                ]
            }
        }
    ]
}],
"project_list":[{
    "id": "6891560630172518670",
    "name": "测试",
    "role": "test",
    "link": "www.test.com",
    "desc": "test",
    "start_time": "1990-01",
    "end_time": "1991-01",
    "customized_data_list": [
        {
            "object_id": "xxxx",
            "name": {
                "zh_cn": "测试",
                "en_us": "test"
            },
            "object_type": 1,
            "value": {
                "content": "text",
                "option": {
                    "key": "AA",
                    "name": {
                        "zh_cn": "测试",
                        "en_us": "test"
                    }
                },
                "option_list": [
                    {
                        "key": "AA",
                        "name": {
                            "zh_cn": "测试",
                            "en_us": "test"
                        }
                    }
                ],
                "time_range": {
                    "start_time": "1625456721",
                    "end_time": "1625656721"
                },
                "time": "1625456721",
                "number": "111",
                "customized_attachment": [
                    {
                        "file_id": "7140517838785481004",
                        "name": "1.13测试1的面试记录.pdf",
                        "content_type": "application/pdf",
                        "file_size": 16615
                    }
                ]
            }
        }
    ]
}],
"works_list":[{
    "id": "6891560630172518670",
    "link": "www.test.com",
    "desc": "test",
    "name": "XX项目",
    "customized_data_list": [
        {
            "object_id": "xxxx",
            "name": {
                "zh_cn": "测试",
                "en_us": "test"
            },
            "object_type": 1,
            "value": {
                "content": "text",
                "option": {
                    "key": "AA",
                    "name": {
                        "zh_cn": "测试",
                        "en_us": "test"
                    }
                },
                "option_list": [
                    {
                        "key": "AA",
                        "name": {
                            "zh_cn": "测试",
                            "en_us": "test"
                        }
                    }
                ],
                "time_range": {
                    "start_time": "1625456721",
                    "end_time": "1625656721"
                },
                "time": "1625456721",
                "number": "111",
                "customized_attachment": [
                    {
                        "file_id": "7140517838785481004",
                        "name": "1.13测试1的面试记录.pdf",
                        "content_type": "application/pdf",
                        "file_size": 16615
                    }
                ]
            }
        }
    ]
}],
"award_list":[{
    "id": "6891560630172518670",
    "title": "最佳新人奖",
    "award_time": "1991",
    "desc": "最优秀的新人奖",
    "customized_data_list": [
        {
            "object_id": "xxxx",
            "name": {
                "zh_cn": "测试",
                "en_us": "test"
            },
            "object_type": 1,
            "value": {
                "content": "text",
                "option": {
                    "key": "AA",
                    "name": {
                        "zh_cn": "测试",
                        "en_us": "test"
                    }
                },
                "option_list": [
                    {
                        "key": "AA",
                        "name": {
                            "zh_cn": "测试",
                            "en_us": "test"
                        }
                    }
                ],
                "time_range": {
                    "start_time": "1625456721",
                    "end_time": "1625656721"
                },
                "time": "1625456721",
                "number": "111",
                "customized_attachment": [
                    {
                        "file_id": "7140517838785481004",
                        "name": "1.13测试1的面试记录.pdf",
                        "content_type": "application/pdf",
                        "file_size": 16615
                    }
                ]
            }
        }
    ]
}],
"language_list":[{
    "id": "6891560630172518670",
    "language": 1,
    "proficiency": 1,
    "customized_data_list": [
        {
            "object_id": "xxxx",
            "name": {
                "zh_cn": "测试",
                "en_us": "test"
            },
            "object_type": 1,
            "value": {
                "content": "text",
                "option": {
                    "key": "AA",
                    "name": {
                        "zh_cn": "测试",
                        "en_us": "test"
                    }
                },
                "option_list": [
                    {
                        "key": "AA",
                        "name": {
                            "zh_cn": "测试",
                            "en_us": "test"
                        }
                    }
                ],
                "time_range": {
                    "start_time": "1625456721",
                    "end_time": "1625656721"
                },
                "time": "1625456721",
                "number": "111",
                "customized_attachment": [
                    {
                        "file_id": "7140517838785481004",
                        "name": "1.13测试1的面试记录.pdf",
                        "content_type": "application/pdf",
                        "file_size": 16615
                    }
                ]
            }
        }
    ]
}],
"sns_list":[{
    "id": "6891560630172518670",
    "sns_type": 1,
    "link": "www.test.com",
    "customized_data_list": [
        {
            "object_id": "xxxx",
            "name": {
                "zh_cn": "测试",
                "en_us": "test"
            },
            "object_type": 1,
            "value": {
                "content": "text",
                "option": {
                    "key": "AA",
                    "name": {
                        "zh_cn": "测试",
                        "en_us": "test"
                    }
                },
                "option_list": [
                    {
                        "key": "AA",
                        "name": {
                            "zh_cn": "测试",
                            "en_us": "test"
                        }
                    }
                ],
                "time_range": {
                    "start_time": "1625456721",
                    "end_time": "1625656721"
                },
                "time": "1625456721",
                "number": "111",
                "customized_attachment": [
                    {
                        "file_id": "7140517838785481004",
                        "name": "1.13测试1的面试记录.pdf",
                        "content_type": "application/pdf",
                        "file_size": 16615
                    }
                ]
            }
        }
    ]
}],
"resume_source_list":[{
    "id": "6891560630172518670",
    "zh_name": "猎头",
    "en_name": "Hunter"
}],
"interview_registration_list":[{
    "id": "6833685612520950030",
    "registration_time": 1618494330932,
    "download_url": "https://hire.feishu.cn/hire/file/blob/...token.../"
}],
"registration_list":[{
    "id": "6833685612520950030",
    "registration_time": 1618494330932,
    "download_url": "https://hire.feishu.cn/hire/file/blob/...token.../",
    "scenario": 5
}],
"resume_attachment_id_list":["64352523512563462"],
"customized_data_list":[{
    "object_id": "xxxx",
    "name": {
        "zh_cn": "测试",
        "en_us": "test"
    },
    "object_type": 1,
    "children": [
        {
            "object_id": "xxxx",
            "name": {
                "zh_cn": "测试",
                "en_us": "test"
            },
            "object_type": 1,
            "value": {
                "content": "text",
                "option": {
                    "key": "AA",
                    "name": {
                        "zh_cn": "测试",
                        "en_us": "test"
                    }
                },
                "option_list": [
                    {
                        "key": "AA",
                        "name": {
                            "zh_cn": "测试",
                            "en_us": "test"
                        }
                    }
                ],
                "time_range": {
                    "start_time": "1625456721",
                    "end_time": "1625656721"
                },
                "time": "1625456721",
                "number": "111",
                "customized_attachment": [
                    {
                        "file_id": "7140517838785481004",
                        "name": "1.13测试1的面试记录.pdf",
                        "content_type": "application/pdf",
                        "file_size": 16615
                    }
                ]
            }
        }
    ]
}],
"top_degree":1,
"first_degree":3}}}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1000001 | Invalid parameter | 请检查参数 |
| 500 | 1002001 | System error | 请联系研发排查 |
| 400 | 1002002 | Invalid parameter | 检查参数是否正确，例如类型，大小 |
| 404 | 1002102 | Talent not found | 请检查`talent_id`参数是否正确 |


