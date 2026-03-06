---
title: "查询单个序列"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/get"
updateTime: "1770621290000"
---

# 查询单个序列详情

该接口通过序列ID查询单个序列详情信息，如序列名称、描述、状态等


> **Warning**: 延迟说明：数据库主从延迟2s以内，即：直接创建序列后2s内调用此接口可能查询不到数据。


> **Tip**: 如果你需要批量序列查询场景，建议通过[批量查询序列信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_family/batch_get)获取序列信息。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/job_families/:job_family_id |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:corehr:readonly` 获取核心人事信息 `corehr:job_family:read` 获取序列信息 `corehr:corehr` 更新核心人事信息 `corehr:job_family:write` 读写序列信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `job_family_id` | `string` | 序列ID。ID获取方式： - 调用[【新建序列】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/create)[【查询租户的序列信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/list)等接口可以返回序列ID<br>**示例值**："1554548" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `job_family` | `job_family` | 序列信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 序列 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言信息，中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 是否启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `selectable` | `boolean` | 是否可被使用，true为可被使用，false为不可被使用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `parent_id` | `string` | 上级序列 ID，详细信息可通过[【查询单个序列】](get.md)接口查询获得（若查询的是一级序列，则该字段不展示） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `pathway_ids` | `string\[\]` | 通道ID，详情可以参考[【获取通道信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/pathway/batch_get) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 当前版本生效日期 - 返回格式：YYYY-MM-DD 00:00:00（最小单位到日） - 日期范围:1900-01-01 00:00:00～9999-12-31 00:00:00 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 当前版本失效日期 - 返回格式：YYYY-MM-DD 00:00:00（最小单位到日） - 日期范围:1900-01-01 00:00:00～9999-12-31 00:00:00 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 (不能与其他记录的编码重复)，当开启自动编码时，该字段会失效 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段（该字段暂不支持，可忽略） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 自定义字段（该字段暂时不支持） |
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
                    "value": "刘梓新"
                }
            ],
            "custom_fields": [
                {
                    "field_name": "序列管理员",
                    "value": "\"Sandy\""
                }
            ]
        }
    }
}
```


