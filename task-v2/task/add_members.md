---
title: "添加任务成员"
fullPath: "/uAjLw4CM/ukTMukTMukTM/task-v2/task/add_members"
updateTime: "1751462763000"
---

# 添加任务成员

添加任务的负责人或者关注人。一次性可以添加多个成员。返回任务的实体中会返回最终任务成员的列表。

* 关于member的格式，详见[功能概述](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/overview)中的“ 如何表示任务和清单的成员？”章节。
* 成员的角色支持"assignee"和"follower"。
* 成员类型支持"user"和"app"。
* 如果要添加的成员已经在任务中，则自动被忽略。


> **Tip**: 添加任务成员需要任务的可编辑权限。详情见[任务功能概述](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/task/overview)中的“任务是如何鉴权的？”章节。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/task/v2/tasks/:task_guid/add_members |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `task:personnel:writeonly` 更新任务人员 `task:task:write` 查看、创建、更新、删除任务 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `task_guid` | `string` | 要添加负责人的任务全局唯一ID<br>**示例值**："d300a75f-c56a-4be9-80d1-e47653028ceb"<br>**数据校验规则**：<br>- 最大长度：`100` 字符 |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**默认值**：`open_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `members` | `member\[\]` | 是 | 要添加的members列表，单请求支持最大50个成员（去重后)。关于member的格式，详见[功能概述](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/overview)中的“ 如何表示任务和清单的成员？”章节。 |
| &nbsp;&nbsp;└ `id` | `string` | 是 | 表示member的id<br>**示例值**："ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f"<br>**数据校验规则**：<br>- 最大长度：`100` 字符 |
| &nbsp;&nbsp;└ `type` | `string` | 否 | 成员类型, 可选值 * user * app<br>**示例值**："user"<br>**默认值**：`user` |
| &nbsp;&nbsp;└ `role` | `string` | 是 | 成员的角色，可选值 * assignee * follower<br>**示例值**："assignee"<br>**数据校验规则**：<br>- 最大长度：`20` 字符 |
| &nbsp;&nbsp;└ `name` | `string` | 否 | 成员名称<br>**示例值**："张明德（明德）" |
| `client_token` | `string` | 否 | 幂等token，如果提供则实现幂等行为。详见[功能概述](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/overview)中的“ 幂等调用 ”章节。<br>**示例值**："6d99f59c-4d7d-4452-98d6-3d0556393cf6"<br>**数据校验规则**：<br>- 长度范围：`10` ～ `100` 字符 |


### 请求体示例

```json
{
    "members": [
        {
            "id": "ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f",
            "type": "user",
            "role": "assignee",
            "name": "张明德（明德）"
        }
    ],
    "client_token": "6d99f59c-4d7d-4452-98d6-3d0556393cf6"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `task` | `task` | 更新完成后的任务实体数据 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `guid` | `string` | 任务guid，任务的唯一ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `summary` | `string` | 任务标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 任务备注 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `due` | `due` | 任务截止时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `timestamp` | `string` | 截止时间/日期的时间戳，距1970-01-01 00:00:00的毫秒数。如果截止时间是一个日期，需要把日期转换成时间戳，并设置 is_all_day=true |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_all_day` | `boolean` | 是否截止到一个日期。如果设为true，timestamp中只有日期的部分会被解析和存储。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `reminders` | `reminder\[\]` | 任务的提醒配置列表。目前每个任务最多有1个。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 提醒时间设置的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `relative_fire_minute` | `int` | 相对于截止时间的提醒时间分钟数。例如30表示截止时间前30分钟提醒；0表示截止时提醒。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `creator` | `member` | 任务创建者 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 表示member的id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 成员的类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `role` | `string` | 成员角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 成员名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `members` | `member\[\]` | 任务成员列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 表示member的id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 成员的类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `role` | `string` | 成员角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 成员名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `completed_at` | `string` | 任务完成的时间戳(ms) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `attachments` | `attachment\[\]` | 任务的附件列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `guid` | `string` | 附件guid |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 附件在云文档系统中的token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 附件名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `size` | `int` | 附件的字节大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `resource` | `resource` | 附件归属的资源 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 资源类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 资源ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `uploader` | `member` | 附件上传者 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 表示member的id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 成员的类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `role` | `string` | 成员角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 成员名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_cover` | `boolean` | 是否是封面图 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `uploaded_at` | `string` | 上传时间戳(ms) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `origin` | `origin` | 任务关联的第三方平台来源信息。创建是设置后就不可更改。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `platform_i18n_name` | `i18n_text` | 任务导入来源的名称，用于在任务中心详情页展示。需提供多语言版本。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_hk` | `string` | 中文（香港地区） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_tw` | `string` | 中文（台湾地区） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 日语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fr_fr` | `string` | 法语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `it_it` | `string` | 意大利语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `de_de` | `string` | 德语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ru_ru` | `string` | 俄语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `th_th` | `string` | 泰语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `es_es` | `string` | 西班牙语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ko_kr` | `string` | 韩语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `href` | `href` | 任务关联的来源平台详情页链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 链接对应的地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 链接对应的标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `extra` | `string` | 任务附带的自定义数据。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tasklists` | `task_in_tasklist_info\[\]` | 任务所属清单的名字。调用者只能看到有权限访问的清单的列表。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tasklist_guid` | `string` | 任务所在清单的guid |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `section_guid` | `string` | 任务所在清单的自定义分组guid |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `repeat_rule` | `string` | 如果任务为重复任务，返回重复任务的配置 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `parent_task_guid` | `string` | 如果当前任务为某个任务的子任务，返回父任务的guid |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `mode` | `int` | 任务的模式。1 - 会签任务；2 - 或签任务 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `source` | `int` | 任务创建的来源<br>**可选值有**：<br>- `0`: 未知来源 - `1`: 任务中心 - `2`: 群组任务/消息转任务 - `6`: 通过开放平台以tenant_access_token授权创建的任务 - `7`: 通过开放平台以user_access_token授权创建的任务 - `8`: 文档任务 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_complete` | `custom_complete` | 任务的自定义完成配置 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc` | `custom_complete_item` | pc客户端自定义完成配置（含mac和windows） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `href` | `string` | 自定义完成的跳转url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tip` | `i18n_text` | 自定义完成的弹出提示为 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_hk` | `string` | 中文（香港地区） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_tw` | `string` | 中文（台湾地区） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 日语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fr_fr` | `string` | 法语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `it_it` | `string` | 意大利语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `de_de` | `string` | 德语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ru_ru` | `string` | 俄语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `th_th` | `string` | 泰语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `es_es` | `string` | 西班牙语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ko_kr` | `string` | 韩语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ios` | `custom_complete_item` | ios端的自定义完成配置 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `href` | `string` | 自定义完成的跳转url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tip` | `i18n_text` | 自定义完成的弹出提示为 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_hk` | `string` | 中文（香港地区） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_tw` | `string` | 中文（台湾地区） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 日语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fr_fr` | `string` | 法语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `it_it` | `string` | 意大利语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `de_de` | `string` | 德语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ru_ru` | `string` | 俄语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `th_th` | `string` | 泰语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `es_es` | `string` | 西班牙语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ko_kr` | `string` | 韩语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `android` | `custom_complete_item` | android端的自定义完成配置 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `href` | `string` | 自定义完成的跳转url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tip` | `i18n_text` | 自定义完成的弹出提示为 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_hk` | `string` | 中文（香港地区） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_tw` | `string` | 中文（台湾地区） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 日语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fr_fr` | `string` | 法语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `it_it` | `string` | 意大利语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `de_de` | `string` | 德语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ru_ru` | `string` | 俄语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `th_th` | `string` | 泰语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `es_es` | `string` | 西班牙语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ko_kr` | `string` | 韩语 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `task_id` | `string` | 任务界面上的代码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `string` | 任务创建时间戳(ms) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_at` | `string` | 任务最后一次更新的时间戳(ms) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `string` | 任务的状态，支持"todo"和"done"两种状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 任务的分享链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start` | `start` | 任务的开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `timestamp` | `string` | 开始时间/日期的时间戳，距1970-01-01 00:00:00的毫秒数。如果开始时间是一个日期，需要把日期转换成时间戳，并设置 is_all_day=true |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_all_day` | `boolean` | 是否开始于一个日期。如果设为true，timestamp中只有日期的部分会被解析和存储。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `subtask_count` | `int` | 该任务的子任务的个数。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_milestone` | `boolean` | 是否是里程碑任务 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_field_value\[\]` | 任务的自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `guid` | `string` | 字段GUID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 自定义字段类型，支持"member", "datetime", "number", "single_select", "multi_select"五种类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number_value` | `string` | 数字类型的自定义字段值，填写一个合法数字的字符串表示，空字符串表示设为空。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `datetime_value` | `string` | 日期类型自定义字段值。可以输入一个表示日期的以毫秒为单位的字符串。设为空字符串表示设为空。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `member_value` | `member\[\]` | 人员类型的自定义字段值，可以设置1个或多个用户的id（遵循member格式，只支持user类型）。当该字段的设置为“不能多选”时只能输入一个值。设为空数组表示设为空。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 表示member的id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 成员的类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `role` | `string` | 成员角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 成员名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `single_select_value` | `string` | 单选类型字段值，填写一个字段选项的option_guid。设置为空字符串表示设为空。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `multi_select_value` | `string\[\]` | 多选类型字段值，可以填写一个或多个本字段的option_guid。设为空数组表示设为空。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 自定义字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_value` | `string` | 文本类型字段值。可以输入一段文本。空字符串表示清空。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dependencies` | `task_dependency\[\]` | 任务依赖 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 依赖类型<br>**可选值有**：<br>- `prev`: 前置依赖 - `next`: 后置依赖 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `task_guid` | `string` | 依赖任务的GUID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `assignee_related` | `task_assignee\[\]` | 任务执行者相关信息，如会签任务各执行者完成时间等 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 任务执行者的id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `completed_at` | `string` | 会签任务中执行者完成的时间戳(ms) |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "task": {
            "guid": "83912691-2e43-47fc-94a4-d512e03984fa",
            "summary": "进行销售年中总结",
            "description": "进行销售年中总结",
            "due": {
                "timestamp": "1675454764000",
                "is_all_day": true
            },
            "reminders": [
                {
                    "id": "10",
                    "relative_fire_minute": 30
                }
            ],
            "creator": {
                "id": "ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f",
                "type": "user",
                "role": "assignee",
                "name": "张明德（明德）"
            },
            "members": [
                {
                    "id": "ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f",
                    "type": "user",
                    "role": "assignee",
                    "name": "张明德（明德）"
                }
            ],
            "completed_at": "1675742789470",
            "attachments": [
                {
                    "guid": "f860de3e-6881-4ddd-9321-070f36d1af0b",
                    "file_token": "boxcnTDqPaRA6JbYnzQsZ2doB2b",
                    "name": "foo.jpg",
                    "size": 62232,
                    "resource": {
                        "type": "task",
                        "id": "e6e37dcc-f75a-5936-f589-12fb4b5c80c2"
                    },
                    "uploader": {
                        "id": "ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f",
                        "type": "user",
                        "role": "assignee",
                        "name": "张明德（明德）"
                    },
                    "is_cover": false,
                    "uploaded_at": "1675742789470"
                }
            ],
            "origin": {
                "platform_i18n_name": {
                    "en_us": "workbench",
                    "zh_cn": "工作台",
                    "zh_hk": "工作臺",
                    "zh_tw": "工作臺",
                    "ja_jp": "作業台",
                    "fr_fr": "Table de travail",
                    "it_it": "banco di lavoro",
                    "de_de": "Werkbank",
                    "ru_ru": "верстак",
                    "th_th": "โต๊ะทำงาน",
                    "es_es": "banco de trabajo",
                    "ko_kr": "작업대"
                },
                "href": {
                    "url": "https://www.example.com",
                    "title": "反馈一个问题，需要协助排查"
                }
            },
            "extra": "dGVzdA==",
            "tasklists": [
                {
                    "tasklist_guid": "cc371766-6584-cf50-a222-c22cd9055004",
                    "section_guid": "e6e37dcc-f75a-5936-f589-12fb4b5c80c2"
                }
            ],
            "repeat_rule": "FREQ=WEEKLY;INTERVAL=1;BYDAY=MO,TU,WE,TH,FR",
            "parent_task_guid": "e297ddff-06ca-4166-b917-4ce57cd3a7a0",
            "mode": 2,
            "source": 6,
            "custom_complete": {
                "pc": {
                    "href": "https://www.example.com",
                    "tip": {
                        "en_us": "workbench",
                        "zh_cn": "工作台",
                        "zh_hk": "工作臺",
                        "zh_tw": "工作臺",
                        "ja_jp": "作業台",
                        "fr_fr": "Table de travail",
                        "it_it": "banco di lavoro",
                        "de_de": "Werkbank",
                        "ru_ru": "верстак",
                        "th_th": "โต๊ะทำงาน",
                        "es_es": "banco de trabajo",
                        "ko_kr": "작업대"
                    }
                },
                "ios": {
                    "href": "https://www.example.com",
                    "tip": {
                        "en_us": "workbench",
                        "zh_cn": "工作台",
                        "zh_hk": "工作臺",
                        "zh_tw": "工作臺",
                        "ja_jp": "作業台",
                        "fr_fr": "Table de travail",
                        "it_it": "banco di lavoro",
                        "de_de": "Werkbank",
                        "ru_ru": "верстак",
                        "th_th": "โต๊ะทำงาน",
                        "es_es": "banco de trabajo",
                        "ko_kr": "작업대"
                    }
                },
                "android": {
                    "href": "https://www.example.com",
                    "tip": {
                        "en_us": "workbench",
                        "zh_cn": "工作台",
                        "zh_hk": "工作臺",
                        "zh_tw": "工作臺",
                        "ja_jp": "作業台",
                        "fr_fr": "Table de travail",
                        "it_it": "banco di lavoro",
                        "de_de": "Werkbank",
                        "ru_ru": "верстак",
                        "th_th": "โต๊ะทำงาน",
                        "es_es": "banco de trabajo",
                        "ko_kr": "작업대"
                    }
                }
            },
            "task_id": "t6272302",
            "created_at": "1675742789470",
            "updated_at": "1675742789470",
            "status": "todo",
            "url": "https://applink.feishu.cn/client/todo/detail?guid=70577c8f-91ab-4c91-b359-a21a751054e8&suite_entity_num=t192012",
            "start": {
                "timestamp": "1675454764000",
                "is_all_day": true
            },
            "subtask_count": 1,
            "is_milestone": false,
            "custom_fields": [
                {
                    "guid": "a4f648d7-76ef-477f-bc8e-0601b5a60093",
                    "type": "number",
                    "number_value": "10.23",
                    "datetime_value": "1687708260000",
                    "member_value": [
                        {
                            "id": "ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f",
                            "type": "user",
                            "role": "editor",
                            "name": "张明德（明德）"
                        }
                    ],
                    "single_select_value": "4216f79b-3fda-4dc6-a0c4-a16022e47152",
                    "multi_select_value": [
                        "4216f79b-3fda-4dc6-a0c4-a16022e47152"
                    ],
                    "name": "优先级",
                    "text_value": "这是一段文本介绍。"
                }
            ],
            "dependencies": [
                {
                    "type": "next",
                    "task_guid": "93b7bd05-35e6-4371-b3c9-6b7cbd7100c0"
                }
            ],
            "assignee_related": [
                {
                    "id": "ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f",
                    "completed_at": "1675742789470"
                }
            ]
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1470400 | 请求参数错误，如传入非法的成员类型和角色。 | 错误原因见返回的msg提示的信息。 |
| 500 | 1470500 | 服务器错误。 | 尝试重试调用。如持续失败，请联系支持人员进行反馈。 |
| 400 | 1470610 | 任务的负责人的数量超过最大限制，无法继续添加。 | 检查当前任务的负责人数量。 |
| 400 | 1470611 | 任务的关注人的数量超过最大限制，无法继续添加。 | 检查当前任务的关注人数量。 |
| 403 | 1470403 | 无权限添加任务成员。 | 检查调用身份是否有任务的可编辑权限。详情见[任务功能概述](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/task/overview)中的“任务是如何鉴权的？”章节。 |
| 404 | 1470404 | 任务数据不存在或者已删除。 | 确认要访问的任务数据是否存在或已删除。 |
| 500 | 1470422 | 使用同样的client_token并发调用接口 | 不要使用client_token并发调用接口。 |


