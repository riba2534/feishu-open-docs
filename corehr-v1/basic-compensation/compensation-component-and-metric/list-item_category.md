---
title: "批量获取薪资项分类信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/compensation-v1/item_category/list"
updateTime: "1715671243000"
---

# 批量获取薪资项分类信息

批量获取薪资项分类信息


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/compensation/v1/item_categories |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:compensation_item_category:read` 获取基础薪酬的薪资项分类信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 分页大小<br>**示例值**：100<br>**默认值**：`100`<br>**数据校验规则**：<br>- 取值范围：`1` ～ `500` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：231412341234 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `item_category\[\]` | 薪资项分类信息列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 薪资项分类ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 薪资项分类名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_names` | `i18n_content\[\]` | 薪资项多语言分类 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语言版本，例如：“zh-CN”、“en-US” |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语言名称 |
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
                "id": "4532312334",
                "name": "基本薪资类",
                "i18n_names": [
                    {
                        "locale": "zh_cn",
                        "value": "中文名称"
                    }
                ]
            }
        ],
        "page_token": "2314123434",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 2290001 | server error | 服务器异常 |
| 400 | 2290002 | param invalid | 参数异常 |
| 500 | 2290003 | rpc fail | 下游服务调用失败 |


