---
title: "创建标签"
fullPath: "/uAjLw4CM/ukTMukTMukTM/group/im-v2/tag/create"
updateTime: "1712631358000"
---

# 创建标签

创建标签并返回标签 ID。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/im/v2/tags |
| HTTP Method | POST |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `im:tag:write` 编辑标签信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `create_tag` | `create_tag` | 是 | 创建标签 |
| &nbsp;&nbsp;└ `tag_type` | `string` | 是 | 标签类型<br>**示例值**："tenant"<br>**可选值有**：<br>- `tenant`: 租户类型标签 |
| &nbsp;&nbsp;└ `name` | `string` | 是 | 标签默认名称<br>**示例值**："default name" |
| &nbsp;&nbsp;└ `i18n_names` | `tag_i18n_name\[\]` | 否 | i18n多语言标签名称集合<br>**数据校验规则**：<br>- 长度范围：`0` ～ `40` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 是 | 语言<br>**示例值**："zh_cn" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 否 | 名称<br>**示例值**："标签1" |


### 请求体示例

```json
{
    "create_tag": {
        "tag_type": "tenant",
        "name": "default name",
        "i18n_names": [
            {
                "locale": "zh_cn",
                "name": "标签1"
            }
        ]
    }
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `id` | `string` | 创建的 tag 的 ID |
| &nbsp;&nbsp;└ `create_tag_fail_reason` | `create_tag_fail_reason` | 创建失败原因 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `duplicate_id` | `string` | 名称重复的标签id |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "id": "716168xxxxx",
        "create_tag_fail_reason": {
            "duplicate_id": "716168xxxxx"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 230001 | param is invalid | 参数错误，请根据接口返回的错误信息或文档内容重新输入 |


