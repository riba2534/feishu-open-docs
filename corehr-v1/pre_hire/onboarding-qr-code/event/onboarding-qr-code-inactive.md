---
title: "入职二维码失效"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/pre_hire/onboarding-qr-code/event/onboarding-qr-code-inactive"
updateTime: "1720766024000"
---

# 入职二维码失效

使用扫码入职功能前，在入职管理后端配置二维码信息，当二维码失效时，会触发此事件{使用示例}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v2&resource=onboarding_qr_code&event=inactive)


## 事件

| 项目 | 值 |
| --- | --- |
| 事件类型 | corehr.onboarding_qr_code.inactive_v2 |
| 支持的应用类型 | custom,isv |
| 权限要求             订阅该事件所需的权限，开启其中任意一项权限即可订阅 开启任一权限即可 | `corehr:pre_hire:read` 获取待入职人员信息 `corehr:pre_hire:write` 读写待入职人员信息 |
| 推送方式 | `Webhook` |


### 事件体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `schema` | `string` | 事件版本，目前为2.0，v1.0 版本的事件，无此字段。 |
| `header` | `event_header` | 事件头 |
| &nbsp;&nbsp;└ `event_id` | `string` | 事件 ID |
| &nbsp;&nbsp;└ `event_type` | `string` | 事件类型 corehr.onboarding_qr_code.inactive_v2 |
| &nbsp;&nbsp;└ `create_time` | `string` | 事件创建时间戳（单位：毫秒） |
| &nbsp;&nbsp;└ `token` | `string` | 事件 Token |
| &nbsp;&nbsp;└ `app_id` | `string` | 应用 ID |
| &nbsp;&nbsp;└ `tenant_key` | `string` | 租户 Key |
| `event` | `\-` | \- |
| &nbsp;&nbsp;└ `code_lists` | `qr_code\[\]` | 二维码信息列表<br>**数据校验规则**：<br>- 长度范围：`0` ～ `10000` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 二维码id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `png` | `string` | 二维码图片链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 二维码值链接 |


### 事件体示例

```json
{
    "schema": "2.0",
    "header": {
        "event_id": "5e3702a84e847582be8db7fb73283c02",
        "event_type": "corehr.onboarding_qr_code.inactive_v2",
        "create_time": "1608725989000",
        "token": "rvaYgkND1GOiu5MM0E1rncYC6PLtF7JV",
        "app_id": "cli_9f5343c580712544",
        "tenant_key": "2ca1d211f64f6438"
    },
    "event": {
        "code_lists": [
            {
                "id": "6892698621939026184",
                "png": "https://open.feishu.cn/people/api/onboarding/scan_code/png?scan_code=6q5yxOKMzAsdBmXUZWVqnslLJR0KWy_tNYQnnkhJAVuDvVxMiUMusDJqTk4uDQhL",
                "url": "https://open.feishu.cn/people/welcome/scan?signKey=6q5yxOKMzAsdBmXUZWVqnslLJR0KWy_tNYQnnkhJAVuDvVxMiUMusDJqTk4uDQhL"
            }
        ]
    }
}
```


