---
title: "回传背调订单的最终结果"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/eco_background_check/update_result"
updateTime: "1723460587000"
---

# 回传背调订单的最终结果

回传背调的最终结果和终版报告。回传后，若租户未启用背调报告审批功能，则背调订单状态将会直接变成「已完成」。若启用背调报告审批功能，则在管理员审批通过后，订单状态流转为「已完成」。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/eco_background_checks/update_result |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:background_check_order` 更新招聘背调信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `background_check_id` | `string` | 是 | 背调 ID。可通过[创建背调](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/eco_background_check/events/created)事件获取<br>**示例值**："6931286400470354183" |
| `result` | `string` | 是 | 背调结果<br>**示例值**："无差异" |
| `result_time` | `string` | 是 | 背调结果时间。毫秒时间戳<br>**示例值**："1660123456789" |
| `report_file_list` | `eco_background_check_report_file\[\]` | 否 | 报告列表 |
| &nbsp;&nbsp;└ `report_name` | `string` | 是 | 报告名称<br>**示例值**："阶段报告.pdf" |
| &nbsp;&nbsp;└ `report_url` | `string` | 是 | 报告地址；当report_url_type 为空或为 1 时需为可下载的 pdf 链接；为 2 时为预览型链接<br>**示例值**："https://xxxxx/xxxxxx/xxxx.pdf" |
| &nbsp;&nbsp;└ `report_url_type` | `int` | 否 | 报告地址类型；枚举值为空或 1 时为可下载的 pdf 链接，2 为预览型链接<br>**示例值**：1<br>**可选值有**：<br>- `1`: 可下载的链接 - `2`: 外链型链接 |


### 请求体示例

```json
{
    "background_check_id": "6931286400470354183",
    "result": "无差异",
    "result_time": "1660123456789",
    "report_file_list": [
        {
            "report_name": "阶段报告.pdf",
            "report_url": "https://xxxxx/xxxxxx/xxxx.pdf",
            "report_url_type": 1
        }
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
| 400 | 1002858 | 订单状态异常 | 请检查参数 |
| 400 | 1002862 | 背调订单不存在 | 请检查入参`background_check_id` |
| 500 | 1002001 | 系统异常 | 请根据实际报错信息定位问题或联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |


