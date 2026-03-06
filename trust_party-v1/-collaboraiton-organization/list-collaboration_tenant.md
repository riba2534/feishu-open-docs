---
title: "获取可见关联组织的列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/trust_party-v1/collaboration_tenant/list"
updateTime: "1745918469000"
---

# 获取可见关联组织的列表

分页获取用户可见的关联列表。


## 提示

使用 user_access_token 时，按照 admin 管理后台关联组织列表中针对用户设置的可见性规则进行校验，使用 tenant_access_token 时，按照应用互通界面中针对应用设置的可见性规则进行校验。

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/trust_party/v1/collaboration_tenants |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `trust_party:collaboration.tenant:readonly` 以应用身份读取关联组织 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：xxxx |
| `page_size` | `int` | 否 | 单次请求的关联组织数量<br>**示例值**：10<br>**默认值**：`10`<br>**数据校验规则**：<br>- 取值范围：`1` ～ `100` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `target_tenant_list` | `collaboration_tenant\[\]` | 关联组织列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tenant_key` | `string` | 关联组织 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tenant_name` | `string` | 目标组织的名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_tenant_name` | `i18n_name` | 目标组织的i18n名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 日文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tenant_short_name` | `string` | 目标组织的简称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_tenant_short_name` | `i18n_name` | 目标组织的i18n简称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 日文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `connect_time` | `int` | 关联时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tenant_tag` | `string` | 标签 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_tenant_tag` | `i18n_name` | i18n标签 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 日文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `avatar` | `avatar_info` | 组织icon信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_72` | `string` | 72*72像素头像链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_240` | `string` | 240*240像素头像链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_640` | `string` | 640*640像素头像链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_origin` | `string` | 原始头像链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `brand` | `string` | 组织品牌 |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "target_tenant_list": [
            {
                "tenant_key": "130426ba5b8f174f",
                "tenant_name": "name",
                "i18n_tenant_name": {
                    "zh_cn": "zh_cn_name",
                    "ja_jp": "ja_jp_name",
                    "en_us": "en_name"
                },
                "tenant_short_name": "tenant_short_name",
                "i18n_tenant_short_name": {
                    "zh_cn": "zh_cn_name",
                    "ja_jp": "ja_jp_name",
                    "en_us": "en_name"
                },
                "connect_time": 1642041636,
                "tenant_tag": "协作",
                "i18n_tenant_tag": {
                    "zh_cn": "zh_cn_name",
                    "ja_jp": "ja_jp_name",
                    "en_us": "en_name"
                },
                "avatar": {
                    "avatar_72": "https://foo.icon.com/xxxx",
                    "avatar_240": "https://foo.icon.com/xxxx",
                    "avatar_640": "https://foo.icon.com/xxxx",
                    "avatar_origin": "https://foo.icon.com/xxxx"
                },
                "brand": "飞书"
            }
        ],
        "has_more": true,
        "page_token": "AQD9/Rn9eij9Pm39ED40/TIx6jupqdAcfLY%2B51xMvNU="
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1970012 | Page token is invalid error. | 使用接口返回的page token |
| 400 | 1970011 | Page size is invalid error. | 使用1-100范围的值 |


