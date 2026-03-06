---
title: "获取外部数据源配置信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/payroll-v1/datasource/list"
updateTime: "1747821620000"
---

# 获取外部数据源配置信息

批量查询飞书人事后台：设置->算薪数据设置->外部数据源设置 中的数据源设置列表


> **Warning**: 停用的数据源、字段不能保存数据


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/payroll/v1/datasources |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `payroll:external_datasource_configuration:read` Payroll外部数据源设置读权限 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 是 | **示例值**：10<br>**数据校验规则**：<br>- 取值范围：`1` ～ `100` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0= |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `datasources` | `datasource\[\]` | 数据源列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 数据源编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_names` | `i18n_content\[\]` | 数据源名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语种 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语种对应的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 名称对应的实体id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 启停用状态<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `fields` | `datasource_field\[\]` | 数据源字段列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 数据源字段编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_names` | `i18n_content\[\]` | 数据源字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语种 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语种对应的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 名称对应的实体id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 金额 - `2`: 数值 - `3`: 文本 - `4`: 日期 - `5`: 百分比 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 字段启停用状态<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_description` | `i18n_content\[\]` | 数据源字段描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语种 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语种对应的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 名称对应的实体id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `decimal_places` | `int` | 保留小数位数。目前只有number、money类型字段需要设置保留小数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_description` | `i18n_content\[\]` | 数据源描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语种 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语种对应的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 名称对应的实体id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `data_period_type` | `int` | 数据写入维度<br>**可选值有**：<br>- `1`: 算薪期间 - `2`: 数据发生日期。功能灰度中，如需创建该维度数据源配置，请申请灰度。 - `3`: 自定义数据周期。功能灰度中，如需创建该维度数据源配置，请申请灰度。 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "page_token": "eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0=",
        "has_more": true,
        "datasources": [
            {
                "code": "test_datasource__c",
                "i18n_names": [
                    {
                        "locale": "zh_cn",
                        "value": "名称",
                        "id": "723123123123123213"
                    }
                ],
                "active_status": 1,
                "fields": [
                    {
                        "code": "test__c",
                        "i18n_names": [
                            {
                                "locale": "zh_cn",
                                "value": "名称",
                                "id": "723123123123123213"
                            }
                        ],
                        "field_type": 1,
                        "active_status": 1,
                        "i18n_description": [
                            {
                                "locale": "zh_cn",
                                "value": "名称",
                                "id": "723123123123123213"
                            }
                        ],
                        "decimal_places": 1
                    }
                ],
                "i18n_description": [
                    {
                        "locale": "zh_cn",
                        "value": "名称",
                        "id": "723123123123123213"
                    }
                ],
                "data_period_type": 1
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 2500001 | unknown error | 未知错误，联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 2500002 | param invalid | 参数异常，检查入参 |


