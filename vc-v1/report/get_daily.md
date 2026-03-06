---
title: "获取会议报告"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/report/get_daily"
updateTime: "1714359532000"
---

# 获取会议报告

获取一段时间内组织的每日会议使用报告。


> **Warning**: 支持最近90天内的数据查询


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/vc/v1/reports/get_daily |
| HTTP Method | GET |
| 接口频率限制 | [特殊频控](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `vc:report:readonly` 获取会议报告 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `start_time` | `string` | 是 | 开始时间（unix时间，单位sec）<br>**示例值**：1608888867 |
| `end_time` | `string` | 是 | 结束时间（unix时间，单位sec）<br>**示例值**：1608888966 |
| `unit` | `int` | 否 | 数据驻留地（传参前提是租户存在多个驻留地数据且开通了该查询功能）<br>**示例值**：0<br>**可选值有**：<br>- `0`: 中国大陆 - `1`: 美国 - `2`: 新加坡 - `3`: 日本 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `meeting_report` | `report` | 会议报告 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `total_meeting_count` | `string` | 总会议数量 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `total_meeting_duration` | `string` | 总会议时长（单位sec） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `total_participant_count` | `string` | 总参会人数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `daily_report` | `report_meeting_daily\[\]` | 每日会议报告列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date` | `string` | 日期（unix时间，单位sec） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `meeting_count` | `string` | 会议数量 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `meeting_duration` | `string` | 会议时长（单位sec） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `participant_count` | `string` | 参会人数 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "meeting_report": {
            "total_meeting_count": "100",
            "total_meeting_duration": "300000",
            "total_participant_count": "20000",
            "daily_report": [
                {
                    "date": "1609113600",
                    "meeting_count": "100",
                    "meeting_duration": "147680",
                    "participant_count": "2000"
                }
            ]
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 121001 | internal error | 服务器内部错误，如果重试无效可联系管理员 |
| 400 | 121002 | not support | 暂不支持该功能 |
| 400 | 121003 | param error | 参数错误，检查参数的取值范围（请按照上面字段说明自查） |


