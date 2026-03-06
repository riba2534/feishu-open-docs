---
title: "获取租户序列列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_family/list"
updateTime: "1720167724000"
---

# 获取租户序列列表

调用该接口获取当前租户下的序列信息，包含序列的名称、描述、启用状态以及 ID 等。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/contact/v3/job_families |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `contact:job_family:readonly` 查询租户下工作序列的详细信息 `contact:job_family` 创建、删除、更新租户的工作序列 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 分页大小，用于限制一次请求所返回的数据条目数。<br>**示例值**：10<br>**默认值**：`10`<br>**数据校验规则**：<br>- 取值范围：`1` ～ `50` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：3 |
| `name` | `string` | 否 | 序列名称。<br>- 传入该字段时，可查询指定序列名称对应的序列信息（不支持模糊查询）。 - 不传入该字段时，查询当前租户下所有序列的信息。<br>**示例值**：产品<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` 字符 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `job_family\[\]` | 序列信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 序列名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 序列描述。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `parent_job_family_id` | `string` | 上级序列 ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `boolean` | 是否启用序列。<br>**可能值有**：<br>- true：启用 - false：禁用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `i18n_content\[\]` | 多语言序列名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语言版本。<br>**可能值有**：<br>- zh_cn：中文 - en_us：英语 - ja_jp：日语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语言版本对应的值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_description` | `i18n_content\[\]` | 多语言序列描述。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语言版本。<br>**可能值有**：<br>- zh_cn：中文 - en_us：英语 - ja_jp：日语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语言版本对应的值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id` | `string` | 序列 ID。后续可通过该 ID 更新、查询、删除序列。 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "name": "产品",
                "description": "负责产品策略制定的相关工作",
                "parent_job_family_id": "mga5oa8ayjlpzjq",
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
                ],
                "job_family_id": "mga5oa8ayjlpkzy"
            }
        ],
        "page_token": "AQD9/Rn9eij9Pm39ED40/RD/cIFmu77WxpxPB/2oHfQLZ+G8JG6tK7+ZnHiT7COhD2hMSICh/eBl7cpzU6JEC3J7COKNe4jrQ8ExwBCR",
        "has_more": true
    }
}
```


更多错误码信息，参见[通用错误码](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)。


