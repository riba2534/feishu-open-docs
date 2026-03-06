---
title: "更新统计设置"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/user_stats_view/update"
updateTime: "1723544573000"
---

# 更新统计设置

更新开发者定制的日度统计或月度统计的统计报表表头设置信息。报表的表头信息可以在考勤统计-[报表](https://example.feishu.cn/people/workforce-management/manage/statistics/report)中查询到具体的报表信息，此接口专门用于更新表头信息。


> **Error**: 本接口会对设置进行全量覆盖更新


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/attendance/v1/user_stats_views/:user_stats_view_id |
| HTTP Method | PUT |
| 接口频率限制 | [50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `attendance:task` 写入打卡数据 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `user_stats_view_id` | `string` | 用户视图 ID，获取方式：1）[查询统计设置](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/user_stats_view/query)<br>**示例值**："TmpZNU5qTTJORFF6T1RnNU5UTTNOakV6TWl0dGIyNTBhQT09" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `employee_type` | `string` | 是 | 响应体中的 user_id 的员工ID类型。如果没有后台管理权限，可使用[通过手机号或邮箱获取用户 ID](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/batch_get_id)<br>**示例值**：employee_id<br>**可选值有**：<br>- `employee_id`: 员工 employee ID，即[飞书管理后台](https://example.feishu.cn/admin/contacts/departmentanduser) > 组织架构 > 成员与部门 > 成员详情中的用户 ID - `employee_no`: 员工工号，即[飞书管理后台](https://example.feishu.cn/admin/contacts/departmentanduser) > 组织架构 > 成员与部门 > 成员详情中的工号 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `view` | `user_stats_view` | 是 | 统计设置 |
| &nbsp;&nbsp;└ `view_id` | `string` | 是 | 视图 ID，可通过[查询统计设置](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/user_stats_view/query)获取<br>**示例值**："TmpZNU5qTTJORFF6T1RnNU5UTTNOakV6TWl0dGIyNTBhQT09" |
| &nbsp;&nbsp;└ `stats_type` | `string` | 是 | 视图类型<br>**示例值**："month"<br>**可选值有**：<br>- `daily`: 日度统计 - `month`: 月度统计 |
| &nbsp;&nbsp;└ `user_id` | `string` | 是 | 操作者的用户id，对应employee_type<br>**示例值**："ec8ddg56" |
| &nbsp;&nbsp;└ `items` | `item\[\]` | 否 | 用户设置字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 是 | 标题编号<br>**示例值**："522" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `child_items` | `child_item\[\]` | 否 | 子标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 是 | 子标题编号<br>**示例值**："50101" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 是 | 开关字段，0：关闭，1：开启<br>**示例值**："0" |


### 请求体示例

```json
{
    "view": {
        "items": [
            {
                "child_items": [
                    {
                        "code": "50102",
                        "value": "0"
                    },
                    {
                        "code": "50111",
                        "value": "0"
                    },
                    {
                        "code": "50104",
                        "value": "0"
                    }
                ],
                "code": "501"
            }
        ],
        "stats_type": "month",
        "user_id": "ec8ddg56",
        "view_id": "TmpnNU5EQXpPVGN3TmpVMU16Y3lPVEEwTXl0dGIyNTBhQT09"
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
| &nbsp;&nbsp;└ `view` | `user_stats_view` | 视图 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `view_id` | `string` | 视图 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `stats_type` | `string` | 视图类型<br>**可选值有**：<br>- `daily`: 日度统计 - `month`: 月度统计 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 操作者的用户id，对应employee_type |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `items` | `item\[\]` | 用户设置字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 标题编号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 标题名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `child_items` | `child_item\[\]` | 子标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 子标题编号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 开关字段，0：关闭，1：开启 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 子标题名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `column_type` | `int` | 列类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `read_only` | `boolean` | 是否只读 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `min_value` | `string` | 最小值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `max_value` | `string` | 最大值 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "",
    "data": {
        "view": {
            "items": [
                {
                    "child_items": [
                        {
                            "code": "50102",
                            "value": "0"
                        },
                        {
                            "code": "50111",
                            "value": "0"
                        },
                        {
                            "code": "50104",
                            "value": "0"
                        }
                    ],
                    "code": "501"
                }
            ],
            "stats_type": "month",
            "user_id": "ec8ddg56",
            "view_id": "TmpnNU5EQXpPVGN3TmpVMU16Y3lPVEEwTXl0dGIyNTBhQT09"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1220001 | param is invalis | 入参校验失败，请根据具体返回的信息检查入参。例如“employee_type invalid”代表人员类型异常。如仍无法解决可联系 [技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1220002 | tenant_id is empty | 请检查入参中的 tenant_access_token是否正确 |
| 500 | 1228000 | 历史错误码，不再使用 | - |
| 400 | 1220600 | 通用错误信息 | 通用错误信息包含多条，详细的错误信息以及处理建议可参见 [错误信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/attendance-development-guidelines) |


