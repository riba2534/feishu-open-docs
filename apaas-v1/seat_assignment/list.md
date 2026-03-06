---
title: "查询席位分配详情"
fullPath: "/uAjLw4CM/ukTMukTMukTM/apaas-v1/seat_assignment/list"
updateTime: "1752136615000"
---

# 查询席位分配详情

获取租户下平台席位和应用访问席位分配详情，如用户 ID 、应用命名空间等，需要飞书 aPaaS 系统管理员作为授权人调用当前 API 。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/apaas/v1/seat_assignments |
| HTTP Method | GET |
| 接口频率限制 | [1 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `app_engine:seat_assignments:read` 查询席位分配详情 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `seat_type` | `string` | 是 | 席位类型，枚举值：per_user、per_user_per_app<br>**示例值**：per_user<br>**可选值有**：<br>- `per_user`: 平台席位 - `per_user_per_app`: 应用访问席位 |
| `page_size` | `string` | 是 | 分页大小，范围：【0，500】<br>**示例值**：10 |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `seat_assignment\[\]` | 席位分配情况列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `int` | aPaaS 产品用户的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `namespace` | `string` | aPaaS 产品应用的 namespace |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `string` | 席位状态，枚举值：in_use 、released<br>**可选值有**：<br>- `in_use`: 席位生效中 - `released`: 席位已释放 |
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
                "user_id": 1803710089388154,
                "namespace": "package_35f605__c",
                "status": "in_use"
            }
        ],
        "page_token": "eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 404 | 2320003 | tenant does not exist | 请自查租户是否可用 |
| 404 | 2320004 | user does not exist | 请自查用户是否存在 |
| 403 | 2320005 | insufficient permissions | 请自查用户是否具备权限 |
| 400 | 2320006 | bad request or invalid parameter | 请自查请求方法、请求信息、请求数据格式等是正确的 |


