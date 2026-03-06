---
title: "获取 OKR 周期规则"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/period_rule/list"
updateTime: "1704766577000"
---

# 获取 OKR 周期规则

获取租户的周期规则列表。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/okr/v1/period_rules |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `okr:okr:readonly` 获取 OKR 信息 `okr:okr` 更新 OKR 信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `period_rules` | `period_rule\[\]` | 周期规则列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `period_rule_id` | `string` | 周期规则ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 周期类型 - year: 年度周期 - month: 月度周期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `length` | `int` | 周期长度（月) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `first_month` | `int` | 每年首个开始月份 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "period_rules": [
            {
                "period_rule_id": "134",
                "type": "year",
                "length": 12,
                "first_month": 12
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1009999 | Unknown error. Please contact Feishu Assistant or your customer success manager. | 内部错误，请联系飞书助手或您的客户成功经理 |
| 400 | 1001001 | Invalid parameters. Please check document and modify accordingly. | 无效的参数，请对照文档检查输入的参数 |
| 403 | 1001002 | No permission. | 您无权访问该接口，请确认您的登录凭证 |
| 400 | 1001003 | User not found. | 用户不存在 |
| 400 | 1001004 | OKR data not found. | 对应ID的数据不存在 |
| 403 | 1000403 | OpenAPI is unavailable in current edition (Standard edition). Please update to Business edition. | 您目前的套餐无法使用开放平台接口功能，请升级至OKR企业版 |


