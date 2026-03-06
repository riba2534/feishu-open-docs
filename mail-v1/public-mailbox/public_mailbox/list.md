---
title: "查询所有公共邮箱"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/public_mailbox/list"
updateTime: "1745841708000"
---

# 查询所有公共邮箱

分页批量获取公共邮箱列表。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/public_mailboxes |
| HTTP Method | GET |
| 接口频率限制 | [特殊频控](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `mail:public_mailbox` 查询、创建、修改公共邮箱 `mail:public_mailbox:readonly` 查询公共邮箱 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID `mail:public_mailbox.public_mailbox_geo` 查看公共邮箱数据驻留地 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：xxx |
| `page_size` | `int` | 否 | 分页大小<br>**示例值**：10<br>**默认值**：`20`<br>**数据校验规则**：<br>- 最大值：`200` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `items` | `public_mailbox\[\]` | 公共邮箱列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `public_mailbox_id` | `string` | 公共邮箱唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 公共邮箱地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 公共邮箱名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `geo` | `string` | 数据驻留地<br>**字段权限要求**： `mail:public_mailbox.public_mailbox_geo` 查看公共邮箱数据驻留地 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "has_more": true,
        "page_token": "xxx",
        "items": [
            {
                "public_mailbox_id": "xxxxxxxxxxxxxxx",
                "email": "test_public_mailbox@xxx.xx",
                "name": "test public mailbox",
                "geo": "cn"
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 503 | 1235003 | Service unavailable | 请稍后重试 |


