---
title: "批量新建记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/apaas-v1/application-object-record/batch_create"
updateTime: "1727087497000"
---

# 批量新建记录

一次新建多条对象中的记录


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/apaas/v1/applications/:namespace/objects/:object_api_name/records/batch_create |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `app_engine:object.record:write` 创建、更新、删除对象记录数据 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `namespace` | `string` | 应用命名空间<br>**示例值**："package_test__c"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| `object_api_name` | `string` | 对象唯一标识<br>**示例值**："user"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `256` 字符 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `records` | `string` | 是 | 记录详情列表，格式为 List>，操作记录数上限为 500 条<br>**示例值**："[{\"book_name\":\"name21\",\"book_count\":2}]" |


### 请求体示例

```json
{
    "records": "[{\"book_name\":\"name21\",\"book_count\":2}]"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `record_result\[\]` | 处理结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `success` | `boolean` | 是否成功 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 记录 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `errors` | `record_result_error\[\]` | 权限错误时的细分 code |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 错误码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `message` | `string` | success |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sub_code` | `string` | 权限错误时的细分 code |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fields` | `string\[\]` | 权限错误时的涉及的字段 APIID 集合 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "success": true,
                "id": "1801464965461024",
                "errors": [
                    {
                        "code": "0",
                        "message": "success",
                        "sub_code": "k_ec_00001",
                        "fields": [
                            "_id"
                        ]
                    }
                ]
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2320001 | param is invalid | 请检查输入参数 |


