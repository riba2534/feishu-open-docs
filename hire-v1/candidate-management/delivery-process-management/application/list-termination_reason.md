---
title: "获取终止投递原因"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/termination_reason/list"
updateTime: "1719285362000"
---

# 获取终止投递原因

获取系统中默认的投递终止原因以及用户配置的自定义投递终止原因。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/termination_reasons |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:application:readonly` 获取投递信息 `hire:application` 更新投递信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：eyJvZmZzZXQiOjEwLCJ0aW1lc3RhbXAiOjE2Mjc1NTUyMjM2NzIsImlkIjpudWxsfQ== |
| `page_size` | `int` | 否 | 每页获取记录数量，默认值为 10<br>**示例值**：10<br>**数据校验规则**：<br>- 最大值：`200` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `termination_reason\[\]` | 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 终止原因 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 终止原因名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `referral_name` | `i18n` | 内推渠道展示文案 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `termination_type` | `int` | 终止原因类型<br>**可选值有**：<br>- `1`: 我们拒绝了候选人 - `22`: 候选人拒绝了我们 - `27`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_used_as_evaluation` | `boolean` | 是否用于评估 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 状态<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "id": "10002",
                "name": {
                    "zh_cn": "测试",
                    "en_us": "test"
                },
                "referral_name": {
                    "zh_cn": "测试",
                    "en_us": "test"
                },
                "termination_type": 22,
                "is_used_as_evaluation": false,
                "active_status": 1
            }
        ],
        "has_more": true,
        "page_token": "eyJvZmZzZXQiOjEwLCJ0aW1lc3RhbXAiOjE2Mjc1NTUyMjM2NzIsImlkIjpudWxsfQ=="
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |


