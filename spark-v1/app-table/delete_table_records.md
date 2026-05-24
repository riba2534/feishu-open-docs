---
title: "删除数据表中的记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/spark-v1/app-table/delete_table_records"
updateTime: "1775706886000"
---

# 删除数据表中的记录

删除指定应用下数据表中符合filter筛选条件的记录，删除后记录不可恢复。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/spark/v1/apps/:app_id/tables/:table_name/records |
| HTTP Method | DELETE |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `spark:app.table.record:write` 修改或删除数据表记录 |

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
| `filter` | `string` | 是 | 筛选条件，遵循 PostgREST 语法，详情可查看 https://docs.postgrest.org/en/v13/references/api/tables_views.html#horizontal-filtering 此处用法和查询数据记录一致<br>**示例值**：age=gt.10 |
| `env` | `string` | 否 | 访问的 database 环境，默认为 online（线上环境）<br>**示例值**：`online`、`dev`<br>**默认值**：`online` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {}
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 3340001 | param is invalid | 请检查请求参数的类型、格式或值是否符合接口要求，具体可参考请求参数说明中的数据校验规则。 |


