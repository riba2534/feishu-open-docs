---
title: "获取人才库列表"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_pool/search"
updateTime: "1725350473000"
---

# 获取人才库列表

获取人才库列表，可获取的信息包括人才库 ID、人才库名称等。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/talent_pools/ |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:talent_folder:readonly` 获取人才库信息 `hire:talent_folder` 更新人才库信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 分页大小<br>**示例值**：100<br>**默认值**：`10`<br>**数据校验规则**：<br>- 最大值：`100` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：eyJvZmZzZXQiOjEwLCJ0aW1lc3RhbXAiOjE2Mjc1NTUyMjM2NzIsImlkIjpudWxsfQ== |
| `id_list` | `string\[\]` | 否 | 人才库 ID 列表。当传入该参数时，返回min(page_size, len(id_list))的人才库信息<br>**示例值**：["6930815272790114324", "6940815272790114325"<br>**数据校验规则**：<br>- 最大长度：`50` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `talent_pool\[\]` | 人才库列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 人才库 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `i18n` | 人才库名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 人才库中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 人才库英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_description` | `i18n` | 人才库描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `parent_id` | `string` | 父级人才库 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_private` | `int` | 是否「部分用户可见」<br>**可选值有**：<br>- `1`: 代表部分用户可见。具体而言，只有满足授权条件的用户，才能查看人才库。授权条件的维度包括：角色、部门、用户 - `2`: 代表全部用户可见。这里的全部用户指的是拥有「查看人才库」权限的用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 人才库创建时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `modify_time` | `string` | 人才库修改时间，毫秒时间戳 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "SUCCESS",
    "data": {
        "items": [
            {
                "id": "6930815272790114324",
                "i18n_name": {
                    "zh_cn": "公共人才库",
                    "en_us": "Common Talent Pool"
                },
                "i18n_description": {
                    "zh_cn": "储备企业内公开可见的人才",
                    "en_us": "The talent pool is visible to all company members"
                },
                "parent_id": "6930815272790114324",
                "is_private": 1,
                "create_time": "1679300424000",
                "modify_time": "1679300424000"
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
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002004 | 分页大小不合法 | 请检查分页大小`page_size `是否在合法范围内 |
| 400 | 1002005 | ID 列表过长 | 请减少入参 `id_list` 列表长度，不超过50 |


