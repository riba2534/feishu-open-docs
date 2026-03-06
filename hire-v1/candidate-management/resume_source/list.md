---
title: "获取简历来源列表"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/resume_source/list"
updateTime: "1721358049000"
---

# 获取简历来源列表

获取简历来源列表。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/resume_sources |
| HTTP Method | GET |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:talent:readonly` 获取人才信息 `hire:talent` 更新人才信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 分页大小<br>**默认值**：1000<br>**示例值**：10<br>**数据校验规则**：<br>- 最大值：`100` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**："6794694704606185741" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `resume_source\[\]` | 数据 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 简历来源 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 简历来源中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 简历来源英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 启用状态<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已禁用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `resume_source_type` | `string` | 来源类型<br>**可选值有**：<br>- `10000`: 内推 - `10001`: 猎头 - `10002`: 内部来源 - `10003`: 第三方招聘网站 - `10004`: 社交媒体 - `10005`: 线下来源 - `10006`: 其他 - `10007`: 外部推荐 - `10008`: 员工转岗 - `10009`: 实习生转正 |
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
                "id": "10000",
                "zh_name": "内推",
                "en_name": "referral",
                "active_status": 1,
                "resume_source_type": "10001"
            }
        ],
        "page_token": "1",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |


