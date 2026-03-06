---
title: "创建通道"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/pathway/create"
updateTime: "1765434856000"
---

# 创建通道

创建通道，可以定义通道的名称、编码和描述信息


> **Tip**: 非必填字段，不传时默认为空


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/pathways |
| HTTP Method | POST |
| 接口频率限制 | [3 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:pathway:write` 读写通道信息 |

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
| `code` | `string` | 否 | 编码<br>**示例值**："A01234" |
| `names` | `i18n\[\]` | 是 | 名称<br>**数据校验规则**：<br>- 长度范围：`0` ～ `2` |
| &nbsp;&nbsp;└ `lang` | `string` | 是 | 中文用zh-CN，英文用en-US<br>**示例值**："zh-CN" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | - 文本内容，最长支持255个字符 - 名称不能包含「/」「；」「;」「\」「'」字符<br>**示例值**："中文示例" |
| `descriptions` | `i18n\[\]` | 否 | 描述<br>**数据校验规则**：<br>- 长度范围：`0` ～ `2` |
| &nbsp;&nbsp;└ `lang` | `string` | 是 | 中文用zh-CN，英文用en-US<br>**示例值**："zh-CN" |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 文本内容，最长支持2000个字符<br>**示例值**："中文示例" |


### 请求体示例

```json
{
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
| &nbsp;&nbsp;└ `pathway_id` | `string` | 通道ID |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "pathway_id": "12345678"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 429 | 1161604 | QPS over limit | 请先参考全量错误码详细描述进行错误排查，如问题始终无法解决请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |


其他错误码参考: [全量错误码详细描述](/document-mod/index?fullPath=%2FuAjLw4CM%2FukTMukTMukTM%2Fcorehr-v2%2Fpathway%2Fpathway-errorcodes)


