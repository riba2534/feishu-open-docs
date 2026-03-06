---
title: "创建邮箱联系人"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/user_mailbox-mail_contact/create"
updateTime: "1745841670000"
---

# 创建邮箱联系人

创建一个邮箱联系人


> **Tip**: 使用 tenant_access_token 时，需要申请邮箱联系人资源的数据权限。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/user_mailboxes/:user_mailbox_id/mail_contacts |
| HTTP Method | POST |
| 接口频率限制 | [20 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `mail:user_mailbox.mail_contact:write` 查看、创建、更新、删除邮箱联系人 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `mail:user_mailbox.mail_contact.mail_address:read` 读取邮箱联系人邮箱地址字段 `mail:user_mailbox.mail_contact.phone:read` 读取邮箱联系人手机号字段 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `user_mailbox_id` | `string` | 用户邮箱地址，使用 user_access_token 时可使用 me<br>**示例值**："user@xxx.xx 或 me" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | `string` | 是 | 联系人姓名<br>**示例值**："张三"<br>**数据校验规则**：<br>- 长度范围：`1` ～ `64` 字符 |
| `company` | `string` | 否 | 联系人公司<br>**示例值**："张三科技有限公司"<br>**数据校验规则**：<br>- 最大长度：`64` 字符 |
| `phone` | `string` | 否 | 联系人手机号<br>**示例值**："19912341234"<br>**数据校验规则**：<br>- 最大长度：`40` 字符 |
| `mail_address` | `string` | 否 | 联系人邮箱<br>**示例值**："zhangsan@example.com"<br>**数据校验规则**：<br>- 最大长度：`319` 字符 |
| `tag` | `string` | 否 | 联系人标签<br>**示例值**："朋友"<br>**数据校验规则**：<br>- 最大长度：`64` 字符 |
| `remark` | `string` | 否 | 联系人备注<br>**示例值**："飞书发布会认识"<br>**数据校验规则**：<br>- 最大长度：`1000` 字符 |
| `position` | `string` | 否 | 联系人职位<br>**示例值**："CEO"<br>**数据校验规则**：<br>- 最大长度：`64` 字符 |


### 请求体示例

```json
{
    "name": "张三",
    "company": "张三科技有限公司",
    "phone": "19912341234",
    "mail_address": "zhangsan@example.com",
    "tag": "朋友",
    "remark": "飞书发布会认识",
    "position": "CEO"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `mail_contact` | `mail_contact` | 联系人实体 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 联系人 id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 联系人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `company` | `string` | 联系人公司 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `phone` | `string` | 联系人手机号<br>**字段权限要求**： `mail:user_mailbox.mail_contact.phone:read` 读取邮箱联系人手机号字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `mail_address` | `string` | 联系人邮箱<br>**字段权限要求**： `mail:user_mailbox.mail_contact.mail_address:read` 读取邮箱联系人邮箱地址字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tag` | `string` | 联系人标签 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `remark` | `string` | 联系人备注 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `avatar` | `string` | 联系人头像 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `position` | `string` | 联系人职位 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "mail_contact": {
            "id": "7256274576546463764",
            "name": "张三",
            "company": "张三科技有限公司",
            "phone": "19912341234",
            "mail_address": "zhangsan@example.com",
            "tag": "朋友",
            "remark": "飞书发布会认识",
            "avatar": "https://exampeimg.com/xxxx.jpg",
            "position": "CEO"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1230001 | 参数错误 | 修改参数后重试 |
| 500 | 1230003 | 内部错误 | 请稍后重试 |
| 403 | 1230002 | 无权限 | 成为公共邮箱成员或申请相关数据权限后调用该接口 |


