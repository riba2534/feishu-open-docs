---
title: "查询审计日志详情"
fullPath: "/uAjLw4CM/ukTMukTMukTM/apaas-v1/application-audit_log/get"
updateTime: "1727166325000"
---

# 飞书低代码平台-查询审计日志详情

根据日志 ID 查询审计日志详情


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/apaas/v1/applications/:namespace/audit_log |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `app_engine:security.audit_log:read` 获取飞书低代码平台审计日志信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `namespace` | `string` | 应用命名空间<br>**示例值**："package_aaa"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` 字符 |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `log_id` | `string` | 是 | 审计日志ID信息（通过[查询审计日志列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/apaas-v1/application-audit_log/audit_log_list)获取单条日志ID）<br>**示例值**：7405456257290600492<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` 字符 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `data` | `audit_log_detail` | 审计日志详情信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `log_id` | `string` | 审计日志ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `basic_info` | `basic_info` | 日志基础信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `log_type` | `string` | 日志类型： - 10000: 全部日志 - 10001: 企业管理日志 - 10002: 登录日志 - 10003: 应用管理日志 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `audit_scope` | `string` | 审计域： - 15001：企业管理后台 - 15002：应用管理后台 - 15003：应用开发平台 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `env_type` | `string` | 环境类型： - 16001：沙箱环境 - 16003：线上环境 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `app_id` | `string` | 应用id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `module` | `string` | 审计日志功能模块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `op_type` | `string` | 事件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `app_name` | `map<string, string>` | 应用名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `op_info` | `audit_log_op_info` | 审计日志操作信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `operator` | `lookup_with_avatar` | 操作人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tenant_id` | `string` | 租户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 用户邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `outsider` | `boolean` | 是否为外部用户，true代表是外部用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `op_detail` | `map<string, string>` | 操作详情内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `string` | 操作状态：18001-成功；18002-失败 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `failed_reason` | `string` | 失败原因 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `failed_reason_i18n` | `map<string, string>` | 多语类型失败原因 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `op_time` | `string` | 操作时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `data_object` | `string` | 数据对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `op_source` | `string` | 操作源：20001-前端；20004-openapi |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `data_changes` | `string\[\]` | 数据变化(旧值和新值) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `login_info` | `audit_log_login_info` | 登录类型信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `login_type` | `string` | 登录类型： - 11001: 飞书登录 - 11003: 账号密码登录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `device_info` | `audit_log_device_info` | 设备信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `device_id` | `string` | 设备ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `web_device_id` | `string` | web端设备ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `terminal_type` | `string` | 终端类型： - 13002: PC类型 - 13003: Web类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `os_type` | `string` | 系统类型： - 14002: window - 14001: 未知 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `os_version` | `string` | 系统版本 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `net_info` | `audit_log_net_info` | 网络信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `client_ip` | `string` | 客户端IP |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ip_loc` | `string` | IP位置 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ip_provider` | `string` | IP提供商 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `referer` | `string` | 引用页面 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `origin` | `string` | 源页面 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_agent` | `string` | 用户代理 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "data": {
            "log_id": "7376574450886557740",
            "basic_info": {
                "log_type": "10000",
                "audit_scope": "15001",
                "env_type": "16003",
                "app_id": "app123",
                "module": "17001",
                "op_type": "19001",
                "app_name": {
                    "2052": "应用名称"
                }
            },
            "op_info": {
                "operator": {
                    "id": "1768491480010814",
                    "name": "郭x",
                    "tenant_id": "72222",
                    "email": "gxxxxx.jim@bytedance.com"
                },
                "outsider": true,
                "op_detail": {
                    "language_code": 2052,
                    "text": "内部用户 赵四 登录了平台"
                },
                "status": "18001",
                "failed_reason": "登录失败",
                "failed_reason_i18n": {
                    "2052": "失败原因"
                },
                "op_time": "1723634726874",
                "data_object": "object_api_aaa",
                "op_source": "20001",
                "data_changes": [
                    "{\"old\": \"OldData\",  \"new\": \"NewData\" }"
                ]
            },
            "login_info": {
                "login_type": "11001"
            },
            "device_info": {
                "device_id": "device_1234",
                "web_device_id": "webDevice_1234",
                "terminal_type": "2",
                "os_type": "14002",
                "os_version": "14.6"
            },
            "net_info": {
                "client_ip": "192.168.1.1",
                "ip_loc": "中国北京",
                "ip_provider": "ISP_com",
                "referer": "https://example.com/referer",
                "origin": "https://example.com/origin",
                "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
            }
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2320001 | param is invalid | 检查请求入参 |


