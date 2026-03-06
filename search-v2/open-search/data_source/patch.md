---
title: "修改数据源"
fullPath: "/uAjLw4CM/ukTMukTMukTM/search-v2/data_source/patch"
updateTime: "1680147707000"
---

# 修改数据源

更新一个已经存在的数据源。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/search/v2/data_sources/:data_source_id |
| HTTP Method | PATCH |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `search:data_source` 查询、创建、修改和删除自定义搜索数据源、数据范式或数据项 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `data_source_id` | `string` | 数据源的唯一标识<br>**示例值**："6953903108179099667" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | `string` | 否 | 数据源的展示名称<br>**示例值**："客服工单" |
| `state` | `int` | 否 | 数据源状态，0-已上线，1-未上线<br>**示例值**：0<br>**可选值有**：<br>- `0`: 已上线 - `1`: 未上线 |
| `description` | `string` | 否 | 对于数据源的描述<br>**示例值**："搜索客服工单" |
| `icon_url` | `string` | 否 | 数据源在 search tab 上的展示图标路径<br>**示例值**："https://www.xxx.com/open.jpg" |
| `i18n_name` | `i18n_meta` | 否 | 数据源名称多语言配置，json格式，key为语言locale，value为对应文案，例如{"zh_cn":"测试数据源", "en_us":"Test DataSource"} |
| &nbsp;&nbsp;└ `zh_cn` | `string` | 否 | 国际化字段：中文<br>**示例值**："任务" |
| &nbsp;&nbsp;└ `en_us` | `string` | 否 | 国际化字段：英文<br>**示例值**："TODO" |
| &nbsp;&nbsp;└ `ja_jp` | `string` | 否 | 国际化字段：日文<br>**示例值**："タスク" |
| `i18n_description` | `i18n_meta` | 否 | 数据源描述多语言配置，json格式，key为语言locale，value为对应文案，例如{"zh_cn":"搜索测试数据源相关数据", "en_us":"Search data from Test DataSource"} |
| &nbsp;&nbsp;└ `zh_cn` | `string` | 否 | 国际化字段：中文<br>**示例值**："任务" |
| &nbsp;&nbsp;└ `en_us` | `string` | 否 | 国际化字段：英文<br>**示例值**："TODO" |
| &nbsp;&nbsp;└ `ja_jp` | `string` | 否 | 国际化字段：日文<br>**示例值**："タスク" |


### 请求体示例

```json
{
    "name": "客服工单",
    "state": 0,
    "description": "搜索客服工单",
    "icon_url": "https://www.xxx.com/open.jpg"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `data_source` | `data_source` | 数据源 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 数据源的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | data_source的展示名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `state` | `int` | 数据源状态，0-已上线，1-未上线。如果未填，默认是未上线状态。<br>**可选值有**：<br>- `0`: 已上线 - `1`: 未上线 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 对于数据源的描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 创建时间，使用Unix时间戳，单位为“秒” |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `update_time` | `string` | 更新时间，使用Unix时间戳，单位为“秒” |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_exceed_quota` | `boolean` | 是否超限 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `icon_url` | `string` | 数据源在 search tab 上的展示图标路径，建议使用png或jpeg格式，否则可能无法在客户端正常展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `template` | `string` | 数据源采用的展示模版名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `searchable_fields` | `string\[\]` | 【已废弃，如有定制需要请使用“数据范式”接口】描述哪些字段可以被搜索 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `i18n_meta` | 数据源的国际化展示名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 国际化字段：中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 国际化字段：英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 国际化字段：日文 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_description` | `i18n_meta` | 数据源的国际化描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 国际化字段：中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 国际化字段：英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 国际化字段：日文 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `schema_id` | `string` | 数据源关联的 schema 标识 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success"
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1270001 | 系统内部错误 | 联系系统开发人员协助定位 |
| 400 | 1270002 | 参数错误 | 根据错误信息和文档排查非法参数 |
| 500 | 1270003 | 调用失败 | 如果重试后仍然失败，请联系系统开发人员 |
| 400 | 1270004 | 数据源不存在 | 确认 datasource ID 是否正确 |
| 400 | 1270005 | 该功能仅对旗舰版可用 | 请联系销售人员升级套餐以使用此高级功能 |
| 400 | 1271003 | 无更改 | 没有更改项，请检查参数是否合法 |
| 401 | 1272001 | 无权限操作数据源 | 确认 datasource ID 是否合法 |
| 500 | 1272002 | 操作鉴权失败 | 如果重试后仍然失败，请联系系统开发人员协助定位 |


