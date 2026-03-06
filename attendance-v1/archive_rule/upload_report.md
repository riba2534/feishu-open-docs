---
title: "写入归档报表结果"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/archive_rule/upload_report"
updateTime: "1722519300000"
---

# 写入归档报表结果

写入归档报表结果，对应假勤管理-考勤统计-报表-[归档报表](https://example.feishu.cn/people/workforce-management/manage/statistics/report)页签，点击报表名称进入后的导入功能。可以将数据直接写入归档报表。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/attendance/v1/archive_rule/upload_report |
| HTTP Method | POST |
| 接口频率限制 | [50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `attendance:task` 写入打卡数据 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `employee_type` | `string` | 是 | 请求体中的 user_ids 和响应体中的 user_id 的员工ID类型。如果没有后台管理权限，可使用[通过手机号或邮箱获取用户 ID](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/batch_get_id)<br>* `employee_id `：员工 employee ID，即[飞书管理后台](https://example.feishu.cn/admin/contacts/departmentanduser) > 组织架构 > 成员与部门 > 成员详情中的用户 ID * `employee_no`：员工工号，即[飞书管理后台](https://example.feishu.cn/admin/contacts/departmentanduser) > 组织架构 > 成员与部门 > 成员详情中的工号<br>**示例值**：employee_id |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `month` | `string` | 是 | 月份，格式为yyyyMM<br>**示例值**："202409" |
| `operator_id` | `string` | 是 | 操作者ID，对应employee_type<br>**示例值**："ax11d" |
| `archive_report_datas` | `archive_report_data\[\]` | 否 | 归档报表内容(不超过50个)<br>**数据校验规则**：<br>- 长度范围：`1` ～ `50` |
| &nbsp;&nbsp;└ `member_id` | `string` | 是 | 用户ID，对应employee_type<br>**示例值**："1aaxxd" |
| &nbsp;&nbsp;└ `start_time` | `string` | 是 | 考勤开始时间，格式为yyyyMMdd<br>**示例值**："20210109" |
| &nbsp;&nbsp;└ `end_time` | `string` | 是 | 考勤结束时间，格式为yyyyMMdd<br>**示例值**："20210109" |
| &nbsp;&nbsp;└ `field_datas` | `archive_field_data\[\]` | 否 | 字段结果(不超过200个)<br>**数据校验规则**：<br>- 长度范围：`1` ～ `200` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 是 | 字段编码，可根据[查询归档报表表头](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/archive_rule/user_stats_fields_query) 获取<br>**示例值**："abd754f7" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 否 | 字段结果值<br>**示例值**："1" |
| `archive_rule_id` | `string` | 是 | 归档规则id，可根据[查询所有归档规则](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/archive_rule/list)获得<br>**示例值**："1" |


### 请求体示例

```json
{
    "month": "202409",
    "operator_id": "ax11d",
    "archive_report_datas": [
        {
            "member_id": "1aaxxd",
            "start_time": "20210109",
            "end_time": "20210109",
            "field_datas": [
                {
                    "code": "abd754f7",
                    "value": "1"
                }
            ]
        }
    ],
    "archive_rule_id": "1"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `invalid_code` | `string\[\]` | 无效的code |
| &nbsp;&nbsp;└ `invalid_member_id` | `string\[\]` | 无效的member_id，对应employee_type |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "invalid_code": [
            "1"
        ],
        "invalid_member_id": [
            "a1xud"
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1220001 | "%v" 表示动态返回，即根据实际的错误场景，返回不同的 err msg | 入参校验失败，请根据具体返回的信息检查入参。例如“employee_type invalid”代表人员类型异常。如仍无法解决可联系 [技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1220600 | 通用错误信息 | 通用错误信息包含多条，详细的错误信息以及处理建议可参见 [错误信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/attendance-development-guidelines) |
| 400 | 1225000 | "%v" 表示动态返回，即根据实际的错误场景，返回不同的 err msg | 请参考实际返回的错误信息排查问题。例如“internal server error”代表内部服务异常。如仍无法解决可联系 [技术支持](https://applink.feishu.cn/TLJpeNdW) |


