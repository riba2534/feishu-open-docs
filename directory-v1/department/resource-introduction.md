---
title: "资源介绍"
fullPath: "/uAjLw4CM/ukTMukTMukTM/directory-v1/department/resource-introduction"
updateTime: "1749798702000"
---

# 资源定义
部门是飞书组织架构里的一个基础实体，每个员工都归属于一个或多个部门。
部门在飞书的身份标识包括`department_id`、`open_department_id`。有关department各类ID的详细介绍，参考 
[部门ID说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/field-overview#23857fe0)。


# 字段说明


| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `department_id` | `string` | 部门ID<br>**字段权限要求（满足任一）**： `directory:department.base:read` 查看部门基础信息 `directory:department.external_id:read` 查看部门自定义 ID |
| `department_count` | `department_count` | 部门成员计数与子部门计数。计算结果可能会有延迟<br>**字段权限要求（满足任一）**： `directory:department.count:read` 查看部门成员与子部门计数 `directory:department.organization:read` 查看部门组织架构信息 |
| &nbsp;&nbsp;└ `recursive_members_count` | `string` | 部门成员数量，包含部门内所有层级子部门的成员数量 |
| &nbsp;&nbsp;└ `direct_members_count` | `string` | 部门成员数量，仅包含直属成员数，不包含子部门成员数 |
| &nbsp;&nbsp;└ `recursive_members_count_exclude_leaders` | `string` | 部门成员数量，包含部门内所有层级子部门的成员数量 |
| &nbsp;&nbsp;└ `recursive_departments_count` | `string` | 部门成员数量，包含部门内所有层级子部门的成员数量 |
| &nbsp;&nbsp;└ `direct_departments_count` | `string` | 部门成员数量，仅包含直属成员数，不包含子部门成员数 |
| `has_child` | `boolean` | 是否有子部门<br>**字段权限要求（满足任一）**： `directory:department.has_child:read` 查看部门是否有子部门 `directory:department.organization:read` 查看部门组织架构信息 |
| `leaders` | `department_leader\[\]` | 部门负责人<br>**字段权限要求**： `directory:department.leader:read` 查看部门负责人信息 |
| &nbsp;&nbsp;└ `leader_type` | `int` | 部门负责人类型<br>**可选值有**：<br>- `1`: 主 - `2`: 副 |
| &nbsp;&nbsp;└ `leader_id` | `string` | 部门负责人ID |
| `parent_department_id` | `string` | 父部门ID<br>**字段权限要求（满足任一）**： `directory:department.organization:read` 查看部门组织架构信息 `directory:department.parent_id:read` 查看部门的父部门 ID |
| `name` | `i18n_text` | 部门名称<br>**字段权限要求（满足任一）**： `directory:department.base:read` 查看部门基础信息 `directory:department.name:read` 查看部门的名称 |
| &nbsp;&nbsp;└ `default_value` | `string` | 默认值 |
| &nbsp;&nbsp;└ `i18n_value` | `map<string, string>` | 国际化值，key为zh_cn, ja_jp, en_us, value为对应的值 |
| `enabled_status` | `boolean` | **字段权限要求**： `directory:department.status:read` 查看部门的停启用状态 |
| `order_weight` | `string` | 部门排序权重<br>**字段权限要求（满足任一）**： `directory:department.order_weight:read` 查看部门排序权重 `directory:department.organization:read` 查看部门组织架构信息 |
| `custom_field_values` | `custom_field_value\[\]` | 部门自定义字段值<br>**字段权限要求**： `directory:department.custom_field:read` 查看部门自定义字段信息 |
| &nbsp;&nbsp;└ `field_key` | `string` | 自定义字段key |
| &nbsp;&nbsp;└ `field_type` | `string` | 自定义字段类型<br>**可选值有**：<br>- `1`: 多行文本 - `2`: 网页链接 - `3`: 枚举选项 - `4`: 人员 |
| &nbsp;&nbsp;└ `text_value` | `i18n_text` | 文本字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `default_value` | `string` | 默认值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_value` | `map<string, string>` | 国际化值，key为zh_cn, ja_jp, en_us, value为对应的值 |
| &nbsp;&nbsp;└ `url_value` | `url_value` | 网页链接字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `link_text` | `i18n_text` | 网页标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `default_value` | `string` | 默认值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_value` | `map<string, string>` | 国际化值，key为zh_cn, ja_jp, en_us, value为对应的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 移动端网页链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `pcurl` | `string` | 桌面端网页链接 |
| &nbsp;&nbsp;└ `enum_value` | `enum_value` | 枚举字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `enum_ids` | `string\[\]` | 选项结果ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `enum_type` | `string` | 选项类型<br>**可选值有**：<br>- `1`: 文本 - `2`: 图片 |
| &nbsp;&nbsp;└ `user_values` | `user_value\[\]` | 人员字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ids` | `string\[\]` | 人员ID |
| `department_path_infos` | `department_base_info\[\]` | 部门路径信息。排列顺序为根级到末级，不包含根部门<br>**字段权限要求**： `directory:department.department_path:read` 查看部门路径信息 |
| &nbsp;&nbsp;└ `department_id` | `string` | 部门ID |
| &nbsp;&nbsp;└ `department_name` | `i18n_text` | i18n文本 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `default_value` | `string` | 默认值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_value` | `map<string, string>` | 国际化值，key为zh_cn, ja_jp, en_us, value为对应的值 |
| `data_source` | `int` | 数据来源<br>**可选值有**：<br>- `1`: 管理后台 - `2`: 人事企业版 - `3`: SCIM<br>**字段权限要求（满足任一）**： `directory:department.base:read` 查看部门基础信息 `directory:department.data_source:read` 查看部门数据来源 |


## 数据示例

```json 
 {
    "department_id": "D100",
    "open_department_id": "od-4e6ac4d14bcd5071a37a39de902c7141",
    "name": {
        "value": "销售部",
        "i18n_value":{
            "language": "en_us"
                "value": "Sale"
            }
        },
    "parent_department_id": "D90",
    "leaders": [
        {
            "leader_ID": "u273y69",
            "DepartmentLeaderType": 1
        }
    ],
    "has_child":true,
    "department_count": {
        "recursive_members_count": 100,
        "direct_members_count": 90,
        "recursive_members_count_exclue_leaders":80,
        "recursive_departments_count": 20,
        "direct_departments_count": 10
    },
    "enabled_status": true,
    "order_weight": 1,
    "department_path_info": [
        {
            "department_id": "D102",
            "department_name":{
                "value": "北京科技有限公司",
                "i18n_value":{
                    "language": "en_us"
                        "value": "Beijing Technology Co., Ltd"
                }
            }
        },
        {
            "department_id": "D101",
            "department_name":{
                "value": "华北大区",
                "i18n_value":{
                    "language": "en_us"
                        "value": "North China Region"
                }
            }
        },
        {
            "department_id": "D100",
            "department_name":{
                "value": "销售部",
                "i18n_value":{
                    "language": "en_us"
                        "value": "Sale"
                }
            }
        }
    ],
    "custom_field_values": [
        {
            "field_id": "DemoId",
            "field_value": {
                "field_type": 1,
                "text_value": "DemoText"
            }
        },
        {
            "field_id": "DemoId_2",
            "field_value": {
                "field_type": 4,
                "user_value": [
                    "9b2fabg5"
                ]
            }
        }
    ],
    "data_source":1   
}

``` 

