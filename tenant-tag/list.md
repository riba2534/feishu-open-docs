---
title: "查询标签"
fullPath: "/uAjLw4CM/ukTMukTMukTM/group/im-v2/tag/list"
updateTime: "1712631382000"
---

# 查询标签信息
根据标签 ID 查询标签信息。

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/im/v2/tags |
| HTTP Method | GET |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `im:tag:read` 查询标签信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `ids` | `string\[\]` | 是 | 标签 ID<br>**示例值**：716168xxxxx<br>**数据校验规则**：<br>- 长度范围：`0` ～ `40` |

### curl示例
```
curl --location 'https://open.feishu.cn/open-apis/im/v2/tags?ids=7307xxx&ids=7311xxx' 
--header 'Authorization: Bearer t-g102cxxxxx'
```

## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `tag_infos` | `tag_info\[\]` | 标签信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 标签 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tag_type` | `string` | 标签类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 标签名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_names` | `tag_i18n_name\[\]` | i18n 多语言名称集合 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `update_time` | `string` | 更新时间 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "tag_infos": [
            {
                "id": "716168xxxxx",
                "tag_type": "tenant",
                "name": "tagName1",
                "i18n_names": [
                    {
                        "locale": "zh-CN",
                        "name": "tagName1"
                    }
                ],
                "create_time": "1700793403850",
                "update_time": "1700793403850"
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 230001 | param is invalid | 参数错误，请根据接口返回的错误信息或文档内容重新输入 |


