---
title: "取消候选人入职"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/cancel_onboard"
updateTime: "1740018694000"
---

# 取消候选人入职

取消待入职状态的候选人入职。


## 注意事项

- 本接口适用于对待入职阶段的候选人取消入职。对于已入职的候选人，取消入职请使用[更新入职状态](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/employee/patch)
对候选人进行离职操作。

- 对于集成了飞书人事的租户，候选人在飞书人事创建待入职记录后，只能在飞书人事取消入职，不可使用本接口取消入职。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/applications/:application_id/cancel_onboard |
| HTTP Method | POST |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:application` 更新投递信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `application_id` | `string` | 投递 ID，如何获取投递 ID 请参考[获取投递列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/list)<br>**示例值**："1111111111" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `termination_type` | `int` | 是 | 终止类型<br>**示例值**：1<br>**可选值有**：<br>- `1`: 我们拒绝了候选人 - `22`: 候选人拒绝了我们 - `27`: 其他 |
| `termination_reason_id_list` | `string\[\]` | 否 | 终止的具体原因的id列表，详细信息请参考[获取终止投递原因](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/termination_reason/list)<br>**示例值**：["6959090661225640000"] |
| `termination_reason_notes` | `string` | 否 | 备注<br>**示例值**："候选人经历不匹配" |


### 请求体示例

```json
{
    "termination_type": 1,
    "termination_reason_id_list": [
        "6959090661225640000"
    ],
    "termination_reason_notes": "候选人经历不匹配"
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
    "msg": "success",
    "data": {}
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |
| 400 | 1002221 | 投递已经终止 | 请检查投递状态，可通过[获取投递信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/get)接口排查 |
| 400 | 1002910 | 候选人已在飞书人事创建待入职记录 | 请在飞书人事取消入职 |


