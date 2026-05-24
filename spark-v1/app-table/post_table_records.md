---
title: "向数据表中添加或更新记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/spark-v1/app-table/post_table_records"
updateTime: "1775199161000"
---

# 向数据表中添加或更新记录

向应用下的数据表中添加或更新记录。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/spark/v1/apps/:app_id/tables/:table_name/records |
| HTTP Method | POST |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `spark:app.table.record:write` 修改或删除数据表记录 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |
| Prefer | string | 否 | 为空时表示 INSERT， resolution=merge-duplicates表示 UPSERT，详细参考 https://docs.postgrest.org/en/v13/references/api/tables_views.html#upsert **示例值**："resolution=merge-duplicates" |


请求头可额外传入 `Prefer` 参数来控制行为。
- 如 `Prefer: missing=default` 代表未传入的字段按默认值处理。
- 如 `Prefer: resolution=merge-duplicates` 代表在 UPSERT 操作中，若存在重复键（如主键或唯一约束），则更新该记录；如果不存在，则插入新记录。
- 如 `Prefer: resolution=ignore-conflicts` 代表在 UPSERT 操作中，若存在重复键（如主键或唯一约束），则忽略该操作，不进行任何更新或插入。

可组合使用，如 `Prefer: resolution=merge-duplicates, missing=default`。

详细参考 [PostgREST 文档 - UPSERT](https://docs.postgrest.org/en/v13/references/api/tables_views.html#upsert)。

### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_id` | `string` | 妙搭应用 id，可从妙搭应用 URL 中获取，如 https://miaoda.feishu.cn/app/app_4jcn5n11bpf5v 中的 app_4jcn5n11bpf5v 即为 app_id<br>**示例值**："app_4jcn5n11bpf5v" |
| `table_name` | `string` | 妙搭数据表表名，必须属于 app_id 对应的妙搭应用，可从妙搭应用数据库管理中获取<br>**示例值**："student_table" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `columns` | `string` | 否 | UPSERT 时使用，指定列，多列英文逗号拼接<br>**示例值**：name,age |
| `on_conflict` | `string` | 否 | UPSERT 时使用，指定使用哪一个或多个具有唯一约束的字段作为冲突判断依据，默认为表主键。 假设 user_products 表有一个由 user_id 和 product_id 组成的复合唯一约束<br>**示例值**：user_id,product_id |
| `env` | `string` | 否 | 访问的 database 环境，默认为 online（线上环境）<br>**示例值**：`online`、`dev`<br>**默认值**：`online` |
| `user_identifier_type` | `string` | 否 | 此次调用使用的用户 ID 类型，将使用指定的 ID 来标示某个用户在接口入参和出参中的值。 示例值：`miaoda_user_id` 可选值： - `miaoda_user_id`：标识一个用户在飞书开发套件应用中的身份。示例值：1838493619298330 - `open_id`：标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。示例值：ou_bdbbd8f3f919829064b3ffc1b9476105 了解更多：如何获取 Open ID - `union_id`：标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。示例值：on_b1b44199e8f3def4ebda5355409e2033 了解更多：如何获取 Union ID？<br>**示例值**：miaoda_user_id<br>**默认值**：`miaoda_user_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `records` | `string` | 是 | 要插入的数据记录列表（JSON数组的字符串形式），单次支持最大记录数量500条<br>**示例值**："[{\"name\":\"王一一\",\"gender\":\"male\",\"age\":10},{\"name\":\"王二二\",\"gender\":\"female\",\"age\":10}]" |


### 请求体示例

```json
{
    "records": "[{\"name\":\"王一一\",\"gender\":\"male\",\"age\":10},{\"name\":\"王二二\",\"gender\":\"female\",\"age\":10}]"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `record_ids` | `string\[\]` | 按照记录顺序创建或更新的记录 ID 列表 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "record_ids": [
            "1cbb280d-fc3d-4dca-9db5-adb14c4c83ec"
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 3340001 | param is invalid | 请检查请求参数的类型、格式或值是否符合接口要求，具体可参考请求参数说明中的数据校验规则。 |


