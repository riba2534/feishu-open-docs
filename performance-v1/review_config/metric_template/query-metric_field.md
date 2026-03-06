---
title: "获取指标字段列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/performance-v2/metric_field/query"
updateTime: "1732870069000"
---

# 获取指标字段列表

批量获取指标的字段基础信息，如指标字段名称、指标字段类型等信息。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/performance/v2/metric_fields/query |
| HTTP Method | POST |
| 接口频率限制 | [20 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `performance:metric:write` 管理关键指标数据 `performance:metric_lib:read` 获取指标配置信息 `performance:metric:read` 获取关键指标数据 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `field_ids` | `string\[\]` | 否 | 指标的字段 ID 列表，填写时获取指定指标字段，不填时获取全部指标字段<br>**示例值**：["7293169069640630291"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `50` |


### 请求体示例

```json
{
    "field_ids": [
        "7293169069640630291"
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
| &nbsp;&nbsp;└ `items` | `metric_field\[\]` | 指标字段信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `field_id` | `string` | 指标字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 指标字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 指标字段中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 指标字段英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 指标字段类型<br>**可选值有**：<br>- `text`: 文本 - `number`: 数字 - `pencentage`: 百分比 - `person`: 人员单选 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "field_id": "7272581996315099155",
                "name": {
                    "zh_cn": "销量",
                    "en_us": "Sales"
                },
                "type": "text"
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1580101 | internal error | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1580102 | param is invalid | 检查参数是否正确，例如类型，大小 |
| 400 | 1580901 | tenant no licnese | 租户无绩效席位，请联系租户管理员开通绩效席位 |


更多错误码信息，参见[通用错误码](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)。


