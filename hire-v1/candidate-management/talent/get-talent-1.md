---
title: "获取人才详情"
fullPath: "/uAjLw4CM/ukTMukTMukTM/hire-v2/talent/get"
updateTime: "1764644267000"
---

# 获取人才详情

根据人才 ID 获取人才详情，包含人才加入文件夹列表、标签、人才库、备注以及屏蔽名单等信息。


> **Tip**: 目前暂不支持查询被删除的人才详情


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v2/talents/:talent_id |
| HTTP Method | GET |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:talent:readonly` 获取人才信息 `hire:talent` 更新人才信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `hire:note:readonly` 获取招聘备注信息 `hire:talent_folder:readonly` 获取人才库信息 `hire:talent_tag` 更新人才标签 `hire:talent_tag:readonly` 获取人才标签 `hire:talent_blocklist:readonly` 查看人才屏蔽名单信息 `hire:talent_folder` 更新人才库信息 `hire:note` 更新招聘备注信息 `contact:user.employee_id:readonly` 获取用户 user ID `hire:talent_blocklist` 更新人才屏蔽名单信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `talent_id` | `string` | 人才 ID，可通过[获取人才列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/list)接口获取<br>**示例值**："6960663240925956555" |


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
| `data` | `composite_talent` | \- |
| &nbsp;&nbsp;└ `talent_id` | `string` | 人才 ID |
| &nbsp;&nbsp;└ `basic_info` | `composite_talent_basic_info` | 基本信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_number` | `string` | 手机 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_code` | `string` | 手机国家区号，遵守国际统一标准，请参考[百度百科-国际长途电话区号](https://baike.baidu.com/item/%E5%9B%BD%E9%99%85%E9%95%BF%E9%80%94%E7%94%B5%E8%AF%9D%E5%8C%BA%E5%8F%B7%E8%A1%A8/12803495?fr=ge_ala) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `experience_years` | `int` | 工作年限 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `age` | `int` | 年龄 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `nationality_code` | `string` | 国籍（地区），详情请查看：[查询地点列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `gender` | `int` | 性别<br>**可选值有**：<br>- `1`: 男 - `2`: 女 - `3`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `current_location_code` | `string` | 所在地点，详情请查看：[查询地点列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `hometown_location_code` | `string` | 家乡，详情请查看：[查询地点列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `preferred_location_code_list` | `string\[\]` | 意向地点，详情请查看：[查询地点列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `home_address` | `string` | 家庭住址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `identification_type` | `int` | 证件类型<br>**可选值有**：<br>- `1`: 中国 - 居民身份证 - `2`: 护照 - `3`: 中国 - 港澳居民居住证 - `4`: 中国 - 台湾居民来往大陆通行证 - `5`: 其他 - `6`: 中国 - 港澳居民来往内地通行证 - `9`: 中国 - 台湾居民居住证 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `identification_number` | `string` | 证件号 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `birthday` | `int` | 生日，秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `marital_status` | `int` | 婚姻状况<br>**可选值有**：<br>- `1`: 已婚 - `2`: 未婚 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID，详情请查看：[获取人才字段](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_object/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 字段中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 字段英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日期 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID，详情请查看：[获取附件信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `hukou_location_code` | `string` | 户口所在地，详情请查看：[查询地点列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `update_time` | `string` | 人才更新时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 人才创建时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `confidential` | `int` | 人才隐藏状态<br>**可选值有**：<br>- `1`: 隐藏 - `2`: 公开 |
| &nbsp;&nbsp;└ `education_list` | `composite_talent_education_info\[\]` | 教育经历 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `degree` | `int` | 学位<br>**可选值有**：<br>- `1`: 小学 - `2`: 初中 - `3`: 专职 - `4`: 高中 - `5`: 大专 - `6`: 本科 - `7`: 硕士 - `8`: 博士 - `9`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `school_name` | `string` | 学校名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `major` | `string` | 专业 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 教育经历的起始日期，精确到月份，格式为YYYY-MM |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 教育经历的结束时间，精确到月份，格式为YYYY-MM |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `education_type` | `int` | 学历类型<br>**可选值有**：<br>- `1`: 海外及港台 - `2`: 统招全日制 - `3`: 非全日制 - `4`: 自考 - `5`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `academic_ranking` | `int` | 成绩排名<br>**可选值有**：<br>- `5`: 前 5 % - `10`: 前 10 % - `20`: 前 20 % - `30`: 前 30 % - `50`: 前 50 % - `-1`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID，详情请查看：[获取人才字段](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_object/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 自定义字段中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 自定义字段英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 自定义字段字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日期 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID，详情请查看：[获取附件信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;└ `career_list` | `composite_talent_career_info\[\]` | 工作经历 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `company_name` | `string` | 公司名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 工作经历描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 工作经历的结束日期，精确到月份，格式为YYYY-MM |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 工作经历的开始日期，精确到月份，格式为YYYY-MM |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 职位名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID，详情请查看：[获取人才字段](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_object/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 字段中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 字段英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日期 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID，详情请查看：[获取附件信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;└ `project_list` | `composite_talent_project_info\[\]` | 项目经历 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `project_name` | `string` | 项目名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `role` | `string` | 项目角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `string` | 项目链接（访问型链接，无有效期限制） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 项目描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 项目的开始日期，精确到月份，格式为YYYY-MM |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 项目的结束日期，精确到月份，格式为YYYY-MM |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID，详情请查看：[获取人才字段](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_object/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 字段中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 字段英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日期 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID，详情请查看：[获取附件信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;└ `works_list` | `composite_talent_works_info\[\]` | 作品 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 作品 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `string` | 作品链接（访问型链接，无有效期限制） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 作品描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID，详情请查看：[获取人才字段](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_object/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 字段中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 字段英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日期 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID，详情请查看：[获取附件信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;└ `award_list` | `composite_talent_award_info\[\]` | 获奖 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `award_name` | `string` | 获奖名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `award_time` | `string` | 获奖日期，精确到月份，格式为YYYY-MM |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 获奖描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID，详情请查看：[获取人才字段](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_object/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 字段中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 字段英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日期 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID，详情请查看：[获取附件信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;└ `language_list` | `composite_talent_language_info\[\]` | 语言能力 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 语言类别<br>**可选值有**：<br>- `1`: 英语 - `2`: 法语 - `3`: 日语 - `4`: 韩语 - `5`: 德语 - `6`: 俄语 - `7`: 西班牙语 - `8`: 葡萄牙语 - `9`: 阿拉伯语 - `10`: 印地语 - `11`: 印度斯坦语 - `12`: 孟加拉语 - `13`: 豪萨语 - `14`: 旁遮普语 - `15`: 波斯语 - `16`: 斯瓦西里语 - `17`: 泰卢固语 - `18`: 土耳其语 - `19`: 意大利语 - `20`: 爪哇语 - `21`: 泰米尔语 - `22`: 马拉地语 - `23`: 越南语 - `24`: 普通话 - `25`: 粤语 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `proficiency` | `int` | 熟练程度<br>**可选值有**：<br>- `1`: 入门 - `2`: 日常会话 - `3`: 商务会话 - `4`: 无障碍沟通 - `5`: 母语 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID，详情请查看：[获取人才字段](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_object/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 字段中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 字段英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日期 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID，详情请查看：[获取附件信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;└ `sns_list` | `composite_talent_sns_info\[\]` | 社交账号 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sns_type` | `int` | 社交平台<br>**可选值有**：<br>- `1`: 领英 - `2`: 脉脉 - `3`: 微信 - `4`: 微博 - `5`: Github - `6`: 知乎 - `7`: 脸书 - `8`: 推特 - `9`: Whatsapp - `10`: 个人网站 - `11`: QQ |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `string` | URL/ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID，详情请查看：[获取人才字段](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_object/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 字段中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 字段英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日期 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID，详情请查看：[获取附件信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;└ `resume_source_list` | `talent_resume_source\[\]` | 简历来源 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 简历来源 ID，详情请查看：[获取简历来源列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/resume_source/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 简历来源中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 简历来源英文名称 |
| &nbsp;&nbsp;└ `internship_list` | `composite_talent_internship_info\[\]` | 实习经历 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `company_name` | `string` | 实习公司名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 实习公司描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 实习的结束日期，精确到月份，格式为YYYY-MM |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 实习的开始日期，精确到月份，格式为YYYY-MM |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 职位名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `customized_data_list` | `talent_customized_data_child\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID，详情请查看：[获取人才字段](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_object/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 字段中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 字段英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日期 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID，详情请查看：[获取附件信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;└ `customized_data_list` | `composite_talent_customized_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `module_id` | `string` | 模块 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 模块名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 模块中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 模块英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 模块类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `children` | `talent_customized_data_child\[\]` | 模块下的字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 自定义字段 ID，详情请查看：[获取人才字段](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_object/query) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 字段中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 字段英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日期 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `talent_customized_value` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 当字段类型为单行文本、多行文本、模块、默认字段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `talent_customized_option` | 当字段类型为单选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_list` | `talent_customized_option\[\]` | 当字段类型为多选时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_range` | `talent_customized_time_range` | 当字段类型为时间段时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间，当值为至今时，返回「-」，秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time` | `string` | 当字段类型为日期选择、月份选择、年份选择时，从此字段取值，该字段是秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `string` | 当字段类型为数字时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `customized_attachment` | `talent_customized_attachment\[\]` | 当字段类型为附件时，从此字段取值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_id` | `string` | 附件 ID，详情请查看：[获取附件信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_name` | `string` | 附件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content_type` | `string` | 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_size` | `int` | 附件大小 |
| &nbsp;&nbsp;└ `resume_attachment_id_list` | `string\[\]` | 简历附件id列表（按照简历创建时间降序），详情请查看：[获取附件信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get) |
| &nbsp;&nbsp;└ `resume_attachment_list` | `talent_resume_attachment\[\]` | 简历附件列表（按照简历创建时间降序） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 附件名，包含文件类型后缀，例如【简历.pdf】 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `mime` | `string` | 附件MIME类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 创建时间，为毫秒级的时间戳 |
| &nbsp;&nbsp;└ `interview_registration_list` | `talent_interview_registration_simple\[\]` | 面试登记表，推荐使用`registration_list`字段获取完整登记表列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 登记表 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `registration_time` | `int` | 创建时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `download_url` | `string` | 下载链接（有效期7天） |
| &nbsp;&nbsp;└ `registration_list` | `registration_basic_info\[\]` | 登记表列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 登记表 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `registration_time` | `int` | 创建时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `download_url` | `string` | 下载链接（有效期7天） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `scenario` | `int` | 登记表场景<br>**可选值有**：<br>- `5`: 面试登记表 - `6`: 入职登记表 - `14`: 信息更新登记表 |
| &nbsp;&nbsp;└ `is_onboarded` | `boolean` | 是否已入职<br>**可选值有**：<br>- `false`: 未入职 - `true`: 已入职 |
| &nbsp;&nbsp;└ `is_in_agency_period` | `boolean` | 是否在猎头保护期<br>**可选值有**：<br>- `false`: 未在猎头保护期 - `true`: 在猎头保护期 |
| &nbsp;&nbsp;└ `top_degree` | `int` | 最高学历， 详情请参考[枚举常量介绍](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/enum)中 DegreeType 枚举 |
| &nbsp;&nbsp;└ `talent_pool_id_list` | `string\[\]` | 人才已加入的人才库列表，详情请查看：[获取人才库列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_pool/search) |
| &nbsp;&nbsp;└ `talent_folder_ref_list_v2` | `talent_folder\[\]` | 文件夹列表<br>**字段权限要求（满足任一）**： `hire:talent_folder:readonly` 获取人才库信息 `hire:talent_folder` 更新人才库信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 文件夹名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `folder_id` | `string` | 文件夹 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `owner_id` | `string` | 所有者 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `add_time` | `string` | 文件夹加入时间，毫秒时间戳 |
| &nbsp;&nbsp;└ `tag_list` | `talent_tag\[\]` | 标签列表<br>**字段权限要求（满足任一）**： `hire:talent_tag` 更新人才标签 `hire:talent_tag:readonly` 获取人才标签 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 标签 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 标签名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 标签中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 标签英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 标签描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 标签中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 标签英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 标签类型<br>**可选值有**：<br>- `1`: 手动标签 - `2`: 自动标签 |
| &nbsp;&nbsp;└ `similar_info_v2` | `talent_similar` | 相似人才信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_similar_talent` | `boolean` | 是否相似人才 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `similar_talent_id_list` | `string\[\]` | 相似人才 ID 列表 |
| &nbsp;&nbsp;└ `block_info` | `talent_block` | 人才屏蔽名单信息<br>**字段权限要求（满足任一）**： `hire:talent_blocklist` 更新人才屏蔽名单信息 `hire:talent_blocklist:readonly` 查看人才屏蔽名单信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `blocked_time` | `string` | 加入屏蔽名单时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `creator_id` | `string` | 屏蔽名单创建者 ID，与入参`user_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `reason` | `string` | 加入屏蔽名单原因 |
| &nbsp;&nbsp;└ `talent_pool_ref_list_v2` | `talent_pool\[\]` | 人才已经加入的人才库列表<br>**字段权限要求（满足任一）**： `hire:talent_folder:readonly` 获取人才库信息 `hire:talent_folder` 更新人才库信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 人才库 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 人才库名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 人才库中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 人才库英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 人才库描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 人才库中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 人才库英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `add_time` | `string` | 人才库加入时间，毫秒级时间戳 |
| &nbsp;&nbsp;└ `note_list_v2` | `talent_note\[\]` | 备注列表<br>**字段权限要求（满足任一）**： `hire:note:readonly` 获取招聘备注信息 `hire:note` 更新招聘备注信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 备注 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `talent_id` | `string` | 人才 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `application_id` | `string` | 投递 ID，详情可查看[获取投递信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 人才备注创建时间,毫秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `update_time` | `string` | 人才备注更新时间，毫秒级时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `creator_id` | `string` | 创建人ID，与入参`user_id_type`类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 备注内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `privacy` | `int` | 备注私密属性<br>**可选值有**：<br>- `1`: 私密 - `2`: 公开 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "talent_id": "6761694410053798151",
        "basic_info": {
            "name": "张三",
            "mobile_number": "18312341234",
            "mobile_code": "86",
            "email": "16xx1@126.com",
            "experience_years": 5,
            "age": 22,
            "nationality_code": "CN",
            "gender": 1,
            "current_location_code": "CN_2",
            "hometown_location_code": "CN_3",
            "preferred_location_code_list": [
                "CN_2"
            ],
            "home_address": "北京朝阳区",
            "identification_type": 1,
            "identification_number": "511699199x1x111234",
            "birthday": 293016767159,
            "marital_status": 1,
            "customized_data_list": [
                {
                    "object_id": "7392444731470547241",
                    "name": {
                        "zh_cn": "字段1",
                        "en_us": "field 1"
                    },
                    "object_type": 1,
                    "value": {
                        "content": "text",
                        "option": {
                            "key": "7350282123172432169",
                            "name": {
                                "zh_cn": "选项1",
                                "en_us": "option 1"
                            }
                        },
                        "option_list": [
                            {
                                "key": "7350282123172432169",
                                "name": {
                                    "zh_cn": "多选1",
                                    "en_us": "multi option1"
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
                                "file_name": "1.13测试1的面试记录.pdf",
                                "content_type": "application/pdf",
                                "file_size": 16615
                            }
                        ]
                    }
                }
            ],
            "hukou_location_code": "CN_1",
            "update_time": "1634801678103",
            "create_time": "1634801678103",
            "confidential": 1
        },
        "education_list": [
            {
                "degree": 1,
                "school_name": "湘港大学",
                "major": "考古",
                "start_time": "1992-01",
                "end_time": "1994-01",
                "education_type": 1,
                "academic_ranking": 5,
                "customized_data_list": [
                    {
                        "object_id": "7392444731470563625",
                        "name": {
                            "zh_cn": "人才过往",
                            "en_us": "talent old history"
                        },
                        "object_type": 1,
                        "value": {
                            "content": "这是一个自定义字段内容",
                            "option": {
                                "key": "7392444731470563625",
                                "name": {
                                    "zh_cn": "选项A",
                                    "en_us": "test"
                                }
                            },
                            "option_list": [
                                {
                                    "key": "7392444731470563625",
                                    "name": {
                                        "zh_cn": "选项A",
                                        "en_us": "Option A"
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
                                    "file_name": "1.13测试1的面试记录.pdf",
                                    "content_type": "application/pdf",
                                    "file_size": 16615
                                }
                            ]
                        }
                    }
                ]
            }
        ],
        "career_list": [
            {
                "company_name": "明日科技公司",
                "description": "明日科技",
                "end_time": "2023-06",
                "start_time": "2023-06",
                "title": "高级工程师",
                "customized_data_list": [
                    {
                        "object_id": "7395082456917641499",
                        "name": {
                            "zh_cn": "经历地址",
                            "en_us": "data english name"
                        },
                        "object_type": 1,
                        "value": {
                            "content": "这是一个单行文本",
                            "option": {
                                "key": "7395082456917641499",
                                "name": {
                                    "zh_cn": "选项 A",
                                    "en_us": "option A"
                                }
                            },
                            "option_list": [
                                {
                                    "key": "7395082456917641499",
                                    "name": {
                                        "zh_cn": "选项 A",
                                        "en_us": "option A"
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
                                    "file_name": "1.13测试1的面试记录.pdf",
                                    "content_type": "application/pdf",
                                    "file_size": 16615
                                }
                            ]
                        }
                    }
                ]
            }
        ],
        "project_list": [
            {
                "project_name": "权限重构项目",
                "role": "项目负责人",
                "link": "www.recruitment-demo.com",
                "description": "招聘网站",
                "start_time": "1990-01",
                "end_time": "1991-01",
                "customized_data_list": [
                    {
                        "object_id": "7395082456917641499",
                        "name": {
                            "zh_cn": "自定义字段",
                            "en_us": "english name"
                        },
                        "object_type": 1,
                        "value": {
                            "content": "这是一个单行文本",
                            "option": {
                                "key": "7395082456917641499",
                                "name": {
                                    "zh_cn": "选项 A",
                                    "en_us": "option A"
                                }
                            },
                            "option_list": [
                                {
                                    "key": "7395082456917641499",
                                    "name": {
                                        "zh_cn": "选项 A",
                                        "en_us": "Option A"
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
                                    "file_name": "1.13测试1的面试记录.pdf",
                                    "content_type": "application/pdf",
                                    "file_size": 16615
                                }
                            ]
                        }
                    }
                ]
            }
        ],
        "works_list": [
            {
                "id": "6891560630172518670",
                "link": "https://open.feishu.cn/document/server-docs/hire-v1/candidate-management/talent/get-2",
                "description": "人才信息页面",
                "customized_data_list": [
                    {
                        "object_id": "7395082456917641499",
                        "name": {
                            "zh_cn": "字段1",
                            "en_us": "english name"
                        },
                        "object_type": 1,
                        "value": {
                            "content": "这是一个单行文本",
                            "option": {
                                "key": "7395082456917641499",
                                "name": {
                                    "zh_cn": "选项A",
                                    "en_us": "option A"
                                }
                            },
                            "option_list": [
                                {
                                    "key": "7395082456917641499",
                                    "name": {
                                        "zh_cn": "选项A",
                                        "en_us": "option A"
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
                                    "file_name": "1.13测试1的面试记录.pdf",
                                    "content_type": "application/pdf",
                                    "file_size": 16615
                                }
                            ]
                        }
                    }
                ]
            }
        ],
        "award_list": [
            {
                "award_name": "最佳新人奖",
                "award_time": "1992-01",
                "description": "最优秀的新人奖",
                "customized_data_list": [
                    {
                        "object_id": "7395082456917641499",
                        "name": {
                            "zh_cn": "字段1",
                            "en_us": "english name"
                        },
                        "object_type": 1,
                        "value": {
                            "content": "这是一个单行文本",
                            "option": {
                                "key": "7395082456917641499",
                                "name": {
                                    "zh_cn": "选项 A",
                                    "en_us": "option A"
                                }
                            },
                            "option_list": [
                                {
                                    "key": "7395082456917641499",
                                    "name": {
                                        "zh_cn": "选项 A",
                                        "en_us": "option A"
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
                                    "file_name": "1.13测试1的面试记录.pdf",
                                    "content_type": "application/pdf",
                                    "file_size": 16615
                                }
                            ]
                        }
                    }
                ]
            }
        ],
        "language_list": [
            {
                "language": 1,
                "proficiency": 1,
                "customized_data_list": [
                    {
                        "object_id": "6792436415209817608",
                        "name": {
                            "zh_cn": "字段 1",
                            "en_us": "english name"
                        },
                        "object_type": 1,
                        "value": {
                            "content": "这是一个单行文本",
                            "option": {
                                "key": "7395082456917641499",
                                "name": {
                                    "zh_cn": "选项 A",
                                    "en_us": "option A"
                                }
                            },
                            "option_list": [
                                {
                                    "key": "7395082456917641499",
                                    "name": {
                                        "zh_cn": "选项 A",
                                        "en_us": "option A"
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
                                    "file_name": "1.13测试1的面试记录.pdf",
                                    "content_type": "application/pdf",
                                    "file_size": 16615
                                }
                            ]
                        }
                    }
                ]
            }
        ],
        "sns_list": [
            {
                "sns_type": 1,
                "link": "1",
                "customized_data_list": [
                    {
                        "object_id": "7395082456917641499",
                        "name": {
                            "zh_cn": "字段 1",
                            "en_us": "option A"
                        },
                        "object_type": 1,
                        "value": {
                            "content": "这是一个单行文本",
                            "option": {
                                "key": "7395082456917641499",
                                "name": {
                                    "zh_cn": "选项 A",
                                    "en_us": "option A"
                                }
                            },
                            "option_list": [
                                {
                                    "key": "7395082456917641499",
                                    "name": {
                                        "zh_cn": "选项 A",
                                        "en_us": "Option A"
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
                                    "file_name": "1.13测试1的面试记录.pdf",
                                    "content_type": "application/pdf",
                                    "file_size": 16615
                                }
                            ]
                        }
                    }
                ]
            }
        ],
        "resume_source_list": [
            {
                "id": "6891560630172518670",
                "zh_name": "猎头",
                "en_name": "Hunter"
            }
        ],
        "internship_list": [
            {
                "company_name": "明日科技",
                "description": "明日科技实习公司",
                "end_time": "1992-01",
                "start_time": "1992-01",
                "title": "实习科学家",
                "customized_data_list": [
                    {
                        "object_id": "7395082456917641499",
                        "name": {
                            "zh_cn": "字段 1",
                            "en_us": "test"
                        },
                        "object_type": 1,
                        "value": {
                            "content": "这是一个单行文本",
                            "option": {
                                "key": "7395082456917641499",
                                "name": {
                                    "zh_cn": "选项 A",
                                    "en_us": "option A"
                                }
                            },
                            "option_list": [
                                {
                                    "key": "7395082456917641499",
                                    "name": {
                                        "zh_cn": "选项 A",
                                        "en_us": "option A"
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
                                    "file_name": "1.13测试1的面试记录.pdf",
                                    "content_type": "application/pdf",
                                    "file_size": 16615
                                }
                            ]
                        }
                    }
                ]
            }
        ],
        "customized_data_list": [
            {
                "module_id": "7106698109352479020",
                "name": {
                    "zh_cn": "模块 1",
                    "en_us": "module 1"
                },
                "object_type": 1,
                "children": [
                    {
                        "object_id": "7395082456917641499",
                        "name": {
                            "zh_cn": "字段 1",
                            "en_us": "english name"
                        },
                        "object_type": 1,
                        "value": {
                            "content": "这是一个单行文本",
                            "option": {
                                "key": "7395082456917641499",
                                "name": {
                                    "zh_cn": "选项 A",
                                    "en_us": "option A"
                                }
                            },
                            "option_list": [
                                {
                                    "key": "7395082456917641499",
                                    "name": {
                                        "zh_cn": "选项 A",
                                        "en_us": "english name"
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
                                    "file_name": "1.13测试1的面试记录.pdf",
                                    "content_type": "application/pdf",
                                    "file_size": 16615
                                }
                            ]
                        }
                    }
                ]
            }
        ],
        "resume_attachment_id_list": [
            "64352523512563462"
        ],
        "resume_attachment_list": [
            {
                "id": "6891560630172518670",
                "name": "1.pdf",
                "mime": "application/pdf",
                "create_time": "1734348840749"
            }
        ],
        "interview_registration_list": [
            {
                "id": "6833685612520950030",
                "registration_time": 1618494330932,
                "download_url": "https://hire.feishu.cn/hire/file/blob/...token.../"
            }
        ],
        "registration_list": [
            {
                "id": "6833685612520950030",
                "registration_time": 1618494330932,
                "download_url": "https://hire.feishu.cn/hire/file/blob/...token.../",
                "scenario": 5
            }
        ],
        "is_onboarded": true,
        "is_in_agency_period": true,
        "top_degree": 1,
        "talent_pool_id_list": [
            "7171693733661327361"
        ],
        "talent_folder_ref_list_v2": [
            {
                "name": "人才文件夹A1",
                "folder_id": "7041806543797995820",
                "owner_id": "ou_85bb308c57f597471cd2bb5b4f580245",
                "add_time": "1634801678103"
            }
        ],
        "tag_list": [
            {
                "id": "7140517838785481004",
                "name": {
                    "zh_cn": "高学历人才",
                    "en_us": "985"
                },
                "description": {
                    "zh_cn": "这是一个标签",
                    "en_us": "this is a english tag"
                },
                "type": 1
            }
        ],
        "similar_info_v2": {
            "is_similar_talent": true,
            "similar_talent_id_list": [
                "6891560630172518670"
            ]
        },
        "block_info": {
            "blocked_time": "1625656721",
            "creator_id": "6891560630172518670",
            "reason": "人才作弊"
        },
        "talent_pool_ref_list_v2": [
            {
                "id": "6891560630172518670",
                "name": {
                    "zh_cn": "测试人才库",
                    "en_us": "Test talent pool"
                },
                "description": {
                    "zh_cn": "这是一个测试人才库",
                    "en_us": "This is a test talent pool"
                },
                "add_time": "1634801678103"
            }
        ],
        "note_list_v2": [
            {
                "id": "6949805467799537964",
                "talent_id": "6916472453069883661",
                "application_id": "6891565253964859661",
                "create_time": "1618209327096",
                "update_time": "1618209327096",
                "creator_id": "ou_f476cb099ac9227c9bae09ce46112579",
                "content": "测试备注内容",
                "privacy": 1
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 404 | 1002102 | 人才不存在 | 人才不存在，请检查`talent_id`参数是否正确 |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |


