---
title: "删除成本中心"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/delete"
updateTime: "1732259877000"
---

# 删除成本中心

删除成本中心记录


> **Tip**: 删除对象时请确认有无在职员工、异动单据、待入职单据关联此对象，如有会导致删除失败。


> **Error**: 删除后无法恢复， 并且在系统中无法搜索到对应成本中心信息，请谨慎操作。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/cost_centers/:cost_center_id |
| HTTP Method | DELETE |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:cost_center:write` 创建、更新、删除成本中心信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `cost_center_id` | `string` | 成本ID。ID获取方式： - 调用[【创建成本中心】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/create)[【搜索成本中心】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)等接口可以返回成本中心ID<br>**示例值**："6862995757234914824" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `operation_reason` | `string` | 是 | 操作原因<br>**示例值**："随着组织架构调整，该成本中心不再使用" |


### 请求体示例

```json
{
    "operation_reason": "随着组织架构调整，该成本中心不再使用"
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
| 400 | 1160408 | Unable to delete | 所有被引用过的成本中心都不可被删除 |


