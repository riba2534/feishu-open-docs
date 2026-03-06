---
title: "更新人才在职状态"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/onboard_status"
updateTime: "1749037826000"
---

# 更新人才在职状态

更新人才的在职状态，可进行的操作包括入职与离职。


## 注意事项
- 进行入职、离职操作后，「飞书招聘」- 「人才库」-「人才详情页」等场景会相应展示已入职、已离职标签

- 已入职的人才不能进行入职操作，已离职的人才不能进行入职操作。已离职的人才若需入职，需走正常的招聘流程

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/talents/:talent_id/onboard_status |
| HTTP Method | POST |
| 接口频率限制 | [20 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:talent` 更新人才信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `talent_id` | `string` | 人才ID，可通过[获取人才列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/list)接口获取<br>**示例值**："6960663240925956661" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `operation` | `int` | 是 | 操作类型<br>**示例值**：1<br>**可选值有**：<br>- `1`: 入职 - `2`: 离职 |
| `onboard_time` | `string` | 否 | 入职时间，毫秒时间戳；当操作类型为入职的时候时必填<br>**示例值**："1676548784889" |
| `overboard_time` | `string` | 否 | 离职时间，毫秒时间戳；当操作类型为离职的时候时必填<br>**示例值**："1676548784890" |


### 请求体示例

```json
{
    "operation": 1,
    "onboard_time": "1676548784889",
    "overboard_time": "1676548784890"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |


### 响应体示例

```json
{
    "code": 0,
    "msg": "SUCCESS",
    "data": {}
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 请检查参数是否正确，例如类型、大小 |


