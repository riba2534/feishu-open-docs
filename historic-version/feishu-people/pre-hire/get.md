---
title: "查询单个待入职信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/pre_hire/get"
updateTime: "1721042402000"
---

# 查询单个待入职信息

根据 ID 查询单个待入职人员，本接口不再推荐使用（个人信息相关数据不完整），请使用[查询待入职](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/pre_hire/query)接口获取更完整信息。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/pre_hires/:pre_hire_id |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:corehr:readonly` 获取核心人事信息 `corehr:pre_hire:read` 查看待入职人员信息 `corehr:corehr` 更新核心人事信息 `corehr:pre_hire:write` 读写待入职人员信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `pre_hire_id` | `string` | 待入职ID，可从[搜索待入职人员信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/pre_hire/search)接口获取<br>**示例值**："121215" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `pre_hire` | `pre_hire` | 待入职信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ats_application_id` | `string` | 招聘投递 ID ，可以通过[获取投递列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/list)接口获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 待入职ID，可从[待入职列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/pre_hire/search)接口获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `hire_date` | `string` | 入职日期，格式："YYYY-MM-DD" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type` | `enum` | 人员类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `worker_id` | `string` | 人员编号 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type_id` | `string` | 人员类型，可通过[【批量查询人员类型】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/list)接口获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `person_id` | `string` | 个人信息ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `object_field_data\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_name` | `string` | 字段名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(如123, 123.23, "true", [\"id1\",\"id2\"], "2006-01-02 15:04:05") |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_rate` | `support_cost_center_item\[\]` | 成本中心分摊信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cost_center_id` | `string` | 支持的成本中心id，详细信息可通过[【搜索成本中心信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rate` | `int` | 分摊比例 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `onboarding_status` | `enum` | 入职状态 - `preboarding`：待入职 - `day_one`：准备就绪 - `completed`：已完成 - `withdrawn`：已撤销 - `deleted`：已删除，对应的系统操作是将待入职人员回退至 Offer 沟通阶段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "pre_hire": {
            "ats_application_id": "4719168654814483759",
            "id": "154545454",
            "hire_date": "2020-01-01",
            "employee_type": {
                "enum_name": "type_1",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ]
            },
            "worker_id": "1245646",
            "employee_type_id": "正式",
            "person_id": "656464648662",
            "custom_fields": [
                {
                    "field_name": "name",
                    "value": "\"Sandy\""
                }
            ],
            "cost_center_rate": [
                {
                    "cost_center_id": "6950635856373745165",
                    "rate": 100
                }
            ],
            "onboarding_status": {
                "enum_name": "type_1",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ]
            }
        }
    }
}
```


