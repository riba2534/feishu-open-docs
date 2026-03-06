---
title: "获取项目列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/performance-v2/activity/query"
updateTime: "1729567628000"
---

# 获取项目列表

批量获取项目的配置信息，如项目名称、项目模式等信息。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/performance/v2/activity/query |
| HTTP Method | POST |
| 接口频率限制 | [10 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `performance:performance` 管理绩效数据 `performance:performance:readonly` 查看绩效数据 `performance:semester_activity:read` 获取周期与项目配置信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**数据校验规则**：<br>- 长度范围：`0` ～ `999999999` 字符<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `semester_ids` | `string\[\]` | 否 | 评估周期 ID 列表，可通过[获取周期](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/performance-v1/semester/list)获取<br>**注意**：若填写了 `activity_ids` 参数时，此参数无效<br>**示例值**：["6992035450862224940"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `10` |
| `activity_ids` | `string\[\]` | 否 | 项目 ID 列表<br>**示例值**：["6992035450862224940"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `50` |


**注意**：当请求参数 `semester_ids`  和 `activity_ids` 都没有填时，返回空数据。


### 请求体示例

```json
{
    "semester_ids": [
        "6992035450862224940"
    ],
    "activity_ids": [
        "6992035450862224940"
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
| &nbsp;&nbsp;└ `activities` | `activity\[\]` | 项目列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 项目 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 项目名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 项目中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 项目英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 项目描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `semester_id` | `string` | 周期 ID，详情可查看：[获取周期](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/performance-v1/semester/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `mode` | `string` | 项目模式<br>**可选值有**：<br>- `metric_development`: 指标制定 - `performance_review`: 绩效评估 - `metric_development_and_performance_review`: 指标制定及绩效评估 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `progress` | `string` | 项目状态<br>**可选值有**：<br>- `configurable`: 待完成配置 - `unable`: 未启动 - `initiating`: 启动中 - `enabled`: 已启动 - `finished`: 已结束 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 项目创建时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `modify_time` | `string` | 项目更新时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_user_id` | `string` | 项目创建人 ID，与入参 `user_id_type` 类型一致 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `modify_user_id` | `string` | 项目更新人 ID，与入参 `user_id_type` 类型一致 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "activities": [
            {
                "id": "7343513161666707459",
                "name": {
                    "zh_cn": "项目一",
                    "en_us": "Activity 1"
                },
                "description": {
                    "zh_cn": "体验",
                    "en_us": "Interactive experience"
                },
                "semester_id": "7343513161666707459",
                "mode": "performance_review",
                "progress": "configurable",
                "create_time": "1691951256000",
                "modify_time": "1691951256000",
                "create_user_id": "6924187793321444877",
                "modify_user_id": "6924187793321444877"
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1580102 | param is invalid | 检查参数是否正确，例如类型，大小 |
| 500 | 1580101 | internal error | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1580901 | tenant no licnese | 租户无绩效席位，请联系租户管理员开通绩效席位 |


更多错误码信息，参见[通用错误码](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)。


