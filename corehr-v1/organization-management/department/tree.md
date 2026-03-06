---
title: "查询指定生效日期的部门架构树"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/tree"
updateTime: "1739172479000"
---

# 查询指定生效日期的部门架构树

支持传入部门ID（不传默认根部门），任意日期（不传默认当前日期）。从给定部门ID开始广度遍历，每页最多返回2000行数据


> **Warning**: - 延迟说明：该数据同步延迟 10s 以内，即：直接创建/更新对象后10s内调用此接口可能查询不到数据，部门上下级关系变化10s内可能查询不到最新数据。
> - 如果对数据延迟较为敏感的场景，可以考虑定期or延迟调用该接口，或者走[批量查询部门V2](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get) 逐级查询组织架构


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/departments/tree |
| HTTP Method | POST |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:department.organize:read` 获取部门组织架构信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 是 | 分页大小，最大 100<br>**示例值**：100<br>**数据校验规则**：<br>- 取值范围：`1` ～ `2000` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：6891251722631890445 |
| `department_id_type` | `string` | 否 | 此次调用中使用的部门 ID 类型<br>**示例值**：people_corehr_department_id<br>**可选值有**：<br>- `open_department_id`: 【飞书】用来在具体某个应用中标识一个部门，同一个department_id 在不同应用中的 open_department_id 相同。 - `department_id`: 【飞书】用来标识租户内一个唯一的部门。 - `people_corehr_department_id`: 【飞书人事】用来标识「飞书人事」中的部门。<br>**默认值**：`people_corehr_department_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `department_id` | `string` | 否 | 部门 ID，默认根部门<br>**示例值**："6893014062142064111" |
| `need_inactive` | `boolean` | 否 | 是否包含失效部门，默认false<br>**示例值**：false |
| `effective_date` | `string` | 否 | 日期，格式yyyy-mm-dd，默认当前日期 - 传2024-01-01，即为返回2024-01-01的组织架构<br>**示例值**："2024-01-01"<br>**数据校验规则**：<br>- 最大长度：`10` 字符 |


### 请求体示例

```json
{
    "department_id": "6893014062142064111",
    "need_inactive": false,
    "effective_date": "2024-01-01"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `department_tree\[\]` | 部门树节点 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 部门 ID - 可通过[批量查询部门V2](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get) 或者[搜索部门信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/search) 获取详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `level` | `int` | 部门绝对层级，根部门层级为0，根部门的子部门层级为1，依次类推 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `children` | `string\[\]` | 下级部门 ID 列表 - 可通过[批量查询部门V2](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get) 或者[搜索部门信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/search) 获取详情 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "id": "4719456877659520852",
                "level": 1,
                "children": [
                    "7094136522860922111"
                ]
            }
        ],
        "page_token": "eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0=",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1160102 | Param is invalid | 请检查参数格式是否正确，无效department_id或effective_date格式错误 |
| 403 | 1160103 | No permission | 检查传入department_id是否有权限 |


