---
title: "更新实习 Offer 入/离职状态"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer/intern_offer_status"
updateTime: "1720669861000"
---

# 更新实习 Offer 入/离职状态

对「实习待入职」状态的实习 Offer 确认入职、放弃入职，或对「实习已入职」状态的实习 Offer 操作离职。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/offers/:offer_id/intern_offer_status |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:offer` 更新 offer 信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `offer_id` | `string` | Offer ID，如何获取请参考[获取 Offer 列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer/list)<br>**示例值**："7016605170635213100" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `operation` | `string` | 是 | 更新入/离职状态的操作<br>**示例值**："confirm_onboarding"<br>**可选值有**：<br>- `confirm_onboarding`: 确认入职 - `cancel_onboarding`: 放弃入职 - `offboard`: 操作离职 |
| `onboarding_info` | `intern_offer_onboarding_info` | 否 | 入职表单信息<br>**注意**：当 operation 为 `confirm_onboarding` 时，该字段必填 |
| &nbsp;&nbsp;└ `actual_onboarding_date` | `string` | 是 | 实际入职日期<br>**值格式**："YYYY-MM-DD"<br>**示例值**："2022-01-01" |
| `offboarding_info` | `intern_offer_offboarding_info` | 否 | 离职表单信息<br>**注意**：当 operation 为 `offboard` 时，该字段必填 |
| &nbsp;&nbsp;└ `actual_offboarding_date` | `string` | 是 | 实际离职日期<br>**注意**：实际离职日期需晚于实际入职日期<br>**值格式**："YYYY-MM-DD"<br>**示例值**："2022-03-02" |
| &nbsp;&nbsp;└ `notes` | `string` | 否 | 备注<br>**示例值**："主动离职" |


### 请求体示例

```json
{
    "operation": "confirm_onboarding",
    "onboarding_info": {
        "actual_onboarding_date": "2022-01-01"
    },
    "offboarding_info": {
        "actual_offboarding_date": "2022-03-02",
        "notes": "主动离职"
    }
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `intern_offer_status` | \- |
| &nbsp;&nbsp;└ `offer_id` | `string` | Offer ID，详细信息请参考[获取 Offer 信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/offer) |
| &nbsp;&nbsp;└ `operation` | `string` | 更新入/离职状态的操作<br>**可选值有**：<br>- `confirm_onboarding`: 确认入职 - `cancel_onboarding`: 放弃入职 - `offboard`: 操作离职 |
| &nbsp;&nbsp;└ `onboarding_info` | `intern_offer_onboarding_info` | 入职表单信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `actual_onboarding_date` | `string` | 实际入职日期<br>**值格式**："YYYY-MM-DD" |
| &nbsp;&nbsp;└ `offboarding_info` | `intern_offer_offboarding_info` | 离职表单信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `actual_offboarding_date` | `string` | 实际离职日期<br>**值格式**："YYYY-MM-DD" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `notes` | `string` | 备注 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "offer_id": "6949805467799537964",
        "operation": "confirm_onboarding",
        "onboarding_info": {
            "actual_onboarding_date": "2022-01-01"
        },
        "offboarding_info": {
            "actual_offboarding_date": "2022-03-02",
            "notes": "主动离职"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |
| 500 | 1002067 | 实习待入职状态错误 | 检查该实习 Offer 的待入职状态是否支持该操作 |
| 500 | 1002068 | 实习入职状态错误 | 检查该实习 Offer 的入职状态是否支持该操作 |


