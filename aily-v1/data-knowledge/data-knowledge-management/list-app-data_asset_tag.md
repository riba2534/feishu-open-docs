---
title: "获取数据知识分类列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/aily-v1/app-data_asset_tag/list"
updateTime: "1752155035000"
---

# 获取数据知识分类列表

获取 Aily 助手的数据知识分类列表


> **Tip**: - `tenant_access_token` 仅支持[ Aily 平台](https://aily.feishu.cn)的渠道应用身份
> - `user_access_token` 要求开发者需要 Aily 平台的应用协作者角色，包括管理员、开发者、运维人员


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/aily/v1/apps/:app_id/data_asset_tags |
| HTTP Method | GET |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `aily:data_asset:read` 获取智能伙伴创建平台数据知识资产 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_id` | `string` | AppID，可通过在 Aily 平台进入应用的开发界面中获取，获取示例 https://***/ai/app_namespace<br>**示例值**："spring_5862e4fea8__c"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 分页参数：分页大小，默认：20，最大：100<br>**示例值**：10 |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0= |
| `keyword` | `string` | 否 | 模糊匹配分类名称<br>**示例值**：电影<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| `data_asset_tag_ids` | `string\[\]` | 否 | 模糊匹配分类名称<br>**示例值**：spring_5862e4fea8__c__asset_tag_aadg2b5ql4gbs<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `data_asset_tag\[\]` | 数据知识分类列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `data_asset_tag_id` | `string` | 数据知识分类名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 数据知识分类ID |
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
                "data_asset_tag_id": "spring_5862e4fea8__c__asset_tag_aadg2b5ql4gbs",
                "name": "电影"
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
| 400 | 2700001 | param is invalid | 请结合文档排查请求参数 |


