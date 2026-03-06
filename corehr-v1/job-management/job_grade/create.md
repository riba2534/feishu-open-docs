---
title: "创建职等"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/create"
updateTime: "1765434836000"
---

# 创建职等

创建职等


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/job_grades |
| HTTP Method | POST |
| 接口频率限制 | [3 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:job_grade:write` 查看、创建、更新、删除职等信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `client_token` | `string` | 否 | 根据client_token是否一致来判断是否为同一请求<br>**示例值**：12454646 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `grade_order` | `int` | 是 | 职等数值<br>**示例值**：9999<br>**数据校验规则**：<br>- 取值范围：`0` ～ `99999` |
| `code` | `string` | 否 | 编码<br>**示例值**："A01234" |
| `names` | `i18n\[\]` | 是 | 名称 - 名称不能包含「/」「；」「;」「\」、「'」字符<br>**数据校验规则**：<br>- 长度范围：`0` ～ `2` |
| &nbsp;&nbsp;└ `lang` | `string` | 是 | 语言编码（IETF BCP 47）<br>**示例值**："zh-CN" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 文本内容<br>**示例值**："中文示例" |
| `descriptions` | `i18n\[\]` | 否 | 描述<br>**数据校验规则**：<br>- 长度范围：`0` ～ `2` |
| &nbsp;&nbsp;└ `lang` | `string` | 是 | 语言编码（IETF BCP 47）<br>**示例值**："zh-CN" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 文本内容<br>**示例值**："中文示例" |


### 请求体示例

```json
{
    "grade_order": 9999,
    "code": "A01234",
    "names": [
        {
            "lang": "zh-CN",
            "value": "中文示例"
        }
    ],
    "descriptions": [
        {
            "lang": "zh-CN",
            "value": "中文示例"
        }
    ]
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `grade_id` | `string` | 职等ID |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "grade_id": "12345678"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1160001 | param is invalid | 请检查参数是否符合要求 |


