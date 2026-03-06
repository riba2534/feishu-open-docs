---
title: "批量查询成本分摊方案"
fullPath: "/uAjLw4CM/ukTMukTMukTM/payroll-v1/cost_allocation_plan/list"
updateTime: "1747796936000"
---

# 批量查询成本分摊方案

根据期间分页批量查询成本分摊方案，仅返回期间内生效的方案列表。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/payroll/v1/cost_allocation_plans |
| HTTP Method | GET |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `payroll:cost_allocation_plan:read` 获取成本分摊方案 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 是 | 分页大小<br>**示例值**：50<br>**数据校验规则**：<br>- 取值范围：`1` ～ `100` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：6823630319749592024 |
| `pay_period` | `string` | 是 | 期间，生成成本分摊报表对应的年月。格式为 yyyy-MM<br>**示例值**：2023-11 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `cost_allocation_plan\[\]` | 方案 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 成本分摊方案id，唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `names` | `i18n_content\[\]` | 方案名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语种 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语种对应的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `applicable_country_region` | `string` | 适用国家ID，通过[查询国家/地区信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dimensions` | `dimension\[\]` | 成本分摊方案对应的汇总维度列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_names` | `i18n_content\[\]` | 汇总维度信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语种 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语种对应的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 名称对应的实体id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `api_name` | `string` | 汇总维度字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_api_name` | `string` | 汇总维度对象名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cost_items` | `cost_item\[\]` | 成本分摊方案对应的成本项列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 成本项的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n_content\[\]` | 成本项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语种 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语种对应的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 名称对应的实体id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enable_correct` | `boolean` | 成本项是否启用更正 |
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
                "id": "6823630319749593096",
                "names": [
                    {
                        "locale": "zh_cn",
                        "value": "名称"
                    }
                ],
                "applicable_country_region": "6823630319749593389",
                "dimensions": [
                    {
                        "i18n_names": [
                            {
                                "locale": "zh_cn",
                                "value": "名称",
                                "id": "723123123123123213"
                            }
                        ],
                        "api_name": "company",
                        "obj_api_name": "jobData"
                    }
                ],
                "cost_items": [
                    {
                        "id": "7433424967234601004",
                        "name": [
                            {
                                "locale": "zh_cn",
                                "value": "名称",
                                "id": "723123123123123213"
                            }
                        ],
                        "enable_correct": true
                    }
                ]
            }
        ],
        "page_token": "6823630319749592467",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 2500001 | unknown error | 未知错误，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 2500002 | param invalid | 参数错误，请检查参数是否符合 |
| 500 | 2500003 | rpc fail | 内部服务调用异常，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |


