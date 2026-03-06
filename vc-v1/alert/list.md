---
title: "获取告警记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/alert/list"
updateTime: "1721719982000"
---

# 获取告警记录

获取特定条件下租户的设备告警记录。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/vc/v1/alerts |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `vc:alert:readonly` 获取告警中心告警信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `start_time` | `string` | 是 | 开始时间（unix时间，单位秒）<br>**示例值**：1608888867 |
| `end_time` | `string` | 是 | 结束时间（unix时间，单位秒）<br>**示例值**：1608888867 |
| `query_type` | `int` | 否 | 查询对象类型，不填返回所有<br>**示例值**：1<br>**可选值有**：<br>- `1`: 会议室 - `2`: 企业会议室连接器 - `3`: SIP会议室系统 |
| `query_value` | `string` | 否 | 查询对象ID，会议室ID或企业会议室连接器ID<br>**示例值**：omm_4de32cf10a4358788ff4e09e37ebbf9b |
| `page_size` | `int` | 否 | 请求期望返回的告警记录数量，不足则返回全部，该值默认为 100，最大为 1000<br>**示例值**：100<br>**数据校验规则**：<br>- 最大值：`200` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：100 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `items` | `alert\[\]` | 告警记录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `alert_id` | `string` | 告警ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `resource_scope` | `string` | 触发告警规则的会议室/服务器具体的名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `monitor_target` | `int` | 触发告警规则的监控对象<br>**可选值有**：<br>- `1`: 飞书会议室 - `2`: 飞书会议室签到板 - `3`: 飞书投屏盒子 - `4`: 飞书投屏 - `5`: sip会议室系统 - `6`: erc节点 - `7`: 飞书传感器 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `alert_strategy` | `string` | 告警规则的规则描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `alert_time` | `string` | 告警通知发生时间（unix时间，单位秒） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `alert_level` | `int` | 告警等级：严重/警告/提醒<br>**可选值有**：<br>- `0`: 提醒 - `1`: 警告 - `2`: 严重 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contacts` | `contact\[\]` | 告警联系人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contact_type` | `int` | 联系人类型<br>**可选值有**：<br>- `1`: 用户 - `2`: 用户组 - `3`: 部门 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contact_name` | `string` | 联系人名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `notifyMethods` | `int\[\]` | 通知方式<br>**可选值有**：<br>- `0`: 飞书机器人 - `1`: 邮件 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `alertRule` | `string` | 规则名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `process_time` | `string` | 处理时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `recover_time` | `string` | 恢复时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `process_status` | `int` | 处理状态：待处理/处理中/已恢复<br>**可选值有**：<br>- `0`: 待处理（deprecated） - `1`: 待处理 - `2`: 处理中 - `3`: 已恢复（deprecated） - `4`: 已恢复 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `alert_rule_id` | `string` | 告警规则ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `monitor_target_room_id` | `string` | 触发告警规则的会议室ID，当触发告警规则的是会议室时返回该信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `monitor_target_room_mac` | `string` | 触发告警规则的会议室主机Mac地址，当monitor_target=1时返回该信息 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "has_more": true,
        "page_token": "50",
        "items": [
            {
                "alert_id": "7115030004018184212",
                "resource_scope": "XX层级",
                "monitor_target": 2,
                "alert_strategy": "连续1个周期（共1分钟），控制器电量 < 50%，则告警",
                "alert_time": "1656914944",
                "alert_level": 2,
                "contacts": [
                    {
                        "contact_type": 1,
                        "contact_name": "张三"
                    }
                ],
                "notifyMethods": [
                    [
                        0,
                        1
                    ]
                ],
                "alertRule": "签到板断开连接",
                "process_time": "1656914944",
                "recover_time": "1656914944",
                "process_status": 2,
                "alert_rule_id": "100",
                "monitor_target_room_id": "omm_4de32cf10a4358788ff4e09e37ebbf9b",
                "monitor_target_room_mac": "52:60:19:9c:97:21"
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 121001 | internal error | 服务器内部错误，如果重试无效可联系管理员 |
| 400 | 121002 | not support | 暂不支持该功能 |
| 400 | 121003 | param error | 参数错误，检查参数的取值范围（请按照上面字段说明自查） |
| 404 | 121004 | data not exist | 无效的请求体，请确保请求方法、请求信息、请求数据格式等是正确的 |


