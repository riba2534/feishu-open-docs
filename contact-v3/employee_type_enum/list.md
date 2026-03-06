---
title: "查询人员类型"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list"
updateTime: "1720166960000"
---

# 查询人员类型

调用该接口查询当前租户下所有的人员类型信息，包括选项 ID、类型、编号以及内容等。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/contact/v3/employee_type_enums |
| HTTP Method | GET |
| 接口频率限制 | [特殊频控](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：3 |
| `page_size` | `int` | 否 | 分页大小，用于限制一次请求返回的条目数。<br>**示例值**：10<br>**默认值**：`20`<br>**数据校验规则**：<br>- 最大值：`100` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `employee_type_enum\[\]` | 人员类型的选项信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `enum_id` | `string` | 选项 ID。后续可以使用该 ID 更新、删除选项。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `enum_value` | `string` | 选项的编号值。后续可使用该编号配置用户的人员类型属性。例如，调用[创建用户](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/create)接口时，employee_type 参数值对应的就是当前的 enum_value。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 选项内容。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `enum_type` | `int` | 选项类型。<br>**可选值有**：<br>- `1`: 内置类型 - `2`: 自定义 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `enum_status` | `int` | 选项的激活状态。<br>**可选值有**：<br>- `1`: 激活 - `2`: 未激活 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_content` | `i18n_content\[\]` | 选项内容的国际化配置。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语言版本。例如：<br>- zh_cn：中文 - en_us：英文 - ja_jp：日文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语言版本对应的内容。 |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "enum_id": "exGeIjow7zIqWMy+ONkFxA==",
                "enum_value": "2",
                "content": "专家",
                "enum_type": 2,
                "enum_status": 1,
                "i18n_content": [
                    {
                        "locale": "zh_cn",
                        "value": "专家（中文）"
                    }
                ]
            }
        ],
        "has_more": true,
        "page_token": "3"
    }
}
```


更多错误码信息，参见[通用错误码](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)。


