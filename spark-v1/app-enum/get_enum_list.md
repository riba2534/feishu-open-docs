---
title: "获取自定义枚举列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/spark-v1/app-enum/get_enum_list"
updateTime: "1774858958000"
---

# 获取自定义枚举列表

获取应用下的自定义枚举列表，包括枚举名称、描述、枚举值列表等字段信息。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/spark/v1/apps/:app_id/enums |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `spark:app.table:read` 读取数据表相关信息 `spark:app.table:write` 修改数据表相关信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_id` | `string` | 妙搭应用 id，可从妙搭应用 URL 中获取，如 https://miaoda.feishu.cn/app/app_4jcn5n11bpf5v 中的 app_4jcn5n11bpf5v 即为 app_id<br>**示例值**："app_4jcn5n11bpf5v" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 分页大小，用于限制一次请求所返回的数据条目数<br>**示例值**：10<br>**默认值**：`10`<br>**数据校验规则**：<br>- 取值范围：`1` ～ `500` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：AQD9/Rn9eij9Pm39ED40/RD/cIFmu77WxpxPB/2oHfQLZ+G8JG6tK7+ZnHiT7COhD2hMSICh/eBl7cpzU6JEC3J7COKNe4jrQ8ExwBCR |
| `env` | `string` | 否 | 访问的 database 环境，默认为 online（线上环境）<br>**示例值**：`online`、`dev`<br>**默认值**：`online` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `items` | `app_enum\[\]` | 枚举列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 枚举名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 枚举描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `options` | `string\[\]` | 枚举值列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `int` | 创建时间，毫秒时间戳 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "has_more": true,
        "page_token": "AQD9/Rn9eij9Pm39ED40/RD/cIFmu77WxpxPB/2oHfQLZ+G8JG6tK7+ZnHiT7COhD2hMSICh/eBl7cpzU6JEC3J7COKNe4jrQ8ExwBCR",
        "items": [
            {
                "name": "enum_demo",
                "description": "enum_demo的描述",
                "options": [
                    "enum_a"
                ],
                "created_at": 1765524810744
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 3340001 | param is invalid | 请检查请求参数的类型、格式或值是否符合接口要求，具体可参考请求参数说明中的数据校验规则。 |


