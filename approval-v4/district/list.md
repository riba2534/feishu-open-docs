---
title: "查询地理库信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/approval-v4/district/list"
updateTime: "1773383131000"
---

# 查询地理库信息

获取审批的地理库数据，用于在发起审批时填写地址控件的区域信息


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/approval/v4/districts |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `approval:approval` 查看、创建、更新、删除审批应用相关信息 `approval:approval:readonly` 访问审批应用 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 分页大小，用于指定一次请求所返回的数据量上限，最大100，默认20<br>**示例值**：10 |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0= |
| `root_district_id` | `string` | 否 | 指定节点进行遍历，仅返回该节点下的数据，默认遍历根节点，返回值内容可参考list_type参数描述<br>**示例值**：1816670 |
| `list_type` | `string` | 否 | 遍历类型，不同的类型内容会有差异<br>**示例值**：sub_level<br>**可选值有**：<br>- `sub_level`: 遍历指定节点的下一层区域，默认方式 - `leaf_level`: 遍历指定节点的所有叶子节点，指定该参数时会返回parent_district |
| `locale` | `string` | 否 | 返回指定语言的内容，默认返回英文数据<br>**示例值**：zh-CN<br>**可选值有**：<br>- `zh-CN`: 中文 - `en-US`: 英文 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `version` | `string` | 地理库的版本，地理库更新时版本会同步更新，如果应用将地理数据存在本地，需要定时判断版本，在变化以及时更新本地数据 |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `items` | `district\[\]` | 区域列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 区域的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `level` | `string` | 层级 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `has_sub_district` | `boolean` | 是否有子区域 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `parent_districts` | `district_base_info\[\]` | 父区域列表，顺序由叶子节点到根节点，不包含叶子节点本身，仅遍历方式为leaf_level时返回 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 区域的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `level` | `string` | 层级 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "version": "7569941109133377539",
        "has_more": true,
        "page_token": "eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0=",
        "items": [
            {
                "id": "2038349",
                "name": "Beijing",
                "level": "Province",
                "has_sub_district": false,
                "parent_districts": [
                    {
                        "id": "1814991",
                        "name": "China",
                        "level": "Country"
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
| 500 | 1395001 | system error | 请根据实际报错信息定位或[咨询客服](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952&extra=%7B%22channel%22:14,%22created_at%22:1614493146,%22scenario_id%22:6885151765134622721,%22signature%22:%22ca94c408b966dc1de2083e5bbcd418294c146e98%22%7D) |
| 400 | 1390001 | invalid parameter | 检查参数是否正确，例如类型，大小 |
| 400 | 1395061 | version updated | 当前分页参数基于旧版数据返回，服务端已更新地理库数据版本，请重新调用本接口获取最新数据 |


