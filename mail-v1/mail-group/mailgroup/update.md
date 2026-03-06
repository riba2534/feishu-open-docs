---
title: "修改邮件组全部信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/mailgroup/update"
updateTime: "1745841705000"
---

# 修改邮件组全部信息

更新邮件组所有信息。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/mailgroups/:mailgroup_id |
| HTTP Method | PUT |
| 接口频率限制 | [100 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `mail:mailgroup` 查询、创建、修改、删除邮件组 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `mailgroup_id` | `string` | 邮件组ID或者邮件组地址<br>**示例值**："xxxxxxxxxxxxxxx 或 test_mail_group@xxx.xx" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `email` | `string` | 否 | 邮件组地址<br>**示例值**："test_mail_group@xxx.xx" |
| `name` | `string` | 否 | 邮件组名称<br>**示例值**："test mail group" |
| `description` | `string` | 否 | 邮件组描述<br>**示例值**："mail group for testing" |
| `who_can_send_mail` | `string` | 否 | 谁可发送邮件到此邮件组<br>**示例值**："ALL_INTERNAL_USERS"<br>**可选值有**：<br>- `ANYONE`: 任何人 - `ALL_INTERNAL_USERS`: 仅组织内部成员 - `ALL_GROUP_MEMBERS`: 仅邮件组成员 - `CUSTOM_MEMBERS`: 自定义成员 |


### 请求体示例

```json
{ 
   "email": "xxx@xxx.com",
    "name": "xxx",
    "description": "xxx",
    "who_can_send_mail": "ANYONE"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `mailgroup` | \- |
| &nbsp;&nbsp;└ `mailgroup_id` | `string` | 邮件组ID |
| &nbsp;&nbsp;└ `email` | `string` | 邮件组地址 |
| &nbsp;&nbsp;└ `name` | `string` | 邮件组名称 |
| &nbsp;&nbsp;└ `description` | `string` | 邮件组描述 |
| &nbsp;&nbsp;└ `direct_members_count` | `string` | 邮件组成员数量 |
| &nbsp;&nbsp;└ `include_external_member` | `boolean` | 是否包含外部成员 |
| &nbsp;&nbsp;└ `include_all_company_member` | `boolean` | 是否是全员邮件组 |
| &nbsp;&nbsp;└ `who_can_send_mail` | `string` | 谁可发送邮件到此邮件组<br>**可选值有**：<br>- `ANYONE`: 任何人 - `ALL_INTERNAL_USERS`: 仅组织内部成员 - `ALL_GROUP_MEMBERS`: 仅邮件组成员 - `CUSTOM_MEMBERS`: 自定义成员 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "mailgroup_id": "xxx",
        "email": "xx@xx.xx",
        "name":"xxx",
        "description":"xxx",
        "direct_members_count":"x",
        "include_external_member": true,
        "include_all_company_member":false,
        "who_can_send_mail":"ANYONE"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 404 | 1234013 | mail group not found | 请确认邮件组是否存在 |
| 400 | 1234008 | request parameter error | 请检查请求参数是否正确 |
| 409 | 1234033 | email address has been used by another member as login account | 邮件地址已被他人用作于登录邮箱，请使用其它邮件地址 |
| 409 | 1234006 | email address has been used | 邮件地址已被占用，请使用其它邮件地址 |
| 409 | 1234023 | email address alias exceed the number limit | 超出了邮箱别名限制 |
| 400 | 1234030 | mailing group count is over max limit | 邮件组成员已达上限，请删除后重新尝试 |


