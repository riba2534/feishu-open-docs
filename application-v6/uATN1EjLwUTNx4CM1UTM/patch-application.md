---
title: "更新应用分组信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/application-v6/application/patch"
updateTime: "1773409068000"
---

# 更新应用分组信息

更新应用的分组信息（分组会影响应用在工作台中的分类情况，请谨慎更新）


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/application/v6/applications/:app_id |
| HTTP Method | PATCH |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `admin:app.category:update` 更新应用分组 `application:application` 更新应用信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_id` | `string` | 应用的 id<br>**示例值**："cli_9b445f5258795107" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `lang` | `string` | 是 | 指定返回的语言<br>**示例值**：zh_cn<br>**可选值有**：<br>- `zh_cn`: 中文 - `en_us`: 英文 - `ja_jp`: 日文 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `common_categories` | `string\[\]` | 否 | 应用分类的国际化描述<br>**示例值**：["分析工具"]<br>**数据校验规则**：<br>- 长度范围：`1` ～ `3` |
| `allow_refresh_token` | `boolean` | 否 | 是否允许刷新user_access_token<br>**示例值**：false |
| `callback_info` | `callback_info` | 否 | 应用回调配置 |
| &nbsp;&nbsp;└ `callback_type` | `string` | 否 | 回调类型<br>**示例值**："webhook"<br>**可选值有**：<br>- `webhook`: 将回调发送至开发者服务器 - `websocket`: 使用长连接接收回调 |
| &nbsp;&nbsp;└ `request_url` | `string` | 否 | 回调地址<br>**示例值**："https://open.feishu.cn/" |
| &nbsp;&nbsp;└ `subscribed_callbacks` | `string\[\]` | 否 | 订阅的回调列表<br>**示例值**：["url.preview.get"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `99999` |


### 请求体示例

```json
{
    "common_categories": [
        "分析工具"
    ],
    "allow_refresh_token": false,
    "callback_info": {
        "callback_type": "webhook",
        "request_url": "https://open.feishu.cn/",
        "subscribed_callbacks": [
            "url.preview.get"
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


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {}
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 210503 | invalid app_id | 请检查请求路径中的 app_id 是否合法 |
| 400 | 210504 | no such app in tenant | 请检查被查询应用与当前调用接口应用是否在同一企业内 |
| 400 | 210505 | target app not a custom app | 请检查被查询应用是否是自建应用 |
| 400 | 210506 | no such app | 请检查请求路径中的 app_id 是否存在 |
| 400 | 211000 | size of common categories out of range, should be between 1 and 3 | 请检查传入的 categories  列表长度是否在 [1, 3] 范围内 |
| 400 | 211001 | common_categories[%d](%s) not exist (index starts from 0) | 请按照提示中的下标，核对传入的应用分类值是否正确，应用分类语言取值需与传入的 lang 参数对应 |


