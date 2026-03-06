---
title: "批量查询部门操作日志"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/query_operation_logs"
updateTime: "1753969399000"
---

# 批量查询部门操作日志

批量查询指定时间范围内的部门操作日志


> **Tip**: - 默认排序条件：默认以操作时间倒序排序
> - 仅支持查询部门基础字段变更的操作日志，对于角色字段变更的操作日志查询功能待上线


> **Warning**: - 时间窗支持大范围查询，限定查询范围在366天以内，例如要查询2020年1月1日至2023年1月1日的数据，建议分成两次查询，分别为2020年1月1日至2021年1月1日，2022年1月2日至2023年1月1日，不建议查询大时间范围数据
> - 支持查询批量部门的操作日志，限定查询最大部门数为100，查询部门数量大于100时，建议分批查询


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/departments/query_operation_logs |
| HTTP Method | POST |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:department.operation_log:read` 获取部门操作日志 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 是 | 分页大小，最大 1000<br>**示例值**：100<br>**数据校验规则**：<br>- 取值范围：`1` ～ `1000` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：2 |
| `department_id_type` | `string` | 否 | 此次调用中使用的部门 ID 类型<br>**示例值**：people_corehr_department_id<br>**可选值有**：<br>- `open_department_id`: 【飞书】用来在具体某个应用中标识一个部门，同一个department_id 在不同应用中的 open_department_id 相同。 - `department_id`: 【飞书】用来标识租户内一个唯一的部门。 - `people_corehr_department_id`: 【飞书人事】用来标识「飞书人事」中的部门。<br>**默认值**：`people_corehr_department_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `department_ids` | `string\[\]` | 是 | 部门ID列表，ID获取方式： - 调用[【创建部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/create)、[【搜索部门】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/search)接口可以返回部门ID - 也可以通过[【事件】创建部门](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/events/created)、[【事件】更新部门](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/events/updated) 获取部门ID<br>**示例值**：["7094136522860922222"]<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` |
| `start_date` | `string` | 是 | 查询的起始操作日期，格式 "YYYY-MM-DD"，不带时分秒，包含start_date传入的时间，系统会以start_date的00:00:00为开始时间进行查询<br>**示例值**："2023-01-01" |
| `end_date` | `string` | 是 | 查询的截止操作日期，注意事项： - 格式 "YYYY-MM-DD"，不带时分秒，包含end_date传入的时间，系统会以end_date的23:59:59为截止时间进行查询。 - 查询截止日期end_date应大于起始日期start_date，起止日期跨度最大为366天<br>**示例值**："2024-01-01" |


### 请求体示例

```json
{
    "department_ids": [
        "7094136522860922222"
    ],
    "start_date": "2023-01-01",
    "end_date": "2024-01-01"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `op_logs` | `organization_op_log\[\]` | 操作日志列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `object_id` | `string` | 部门ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `changes` | `operation_log_entity_field\[\]` | 字段变化列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `field` | `string` | 变更字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `before` | `string` | 旧值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `after` | `string` | 新值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operator` | `string` | 操作人工号，更多详细信息可通过[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operation_type` | `int` | 操作类型。现有如下类型： - `10`：新建部门记录 - `20`：新建/复制部门版本 - `50`：编辑部门版本 - `60`：撤销部门版本 - `70`：停用部门 - `80`：启用部门 - `90`：删除部门记录 - `100`：自定义部门排序 - `110`：更新部门 - `120`：编辑部门关联规则 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operation_time` | `string` | 操作时间，带时分秒。示例值：2023-11-15 19:25:45 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `effective_time` | `string` | 操作生效时间，表示被操作的部门版本的生效日期。示例值：2023-10-28 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operation_reason` | `string` | 操作原因说明 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `change_reasons` | `string\[\]` | 调整原因列表 |
| &nbsp;&nbsp;└ `next_page_token` | `string` | 下一页token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "op_logs": [
            {
                "object_id": "7094136522860922111",
                "changes": [
                    {
                        "field": "description",
                        "before": "优秀部门",
                        "after": "更优秀的部门"
                    }
                ],
                "operator": "E001",
                "operation_type": 10,
                "operation_time": "2023-11-15 19:25:45",
                "effective_time": "2023-10-28",
                "operation_reason": "因人员调整,变更部门负责人为张三",
                "change_reasons": [
                    "新建部门"
                ]
            }
        ],
        "next_page_token": "2",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1160101 | date interval exceeds 366 | 起止日期间隔超过了366天的限定值，请校验起止日期范围是否在限定值366天内 |


