---
title: "更新标签"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/user_mailbox-label/patch"
updateTime: "1776073242000"
---

# 更新标签

更新用户指定标签的名字、颜色等信息


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/user_mailboxes/:user_mailbox_id/labels/:label_id |
| HTTP Method | PATCH |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `mail:user_mailbox.message:modify` 修改邮件 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `user_mailbox_id` | `string` | 用户邮箱地址。当使用用户身份访问时，可以输入"me"代表当前调用接口用户<br>**示例值**："user@xxx.xx 或 me" |
| `label_id` | `string` | 标签ID，创建标签成功后返回的标签ID，或可通过列出标签、获取邮件详情等接口获得<br>**示例值**："7620003644728938013" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `label` | `label` | 是 | 邮件标签，必须填写名字或颜色中的至少一个字段 |
| &nbsp;&nbsp;└ `name` | `string` | 否 | 标签名称，可选填写。最长255个字符。<br>**示例值**："test"<br>**数据校验规则**：<br>- 长度范围：`1` ～ `255` 字符 |
| &nbsp;&nbsp;└ `background_color` | `string` | 否 | 标签背景颜色，可选填写。支持以下颜色值：blue、indigo、purple、violet、carmine、red、orange、yellow、lime、green、turquoise、wathet<br>**示例值**："blue" |


### 请求体示例

```json
{
    "label": {
        "name": "test",
        "background_color": "blue"
    }
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `label` | `label` | 标签 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 标签ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 标签名称，最长 255 个字符。支持嵌套标签，嵌套层级之间以 / 分隔（如 a/b/c 表示三级嵌套标签）。创建或更新嵌套标签时，需要传入完整路径（如 a/b/c），不能只传最后一级名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `background_color` | `string` | 标签背景颜色，支持以下颜色值：blue、indigo、purple、violet、carmine、red、orange、yellow、lime、green、turquoise、wathet |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `messages_unread` | `int` | 带有该标签的未读邮件数量 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "label": {
            "id": "7620003644728938013",
            "name": "test",
            "background_color": "blue",
            "messages_unread": 0
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1234000 | invalid params | 不合法的参数，请参考文档修改参数 |
| 500 | 1234017 | internal error | 服务器内部错误，请稍后重试 |
| 403 | 1234030 | permission deny | 无权限访问，请检查是否已经申请对应权限 |
| 400 | 1234013 | user mailbox not found or user mailbox not active | 指定的邮箱地址不存在或邮箱地址状态不正常，请检查输入的邮箱地址 |
| 400 | 1230100 | label not found | 指定的标签不存在，请检查输入的标签 |
| 400 | 1230101 | label name already exists | 指定的标签名已经存在，无法重复创建，请更换标签名字 |
| 400 | 1230103 | label name is reserved by system | 自定义标签无法使用系统内置的标签名，请更换标签名字 |


