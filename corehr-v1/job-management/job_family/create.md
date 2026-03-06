---
title: "创建序列"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/create"
updateTime: "1765434826000"
---

# 创建单个序列

该接口用于创建单个序列，创建后系统中新增一条包含序列编码、名称、描述等信息的序列记录


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/job_families |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:corehr` 更新核心人事信息 `corehr:job_family:write` 读写序列信息 |

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
| `name` | `i18n\[\]` | 是 | 序列名称 - 每个name元素必须包含lang和value参数，表明对应语言下具体的name值 - 目前name最大元素个数为2，仅支持中、英文 |
| &nbsp;&nbsp;└ `lang` | `string` | 是 | 名称信息的语言，中文用zh-CN，英文用en-US - 必须与 value 字段同时传入<br>**示例值**："zh-CN" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 名称信息的内容，注意事项： - 名称不能包含「/」「；」「;」「\」「'」字符 - 序列中英文名称会有全局唯一校验 - 最小1字符，最大200字符 - 必须与 lang 字段同时传入<br>**示例值**："技术" |
| `active` | `boolean` | 是 | 是否启用，true为启用，false为停用<br>**示例值**：true |
| `selectable` | `boolean` | 否 | 是否可被使用，true为可被使用，false为不可被使用。默认值为true，代表可被使用<br>**示例值**：true |
| `parent_id` | `string` | 否 | 上级序列 ID。ID获取方式： - 调用[【新建序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/create)[【查询租户的序列信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/list)等接口可以返回序列ID<br>**示例值**："4698020757495316313" |
| `pathway_ids` | `string\[\]` | 否 | 通道ID，详情可以参考[【获取通道信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/pathway/batch_get)。默认值为空数组，表示不关联任何通道<br>**示例值**：["4719519211875096301"] |
| `effective_time` | `string` | 是 | 版本生效日期。注意事项： - 填写格式：YYYY-MM-DD 00:00:00（系统会自动将时分秒改为00:00:00） - 系统默认为填写日期当天的 00:00:00 生效  - 该接口只支持到最小单位为日 - 日期范围要求:1900-01-01 00:00:00～9999-12-31 23:59:59 - 最小19字符（格式为YYYY-MM-DD 00:00:00），最大19字符 - 详情可以参考[时间轴介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/about-timeline-version)<br>**示例值**："2020-05-01 00:00:00" |
| `code` | `string` | 否 | 编码 (不能与其他记录的编码重复)，当开启自动编码时，该字段会失效<br>**示例值**："123456" |
| `description` | `i18n\[\]` | 否 | 描述。默认值为空数组，表示没有描述 - 每个description元素必须包含lang和value参数，表明对应语言下具体的描述值 |
| &nbsp;&nbsp;└ `lang` | `string` | 是 | 语言，中文用zh-CN，英文用en-US<br>**示例值**："zh-CN" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 内容 - 最小1字符，最大200字符<br>**示例值**："这是一个技术序列的描述" |
| `custom_fields` | `object_field_data\[\]` | 否 | 自定义字段（序列暂时不支持自定义字段），格式参考：[【自定义字段说明】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)岗位、职务、自定义组织模块。默认值为空数组，表示没有自定义字段 |
| &nbsp;&nbsp;└ `field_name` | `string` | 是 | 字段名 - 最少1个字符，最多200个字符<br>**示例值**："name" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(如123, 123.23, "true", [\"id1\",\"id2\"], "2006-01-02 15:04:05") - 自定义字段类型，详细见[获取自定义字段列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query)  - 最少1个字符，最多200个字符<br>**示例值**："\"Sandy\"" |


### 请求体示例

```json
{
    "name": [
        {
            "lang": "zh-CN",
            "value": "技术"
        }
    ],
    "active": true,
    "selectable": true,
    "parent_id": "4698020757495316313",
    "pathway_ids": [
        "4719519211875096301"
    ],
    "effective_time": "2020-05-01 00:00:00",
    "code": "123456",
    "description": [
        {
            "lang": "zh-CN",
            "value": "这是一个技术序列的描述"
        }
    ],
    "custom_fields": [
        {
            "field_name": "name",
            "value": "\"Sandy\""
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
| &nbsp;&nbsp;└ `job_family` | `job_family` | 创建成功的序列信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 序列 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言，中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 是否启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `selectable` | `boolean` | 是否可被使用，true为可被使用，false为不可被使用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `parent_id` | `string` | 上级序列 ID - 可通过[批量查询序列](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_family/batch_get)获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `pathway_ids` | `string\[\]` | 通道ID，详情可以参考[【获取通道信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/pathway/batch_get) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 版本生效日期 - 返回格式：YYYY-MM-DD 00:00:00（最小单位到日） - 日期范围:1900-01-01 00:00:00～9999-12-31 23:59:59 - 详情可以参考[时间轴介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/about-timeline-version) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 版本失效日期 - 返回格式：YYYY-MM-DD 00:00:00（最小单位到日） - 日期范围:1900-01-01 00:00:00～9999-12-31 23:59:59 - 详情可以参考[时间轴介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/about-timeline-version) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言，中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段（暂不支持该功能，可忽略） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(如123, 123.23, "true", [\"id1\",\"id2\"], "2006-01-02 15:04:05") |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "job_family": {
            "id": "4698019107896524633",
            "name": [
                {
                    "lang": "zh-CN",
                    "value": "张三"
                }
            ],
            "active": true,
            "selectable": true,
            "parent_id": "4698020757495316313",
            "pathway_ids": [
                "4719519211875096301"
            ],
            "effective_time": "2020-05-01 00:00:00",
            "expiration_time": "2020-05-02 00:00:00",
            "code": "123456",
            "description": [
                {
                    "lang": "zh-CN",
                    "value": "这是一个技术序列的描述"
                }
            ],
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


