---
title: "创建授予名单"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/admin-v1/badge-grant/create"
updateTime: "1684228044000"
---

# 创建授予名单

通过该接口可以为特定勋章创建一份授予名单，一枚勋章下最多可创建1000份授予名单。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/admin/v1/badges/:badge_id/grants |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `admin:badge.grant` 查看、创建、编辑、删除勋章授予名单 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `badge_id` | `string` | 勋章ID<br>**示例值**："m_DjMzaK"<br>**数据校验规则**：<br>- 长度范围：`1` ～ `64` 字符 |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**："open_id"<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 此次调用中使用的部门ID的类型。<br>**示例值**："open_department_id"<br>**可选值有**：<br>- `department_id`: 以自定义department_id来标识部门 - `open_department_id`: 以open_department_id来标识部门<br>**默认值**：`open_department_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | `string` | 是 | 勋章下唯一的授予事项，最多100个字符。<br>**示例值**："激励勋章的授予名单" |
| `grant_type` | `int` | 是 | 授予名单类型<br>**示例值**：0<br>**可选值有**：<br>- `0`: 手动选择有效期 - `1`: 匹配系统入职时间<br>**默认值**：`0`<br>**数据校验规则**：<br>- 取值范围：`0` ～ `1` |
| `time_zone` | `string` | 是 | 授予名单的生效时间对应的时区，用于检查RuleDetail的时间戳的取值是否规范，取值范围为TZ database name<br>**示例值**："Asia/Shanghai"<br>**数据校验规则**：<br>- 最小长度：`1` 字符 |
| `rule_detail` | `rule_detail` | 是 | 规则详情 |
| &nbsp;&nbsp;└ `effective_time` | `string` | 否 | 开始生效的时间戳。1.手动设置有效期类型勋章，配置有效期限需要配置该字段；2.时间戳必须是所在时区当天的零点时间戳，如时区为Asia/Shanghai时区时的1649606400<br>**示例值**："1649606400" |
| &nbsp;&nbsp;└ `expiration_time` | `string` | 否 | 结束生效的时间戳。1.手动设置有效期类型勋章，配置有效期限需要配置该字段；2.最大值：不得超过effective_time+100 年；3.非永久有效：时间戳必须是所在时区当天的23:59:59时间戳，如时区为Asia/Shanghai时区时的1649692799；4.永久有效：传值为0即可<br>**示例值**："1649692799" |
| &nbsp;&nbsp;└ `anniversary` | `int` | 否 | 入职周年日。根据入职时间发放类型勋章，需要配置该字段。<br>**示例值**：1<br>**默认值**：`1`<br>**数据校验规则**：<br>- 取值范围：`1` ～ `60` |
| &nbsp;&nbsp;└ `effective_period` | `int` | 否 | 有效期限。根据入职时间发放类型勋章，需要配置该字段。<br>**示例值**：1<br>**可选值有**：<br>- `1`: 有效期为一年 - `2`: 永久有效<br>**默认值**：`1`<br>**数据校验规则**：<br>- 取值范围：`1` ～ `2` |
| `is_grant_all` | `boolean` | 是 | 是否授予给全员。1.为false时，需要关联1~500个用户群体。2.为true时，不可关联用户、用户组、部门。<br>**示例值**：false<br>**默认值**：`false` |
| `user_ids` | `string\[\]` | 否 | 授予的用户ID列表，授予名单列表接口返回结果中不返回该字段，只在详情接口返回<br>**示例值**：["u273y71"] |
| `department_ids` | `string\[\]` | 否 | 授予的部门ID列表，授予名单列表接口返回结果中不返回该字段，只在详情接口返回<br>**示例值**：["h121921"] |
| `group_ids` | `string\[\]` | 否 | 授予的用户组ID列表，授予名单列表接口返回结果中不返回该字段，只在详情接口返回<br>**示例值**：["g122817"] |


### 请求体示例

```json
{
    "name": "激励勋章的授予名单",
    "grant_type": 0,
    "time_zone": "Asia/Shanghai",
    "rule_detail": {
        "effective_time": "1649606400",
        "expiration_time": "1649692799",
        "anniversary": 1,
        "effective_period": 1
    },
    "is_grant_all": false,
    "user_ids": [
        "u273y71"
    ],
    "department_ids": [
        "h121921"
    ],
    "group_ids": [
        "g122817"
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
| &nbsp;&nbsp;└ `grant` | `grant` | 授予名单的信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 租户内授予名单的唯一标识，该值由系统随机生成。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `badge_id` | `string` | 企业勋章的唯一ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 勋章下唯一的授予事项，最多100个字符。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `grant_type` | `int` | 授予名单类型<br>**可选值有**：<br>- `0`: 手动选择有效期 - `1`: 匹配系统入职时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `time_zone` | `string` | 授予名单的生效时间对应的时区，用于检查RuleDetail的时间戳的取值是否规范，取值范围为TZ database name |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `rule_detail` | `rule_detail` | 规则详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 开始生效的时间戳。1.手动设置有效期类型勋章，配置有效期限需要配置该字段；2.时间戳必须是所在时区当天的零点时间戳，如时区为Asia/Shanghai时区时的1649606400 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expiration_time` | `string` | 结束生效的时间戳。1.手动设置有效期类型勋章，配置有效期限需要配置该字段；2.最大值：不得超过effective_time+100 年；3.非永久有效：时间戳必须是所在时区当天的23:59:59时间戳，如时区为Asia/Shanghai时区时的1649692799；4.永久有效：传值为0即可 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `anniversary` | `int` | 入职周年日。根据入职时间发放类型勋章，需要配置该字段。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `effective_period` | `int` | 有效期限。根据入职时间发放类型勋章，需要配置该字段。<br>**可选值有**：<br>- `1`: 有效期为一年 - `2`: 永久有效 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_grant_all` | `boolean` | 是否授予给全员。1.为false时，需要关联1~500个用户群体。2.为true时，不可关联用户、用户组、部门。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_ids` | `string\[\]` | 授予的用户ID列表，授予名单列表接口返回结果中不返回该字段，只在详情接口返回 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_ids` | `string\[\]` | 授予的部门ID列表，授予名单列表接口返回结果中不返回该字段，只在详情接口返回 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `group_ids` | `string\[\]` | 授予的用户组ID列表，授予名单列表接口返回结果中不返回该字段，只在详情接口返回 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "grant": {
            "id": "g_49Z7CQ",
            "badge_id": "m_qTR2HM",
            "name": "激励勋章的授予名单",
            "grant_type": 0,
            "time_zone": "Asia/Shanghai",
            "rule_detail": {
                "effective_time": "1649606400",
                "expiration_time": "1649692799",
                "anniversary": 1,
                "effective_period": 1
            },
            "is_grant_all": false,
            "user_ids": [
                "u273y71"
            ],
            "department_ids": [
                "h121921"
            ],
            "group_ids": [
                "g122817"
            ]
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1051000 | unknown server error | 服务内部错误，请稍后重试 |
| 400 | 1051001 | request contain invalid param | 请求中包含非法参数 |
| 403 | 1051002 | request to exceed authority | 请求发生越权 |
| 400 | 1051200 | grant name are duplicated | 授予名单名称发生冲突 |
| 400 | 1051201 | cannot exceed the max length limit of grant name | 授予名单名称的长度超过限制 |
| 400 | 1051202 | already choose all staff, cannot related other user entity | 禁止为全员授予类型名单关联用户群体 |
| 400 | 1051204 | reach the count limit of grant | 授予名单数量达到上限 |
| 400 | 1051113 | cannot find this badge | 未找到该勋章的信息 |


