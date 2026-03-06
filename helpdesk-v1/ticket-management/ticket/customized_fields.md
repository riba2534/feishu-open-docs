---
title: "获取服务台自定义字段"
fullPath: "/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/ticket/customized_fields"
updateTime: "1692084861000"
---

# 获取服务台自定义字段

该接口用于获取服务台自定义字段详情。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/helpdesk/v1/customized_fields |
| HTTP Method | GET |
| 接口频率限制 | [特殊频控](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `helpdesk:all:readonly` 获取服务台资源详情 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


> **Tip**: 服务台请求Header中还需添加“服务台token”参数：
>   
>   Key: X-Lark-Helpdesk-Authorization
>   
>   Value: base64(helpdesk_id:helpdesk_token)，通过base64加密将helpdesk_id和helpdesk_token用':'连接而成的字符串。
>   
>   [了解更多：获取与使用服务台token](https://open.larkoffice.com/document/ukTMukTMukTM/ugDOyYjL4gjM24CO4IjN)


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `visible_only` | `boolean` | 否 | visible only<br>**示例值**：true |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `user_customized_fields` | `user_customized_field\[\]` | 用户自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_customized_field_id` | `string` | 字段ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 旧字段ID，向后兼容用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `helpdesk_id` | `string` | 服务台ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `key_name` | `string` | 字段键 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `display_name` | `string` | 字段展示名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `position` | `string` | 字段在列表中的展示位置 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `field_type` | `string` | 字段类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 字段描述信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `visible` | `boolean` | 字段是否可见 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `editable` | `boolean` | 字段是否可编辑 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `required` | `boolean` | 字段是否必填 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `string` | 字段创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_at` | `string` | 字段修改时间 |
| &nbsp;&nbsp;└ `ticket_customized_fields` | `ticket_customized_field\[\]` | 自定义工单字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ticket_customized_field_id` | `string` | 工单自定义字段ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `helpdesk_id` | `string` | 服务台ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `key_name` | `string` | 键名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `display_name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `position` | `string` | 字段在列表后台管理列表中的位置 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `field_type` | `string` | 类型<br>string - 单行文本<br>multiline - 多行文本<br>dropdown - 下拉列表<br>dropdown_nested - 级联下拉 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `visible` | `boolean` | 是否可见 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `editable` | `boolean` | 是否可以修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `required` | `boolean` | 是否必填 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `string` | 创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_at` | `string` | 更新时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_by` | `ticket_user` | 创建用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_url` | `string` | 用户头像url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 用户邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `string` | 所在部门名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city` | `string` | 城市 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country` | `string` | 国家代号(CountryCode)，参考：http://www.mamicode.com/info-detail-2186501.html |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_by` | `ticket_user` | 更新用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_url` | `string` | 用户头像url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 用户邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `string` | 所在部门名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city` | `string` | 城市 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country` | `string` | 国家代号(CountryCode)，参考：http://www.mamicode.com/info-detail-2186501.html |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dropdown_allow_multiple` | `boolean` | 是否支持多选，仅在字段类型是dropdown的时候有效 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "user_customized_fields": [
            {
                "user_customized_field_id": "6746384425543548981",
                "id": "6746384425543548981",
                "helpdesk_id": "1542164574896126",
                "key_name": "company_id3",
                "display_name": "Company ID",
                "position": "1",
                "field_type": "string",
                "description": "租户ID",
                "visible": false,
                "editable": false,
                "required": false,
                "created_at": "1574040677000",
                "updated_at": "1574040677000"
            }
        ],
        "ticket_customized_fields": [
            {
                "ticket_customized_field_id": "6834320707288072194",
                "helpdesk_id": "1542164574896126",
                "key_name": "test dropdown",
                "display_name": "test dropdown",
                "position": "3",
                "field_type": "dropdown",
                "description": "下拉示例",
                "visible": true,
                "editable": true,
                "required": false,
                "created_at": "1591239289000",
                "updated_at": "1591239289000",
                "created_by": {
                    "id": "ou_37019b7c830210acd88fdce886e25c71",
                    "avatar_url": "https://xxxx",
                    "name": "abc",
                    "email": "xxxx@abc.com",
                    "department": "用户部门名称(有权限才展示)",
                    "city": "城市",
                    "country": "国家"
                },
                "updated_by": {
                    "id": "ou_37019b7c830210acd88fdce886e25c71",
                    "avatar_url": "https://xxxx",
                    "name": "abc",
                    "email": "xxxx@abc.com",
                    "department": "用户部门名称(有权限才展示)",
                    "city": "城市",
                    "country": "国家"
                },
                "dropdown_allow_multiple": true
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 401 | 154001 | Unauthorized, please check you have the correct access | 检查Authorization 和 X-Lark-Helpdesk-Authorization 是否正确，应用和服务台属于同一租户 |
| 404 | 154004 | Resource not found | 资源不存在，请检查ID值 |
| 500 | 155000 | Internal error | 内部错误，请联系我们 |


