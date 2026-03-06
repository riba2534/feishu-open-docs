---
title: "获取 OKR 周期列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/period/list"
updateTime: "1688380954000"
---

# 获取 OKR 周期列表

获取 OKR 周期列表。


> **Tip**: 使用`tenant_access_token`需要额外申请权限以应用身份访问OKR信息


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/okr/v1/periods |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `okr:okr:readonly` 获取 OKR 信息 `okr:okr` 更新 OKR 信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：xaasdasdax |
| `page_size` | `int` | 否 | 分页大小，默认10<br>**示例值**：10<br>**默认值**：`10` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `items` | `period\[\]` | 数据项 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `zh_name` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 启用状态<br>**可选值有**：<br>- `0`: 正常状态 - `1`: 暂不处理 - `2`: 标记失效 - `3`: 隐藏周期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `period_start_time` | `string` | 周期开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `period_end_time` | `string` | 周期结束时间 |


### 响应体示例

```json
{
    "code": 0,
    "data": {
        "has_more": false,
        "items": [
            {
                "en_name": "Jan - Mar 2022",
                "id": "7071200999834255380",
                "period_end_time": "1577721600000",
                "period_start_time": "1546272000000",
                "status": 0,
                "zh_name": "2022 年 1 月 - 3 月"
            }
        ]
    },
    "msg": "success"
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1009999 | internal server error | 内部错误，请联系飞书助手或您的客户成功经理 |
| 500 | 1009998 | system exception | 系统异常 |
| 400 | 1001001 | invalid parameters | 无效的参数，请对照文档检查输入的参数 |
| 400 | 1001002 | no permission | 您无权访问该接口，请确认您的登录凭证 |
| 400 | 1001003 | user not found | 用户不存在 |
| 400 | 1001004 | okr data not found | 对应ID的数据不存在 |


