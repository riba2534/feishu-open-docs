---
title: "创建子任务"
fullPath: "/uAjLw4CM/ukTMukTMukTM/task-v2/task-subtask/create"
updateTime: "1689824557000"
---

# 创建子任务

给一个任务创建一个子任务。

接口功能除了额外需要输入父任务的GUID之外，和[创建任务](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/task/create)接口功能完全一致。


> **Tip**: 创建子任务需要拥有父任务的编辑权限。详见[任务是如何鉴权的？](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/faq)
> 
> 如果将新任务加入清单，则需要清单的可编辑权限。详情见[任务功能概述](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/task/overview)中的“任务是如何鉴权的？”章节。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/task/v2/tasks/:task_guid/subtasks |
| HTTP Method | POST |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `task:task:write` 查看、创建、更新、删除任务 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `task_guid` | `string` | 父任务GUID<br>**示例值**："e297ddff-06ca-4166-b917-4ce57cd3a7a0"<br>**数据校验规则**：<br>- 最大长度：`100` 字符 |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**默认值**：`open_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `summary` | `string` | 是 | 任务标题<br>**示例值**："针对全年销售进行一次复盘"<br>**数据校验规则**：<br>- 最大长度：`10000` 字符 |
| `description` | `string` | 否 | 任务摘要<br>**示例值**："需要事先阅读复盘总结文档" |
| `due` | `due` | 否 | 任务截止时间戳(ms)，截止时间戳和截止日期选择一个填写。<br>**示例值**：1675742789470 |
| &nbsp;&nbsp;└ `timestamp` | `string` | 否 | 截止时间/日期的时间戳，距1970-01-01 00:00:00的毫秒数。如果截止时间是一个日期，需要把日期转换成时间戳，并设置 is_all_day=true<br>**示例值**："1675454764000" |
| &nbsp;&nbsp;└ `is_all_day` | `boolean` | 否 | 是否截止到一个日期。如果设为true，timestamp中只有日期的部分会被解析和存储。<br>**示例值**：true |
| `origin` | `origin` | 否 | 任务关联的第三方平台来源信息。详见[如何使用Origin?](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/task/overview) |
| &nbsp;&nbsp;└ `platform_i18n_name` | `i18n_text` | 否 | 任务导入来源的名称，用于在任务中心详情页展示。需提供多语言版本。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 否 | 英文<br>**示例值**："workbench"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 否 | 中文<br>**示例值**："工作台"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `zh_hk` | `string` | 否 | 中文（香港地区）<br>**示例值**："工作臺"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `zh_tw` | `string` | 否 | 中文（台湾地区）<br>**示例值**："工作臺"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 否 | 日语<br>**示例值**："作業台"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `fr_fr` | `string` | 否 | 法语<br>**示例值**："Table de travail" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `it_it` | `string` | 否 | 意大利语<br>**示例值**："banco di lavoro" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `de_de` | `string` | 否 | 德语<br>**示例值**："Werkbank" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ru_ru` | `string` | 否 | 俄语<br>**示例值**："верстак" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `th_th` | `string` | 否 | 泰语<br>**示例值**："โต๊ะทำงาน" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `es_es` | `string` | 否 | 西班牙语<br>**示例值**："banco de trabajo" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ko_kr` | `string` | 否 | 韩语<br>**示例值**："작업대" |
| &nbsp;&nbsp;└ `href` | `href` | 否 | 任务关联的来源平台详情页链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 否 | 链接对应的地址<br>**示例值**："https://www.example.com"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1024` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 否 | 链接对应的标题<br>**示例值**："反馈一个问题，需要协助排查"<br>**数据校验规则**：<br>- 最大长度：`512` 字符 |
| `extra` | `string` | 否 | 调用者可以传入的任意附带到任务上的数据。在获取任务详情时会原样返回。<br>**示例值**："dGVzdA=="<br>**数据校验规则**：<br>- 最大长度：`65536` 字符 |
| `completed_at` | `string` | 否 | 任务的完成时刻时间戳(ms)<br>**示例值**："1675742789470"<br>**默认值**：`0`<br>**数据校验规则**：<br>- 最大长度：`20` 字符 |
| `members` | `member\[\]` | 否 | 任务成员列表<br>**示例值**：[ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f]<br>**数据校验规则**：<br>- 最大长度：`500` |
| &nbsp;&nbsp;└ `id` | `string` | 否 | 表示member的id<br>**示例值**："ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f"<br>**数据校验规则**：<br>- 最大长度：`100` 字符 |
| &nbsp;&nbsp;└ `type` | `string` | 否 | 成员的类型<br>**示例值**："user"<br>**默认值**：`user` |
| &nbsp;&nbsp;└ `role` | `string` | 否 | 成员角色，支持"assignee"或者"follower"<br>**示例值**："assignee"<br>**数据校验规则**：<br>- 最大长度：`20` 字符 |
| `repeat_rule` | `string` | 否 | 如果设置，则该任务为“重复任务”。该字段表示了重复任务的重复规则。详见[功能概述](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/overview)中的“如何使用重复任务？”章节。<br>**示例值**："FREQ=WEEKLY;INTERVAL=1;BYDAY=MO,TU,WE,TH,FR"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| `custom_complete` | `custom_complete` | 否 | 任务自定义完成规则。详见[功能概述](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/overview)中的“如何使用自定义完成？”章节。 |
| &nbsp;&nbsp;└ `pc` | `custom_complete_item` | 否 | pc客户端自定义完成配置（含mac和windows） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `href` | `string` | 否 | 自定义完成的跳转url<br>**示例值**："https://www.example.com" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tip` | `i18n_text` | 否 | 自定义完成的弹出提示为 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 否 | 英文<br>**示例值**："workbench"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 否 | 中文<br>**示例值**："工作台"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_hk` | `string` | 否 | 中文（香港地区）<br>**示例值**："工作臺"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_tw` | `string` | 否 | 中文（台湾地区）<br>**示例值**："工作臺"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 否 | 日语<br>**示例值**："作業台"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fr_fr` | `string` | 否 | 法语<br>**示例值**："Table de travail" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `it_it` | `string` | 否 | 意大利语<br>**示例值**："banco di lavoro" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `de_de` | `string` | 否 | 德语<br>**示例值**："Werkbank" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ru_ru` | `string` | 否 | 俄语<br>**示例值**："верстак" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `th_th` | `string` | 否 | 泰语<br>**示例值**："โต๊ะทำงาน" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `es_es` | `string` | 否 | 西班牙语<br>**示例值**："banco de trabajo" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ko_kr` | `string` | 否 | 韩语<br>**示例值**："작업대" |
| &nbsp;&nbsp;└ `ios` | `custom_complete_item` | 否 | 飞书ios端的自定义完成配置 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `href` | `string` | 否 | 自定义完成的跳转url<br>**示例值**："https://www.example.com" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tip` | `i18n_text` | 否 | 自定义完成的弹出提示为 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 否 | 英文<br>**示例值**："workbench"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 否 | 中文<br>**示例值**："工作台"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_hk` | `string` | 否 | 中文（香港地区）<br>**示例值**："工作臺"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_tw` | `string` | 否 | 中文（台湾地区）<br>**示例值**："工作臺"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 否 | 日语<br>**示例值**："作業台"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fr_fr` | `string` | 否 | 法语<br>**示例值**："Table de travail" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `it_it` | `string` | 否 | 意大利语<br>**示例值**："banco di lavoro" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `de_de` | `string` | 否 | 德语<br>**示例值**："Werkbank" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ru_ru` | `string` | 否 | 俄语<br>**示例值**："верстак" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `th_th` | `string` | 否 | 泰语<br>**示例值**："โต๊ะทำงาน" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `es_es` | `string` | 否 | 西班牙语<br>**示例值**："banco de trabajo" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ko_kr` | `string` | 否 | 韩语<br>**示例值**："작업대" |
| &nbsp;&nbsp;└ `android` | `custom_complete_item` | 否 | 飞书android端的自定义完成配置 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `href` | `string` | 否 | 自定义完成的跳转url<br>**示例值**："https://www.example.com" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tip` | `i18n_text` | 否 | 自定义完成的弹出提示为 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 否 | 英文<br>**示例值**："workbench"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 否 | 中文<br>**示例值**："工作台"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_hk` | `string` | 否 | 中文（香港地区）<br>**示例值**："工作臺"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_tw` | `string` | 否 | 中文（台湾地区）<br>**示例值**："工作臺"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 否 | 日语<br>**示例值**："作業台"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fr_fr` | `string` | 否 | 法语<br>**示例值**："Table de travail" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `it_it` | `string` | 否 | 意大利语<br>**示例值**："banco di lavoro" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `de_de` | `string` | 否 | 德语<br>**示例值**："Werkbank" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ru_ru` | `string` | 否 | 俄语<br>**示例值**："верстак" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `th_th` | `string` | 否 | 泰语<br>**示例值**："โต๊ะทำงาน" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `es_es` | `string` | 否 | 西班牙语<br>**示例值**："banco de trabajo" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ko_kr` | `string` | 否 | 韩语<br>**示例值**："작업대" |
| `tasklists` | `task_in_tasklist_info\[\]` | 否 | 任务所在清单的信息。如果设置，则表示创建的任务要直接加入到指定清单。 |
| &nbsp;&nbsp;└ `tasklist_guid` | `string` | 否 | 任务要加入的清单的GUID。<br>**示例值**："cc371766-6584-cf50-a222-c22cd9055004"<br>**数据校验规则**：<br>- 最大长度：`100` 字符 |
| &nbsp;&nbsp;└ `section_guid` | `string` | 否 | 任务所在清单的自定义分组GUID。如果设置了清单GUID但没有设置自定义分组GUID，则自动加入该清单的默认分组。<br>**示例值**："e6e37dcc-f75a-5936-f589-12fb4b5c80c2" |
| `client_token` | `string` | 否 | 幂等token。如果提供则触发后端实现幂等行为。详见[功能概述](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/overview)中的“ 幂等调用 ”章节。<br>**示例值**："daa2237f-8310-4707-a83b-52c8a81e0fb7"<br>**数据校验规则**：<br>- 长度范围：`10` ～ `100` 字符 |
| `start` | `start` | 否 | 任务的开始时间(ms) |
| &nbsp;&nbsp;└ `timestamp` | `string` | 否 | 开始时间/日期的时间戳，距1970-01-01 00:00:00的毫秒数。如果开始时间是一个日期，需要把日期转换成时间戳，并设置 is_all_day=true<br>**示例值**："1675454764000" |
| &nbsp;&nbsp;└ `is_all_day` | `boolean` | 否 | 是否开始于一个日期。如果设为true，timestamp中只有日期的部分会被解析和存储。<br>**示例值**：true |
| `reminders` | `reminder\[\]` | 否 | 任务提醒 |
| &nbsp;&nbsp;└ `relative_fire_minute` | `int` | 是 | 相对于截止时间的提醒时间分钟数。例如30表示截止时间前30分钟提醒；0表示截止时提醒。<br>**示例值**：30 |


### 请求体示例

```json
{
    "summary": "针对全年销售进行一次复盘",
    "description": "需要事先阅读复盘总结文档",
    "due": {
        "timestamp": "1675454764000",
        "is_all_day": true
    },
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
    "completed_at": "1675742789470",
    "members": [
        {
            "id": "ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f",
            "type": "user",
            "role": "assignee"
        }
    ],
    "repeat_rule": "FREQ=WEEKLY;INTERVAL=1;BYDAY=MO,TU,WE,TH,FR",
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
    "tasklists": [
        {
            "tasklist_guid": "cc371766-6584-cf50-a222-c22cd9055004",
            "section_guid": "e6e37dcc-f75a-5936-f589-12fb4b5c80c2"
        }
    ],
    "client_token": "daa2237f-8310-4707-a83b-52c8a81e0fb7",
    "start": {
        "timestamp": "1675454764000",
        "is_all_day": true
    },
    "reminders": [
        {
            "relative_fire_minute": 30
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
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `subtask` | `task` | 创建的任务 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `guid` | `string` | 任务guid，任务的唯一ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `summary` | `string` | 任务标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 任务描述 |
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
| &nbsp;&nbsp;&nbsp;&nbsp;└ `members` | `member\[\]` | 任务成员列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 表示member的id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 成员的类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `role` | `string` | 成员角色 |
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
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start` | `start` | 任务的开始时间。<br>如果同时设置任务的开始时间和截止时间，开始时间必须<=截止时间，并且开始/截止时间的is_all_day设置必须相同。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `timestamp` | `string` | 开始时间/日期的时间戳，距1970-01-01 00:00:00 UTC的毫秒数。如果开始时间是一个日期，需要把日期转换成时间戳，并设置 is_all_day=true。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_all_day` | `boolean` | 是否开始于一个日期。如果设为true，timestamp中只有日期的部分会被解析和存储。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `subtask_count` | `int` | 该任务的子任务的个数。 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "subtask": {
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
                "role": "assignee"
            },
            "members": [
                {
                    "id": "ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f",
                    "type": "user",
                    "role": "类型"
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
                        "role": "assignee"
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
            "subtask_count": 1
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1470400 | 请求参数错误。例如没有输入任务标题。 | 错误原因见返回的msg提示的信息。 |
| 404 | 1470404 | 父任务数据不存在或者已删除。 | 确认父任务数据是否存在或已删除。 |
| 500 | 1470500 | 服务器错误。 | 尝试重试调用。如持续失败，请联系支持人员进行反馈。 |
| 403 | 1470403 | 缺少父任务的编辑权限。 | 检查调用身份是否有父任务的可编辑权限。详情见[任务功能概述](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/task/overview)中的“任务是如何鉴权的？”章节。 |
| 500 | 1470422 | 使用相同的client_token并发调用接口。 | 不要使用相同的client_token并发调用接口。 |


