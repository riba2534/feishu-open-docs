---
title: "更新职级"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_level/update"
updateTime: "1720167692000"
---

# 更新职级

调用该接口更新指定职级的信息。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/contact/v3/job_levels/:job_level_id |
| HTTP Method | PUT |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `contact:contact` 更新通讯录 `contact:job_level` 创建、删除、更新职级 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `job_level_id` | `string` | 职级 ID。获取方式：<br>- 创建职级时，可以从返回结果中获取职级 ID。 - 调用[获取租户职级列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_level/list)接口，查找指定职级的 ID 信息。<br>**示例值**："mga5oa8ayjlp9rb" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | `string` | 否 | 职级的通用名称。如果未设置多语言名称，则默认展示该名称。<br>**默认值**：空，表示不更新。<br>**示例值**："高级专家"<br>**数据校验规则**：<br>- 长度范围：`1` ～ `255` 字符 |
| `description` | `string` | 否 | 职级的通用描述。如果未设置多语言描述，则默认展示该描述。<br>**默认值**：空，表示不更新。<br>**示例值**："公司内部中高级职称，有一定专业技术能力的人员" |
| `order` | `int` | 否 | 职级排序。数值越小，排序越靠前。<br>**默认值**：空，表示不更新。<br>**示例值**：200<br>**数据校验规则**：<br>- 取值范围：`100` ～ `100000` |
| `status` | `boolean` | 否 | 是否启用该职级。<br>**可选值有**： - true：启用 - false：不启用<br>**默认值**：空，表示不更新。<br>**示例值**：true |
| `i18n_name` | `i18n_content\[\]` | 否 | 多语言职级名称。 |
| &nbsp;&nbsp;└ `locale` | `string` | 否 | 语言版本。例如：<br>- zh_cn：中文 - en_us：英语 - ja_jp：日语<br>**默认值**：空，表示不更新。<br>**示例值**："zh_cn" |
| &nbsp;&nbsp;└ `value` | `string` | 否 | 语言版本对应的职级名称。<br>**默认值**：空，表示不更新。<br>**示例值**："多语言内容" |
| `i18n_description` | `i18n_content\[\]` | 否 | 多语言职级描述。 |
| &nbsp;&nbsp;└ `locale` | `string` | 否 | 语言版本。例如：<br>- zh_cn：中文 - en_us：英语 - ja_jp：日语<br>**示例值**："zh_cn" |
| &nbsp;&nbsp;└ `value` | `string` | 否 | 语言版本对应的职级描述。<br>**示例值**："多语言内容" |


### 请求体示例

```json
{
    "name": "高级专家",
    "description": "公司内部中高级职称，有一定专业技术能力的人员",
    "order": 200,
    "status": true,
    "i18n_name": [
        {
            "locale": "zh_cn",
            "value": "多语言内容"
        }
    ],
    "i18n_description": [
        {
            "locale": "zh_cn",
            "value": "多语言内容"
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
| &nbsp;&nbsp;└ `job_level` | `job_level` | 职级信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 职级名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 职级描述。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `order` | `int` | 职级排序。数值越小，排序越靠前。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `boolean` | 是否启用职级。<br>**可能值有**：<br>true：启用 false：不启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_level_id` | `string` | 职级 ID。后续可通过该 ID 删除、更新、查询职级。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `i18n_content\[\]` | 多语言名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语言版本。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语言版本对应的名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_description` | `i18n_content\[\]` | 多语言描述。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语言版本。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语言版本对应的描述。 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "job_level": {
            "name": "高级专家",
            "description": "公司内部中高级职称，有一定专业技术能力的人员",
            "order": 200,
            "status": true,
            "job_level_id": "mga5oa8ayjlp9rb",
            "i18n_name": [
                {
                    "locale": "zh_cn",
                    "value": "多语言内容"
                }
            ],
            "i18n_description": [
                {
                    "locale": "zh_cn",
                    "value": "多语言内容"
                }
            ]
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 42302 | job level tenant lock fail | 并发更新职级受限，请等待一段时间重试。 |
| 400 | 42303 | job level name not valid | 职级名称不合法。请求时设置的名称长度限制为 1 ~ 255 个字符。 |
| 400 | 42305 | job level name duplicate | 职级名称重复。请调整名称取值后重试。 |
| 400 | 42306 | job level order duplicate | 职级排序值重复。请调整排序取值后重试。 |
| 400 | 42304 | job level description not valid | 描述不合法。 |
| 400 | 42307 | job level external id duplicate | 职级 ID 重复。 |
| 404 | 42301 | job level not exist | 职级不存在。请确保传入的职级 ID 正确后重试。 |
| 400 | 42308 | job level invalid order | 排序值不合法。职级排序取值范围为 100 ~ 100000。 |


更多错误码信息，参见[通用错误码](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)。


