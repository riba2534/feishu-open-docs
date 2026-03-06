---
title: "设备绑定权限组"
fullPath: "/uAjLw4CM/ukTMukTMukTM/acs-v1/rule_external/device_bind"
updateTime: "1704791422000"
---

# 设备绑定权限组

设备绑定权限组


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/acs/v1/rule_external/device_bind |
| HTTP Method | POST |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `acs:device:write` 门禁机设备写入权限 `acs:users` 查看、更新智能门禁用户 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `device_id` | `string` | 是 | 设备id<br>**示例值**："6939433228970082593" |
| `rule_ids` | `string\[\]` | 是 | 权限组id列表<br>**示例值**：["7298933941867135276"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `10000` |


### 请求体示例

```json
{
    "device_id": "6939433228970082593",
    "rule_ids": [
        "7298933941867135276"
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
| 400 | 1490030 | device does not exist | 请检查设备id,该id不存在 |
| 400 | 1490090 | rule id is invalid | 请检查权限组id,该id不存在 |


