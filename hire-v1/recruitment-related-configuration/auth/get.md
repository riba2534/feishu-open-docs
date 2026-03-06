---
title: "获取角色详情"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/role/get"
updateTime: "1730873717000"
---

# 获取角色详情

可通过此接口获取角色详情信息，包括名称、描述、权限列表等


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/roles/:role_id |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:auth:readonly` 获取招聘权限信息 `hire:auth` 更新招聘权限信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `role_id` | `string` | 角色 ID，调用 [获取角色列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/role/list)获取。<br>**示例值**："7350589232462807068" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `role` | `role_detail` | 角色详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 角色 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 角色名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 角色中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 角色英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 角色描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 角色中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 角色英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `modify_time` | `string` | 更新时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `role_status` | `int` | 角色启用状态<br>**可选值有**：<br>- `1`: 启用 - `2`: 停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `role_type` | `int` | 角色类型<br>**可选值有**：<br>- `1`: 系统内置角色 - `2`: 普通用户 - `5`: 自定义角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `scope_of_application` | `int` | 角色适用范围<br>**可选值有**：<br>- `1`: 社招 - `2`: 校招 - `3`: 都包含 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `has_business_management_scope` | `boolean` | 是否在角色上配置业务管理范围 - `true`：配置了业务管理范围 - `false`：未配置业务管理范围 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `socail_permission_collection` | `permission_collection` | 社招权限配置，仅当`scope_of_application`为“社招”或“都包含”时有值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `feature_permissions` | `id_name_object\[\]` | 功能权限 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 权限点 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 权限点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 权限点中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 权限点英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `management_permissions` | `id_name_object\[\]` | 管理权限 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 权限点 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 权限点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 权限点中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 权限点英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `data_permissions` | `data_permission\[\]` | 数据权限 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 权限点 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 权限点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 权限点中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 权限点英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `select_status` | `int` | 数据权限状态<br>**可选值有**：<br>- `0`: 不可见 - `1`: 可见 - `2`: 可编辑 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `business_management_scopes` | `business_management_scope\[\]` | 业务管理范围 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `entity` | `entity_info` | 实体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 实体code，枚举如下 - `talent`：人才 - `application`：投递 - `interview`：面试 - `interview_appointment_project`：预约面试 - `jobfair`：集中面试 - `exam_session`：集中笔试 - `offer`：Offer - `job`：职位 - `job_recruitment`：招聘需求 - `reward`：内推奖励 - `info_session`：宣讲会 - `bi`：BI - `subject`：对应项目 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 实体名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 实体中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 实体英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `permission_groups` | `permission_group_info\[\]` | 权限分组 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `permission_ids` | `string\[\]` | 权限点 ID列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `scope_rule` | `permission_scope_rule` | 管理范围规则 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rule_type` | `int` | 规则类型<br>**可选值有**：<br>- `0`: 无数据权限 - `1`: 全部数据权限 - `2`: 按规则指定范围，当前系统暂不支持返回详细规则 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `campus_permission_collection` | `permission_collection` | 校招权限配置，仅当`scope_of_application`为“校招”或“都包含”时有值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `feature_permissions` | `id_name_object\[\]` | 功能权限 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 权限点 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 权限点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 权限点中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 权限点英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `management_permissions` | `id_name_object\[\]` | 管理权限 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 权限点 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 权限点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 权限点中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 权限点英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `data_permissions` | `data_permission\[\]` | 数据权限 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 权限点 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 权限点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 权限点中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 权限点英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `select_status` | `int` | 数据权限状态<br>**可选值有**：<br>- `0`: 不可见 - `1`: 可见 - `2`: 可编辑 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `business_management_scopes` | `business_management_scope\[\]` | 业务管理范围 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `entity` | `entity_info` | 实体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 实体code，枚举如下 - `talent`：人才 - `application`：投递 - `interview`：面试 - `interview_appointment_project`：预约面试 - `jobfair`：集中面试 - `exam_session`：集中笔试 - `offer`：Offer - `job`：职位 - `job_recruitment`：招聘需求 - `reward`：内推奖励 - `info_session`：宣讲会 - `bi`：BI - `subject`：对应项目 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 实体名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 实体中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 实体英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `permission_groups` | `permission_group_info\[\]` | 权限分组 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `permission_ids` | `string\[\]` | 权限点 ID列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `scope_rule` | `permission_scope_rule` | 管理范围规则 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rule_type` | `int` | 规则类型<br>**可选值有**：<br>- `0`: 无数据权限 - `1`: 全部数据权限 - `2`: 按规则指定范围，当前系统暂不支持返回详细规则 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "SUCCESS",
    "data": {
        "role": {
            "id": "6930815272790114324",
            "name": {
                "zh_cn": "招聘 HRBP",
                "en_us": "Recruitment HRBP"
            },
            "description": {
                "zh_cn": "赋予HRBP的权限",
                "en_us": "Authority given to HRBP"
            },
            "modify_time": "1716535727510",
            "role_status": 1,
            "role_type": 1,
            "scope_of_application": 1,
            "has_business_management_scope": true,
            "socail_permission_collection": {
                "feature_permissions": [
                    {
                        "id": "10101000",
                        "name": {
                            "zh_cn": "查看人才",
                            "en_us": "View talent"
                        }
                    }
                ],
                "management_permissions": [
                    {
                        "id": "20101001",
                        "name": {
                            "zh_cn": "门店管理",
                            "en_us": "Store management"
                        }
                    }
                ],
                "data_permissions": [
                    {
                        "id": "30203005",
                        "name": {
                            "zh_cn": "私密备注",
                            "en_us": "Private notes"
                        },
                        "select_status": 0
                    }
                ],
                "business_management_scopes": [
                    {
                        "entity": {
                            "code": "application",
                            "name": {
                                "zh_cn": "投递",
                                "en_us": "Application"
                            }
                        },
                        "permission_groups": [
                            {
                                "permission_ids": [
                                    "6930815272790114324"
                                ],
                                "scope_rule": {
                                    "rule_type": 1
                                }
                            }
                        ]
                    }
                ]
            },
            "campus_permission_collection": {
                "feature_permissions": [
                    {
                        "id": "10101002",
                        "name": {
                            "zh_cn": "查看投递",
                            "en_us": "View application"
                        }
                    }
                ],
                "management_permissions": [
                    {
                        "id": "20101002",
                        "name": {
                            "zh_cn": "编辑权限",
                            "en_us": "Edit permissions"
                        }
                    }
                ],
                "data_permissions": [
                    {
                        "id": "30103001",
                        "name": {
                            "zh_cn": "操作记录",
                            "en_us": "Action history"
                        },
                        "select_status": 0
                    }
                ],
                "business_management_scopes": [
                    {
                        "entity": {
                            "code": "application",
                            "name": {
                                "zh_cn": "投递",
                                "en_us": "application"
                            }
                        },
                        "permission_groups": [
                            {
                                "permission_ids": [
                                    "6930815272790114324"
                                ],
                                "scope_rule": {
                                    "rule_type": 0
                                }
                            }
                        ]
                    }
                ]
            }
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或[联系客服](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952&extra=%7B%22channel%22:14,%22created_at%22:1614493146,%22scenario_id%22:6885151765134622721,%22signature%22:%22ca94c408b966dc1de2083e5bbcd418294c146e98%22%7D) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型、大小 |
| 400 | 1002352 | 角色不存在 | 请检查入参`role_id`是否正确，role_id可通过接口 [获取角色列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/role/list)获取 |


