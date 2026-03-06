---
title: "新建记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/apaas-v1/application-object-record/create"
updateTime: "1727087407000"
---

# 新建记录

在对象中新建记录


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/apaas/v1/applications/:namespace/objects/:object_api_name/records |
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
| `record` | `string` | 是 | 创建对象使用的数据，键为字段 API 名称，值为字段值，格式可参考字段值格式<br>**示例值**："{\"book_name\":\"test\"}"<br>**数据校验规则**：<br>- 最小长度：`0` 字符 |


### 请求体示例

```json
{
    "record": "{\"book_name\":\"test\"}"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `id` | `string` | 记录 ID |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "id": "1764024447556775"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2320001 | param is invalid | 请检查输入参数 |


