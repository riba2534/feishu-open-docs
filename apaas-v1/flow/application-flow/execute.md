---
title: "发起流程"
fullPath: "/uAjLw4CM/ukTMukTMukTM/apaas-v1/application-flow/execute"
updateTime: "1732872409000"
---

# 发起流程

执行相应流程


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/apaas/v1/applications/:namespace/flows/:flow_id/execute |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `app_engine:flow:write` 执行流程 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `namespace` | `string` | 应用命名空间(低代码平台->我的应用->应用管理->可查看到)<br>**示例值**："package_7344545d87__c" |
| `flow_id` | `string` | 流程API名称（低代码平台->我的应用->开发->流程->展开为表格->可查看到）<br>**示例值**："deleteObject_99c656599f" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `is_async` | `boolean` | 否 | 是否异步执行(不传默认false)<br>**示例值**：true |
| `idempotent_key` | `string` | 否 | 幂等键（建议本地生成uuid传入，重复的话请求会报错）<br>**示例值**："iuhg23897489797" |
| `loop_masks` | `string\[\]` | 否 | 循环标志信息(当前版本可不传)<br>**示例值**：["\"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `20` |
| `params` | `string` | 否 | 流程入参（json 字符串，无入参不传）<br>**示例值**："`{\"variable_rgrtgqworiginal\": {\"_id\": 5454545}}`" |
| `operator` | `string` | 是 | 操作人（_id和email至少填一个，低代码平台用户的 id和email，需要从低代码平台获取，json字符串）<br>**示例值**："`{\"_id\": 1111, \"email\": \"apaas@bytedance.com\"}`" |


### 请求体示例

```json
{
    "operator": "{\"_id\": 1111, \"email\": \"apaas@bytedance.com\"}",
    "params": "{\"variable_rgrtgqworiginal\": {\"_id\": 5454545}}",
    "is_async": true
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `status` | `string` | 状态 |
| &nbsp;&nbsp;└ `out_params` | `string` | 输出参数 |
| &nbsp;&nbsp;└ `execution_id` | `string` | 执行id |
| &nbsp;&nbsp;└ `error_msg` | `string` | 错误信息 |
| &nbsp;&nbsp;└ `code` | `string` | code |


### 响应体示例

```json
{
    "code": 0,
    "data": {
        "code": "",
        "error_msg": "",
        "execution_id": "1816970091484211",
        "out_params": "[{\"api_name\":\"_flowExecutionID\",\"value\":1816970091484211}]",
        "status": "end"
    },
    "msg": "success"
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2320001 | param is invalid | 请检查本地输入 |


