---
title: "获取单个序列信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_family/get"
updateTime: "1720167724000"
---

# 获取单个序列信息

调用该接口获取指定序列的信息，包括序列的名称、描述、启用状态以及 ID 等。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/contact/v3/job_families/:job_family_id |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `contact:job_family:readonly` 查询租户下工作序列的详细信息 `contact:job_family` 创建、删除、更新租户的工作序列 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `job_family_id` | `string` | 序列 ID。获取方式：<br>- [创建序列](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_family/create)时可以从返回结果中获取（job_family_id）。 - 调用[获取租户序列列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_family/list)接口获取序列 ID。<br>**示例值**："mga5oa8ayjlp9rb" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `job_family` | `job_family` | 序列信息。 |
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
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id` | `string` | 序列 ID。 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "job_family": {
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
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 404 | 42404 | job family not exist | 序列不存在。你需要检查并传入正确的序列 ID。 |


更多错误码信息，参见[通用错误码](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)。


