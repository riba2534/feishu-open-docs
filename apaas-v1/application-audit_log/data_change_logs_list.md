---
title: "查询数据变更日志列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/apaas-v1/application-audit_log/data_change_logs_list"
updateTime: "1737441335000"
---

# 飞书低代码平台-查询数据变更日志列表

根据搜索/筛选条件，查询数据变更日志列表


> **Tip**: 每次最多可查询 10,000 条数据


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/apaas/v1/applications/:namespace/audit_log/data_change_logs_list |
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
| `namespace` | `string` | 应用命名空间<br>**示例值**："package_aa_bb"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `30` 字符 |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `quick_query` | `string` | 否 | 模糊查询<br>**示例值**：Intel Mac OS<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` 字符 |
| `page_size` | `string` | 是 | 分页大小<br>**示例值**：0<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` 字符 |
| `offset` | `string` | 是 | 翻页数量<br>**示例值**：0<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` 字符 |
| `from` | `string` | 否 | 查询时间范围：开始时间<br>**示例值**：1723691857002<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` 字符 |
| `to` | `string` | 否 | 查询时间范围：结束时间<br>**示例值**：1724296657002<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` 字符 |
| `log_type` | `string` | 是 | ”日志类型：10007-数据变更日志“<br>**示例值**：10007<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` 字符 |
| `filter` | `string` | 否 | 日志查询：筛选能力<br>**示例值**：{"items":[{"left":"eventName","operator":"=","right":[19001]}]}<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` 字符 |
| `columns` | `string\[\]` | 否 | 日志列表：选择展示行信息，例如["opTime","appName","eventName","clientIP","operator","status"]<br>**示例值**：operator<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` |
| `sort_by` | `string` | 否 | 查询排序字段：可选项为操作时间（opTime）<br>**示例值**：opTime<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` 字符 |
| `sort_order` | `string` | 否 | 查询排序：按时间从小到大使用 asc<br>**示例值**：asc<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` 字符 |
| `app_type` | `string` | 否 | 应用类型，0为apaas类型，1为aily类型<br>**示例值**：0<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` 字符 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `audit_log_es_field\[\]` | 数据变更日志查询结果列表详情信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `log_id` | `string` | 数据变更日志ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `op_time` | `string` | 操作时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `log_type` | `string` | “日志类型:10007-数据变更日志” |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `operator` | `lookup_with_avatar` | 操作人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tenant_id` | `string` | 租户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 用户邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `outsider` | `boolean` | 是否为外部用户,true代表是外部用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `login_type` | `string` | 登录类型:11001-飞书登录;11003-账号密码登录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `lark_tenant_id` | `string` | 飞书租户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `apaas_tenant_id` | `string` | apaas租户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_geo` | `string` | 用户地理信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `client_ip` | `string` | 客户端IP |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ip_loc` | `string` | IP位置 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ip_provider` | `string` | IP提供商 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `referer` | `string` | 引用页面 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `origin` | `string` | 源页面 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `api_path` | `string` | 路由路径 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `full_path` | `string` | 网关路径 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_agent` | `string` | 用户代理 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `device_id` | `string` | 设备ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `web_device_id` | `string` | web端设备ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `terminal_type` | `string` | 终端类型:13002-PC类型;13003-Web类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `os_type` | `string` | 系统类型:14002-window;14001-未知 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `os_version` | `string` | 系统版本 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `module` | `string` | 功能模块 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `data_object` | `string` | 数据对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `audit_scope` | `string` | 审计域:15001-企业管理后台;15002-应用管理后 台;15003-应用开发平台 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tenant_id` | `string` | 租户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `namespace` | `string` | 应用唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `env_type` | `string` | 环境类型:16001-沙箱环境;16003-线上环境 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `op_type` | `string` | 事件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `op_detail` | `map<string, string>` | 操作详情内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `op_source` | `string` | 操作源:20001-前端;20004-openapi |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `string` | 操作状态:18001-成功;18002-失败 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `failed_reason_i18n` | `map<string, string>` | 失败原因 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `data_changes` | `string\[\]` | 数据变化(旧值和新值) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `app_name` | `map<string, string>` | 应用名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `keyword_field_app_version` | `string` | 应用版本号 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `keyword_field_functional_sub_module` | `string` | 审计日志事件子模块 |
| &nbsp;&nbsp;└ `total` | `string` | 数据变更日志查询总条数 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "log_id": "7376574450886557740",
                "op_time": "1723634726874",
                "log_type": "10000",
                "operator": {
                    "id": "1768491480010814",
                    "name": "郭晋",
                    "tenant_id": "79844",
                    "email": "guojin.jim@bytedance.com"
                },
                "outsider": true,
                "login_type": "11001",
                "lark_tenant_id": "123",
                "apaas_tenant_id": "23333",
                "user_geo": "America/Chicago",
                "client_ip": "192.168.1.1",
                "ip_loc": "中国北京",
                "ip_provider": "ISP_com",
                "referer": "https://example.com/referer",
                "origin": "https://example.com/origin",
                "api_path": "/api/xxx",
                "full_path": "/api/xxx",
                "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                "device_id": "device_1234",
                "web_device_id": "webDevice_1234",
                "terminal_type": "2",
                "os_type": "14002",
                "os_version": "14.6",
                "module": "17001",
                "data_object": "object_api_aaa",
                "audit_scope": "15001",
                "tenant_id": "23335",
                "namespace": "package_aacc",
                "env_type": "16003",
                "op_type": "19001",
                "op_detail": {},
                "op_source": "20001",
                "status": "18001",
                "failed_reason_i18n": {
                    "zh": "失败信息"
                },
                "data_changes": [
                    "{\"old\": \"OldData\",\"new\": \"NewData\"}"
                ],
                "app_name": {
                    "zh": "新闻资讯平台"
                },
                "keyword_field_app_version": "v1.2.3",
                "keyword_field_functional_sub_module": "223"
            }
        ],
        "total": "10"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2320001 | param is invalid | 检查请求入参 |


