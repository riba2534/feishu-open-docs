---
title: "批量查询用户授权"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/authorization/query"
updateTime: "1754968240000"
---

# 批量查询用户授权

批量查询[飞书人事管理后台](https://people.feishu.cn/people/) -「设置」-「权限设置」中的用户授权信息。授权列表信息中包括员工ID、被授权的角色等信息。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/authorizations/query |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:authorization:read` 获取用户授权数据 `corehr:corehr:readonly` 获取核心人事信息 `corehr:corehr` 更新核心人事信息 `corehr:authorization:write` 更新用户权限 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `employment_id_list` | `string\[\]` | 否 | 员工ID列表，最大100个（不传则默认查询全部员工）。ID类型与user_id_type的取值意义一致。默认为飞书人事中的 ==employment_id==。 > 「**注意事项**」： - 如果你需要不同类型的ID进行转换，可以使用 [ID转换服务](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/common_data-id/convert) 换取 ==employment_id== - 如果需要一次查询多个员工ID，需通过 "employment_id_list=empId1&employment_id_list=empId2" 的方式传递，且调试台暂不支持多员工ID调试。<br>**示例值**：6969864184272078374 |
| `role_id_list` | `string\[\]` | 否 | 角色 ID 列表，最大 100 个。当传该参数时，会根据rold_id过滤，只返回包含该角色的授权信息。 > 「**注意事项**」： - 你可以使用 [批量获取角色列表](https://open.larkoffice.com/document/server-docs/corehr-v1/authorization/list) 获取角色ID，或者在角色详情中获取（URL 末的数字）。<br>- 如果需要一次查询多个角色ID，需通过需通过“rold_id_list=rold_id1&rold_id_list=rold_id2” 的方式传递，且调试台暂不支持多角色ID查询。<br>**示例值**：6969864184272078374 |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：6969864184272078374 |
| `page_size` | `string` | 否 | 每页获取记录数量，最大20(不传该参数，默认为20)<br>**示例值**：20 |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：people_corehr_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`people_corehr_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `updated_at_gte` | `string` | 否 | 授权时间大于，单位为秒（Unix时间戳）<br>**示例值**：1729773628 |
| `updated_at_lte` | `string` | 否 | 授权时间小于，单位为秒（Unix时间戳）<br>**示例值**：1729773628 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `role_authorization\[\]` | 查询的用户授权信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employment_id` | `string` | 员工 ID > 可以使用[搜索员工信息](https://open.larkoffice.com/document/server-docs/corehr-v1/employee/search)接口获取员工其他信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `permission_detail_list` | `permission_detail\[\]` | 授权列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `role` | `security_group` | 角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 角色ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 角色code |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `name` | 角色名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 状态，1表示角色启用，2表示角色停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `name` | 角色描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `group_type` | `int` | 角色类型<br>- 3 = 组织类角色 - 7 = 非组织类角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `created_by` | `string` | 创建人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `update_time` | `string` | 更新时间，单位为秒（秒级时间戳） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `org_truncation` | `org_truncation\[\]` | 组织管理维度 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `org_key` | `string` | 组织管理维度名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 下钻类型 - 0 = 对当前管理维度及下级管理维度均有权限 - 1 = 只对当前管理维度有权限，不包含其下级管理维度 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `depth` | `int` | 下钻深度（单位：层） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `assigned_organization_list` | `assigned_organization\[\]\[\]` | 指定管理对象列表，如果该值为null，则使用设置数据权限(grantor_rule_list)<br>json结构见响应体示例，其中：<br>org_key：组织key<br>org_name：组织名称<br>org_id_list：组织id，包含被删除/停用的组织id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `grantor_rule_list` | `permission_security_group\[\]` | 设置数据权限，如果该值为null，则使用指定管理对象列表(assigned_organization_list) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rule_dimension` | `rule_dimension` | 管理维度 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `entity_key` | `string` | 维度的key |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `entity_name` | `name` | 维度名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rule_type` | `int` | 管理类型 - 0：无数据权限   - 1：全部数据权限   - 2：被授权的用户自己   - 3：按规则指定范围 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `expression` | `filter_expression` | 规则 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `conditions` | `filter_condition\[\]` | 规则 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `left` | `filter_rule_value` | 左值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 规则值类型（value的类型） - 0 = 字符串 - 1 = 数字 - 2 = 字符串数组 - 3 = 数字数组 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 规则值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lookup_value` | `string` | 下钻值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lookup_type` | `string` | 下钻类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `right` | `filter_rule_value` | 右值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 规则值类型（value的类型） - 0 = 字符串 - 1 = 数字 - 2 = 字符串数组 - 3 = 数字数组 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 规则值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lookup_value` | `string` | 下钻值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lookup_type` | `string` | 下钻类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `operator` | `int` | 操作符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `right_value_type` | `int` | 右值类型 - 1 = 指定值 - 2 = 引用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `logic_expression` | `string` | 表达式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `update_time` | `string` | 更新时间(时间戳，单位：s) |
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
                "employment_id": "6967639606963471902",
                "permission_detail_list": [
                    {
                        "role": {
                            "id": "7034393015968122400",
                            "code": "department_manager",
                            "name": {
                                "zh_cn": "部门经理",
                                "en_us": "department manager"
                            },
                            "active_status": 1,
                            "description": {
                                "zh_cn": "中文描述",
                                "en_us": "英文描述"
                            },
                            "group_type": 1,
                            "created_by": "6967639606963471902",
                            "update_time": "1720584039",
                            "org_truncation": [
                                {
                                    "org_key": "department",
                                    "type": 0,
                                    "depth": 0
                                }
                            ]
                        },
                        "assigned_organization_list": [
                            [
                                {
                                    "org_key": "department",
                                    "org_name": {
                                        "zh_cn": "部门",
                                        "en_us": "department"
                                    },
                                    "org_id_list": [
                                        "6967639606963471902"
                                    ]
                                }
                            ]
                        ],
                        "grantor_rule_list": [
                            {
                                "rule_dimension": {
                                    "entity_key": "user",
                                    "entity_name": {
                                        "zh_cn": "员工",
                                        "en_us": "User"
                                    }
                                },
                                "rule_type": 1,
                                "expression": {
                                    "conditions": [
                                        {
                                            "left": {
                                                "type": 1,
                                                "value": "a",
                                                "lookup_value": "1",
                                                "lookup_type": "user"
                                            },
                                            "right": {
                                                "type": 1,
                                                "value": "a",
                                                "lookup_value": "1",
                                                "lookup_type": "user"
                                            },
                                            "operator": 1,
                                            "right_value_type": 1
                                        }
                                    ],
                                    "logic_expression": "1 and 2"
                                }
                            }
                        ],
                        "update_time": "1720584039"
                    }
                ]
            }
        ],
        "has_more": true,
        "page_token": "1234452132"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1161401 | Incorrect parameter type | 请检查字符串、数字等的参数类型 |
| 400 | 1161402 | Incorrect parameter range | 请检查数字类型参数是否超出约定范围 |
| 400 | 1161403 | Incorrect parameter length | 参数长度错误，请检查List，Map等容器类型参数 |
| 500 | 1161501 | System internal error | 请参考详细错误信息，如有问题请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |


