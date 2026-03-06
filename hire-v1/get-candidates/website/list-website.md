---
title: "获取招聘官网列表"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/website/list"
updateTime: "1722568753000"
---

# 获取招聘官网列表

获取招聘官网列表，返回信息包括官网名称、官网ID、招聘渠道ID等。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/websites |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:site:readonly` 获取官网信息 `hire:site` 更新官网信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：eyJvZmZzZXQiOjEwLCJ0aW1lc3RhbXAiOjE2Mjc1NTUyMjM2NzIsImlkIjpudWxsfQ== |
| `page_size` | `int` | 否 | 每页获取记录数量  <br>**默认值** : 10<br>**示例值**：10<br>**数据校验规则**：<br>- 最大值：`10` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `website\[\]` | 官网列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 官网ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 官网名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 官网中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 官网英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `process_type_list` | `int\[\]` | 流程类型 - 1: 社招 - 2: 校招 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_channel_id` | `string` | 招聘渠道ID，每个官网拥有唯一的招聘渠道ID，可用于[职位发布至官网](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/advertisement/publish) |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |


### 响应体示例

```json
{
    "code": 0,
    "msg": "ok",
    "data": {
        "items": [
            {
                "id": "1213213123123",
                "name": {
                    "zh_cn": "校招官网",
                    "en_us": "campus recruitment site"
                },
                "process_type_list": [
                    2
                ],
                "job_channel_id": "1213213123123"
            }
        ],
        "has_more": true,
        "page_token": "eyJvZmZzZXQiOjEwLCJ0aW1lc3RhbXAiOjE2Mjc1NTUyMjM2NzIsImlkIjpudWxsfQ=="
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。 |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |


