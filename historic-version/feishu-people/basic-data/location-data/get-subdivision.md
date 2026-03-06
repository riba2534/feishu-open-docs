---
title: "查询单条省份/行政区信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/subdivision/get"
updateTime: "1689316826000"
---

# 查询单条省份/行政区信息

查询单条省份/行政区信息。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/subdivisions/:subdivision_id |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:common_data.basic_data:read` 获取基础数据信息 `corehr:corehr:readonly` 获取核心人事信息 `corehr:corehr` 更新核心人事信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `subdivision_id` | `string` | 省份/行政区 ID<br>**示例值**："67489937334909845" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `subdivision` | `subdivision` | 国家/地址信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 省份/行政区id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n\[\]` | 省份/行政区名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `country_region_id` | `string` | 所属国家/地区id，详细信息可通过【查询国家/地区信息】接口查询获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `subdivision_type` | `enum` | 行政区类型，枚举值可通过文档【飞书人事枚举常量】行政区类型（subdivision_type）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 名称信息的语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 名称信息的内容 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "subdivision": {
            "id": "12",
            "name": [
                {
                    "lang": "zh-CN",
                    "value": "张三"
                }
            ],
            "country_region_id": "12",
            "subdivision_type": {
                "enum_name": "type_1",
                "display": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ]
            }
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1160101 | marshal error | 检查消息体格式是否符合要求 |
| 500 | 1160102 | unmarshal error | 联系飞书人事 Oncall |
| 500 | 1160103 | request ID repeat | 相同 Request ID 的请求只有第一条会成功，多次请求请更换Request ID |
| 500 | 1160104 | custom field format error | 检查自定义字段格式是否符合元数据定义 |
| 500 | 1160105 | field is required | 检查必填字段是否未填写 |
| 500 | 1160106 | date format should be 2006-01-02 | 检查日期格式是否正确 |
| 400 | 1160107 | param is invalid | 检查调用参数是否正确 |


