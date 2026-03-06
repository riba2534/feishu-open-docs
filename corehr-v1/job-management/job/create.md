---
title: "创建职务"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job/create"
updateTime: "1765434866000"
---

# 创建职务

该接口用于创建职务信息，创建后系统中新增一条包含职务编码、名称、描述等信息的职务记录，适用于企业新增职务类型时，HR需要创建职务信息以便分配给员工的场景


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/jobs |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:corehr` 更新核心人事信息 `corehr:job:write` 读写职务信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `client_token` | `string` | 否 | 根据client_token是否一致来判断是否为同一请求<br>**示例值**：12454646 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `code` | `string` | 否 | 职务编码（不能与其他记录的编码重复） - 开启自动编码时，以自动生成的编码值为准，传入值不生效 - 未开启自动编码时，编码字段值以传入值为准 - 最少1个字符，最多200个字符<br>**示例值**："JP422119" |
| `name` | `i18n\[\]` | 是 | 职务名称 - 名称不能包含「/」「；」「;」「\」「'」字符 - 职务中英文名称会有全局唯一校验（已停用职务也会校验） - 每个name元素必须包含lang和value参数，表明对应语言下具体的name值 - 目前name最大元素个数为2，仅支持中、英文 |
| &nbsp;&nbsp;└ `lang` | `string` | 是 | 语言信息，中文用zh-CN，英文用en-US。最少1个字符，最多200个字符<br>**示例值**："zh-CN" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 名称信息的内容。最少1个字符，最多200个字符<br>**示例值**："软件工程师" |
| `description` | `i18n\[\]` | 否 | 描述 |
| &nbsp;&nbsp;└ `lang` | `string` | 是 | 语言信息，中文用zh-CN，英文用en-US。最少1个字符，最多200个字符<br>**示例值**："zh-CN" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 描述信息的内容。最少1个字符，最多200个字符<br>**示例值**："负责软件系统的设计、开发与维护，参与需求分析和技术方案制定" |
| `active` | `boolean` | 是 | 是否启用，true为启用，fasle为停用。<br>**示例值**：true |
| `job_title` | `i18n\[\]` | 否 | 职务头衔 |
| &nbsp;&nbsp;└ `lang` | `string` | 是 | 职务头衔信息的语言，最少1个字符，最多200个字符<br>**示例值**："zh-CN" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 职务头衔信息的内容，最少1个字符，最多200个字符<br>**示例值**："高级软件工程师" |
| `pathway_id` | `string` | 否 | 通道ID<br>**示例值**："4719519211875096301" |
| `job_family_id_list` | `string\[\]` | 否 | 职务序列 ID 列表 - 可通过[批量查询序列](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_family/batch_get)获取详情<br>**示例值**：["4719519211875096301"] |
| `job_level_id_list` | `string\[\]` | 否 | 职务级别 ID 列表 - 可通过[批量查询职级](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_level/batch_get)获取详情<br>**示例值**：["4719519212005299950"] |
| `working_hours_type_id` | `string` | 否 | 工时制度 ID，枚举值及详细信息可通过[【批量查询工时制度】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/list)接口查询获得<br>**示例值**："6890452208593372679" |
| `effective_time` | `string` | 是 | 版本生效日期 - 填写格式：YYYY-MM-DD 00:00:00（系统会自动将时分秒改为00:00:00） - 系统默认为填写日期当天的 00:00:00 生效  - 该接口只支持到最小单位为日 - 日期范围要求:1900-01-01 00:00:00～9999-12-31 23:59:59 - 最小19字符（格式为YYYY-MM-DD 00:00:00），最大19字符 - 详情可以参考[时间轴介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/about-timeline-version)<br>**示例值**："2020-01-01 00:00:00" |
| `custom_fields` | `object_field_data\[\]` | 否 | 自定义字段，格式参考：[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)岗位、职务、自定义组织模块 |
| &nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名，最小1字符，最大50字符<br>**示例值**："name" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(如123, 123.23, "true", [\"id1\",\"id2\"], "2006-01-02 15:04:05")，最小1字符，最大200字符<br>**示例值**："Sandy" |


### 请求体示例

```json
{
    "code": "JP422119",
    "name": [
        {
            "lang": "zh-CN",
            "value": "软件工程师"
        }
    ],
    "description": [
        {
            "lang": "zh-CN",
            "value": "负责软件系统的设计、开发与维护，参与需求分析和技术方案制定"
        }
    ],
    "active": true,
    "job_title": [
        {
            "lang": "zh-CN",
            "value": "高级软件工程师"
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
    "custom_fields": [
        {
            "field_name": "name",
            "value": "Sandy"
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
| &nbsp;&nbsp;└ `job` | `job` | 创建成功的Job信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 职务 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 职务编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 软件工程师 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容，最小1字符，最大100字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 是否启用，true为启用，false为停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_title` | `i18n\[\]` | 职务头衔 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `pathway_id` | `string` | 通道ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id_list` | `string\[\]` | 职务序列 ID 列表 - 可通过[批量查询序列](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_family/batch_get)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_level_id_list` | `string\[\]` | 职务级别 ID 列表 - 可通过[批量查询职级](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_level/batch_get)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `working_hours_type_id` | `string` | 工时制度 ID，枚举值及详细信息可通过[【批量查询工时制度】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/list)接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 版本生效日期（UTC+8） - 返回格式：YYYY-MM-DD 00:00:00（最小单位到日） - 日期范围:1900-01-01 00:00:00～9999-12-31 23:59:59 - 详情可以参考[时间轴介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/about-timeline-version) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 版本失效日期 - 返回格式：YYYY-MM-DD 00:00:00（最小单位到日） - 日期范围:1900-01-01 00:00:00～9999-12-31 23:59:59 - 详情可以参考[时间轴介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/about-timeline-version) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段，格式参考：[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)岗位、职务、自定义组织模块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(如123, 123.23, "true", [\"id1\",\"id2\"], "2006-01-02 15:04:05") |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "job": {
            "id": "4698040628992333549",
            "code": "JP422119",
            "name": [
                {
                    "lang": "zh-CN",
                    "value": "软件工程师"
                }
            ],
            "description": [
                {
                    "lang": "zh-CN",
                    "value": "负责软件系统的设计、开发与维护，参与需求分析和技术方案制定"
                }
            ],
            "active": true,
            "job_title": [
                {
                    "lang": "zh-CN",
                    "value": "高级软件工程师"
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
                    "value": "\"Sandy\""
                }
            ]
        }
    }
}
```


