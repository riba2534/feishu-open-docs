---
title: "获取邮箱文件信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/mail-v1/user_mailbox-folder/get"
updateTime: "1776073368000"
---

# 获取邮箱文件夹信息

通过指定文件夹ID，获取文件夹信息，包括名称、类型等


> **Tip**: 使用应用身份访问时，需要申请邮箱文件夹资源的数据权限。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/mail/v1/user_mailboxes/:user_mailbox_id/folders/:folder_id |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `mail:user_mailbox.folder:read` 查询邮箱文件夹 `mail:user_mailbox.folder:write` 查看、创建、更新、删除邮箱文件夹 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `user_mailbox_id` | `string` | 用户邮箱地址。当使用用户身份访问时，可以输入"me"代表当前调用接口用户。<br>**示例值**："user@xxx.xx 或 me" |
| `folder_id` | `string` | 邮件文件夹唯一标识。可通过「获取邮箱文件夹列表」接口获取目标文件夹的 ID；若未传入该参数，默认返回根文件夹（收件箱）详情。<br>**示例值**："7620095646711680541" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `folder` | `folder` | 邮件文件夹的完整信息，包含文件夹ID、名称、归属层级、类型及未读统计数据。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | folder id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 文件夹名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `parent_folder_id` | `string` | 父文件夹 id，该值为 0 表示根文件夹 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `folder_type` | `int` | 文件夹类型<br>**可选值有**：<br>- `1`: 系统文件夹 - `2`: 用户文件夹 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `unread_message_count` | `int` | 未读邮件数量 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `unread_thread_count` | `int` | 未读会话数量 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "folder": {
            "id": "7620095646711680541",
            "name": "newsletter 相关",
            "parent_folder_id": "725627422334644",
            "folder_type": 1,
            "unread_message_count": 3,
            "unread_thread_count": 4
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1230001 | invalid param | 参数错误，请检查请求参数的类型、格式或值是否与接口要求一致，具体可参考接口文档中的参数说明 |
| 500 | 1230003 | internal server error | 内部服务错误，请重试 |
| 403 | 1230002 | permission denied | 无权限访问，请确认应用是否具备访问该资源的权限。如使用用户身份访问，请确认具备此用户的访问权限；如使用租户身份访问，请确认已申请对应的数据范围权限。 |


