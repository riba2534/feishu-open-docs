---
title: "获取单个工作城市信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/work_city/get"
updateTime: "1720167908000"
---

# 获取单个工作城市信息

调用该接口获取指定工作城市的信息，包括工作城市的 ID、名称、多语言名称以及启用状态。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/contact/v3/work_cities/:work_city_id |
| HTTP Method | GET |
| 接口频率限制 | [10 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `contact:work_city:readonly` 获取工作城市列表 `contact:contact:access_as_user` 以用户身份访问通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `work_city_id` | `string` | 工作城市 ID。你可以调用[获取租户工作城市列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/work_city/list)接口，获取工作城市 ID。<br>**示例值**："dd39369b19b9" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `work_city` | `work_city` | 工作城市信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_city_id` | `string` | 工作城市 ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 工作城市名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `i18n_content\[\]` | 多语言工作城市名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语言版本。例如：<br>- zh_cn：中文 - en_us：英语 - ja_jp：日语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 多语言版本对应的值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `boolean` | 是否启用工作城市。<br>**可能值有**： - true：启用 - false：禁用 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "work_city": {
            "work_city_id": "0dd1ec95f021",
            "name": "北京",
            "i18n_name": [
                {
                    "locale": "zh_cn",
                    "value": "北京"
                }
            ],
            "status": true
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 40001 | invalid param | 无效参数。请根据接口文档的参数描述，检查并传入正确的参数值后重试。 |


更多错误码信息，参见[通用错误码](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)。


