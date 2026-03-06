---
title: "获取通道信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/pathway/batch_get"
updateTime: "1755516885000"
---

# 获取通道信息

根据通道的ID批量获取通道的名称、编码、描述信息


> **Tip**: 延迟说明：数据库主从延迟2s以内，即：创建通道后2s内调用此接口可能查询不到数据。


> **Warning**: 由于该接口为ByID批量查询接口，当请求参数中的某个通道ID错误或者被删除时，接口不会报错。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/pathways/batch_get |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:pathway:read` 获取通道信息 `corehr:pathway:write` 读写通道信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `pathway_ids` | `string\[\]` | 是 | 通道 ID 列表。ID获取方式 - 调用[创建通道接口](/document-mod/index?fullPath=%2FuAjLw4CM%2FukTMukTMukTM%2Fcorehr-v2%2Fpathway%2Fcreate)后，从响应结果的`pathway_id`获取。 - 监听[通道创建事件](/document-mod/index?fullPath=/uAjLw4CM/ukTMukTMukTM/corehr-v2/pathway/events/created)，当触发该事件后可从事件体内获取`pathway_id` - 监听[通道更新事件](/document-mod/index?fullPath=/uAjLw4CM/ukTMukTMukTM/corehr-v2/pathway/events/updated)，当触发该事件后可从事件体内获取`pathway_id` - 监听[通道删除事件](/document-mod/index?fullPath=%2FuAjLw4CM%2FukTMukTMukTM%2Fcorehr-v2%2Fpathway%2Fevents%2Fdeleted)，当触发该事件后可从事件体内获取`pathway_id`<br>**示例值**：["4692446793125560154"]<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` |


### 请求体示例

```json
{
    "pathway_ids": [
        "4692446793125560154"
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
| &nbsp;&nbsp;└ `items` | `pathway\[\]` | 查询的通道信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `pathway_id` | `string` | 通道 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `names` | `i18n\[\]` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `descriptions` | `i18n\[\]` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 中文用zh-CN，英文用en-US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active` | `boolean` | 停启用状态；true：启用，false：停用 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "pathway_id": "4692446793125560154",
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
                ],
                "active": true
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 429 | 1161604 | QPS over limit | 请先参考全量错误码详细描述进行错误排查，如问题始终无法解决请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |


其他错误码参考: [全量错误码详细描述](/document-mod/index?fullPath=%2FuAjLw4CM%2FukTMukTMukTM%2Fcorehr-v2%2Fpathway%2Fpathway-errorcodes)


