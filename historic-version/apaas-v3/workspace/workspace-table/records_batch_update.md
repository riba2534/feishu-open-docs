---
title: "批量更新数据表中的记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/apaas-v1/workspace-table/records_batch_update"
updateTime: "1764571041000"
---

# 批量更新数据表中的记录

批量更新数据表中的记录


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/apaas/v1/workspaces/:workspace_id/tables/:table_name/records_batch_update |
| HTTP Method | PATCH |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `app_engine:workspace.table.record:write` 修改或删除数据表数据记录 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `workspace_id` | `string` | 工作空间id，可以从数据平台的 URL 中获取，如 `https://apaas.feishu.cn/suda/workspace/workspace_aadimx5uzpsls/table-manage/main?tableId=table_1846786627963081&tab=objectManage` 中的 workspace_aadimx5uzpsls 就是 workspace_id<br>**示例值**："workspace_aadimx5uzpsls" |
| `table_name` | `string` | 数据表表名，可以从数据平台获取对应的数据表名。<br>**示例值**："table_name_1" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `records` | `string` | 是 | 要更新的数据记录列表，单次支持最多 500条，每行 record 都必须包含主键 _id，且不同行要更新的字段需保持一致<br>**示例值**："[{\"_id\":\"657fade8-394d-4d86-aa35-0129e3bd7614\",\"age\":10}]" |


### 请求体示例

```json
{
    "records": "[{\"_id\":\"657fade8-394d-4d86-aa35-0129e3bd7614\",\"age\":10}]"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `record_ids` | `string\[\]` | 更新的记录唯一ID列表 |


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
| 400 | 2320001 | param is invalid | 请检查请求参数的类型、格式或值是否符合接口要求，具体可参考请求参数说明中的数据校验规则。 |


