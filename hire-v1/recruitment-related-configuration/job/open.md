---
title: "重启职位"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/open"
updateTime: "1725008224000"
---

# 重启职位

对于已关闭的职位，可通过本接口重启职位。


> **Tip**: 在调用本接口前，须在「飞书招聘」-「设置」-「职位管理」-「职位设置」中开启「通过 API 同步职位」开关，否则将只能在招聘系统内重启职位。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/jobs/:job_id/open |
| HTTP Method | POST |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:job` 更新职位信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `job_id` | `string` | 职位 ID，可通过[获取职位列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/list)获取<br>**示例值**："6960663240925956555" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `expiry_time` | `int` | 否 | 到期日期，毫秒时间戳（int64类型） **注意**：当`is_never_expired`为`false`时该字段必填且大于当前时间<br>**示例值**：1830259120000 |
| `is_never_expired` | `boolean` | 是 | 是否长期有效 **可选值有**： * `true`：长期有效 * `false`：指定到期日期<br>**示例值**：true |


### 请求体示例

```json
{
    "expiry_time": 1830259120000,
    "is_never_expired": true
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
    "msg": "ok",
    "data": {}
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位问题或联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确 |
| 400 | 1002601 | 职位不存在 | 请检查职位 ID 参数 |
| 400 | 1002613 | 未开启「通过 API 同步职位」 | 请在「飞书招聘」-「设置」-「职位管理」-「职位设置」中开启「通过 API 同步职位」开关 |
| 400 | 1002616 | 职位已经被重启 | 请检查职位 ID 参数 |


