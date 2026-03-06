---
title: "查询用户或部门是否在应用的可用或禁用名单"
fullPath: "/uAjLw4CM/ukTMukTMukTM/application-v6/application-visibility/check_white_black_list"
updateTime: "1689924100000"
---

# 查询用户或部门是否在应用的可用或禁用名单

该接口用于查询用户、部门、用户组是否在应用的可用或禁用名单中


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/application/v6/applications/:app_id/visibility/check_white_black_list |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `application:application:self_manage` 管理应用自身资源 `admin:app.info:readonly` 获取应用信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_id` | `string` | 应用的 AppID，可以在[开发者后台](https://open.feishu.cn/app) > **凭证与基础信息**页查看。 * 仅查询本应用信息时，可填应用自身AppID。<br>* 当值为其他应用的App ID时，必须申请以下权限：`admin:app.info:readonly` 获取应用信息<br>**示例值**："cli_a3axxx01b" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：user_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 部门ID类型<br>**示例值**：department_id<br>**可选值有**：<br>- `department_id`: 以自定义department_id来标识部门 - `open_department_id`: 以open_department_id来标识部门<br>**默认值**：`department_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_ids` | `string\[\]` | 否 | 想要查询的用户id列表，按照user_id_type录入，最多录入100个。<br>可以调用[获取部门直属用户列表](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/find_by_department)接口获取。<br>**示例值**：["ou_d317f090b7258ad0372aa53963cda70d"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `department_ids` | `string\[\]` | 否 | 想要查询的部门的 id 列表，最多录入100个。<br>可以[调用获取子部门列表](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/children)接口获取。<br>**示例值**：["od-aa2c50a04769feefededb7a05b7525a8"]<br>**数据校验规则**：<br>- 最大长度：`100` |
| `group_ids` | `string\[\]` | 否 | 想要查询的用户组id列表，最多录入100个。<br>可以调用[查询用户组列表](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group/simplelist)接口获取。<br>**示例值**：["96815a9cd9beg8g4"]<br>**数据校验规则**：<br>- 最大长度：`100` |


### 请求体示例

```json
{
    "user_ids": [
        "ou_d317f090b7258ad0372aa53963cda70d"
    ],
    "department_ids": [
        "od-aa2c50a04769feefededb7a05b7525a8"
    ],
    "group_ids": [
        "96815a9cd9beg8g4"
    ]
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `user_visibility_list` | `application.visibility.user_white_black_info\[\]` | 查询的用户可见性结果列表，如果用户在白名单或付费白名单，且不在黑名单中，则可见该应用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 查询的用户ID，ID类型和user_id_type传参类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `in_white_list` | `boolean` | 是否在白名单。<br>**可选值**： - **true**：在白名单 - **false**：不在白名单 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `in_black_list` | `boolean` | 是否在黑名单。<br>**可选值**： - **true**：在黑名单 - **false**：不在黑名单 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `in_paid_list` | `boolean` | 是否在付费名单。<br>**可选值**： - **true**：在付费名单 - **false**：不在付费名单 |
| &nbsp;&nbsp;└ `department_visibility_list` | `application.visibility.department_white_black_info\[\]` | 查询的部门可见性结果列表，如果部门在白名单，且不在黑名单，则该部门下的用户可见该应用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 查询的部门ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `in_white_list` | `boolean` | 是否在白名单。<br>**可选值**： - **true**：在白名单 - **false**：不在白名单 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `in_black_list` | `boolean` | 是否在黑名单。<br>**可选值**： - **true**：在黑名单 - **false**：不在黑名单 |
| &nbsp;&nbsp;└ `group_visibility_list` | `application.visibility.group_white_black_info\[\]` | 查询的用户组可见性结果列表，如果用户组在白名单，且不在黑名单，则该用户组下的用户可见该应用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `group_id` | `string` | 查询的用户组ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `in_white_list` | `boolean` | 是否在白名单。<br>**可选值**： - **true**：在白名单 - **false**：不在白名单 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `in_black_list` | `boolean` | 是否在黑名单。<br>**可选值**： - **true**：在黑名单 - **false**：不在黑名单 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "user_visibility_list": [
            {
                "user_id": "ou_d317f090b7258ad0372aa53963cda70d",
                "in_white_list": false,
                "in_black_list": false,
                "in_paid_list": false
            }
        ],
        "department_visibility_list": [
            {
                "department_id": "od-aa2c50a04769feefededb7a05b7525a8",
                "in_white_list": false,
                "in_black_list": false
            }
        ],
        "group_visibility_list": [
            {
                "group_id": "96815a9cd9beg8g4",
                "in_white_list": false,
                "in_black_list": false
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 210001 | param is invalid | 检查参数 |


