---
title: "创建入职二维码"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/pre_hire/onboarding-qr-code/create-onboarding-qr-code"
updateTime: "1720766037000"
---

# 创建入职二维码

使用扫码入职功能时，创建入职二维码 


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/onboarding_qr_codes |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:pre_hire:write` 读写待入职人员信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `dimension_value_list` | `qr_code_dimension_value\[\]` | 是 | 维度数据<br>**数据校验规则**:<br>- 长度范围: `1` ～ `1000` |
| &nbsp;&nbsp;└ `dimension` | `qr_code_dimension` | 是 | 维度类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `api_name` | `string` | 是 | 维度标识<br>**示例值**："company"<br>**备注**：api_name 可从       [二维码维度列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/pre_hire/onboarding-qr-code/onboarding-qr-code-dimension) 接口获取 |
| &nbsp;&nbsp;└ `value` | `qr_code_value` | 是 | **备注**：select_value、multi_select_value 等值可从 [二维码维度列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/pre_hire/onboarding-qr-code/onboarding-qr-code-dimension) 接口获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `select_value` | `string` | 否 | **示例值**: "7147562782945478177" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `multi_select_value` | `string\[\]` | 否 | **示例值**: ["7147562782945478177","7147562782945478190"]<br>**数据校验规则**:<br>- 长度范围: `1` ～ `1000` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `bool_value` | `boolean` | 否 | **示例值**: false |


### 请求体示例

```json
{
    "dimension_value_list": [
        {
            "dimension": {
                "api_name": "company"
            },
            "value": {
                "select_value": "7147562782945478177"
            }
        },
        {
            "dimension": {
                "api_name": "multi_select_field__c"
            },
            "value": {
                "multi_select_value": ["7147562782945478177","7147562782945478190"]
            }
        },
        {
            "dimension": {
                "api_name": "bool_field__c"
            },
            "value": {
                "bool_value": true
            }
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
| &nbsp;&nbsp;└ `qr_code` | `qr_code` | 二维码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 二维码id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `png` | `string` | 二维码图片链接,文件名区分语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 二维码值链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 有效性 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_by` | `string` | 创建人 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_by` | `string` | 更新人 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `int` | 创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_at` | `int` | 更新时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dimension_value_list` | `qr_code_dimension_value\[\]` | 维度值列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dimension` | `qr_code_dimension` | 维度类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `api_name` | `string` | 维度API name |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_name` | `i18n_v2` | 维度名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | zh-CN |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 维度类型<br>**可选值有**：<br>- `1`: 单选类型 - `2`: 多选类型 - `3`: 布尔类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `qr_code_value` | 维度数据 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `select_value` | `string` | 单选值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `multi_select_value` | `string\[\]` | 多选值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bool_value` | `boolean` | 布尔值 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "qr_code": {
            "id": "6892698621939026184",
  			"png": "https://open.feishu.cn/people/api/onboarding/scan_code/png?scan_code=6q5yxOKMzAsdBmXUZWVqnslLJR0KWy_tNYQnnkhJAVuDvVxMiUMusDJqTk4uDQhL",
  			"url": "https://open.feishu.cn/people/welcome/scan?signKey=6q5yxOKMzAsdBmXUZWVqnslLJR0KWy_tNYQnnkhJAVuDvVxMiUMusDJqTk4uDQhL",
            "active": true,
            "created_by": "7032210902531327521",
            "updated_by": "7032210902531327521",
            "created_at": 1704038400,
            "updated_at": 1704038400,
            "dimension_value_list": [
                {
                    "dimension": {
                        "api_name": "company",
                        "display_name": {
                            "zh_cn": "公司",
                            "en_us": "Company"
                        },
                        "type": 1
                    },
                    "value": {
                        "select_value": "7147562782945478177"
                    }
                },
                {
                    "dimension": {
                        "api_name": "multi_select_field__c",
                        "display_name": {
                            "zh_cn": "多选字段",
                            "en_us": "multi_select_field"
                        },
                        "type": 2
                    },
                    "value": {
                        "multi_select_value": ["7147562782945478177","7147562782945478190"]
                    }
                },
                {
                    "dimension": {
                        "api_name": "bool_field__c",
                        "display_name": {
                            "zh_cn": "布尔字段",
                            "en_us": "bool_field"
                        },
                        "type": 3
                    },
                    "value": {
                        "bool_value": true
                    }
                }
            ]
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1161001 | 参数无效 | 详见返回结果 |
| 400 | 1161002 | 租户未初始化二维码维度 | 初始化二维码维度 |


