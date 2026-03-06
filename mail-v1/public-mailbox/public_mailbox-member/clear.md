---
title: "删除公共邮箱所有成员"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/public_mailbox-member/clear"
updateTime: "1745841720000"
---

# 删除公共邮箱所有成员

删除公共邮箱所有成员。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/public_mailboxes/:public_mailbox_id/members/clear |
| HTTP Method | POST |
| 接口频率限制 | [特殊频控](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `mail:public_mailbox` 查询、创建、修改公共邮箱 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `public_mailbox_id` | `string` | 公共邮箱唯一标识或公共邮箱地址<br>**示例值**："xxxxxxxxxxxxxxx 或 test_public_mailbox@xxx.xx" |


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
| 404 | 1234016 | public mailbox not found | 请确认公共邮箱是否存在 |


