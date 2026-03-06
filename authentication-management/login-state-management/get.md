---
title: "获取用户信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/authen-v1/user_info/get"
updateTime: "1753149455000"
---

# 获取用户信息

通过 `user_access_token` 获取相关用户信息。


> **Warning**: 手机号和邮箱信息为管理员导入的用户联系方式，未经过用户本人实时验证，不建议开发者直接将其作为业务系统的登录凭证。如使用，务必自行认证。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/authen/v1/user_info |
| HTTP Method | GET |
| 接口频率限制 | [特殊频控](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | 无 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee:readonly` 获取用户受雇信息 `contact:user.employee_id:readonly` 获取用户 user ID `contact:user.phone:readonly` 获取用户手机号 `contact:user.email:readonly` 获取用户邮箱信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `user_info` | \- |
| &nbsp;&nbsp;└ `name` | `string` | 用户姓名 |
| &nbsp;&nbsp;└ `en_name` | `string` | 用户英文名称 |
| &nbsp;&nbsp;└ `avatar_url` | `string` | 用户头像 |
| &nbsp;&nbsp;└ `avatar_thumb` | `string` | 用户头像 72x72 |
| &nbsp;&nbsp;└ `avatar_middle` | `string` | 用户头像 240x240 |
| &nbsp;&nbsp;└ `avatar_big` | `string` | 用户头像 640x640 |
| &nbsp;&nbsp;└ `open_id` | `string` | 用户在应用内的唯一标识 |
| &nbsp;&nbsp;└ `union_id` | `string` | 用户对ISV的唯一标识，对于同一个ISV，用户在其名下所有应用的union_id相同 |
| &nbsp;&nbsp;└ `email` | `string` | 用户邮箱。邮箱信息为管理员导入的用户联系方式，未经过用户本人实时验证，不建议开发者直接将其作为业务系统的登录凭证。如使用，务必自行认证。<br>**字段权限要求**： `contact:user.email:readonly` 获取用户邮箱信息 |
| &nbsp;&nbsp;└ `enterprise_email` | `string` | 企业邮箱，请先确保已在管理后台启用飞书邮箱服务<br>**字段权限要求**： `contact:user.employee:readonly` 获取用户受雇信息 |
| &nbsp;&nbsp;└ `user_id` | `string` | 用户 user_id<br>**字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| &nbsp;&nbsp;└ `mobile` | `string` | 用户手机号。手机号信息为管理员导入的用户联系方式，未经过用户本人实时验证，不建议开发者直接将其作为业务系统的登录凭证。如使用，务必自行认证。<br>**字段权限要求**： `contact:user.phone:readonly` 获取用户手机号 |
| &nbsp;&nbsp;└ `tenant_key` | `string` | 当前企业标识 |
| &nbsp;&nbsp;└ `employee_no` | `string` | 用户工号<br>**字段权限要求（满足任一）**： `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "name": "zhangsan",
        "en_name": "zhangsan",
        "avatar_url": "www.feishu.cn/avatar/icon",
        "avatar_thumb": "www.feishu.cn/avatar/icon_thumb",
        "avatar_middle": "www.feishu.cn/avatar/icon_middle",
        "avatar_big": "www.feishu.cn/avatar/icon_big",
        "open_id": "ou-caecc734c2e3328a62489fe0648c4b98779515d3",
        "union_id": "on-d89jhsdhjsajkda7828enjdj328ydhhw3u43yjhdj",
        "email": "zhangsan@feishu.cn",
        "enterprise_email": "demo@mail.com",
        "user_id": "5d9bdxxx",
        "mobile": "+86130002883xx",
        "tenant_key": "736588c92lxf175d",
		"employee_no": "111222333"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 200 | 20001 | Invalid request. Please check request param | 参数错误，请检查请求参数。 |
| 200 | 20005 | The user access token passed is invalid. Please check the value | 提供的 `user_access_token` 无效，请使用有效的 `user_access_token`。相关文档：[获取 user_access_token](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/authentication-management/access-token/get-user-access-token)。 |
| 200 | 20008 | User not exist | 用户不存在，无法获取信息。 |
| 200 | 20021 | User resigned | 用户离职，无法获取信息。 |
| 200 | 20022 | User frozen | 用户被冻结，无法获取信息。 |
| 200 | 20023 | User not registered | 用户没有完成注册，无法获取信息。 |
| 500 | 20050 | System error | 系统错误，请重试。 |


