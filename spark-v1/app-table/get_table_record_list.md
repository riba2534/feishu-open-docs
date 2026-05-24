---
title: "查询数据表数据记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/spark-v1/app-table/get_table_record_list"
updateTime: "1775706922000"
---

# 查询数据表数据记录

查询应用下的数据表数据记录，包括指定列、字段值及分页信息，适用于需要获取应用下某数据表数据的记录、展示等场景。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/spark/v1/apps/:app_id/tables/:table_name/records |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `spark:app.table.record:read` 读取数据表记录 `spark:app.table.record:write` 修改或删除数据表记录 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_id` | `string` | 妙搭应用 id，可从妙搭应用 URL 中获取，如 https://miaoda.feishu.cn/app/app_4jcn5n11bpf5v 中的 app_4jcn5n11bpf5v 即为 app_id<br>**示例值**："app_4jcn5n11bpf5v" |
| `table_name` | `string` | 妙搭数据表表名，必须属于 app_id 对应的妙搭应用，可从妙搭应用数据库管理中获取<br>**示例值**："student_table" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 分页大小，用于限制一次请求所返回的数据条目数。默认10，最大500<br>**示例值**：10<br>**默认值**：`10`<br>**数据校验规则**：<br>- 取值范围：`1` ～ `500` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0= |
| `select` | `string` | 否 | 返回的列，默认为 *，即返回所有列。 遵循 PostgREST 语法，详情可查看 https://docs.postgrest.org/en/v13/references/api/tables_views.html#vertical-filtering<br>**示例值**：_id,_created_at,name |
| `filter` | `string` | 否 | 筛选条件，遵循 PostgREST 语法，详情可查看 https://docs.postgrest.org/en/v13/references/api/tables_views.html#horizontal-filtering<br>**示例值**：age=gt.10 |
| `order` | `string` | 否 | 排序条件，如果没指定 asc/desc，默认为 asc，null 值可排在最前或最后。 遵循 PostgREST 语法，详情可查看 https://docs.postgrest.org/en/v13/references/api/tables_views.html#ordering<br>**示例值**：age.desc,score.asc |
| `env` | `string` | 否 | 访问的 database 环境，默认为 online（线上环境）<br>**示例值**：`online`、`dev`<br>**默认值**：`online` |
| `user_identifier_type` | `string` | 否 | 此次调用使用的用户 ID 类型，将使用指定的 ID 来标示某个用户在接口入参和出参中的值。 示例值：`miaoda_user_id` 可选值： - `miaoda_user_id`：标识一个用户在飞书开发套件应用中的身份。示例值：1838493619298330 - `open_id`：标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。示例值：ou_bdbbd8f3f919829064b3ffc1b9476105 了解更多：如何获取 Open ID - `union_id`：标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。示例值：on_b1b44199e8f3def4ebda5355409e2033 了解更多：如何获取 Union ID？<br>**示例值**：miaoda_user_id<br>**默认值**：`miaoda_user_id` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `total` | `int` | 符合条件的记录总数 |
| &nbsp;&nbsp;└ `items` | `string` | 数据记录列表，格式为数组序列化后的 JSONString |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "has_more": true,
        "page_token": "eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0=",
        "total": 2,
        "items": "[{\"name\":\"王一一\",\"gender\":\"male\",\"age\":10},{\"name\":\"王二二\",\"gender\":\"female\",\"age\":10}]"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 3340001 | param is invalid | 请检查请求参数的类型、格式或值是否符合接口要求，具体可参考请求参数说明中的数据校验规则。 |


