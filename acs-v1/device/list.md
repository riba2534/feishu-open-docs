---
title: "获取门禁设备列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/acs-v1/device/list"
updateTime: "1671441948000"
---

# 获取门禁设备列表

使用该接口获取租户内所有门禁设备。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/acs/v1/devices |
| HTTP Method | GET |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `acs:devices:readonly` 查看智能门禁设备列表 |

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
| &nbsp;&nbsp;└ `items` | `device\[\]` | - |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `device_id` | `string` | 门禁设备 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `device_name` | `string` | 设备名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `device_sn` | `string` | 设备 SN 码 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "device_id": "6939433228970082593",
                "device_name": "东门",
                "device_sn": "3X811621174000240"
            }
        ]
    }
}
```


